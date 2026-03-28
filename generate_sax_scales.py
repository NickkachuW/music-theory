"""
Generate a Scale & Chord Reference PDF for Alto and Tenor Saxophone.
All scales from the FQBK handbook Scale Syllabus, transposed for Eb and Bb instruments.
"""
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import math

PAGE_W, PAGE_H = letter
MARGIN = 0.6 * inch
STAFF_LINE_SPACING = 8  # points between staff lines
NOTE_SPACING = 18  # horizontal spacing between notes (tighter to fit ascending + descending)
STAFF_LEFT = MARGIN + 40  # leave room for clef
STAFF_RIGHT = PAGE_W - MARGIN

# ── Music theory helpers ──────────────────────────────────────────────

NOTE_LETTERS = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
# Semitone value of each natural note
NATURAL_SEMITONES = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}

def parse_note(note_str):
    """Parse 'C', 'Eb', 'F#', 'Bbb' etc. into (letter, accidental_semitones)."""
    letter = note_str[0].upper()
    acc = 0
    for ch in note_str[1:]:
        if ch in ('b', '\u266d'):  # flat
            acc -= 1
        elif ch in ('#', '\u266f'):  # sharp
            acc += 1
    return letter, acc

def note_to_midi(letter, acc, octave):
    return NATURAL_SEMITONES[letter] + acc + octave * 12

def transpose_note(letter, acc, semitone_offset, letter_offset):
    """Transpose a note by the given semitone and letter offsets.
    Returns (new_letter, new_acc)."""
    old_midi = NATURAL_SEMITONES[letter] + acc
    new_midi = (old_midi + semitone_offset) % 12
    new_letter_idx = (NOTE_LETTERS.index(letter) + letter_offset) % 7
    new_letter = NOTE_LETTERS[new_letter_idx]
    new_natural = NATURAL_SEMITONES[new_letter]
    new_acc = (new_midi - new_natural + 6) % 12 - 6  # range -5..+6, but practically -2..+2
    return new_letter, new_acc

def acc_str(acc):
    """Convert accidental number to display string."""
    if acc == 0: return ''
    if acc == 1: return '#'
    if acc == -1: return 'b'
    if acc == 2: return '##'
    if acc == -2: return 'bb'
    return '#' * acc if acc > 0 else 'b' * (-acc)

def note_display(letter, acc):
    return letter + acc_str(acc)

def transpose_scale(notes, semitone_offset, letter_offset):
    """Transpose a list of (letter, acc) tuples."""
    return [transpose_note(l, a, semitone_offset, letter_offset) for l, a in notes]

# ── Scale data (all in concert C) ────────────────────────────────────
# Each entry: (scale_name, chord_symbol, [(letter, acc), ...])

def build_scale_from_notes(note_str_list):
    return [parse_note(n) for n in note_str_list]

SCALE_CATEGORIES = [
    ("1. MAJOR SCALES", [
        ("Major", "C\u0394", "C D E F G A B C"),
        ("Major Pentatonic", "C", "C D E G A C"),
        ("Lydian", "C\u0394#4", "C D E F# G A B C"),
        ("Bebop (Major)", "C\u0394", "C D E F G G# A B C"),
        ("Harmonic Major", "C\u0394b6", "C D E F G Ab B C"),
        ("Lydian Augmented", "C\u0394#5,#4", "C D E F# G# A B C"),
        ("Augmented", "C", "C D# E G Ab B C"),
        ("6th Mode of Harmonic Minor", "C", "C D# E F# G A B C"),
        ("Diminished (begin with H)", "C", "C Db D# E F# G A Bb C"),
        ("Blues Scale", "C", "C Eb F F# G Bb C"),
    ]),
    ("2. DOMINANT 7th SCALES", [
        ("Dominant 7th (Mixolydian)", "C7", "C D E F G A Bb C"),
        ("Major Pentatonic", "C7", "C D E G A C"),
        ("Bebop (Dominant)", "C7", "C D E F G A Bb B C"),
        ("Spanish / Jewish", "C7b9", "C Db E F G Ab Bb C"),
        ("Lydian Dominant", "C7#4", "C D E F# G A Bb C"),
        ("Hindu", "C7b6", "C D E F G Ab Bb C"),
        ("Whole Tone", "C7#5", "C D E F# G# Bb C"),
        ("Diminished (begin with H)", "C7b9", "C Db D# E F# G A Bb C"),
        ("Diminished Whole Tone", "C7#9", "C Db D# E F# G# Bb C"),
        ("Blues Scale", "C7", "C Eb F F# G Bb C"),
    ]),
    ("2b. DOMINANT 7th SUSPENDED 4th", [
        ("Dom. 7th (don't emphasize 3rd)", "C7sus4", "C D E F G A Bb C"),
        ("Maj. Pentatonic built on b7", "C7sus4", "Bb C D F G Bb"),
        ("Bebop Scale", "C7sus4", "C D E F G A Bb B C"),
    ]),
    ("3. MINOR SCALES", [
        ("Minor (Dorian)", "C\u20137", "C D Eb F G A Bb C"),
        ("Pentatonic (Minor)", "C\u20137", "C Eb F G Bb C"),
        ("Bebop (Minor)", "C\u20137", "C D Eb E F G A Bb C"),
        ("Melodic Minor (ascending)", "C\u2013\u0394", "C D Eb F G A B C"),
        ("Bebop Minor No. 2", "C\u20136", "C D Eb F G G# A B C"),
        ("Blues Scale", "C\u20137", "C Eb F F# G Bb C"),
        ("Harmonic Minor", "C\u2013\u0394b6", "C D Eb F G Ab B C"),
        ("Diminished (begin with W)", "C\u20137", "C D Eb F F# G# A B C"),
        ("Phrygian", "C\u2013b9b6", "C Db Eb F G Ab Bb C"),
        ("Pure / Natural Minor (Aeolian)", "C\u2013b6", "C D Eb F G Ab Bb C"),
    ]),
    ("4. HALF DIMINISHED SCALES", [
        ("Half Diminished (Locrian)", "C\u00d8", "C Db Eb F Gb Ab Bb C"),
        ("Locrian #2", "C\u00d8#2", "C D Eb F Gb Ab Bb C"),
        ("Bebop Scale", "C\u00d8", "C Db Eb F Gb G Ab Bb C"),
    ]),
    ("5. DIMINISHED SCALE", [
        ("Diminished (8-tone)", "C\u00b0", "C D Eb F Gb Ab A B C"),
    ]),
]

# Parse all scales
PARSED_CATEGORIES = []
for cat_name, scales in SCALE_CATEGORIES:
    parsed_scales = []
    for scale_name, chord_sym, notes_str in scales:
        notes = build_scale_from_notes(notes_str.split())
        parsed_scales.append((scale_name, chord_sym, notes))
    PARSED_CATEGORIES.append((cat_name, parsed_scales))

# ── Chord data ────────────────────────────────────────────────────────
CHORD_TYPES = [
    ("Major 7th", "\u0394", [('C',0), ('E',0), ('G',0), ('B',0)]),
    ("Dominant 7th", "7", [('C',0), ('E',0), ('G',0), ('B',-1)]),
    ("Minor 7th", "\u20137", [('C',0), ('E',-1), ('G',0), ('B',-1)]),
    ("Half Diminished", "\u00d8", [('C',0), ('E',-1), ('G',-1), ('B',-1)]),
    ("Diminished 7th", "\u00b0", [('C',0), ('E',-1), ('G',-1), ('A',0)]),
]

# 12 written keys — using practical enharmonic spellings (Gb not F#) to avoid
# double sharps/flats. Each entry: (name, semitone_offset_from_C, letter_offset_from_C)
TWELVE_KEYS = [
    ("C",  0, 0), ("Db", 1, 1), ("D",  2, 1), ("Eb", 3, 2), ("E",  4, 2),
    ("F",  5, 3), ("Gb", 6, 4), ("G",  7, 4), ("Ab", 8, 5),
    ("A",  9, 5), ("Bb",10, 6), ("B", 11, 6),
]

# Map of enharmonic equivalents to standard key names
ENHARMONIC_NORMALIZE = {
    'Fb': 'E', 'Cb': 'B', 'B#': 'C', 'E#': 'F',
    'F##': 'G', 'C##': 'D', 'G##': 'A', 'D##': 'E',
    'Abb': 'G', 'Ebb': 'D', 'Bbb': 'A', 'Fbb': 'Eb',
    'Gbb': 'F', 'Dbb': 'C', 'Cbb': 'Bb',
}

def concert_key_label(written_root_name, inst_semi, inst_letter):
    """Given a written key root and instrument transposition, compute the concert key name.
    Concert = written - instrument_offset, i.e. transpose DOWN by the instrument interval."""
    letter, acc = parse_note(written_root_name)
    reverse_semi = (12 - inst_semi) % 12
    reverse_letter = (7 - inst_letter) % 7
    concert_l, concert_a = transpose_note(letter, acc, reverse_semi, reverse_letter)
    name = note_display(concert_l, concert_a)
    return ENHARMONIC_NORMALIZE.get(name, name)

# ── Drawing helpers ───────────────────────────────────────────────────

def staff_y_position(letter, acc, octave, staff_bottom_y):
    """Get the y coordinate for a note on the staff.
    staff_bottom_y = y of the bottom staff line.
    E4 sits on the bottom line."""
    # Diatonic position: E4 = 0 (bottom line)
    letter_pos = NOTE_LETTERS.index(letter)
    pos = letter_pos + (octave - 4) * 7 - 2  # E4 => 2 + 0 - 2 = 0
    half_space = STAFF_LINE_SPACING / 2.0
    return staff_bottom_y + pos * half_space

def choose_octave_for_scale(notes, instrument):
    """Choose a starting octave so the scale sits nicely on the treble clef staff.
    We want most notes between E4 and F5 (the staff lines).
    For alto sax scales starting on A, start at A4.
    For tenor sax scales starting on D, start at D4 or D5."""
    first_letter, first_acc = notes[0]
    first_midi_in_octave_4 = NATURAL_SEMITONES[first_letter] + first_acc

    # Try octave 4 first, check if scale stays in reasonable range
    # Compute all midi values
    octave = 4
    midi_values = []
    current_midi = note_to_midi(first_letter, first_acc, octave)
    midi_values.append(current_midi)
    for i in range(1, len(notes)):
        l, a = notes[i]
        candidate = note_to_midi(l, a, octave)
        # If this note would be lower than the previous, bump octave
        if candidate <= midi_values[-1]:
            octave += 1
            candidate = note_to_midi(l, a, octave)
        midi_values.append(candidate)
        # Track octave for next note
        if i < len(notes) - 1:
            # Reset octave based on current note's actual octave
            octave = (candidate - NATURAL_SEMITONES[l] - a) // 12

    # Check range — we want bottom note around C4-E4 for comfortable reading
    min_midi = min(midi_values)
    # If lowest note is below C4 (midi 48), shift everything up
    if min_midi < 48:
        return 5
    # If lowest note is above A4 (midi 69), shift down
    if min_midi > 69:
        return 4
    return 4

def compute_note_positions(notes, start_octave):
    """Given a list of (letter, acc) for a scale, compute (letter, acc, octave) for each note,
    ensuring ascending order."""
    result = []
    octave = start_octave
    prev_midi = -1
    for i, (letter, acc) in enumerate(notes):
        midi = note_to_midi(letter, acc, octave)
        if i > 0 and midi <= prev_midi:
            octave += 1
            midi = note_to_midi(letter, acc, octave)
        result.append((letter, acc, octave))
        prev_midi = midi
    return result

def draw_treble_clef(c, x, staff_bottom_y):
    """Draw a simplified treble clef symbol."""
    # Use text-based approach with a large font
    c.saveState()
    # Try to use a font that has the treble clef
    try:
        c.setFont("Helvetica-Bold", 28)
    except:
        c.setFont("Helvetica-Bold", 28)
    # Draw a stylized G-clef using curves
    # Simple approach: draw the & symbol or use line art
    # Let's draw a proper-ish treble clef with bezier curves
    by = staff_bottom_y
    ls = STAFF_LINE_SPACING

    c.setLineWidth(1.5)
    c.setStrokeColorRGB(0, 0, 0)
    c.setFillColorRGB(0, 0, 0)

    # Treble clef approximation using bezier paths
    cx = x + 8
    p = c.beginPath()

    # Bottom curl
    p.moveTo(cx + 2, by - ls * 0.5)
    p.curveTo(cx - 6, by + ls * 0.3, cx - 4, by + ls * 1.8, cx + 3, by + ls * 2.0)
    # Main curve up
    p.curveTo(cx + 10, by + ls * 2.2, cx + 10, by + ls * 3.2, cx + 4, by + ls * 3.8)
    # Top curve
    p.curveTo(cx - 2, by + ls * 4.5, cx - 8, by + ls * 3.5, cx - 6, by + ls * 2.5)
    # Back down through center
    p.curveTo(cx - 4, by + ls * 1.5, cx - 1, by + ls * 0.8, cx + 2, by - ls * 0.5)

    c.drawPath(p, stroke=1, fill=0)

    # Vertical line through clef
    c.line(cx + 1, by - ls * 0.8, cx + 1, by + ls * 4.3)

    # Small bottom circle
    c.circle(cx, by - ls * 0.8, 2, fill=1)

    c.restoreState()

def draw_staff(c, x_start, x_end, y_bottom):
    """Draw 5 staff lines."""
    c.setLineWidth(0.5)
    c.setStrokeColorRGB(0, 0, 0)
    for i in range(5):
        y = y_bottom + i * STAFF_LINE_SPACING
        c.line(x_start, y, x_end, y)

def draw_notehead(c, x, y, filled=True):
    """Draw an elliptical notehead."""
    c.saveState()
    c.setFillColorRGB(0, 0, 0)
    # Slightly tilted ellipse
    c.translate(x, y)
    c.rotate(20)
    if filled:
        c.ellipse(-4.5, -3, 4.5, 3, fill=1, stroke=0)
    else:
        c.setLineWidth(1.2)
        c.ellipse(-4.5, -3, 4.5, 3, fill=0, stroke=1)
    c.restoreState()

def draw_ledger_lines(c, x, y, staff_bottom_y):
    """Draw ledger lines if note is above or below the staff."""
    ls = STAFF_LINE_SPACING
    staff_top_y = staff_bottom_y + 4 * ls

    # Below staff
    line_y = staff_bottom_y - ls
    while line_y >= y - ls * 0.3:
        c.setLineWidth(0.8)
        c.line(x - 8, line_y, x + 8, line_y)
        line_y -= ls

    # Above staff
    line_y = staff_top_y + ls
    while line_y <= y + ls * 0.3:
        c.setLineWidth(0.8)
        c.line(x - 8, line_y, x + 8, line_y)
        line_y += ls

def draw_accidental(c, x, y, acc):
    """Draw accidental symbol to the left of a note."""
    c.saveState()
    c.setFont("Helvetica-Bold", 11)
    c.setFillColorRGB(0, 0, 0)
    if acc == 1:
        c.drawString(x - 12, y - 4, "#")
    elif acc == -1:
        c.drawString(x - 11, y - 4, "b")
    elif acc == 2:
        c.drawString(x - 17, y - 4, "##")
    elif acc == -2:
        c.drawString(x - 15, y - 4, "bb")
    c.restoreState()

def draw_scale_on_staff(c, scale_notes_with_octave, staff_bottom_y, x_start, label_name, chord_sym, interval_str, concert_label=""):
    """Draw a single scale on a staff."""
    staff_width = STAFF_RIGHT - MARGIN
    x_end = STAFF_RIGHT

    # Draw staff
    draw_staff(c, MARGIN, x_end, staff_bottom_y)

    # Draw clef
    draw_treble_clef(c, MARGIN + 2, staff_bottom_y)

    # Label above staff
    c.saveState()
    c.setFont("Helvetica-Bold", 9)
    label_y = staff_bottom_y + 5 * STAFF_LINE_SPACING + 6
    main_label = f"{chord_sym}  \u2014  {label_name}"
    c.drawString(MARGIN, label_y, main_label)
    if concert_label:
        c.setFont("Helvetica", 7)
        c.setFillColorRGB(0.4, 0.4, 0.4)
        label_width = c.stringWidth(main_label, "Helvetica-Bold", 9)
        c.drawString(MARGIN + label_width + 10, label_y, concert_label)

    # Interval pattern below staff
    c.setFont("Helvetica", 7)
    c.setFillColorRGB(0.3, 0.3, 0.3)
    c.drawString(MARGIN, staff_bottom_y - STAFF_LINE_SPACING * 1.8, interval_str)
    c.restoreState()

    # Draw notes — ascending then descending
    # Build the full ascending + descending sequence
    # Ascending is the full scale; descending omits the top note (already played) and goes back down
    full_sequence = list(scale_notes_with_octave)
    if len(scale_notes_with_octave) > 2:
        descending = list(reversed(scale_notes_with_octave[:-1]))  # skip last (top) note, reverse the rest
        full_sequence.extend(descending[1:])  # skip the second-to-top since it's already there

    note_x = x_start
    for letter, acc, octave in full_sequence:
        y = staff_y_position(letter, acc, octave, staff_bottom_y)
        draw_ledger_lines(c, note_x, y, staff_bottom_y)
        draw_notehead(c, note_x, y)
        if acc != 0:
            draw_accidental(c, note_x, y, acc)

        # Note name below
        c.saveState()
        c.setFont("Helvetica", 5)
        c.setFillColorRGB(0.4, 0.4, 0.4)
        name = note_display(letter, acc)
        c.drawCentredString(note_x, staff_bottom_y - STAFF_LINE_SPACING * 2.5, name)
        c.restoreState()

        note_x += NOTE_SPACING

def get_interval_str(notes):
    """Compute interval string from consecutive notes."""
    intervals = []
    for i in range(len(notes) - 1):
        l1, a1 = notes[i]
        l2, a2 = notes[i + 1]
        # Compute semitone difference
        s1 = NATURAL_SEMITONES[l1] + a1
        s2 = NATURAL_SEMITONES[l2] + a2
        diff = (s2 - s1) % 12
        if diff == 0:
            diff = 12
        if diff == 1:
            intervals.append("H")
        elif diff == 2:
            intervals.append("W")
        elif diff == 3:
            intervals.append("m3")
        else:
            intervals.append(f"{diff}H")
    return " ".join(intervals)

# ── Transposition configs ─────────────────────────────────────────────

INSTRUMENTS = [
    ("Alto Saxophone (Eb)", 9, 5),   # +9 semitones, +5 letters
    ("Tenor Saxophone (Bb)", 2, 1),   # +2 semitones, +1 letter
]

# ── Chord transposition and rendering ─────────────────────────────────

def transpose_chord_tones(tones, semitone_offset, letter_offset):
    return [transpose_note(l, a, semitone_offset, letter_offset) for l, a in tones]

def transpose_root_name(root_name, semitone_offset, letter_offset):
    """Transpose a root name like 'C', 'Db', 'F#' etc."""
    letter, acc = parse_note(root_name)
    new_l, new_a = transpose_note(letter, acc, semitone_offset, letter_offset)
    return note_display(new_l, new_a)

# ── PDF Generation ────────────────────────────────────────────────────

def new_page_with_header(c, title, subtitle=""):
    c.showPage()
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(PAGE_W / 2, PAGE_H - MARGIN - 10, title)
    if subtitle:
        c.setFont("Helvetica", 10)
        c.drawCentredString(PAGE_W / 2, PAGE_H - MARGIN - 26, subtitle)
    return PAGE_H - MARGIN - 50  # return starting y for content

def generate_pdf(output_path):
    c = canvas.Canvas(output_path, pagesize=letter)

    # ── Title Page ────────────────────────────────────────────────
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 + 60, "Scale & Chord Reference")
    c.setFont("Helvetica", 16)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 + 30, "for Alto Saxophone & Tenor Saxophone")
    c.setFont("Helvetica", 11)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 10, "Based on the FQBK Handbook Scale Syllabus")
    c.setFont("Helvetica", 9)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 40, "All scales in all 12 keys, transposed for each instrument.")
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 55, "Note names shown below each notehead for reference.")

    c.setFont("Helvetica", 8)
    c.drawCentredString(PAGE_W / 2, MARGIN + 20,
        "Legend: W = Whole Step, H = Half Step, m3 = Minor Third (3 half steps)")

    # ── Scale Pages ───────────────────────────────────────────────
    scale_height = STAFF_LINE_SPACING * 4 + STAFF_LINE_SPACING * 6  # staff + padding
    scales_per_page = 5

    for inst_name, inst_semi, inst_letter in INSTRUMENTS:
        for cat_name, scales in PARSED_CATEGORIES:
            for scale_name, chord_sym, concert_notes in scales:
                # Extract chord symbol suffix (everything after the root)
                root_end = 1
                while root_end < len(chord_sym) and chord_sym[root_end] in ('b', '#', '\u266d', '\u266f'):
                    root_end += 1
                suffix = chord_sym[root_end:]

                # Compute interval string (same for all keys)
                interval_str = get_interval_str(concert_notes)

                # Generate this scale in all 12 written keys
                count_on_page = 0
                cursor_y = None
                for key_name, key_semi, key_letter_off in TWELVE_KEYS:
                    if count_on_page == 0 or count_on_page >= scales_per_page:
                        page_title = f"{inst_name}"
                        subtitle = f"{cat_name} \u2014 {scale_name}"
                        if cursor_y is not None:
                            subtitle += " (cont.)"
                        cursor_y = new_page_with_header(c, page_title, subtitle)
                        count_on_page = 0

                    # Build scale in this written key by transposing from C
                    transposed = transpose_scale(concert_notes, key_semi, key_letter_off)

                    # Build chord symbol with this key's root
                    root_l, root_a = parse_note("C")
                    new_root_l, new_root_a = transpose_note(root_l, root_a, key_semi, key_letter_off)
                    written_chord_sym = note_display(new_root_l, new_root_a) + suffix

                    # Concert key label
                    ck = concert_key_label(key_name, inst_semi, inst_letter)
                    label_with_concert = f"(Concert: {ck})"

                    # Choose octave and compute positions
                    start_oct = choose_octave_for_scale(transposed, inst_name)
                    notes_with_oct = compute_note_positions(transposed, start_oct)

                    # Calculate staff bottom y
                    staff_bottom = cursor_y - STAFF_LINE_SPACING * 4
                    note_x_start = STAFF_LEFT + 20

                    draw_scale_on_staff(c, notes_with_oct, staff_bottom, note_x_start,
                                       scale_name, written_chord_sym, interval_str,
                                       concert_label=label_with_concert)

                    cursor_y -= scale_height + 12
                    count_on_page += 1

    # ── Chord Reference Pages ─────────────────────────────────────
    for inst_name, semi_offset, letter_offset in INSTRUMENTS:
        cursor_y = new_page_with_header(c, f"Chord Reference \u2014 {inst_name}",
                                        "Chord tones for all 12 keys")

        # Table header
        c.setFont("Helvetica-Bold", 8)
        col_x = MARGIN
        col_w = (PAGE_W - 2 * MARGIN) / 6  # Key, Maj7, Dom7, Min7, HalfDim, Dim7

        headers = ["Key", "Major 7th (\u0394)", "Dom. 7th (7)", "Minor 7th (\u20137)",
                   "Half Dim. (\u00d8)", "Dim. 7th (\u00b0)"]
        for i, h in enumerate(headers):
            c.drawString(col_x + i * col_w, cursor_y, h)

        cursor_y -= 4
        c.setLineWidth(0.5)
        c.line(MARGIN, cursor_y, PAGE_W - MARGIN, cursor_y)
        cursor_y -= 12

        c.setFont("Helvetica", 7.5)
        row_height = 14

        for key_idx, (key_name, key_semi, key_letter_off) in enumerate(TWELVE_KEYS):
            if cursor_y < MARGIN + 30:
                cursor_y = new_page_with_header(c, f"Chord Reference \u2014 {inst_name}",
                                                "Chord tones for all 12 keys (cont.)")
                # Redraw headers
                c.setFont("Helvetica-Bold", 8)
                for i, h in enumerate(headers):
                    c.drawString(col_x + i * col_w, cursor_y, h)
                cursor_y -= 4
                c.line(MARGIN, cursor_y, PAGE_W - MARGIN, cursor_y)
                cursor_y -= row_height
                c.setFont("Helvetica", 7.5)

            # Alternating row background (draw BEFORE text so it doesn't cover it)
            if key_idx % 2 == 0:
                c.saveState()
                c.setFillColorRGB(0.93, 0.93, 0.93)
                c.rect(MARGIN, cursor_y - 4, PAGE_W - 2 * MARGIN, row_height, fill=1, stroke=0)
                c.restoreState()

            # Transpose key name for instrument
            inst_key = transpose_root_name(key_name, semi_offset, letter_offset)
            c.setFont("Helvetica-Bold", 8.5)
            c.drawString(col_x, cursor_y, inst_key)
            c.setFont("Helvetica", 8)

            for ci, (chord_type_name, chord_suffix, chord_tones) in enumerate(CHORD_TYPES):
                # Transpose chord tones from C to this key, then to instrument
                total_semi = (key_semi + semi_offset) % 12
                total_letter = (key_letter_off + letter_offset) % 7
                transposed_tones = transpose_chord_tones(chord_tones, total_semi, total_letter)
                tone_str = " ".join(note_display(l, a) for l, a in transposed_tones)
                c.drawString(col_x + (ci + 1) * col_w, cursor_y, tone_str)

            cursor_y -= row_height

    c.save()
    print(f"PDF saved to: {output_path}")

if __name__ == "__main__":
    output = r"C:\Users\nicwo\Downloads\Scale_and_Chord_Reference_Saxophones.pdf"
    generate_pdf(output)
