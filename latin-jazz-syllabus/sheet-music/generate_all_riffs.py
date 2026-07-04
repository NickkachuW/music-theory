"""
Generate MusicXML sheet music files for all Latin Jazz & Tango riffs and licks.
Open these in MuseScore, Finale, Sibelius, Flat.io, or any MusicXML-compatible app.
"""
import os
from music21 import (
    stream, note, chord, key, meter, tempo, clef,
    metadata, expressions, layout, instrument
)

OUT = r"C:\Users\nicwo\Projects\music theory\latin-jazz-syllabus\sheet-music"
os.makedirs(OUT, exist_ok=True)

def make_note(pitch_str, dur='quarter', dots=0):
    """Create a note. dur: 'whole','half','quarter','eighth','16th'"""
    n = note.Note(pitch_str)
    n.duration.type = dur
    n.duration.dots = dots
    return n

def make_rest(dur='quarter', dots=0):
    r = note.Rest()
    r.duration.type = dur
    r.duration.dots = dots
    return r

def build_score(title, subtitle, parts_data, ts='4/4', bpm=120, sax_type='alto'):
    """
    Build a score with one or more labeled lines.
    parts_data: list of (label, [note_objects])
    """
    score = stream.Score()
    score.metadata = metadata.Metadata()
    score.metadata.title = title
    score.metadata.movementName = subtitle

    for label, notes in parts_data:
        part = stream.Part()
        if sax_type == 'alto':
            inst = instrument.AltoSaxophone()
        else:
            inst = instrument.TenorSaxophone()
        part.insert(0, inst)

        m = stream.Measure(number=1)
        m.insert(0, meter.TimeSignature(ts))
        m.insert(0, tempo.MetronomeMark(number=bpm))

        # Add a text expression for the label
        if label:
            te = expressions.TextExpression(label)
            te.style.fontWeight = 'bold'
            te.style.fontSize = 11
            m.insert(0, te)

        current_measure = m
        beat_count = 0
        beats_per_measure = int(ts.split('/')[0])

        for n in notes:
            dur_beats = n.duration.quarterLength
            if beat_count + dur_beats > beats_per_measure:
                part.append(current_measure)
                current_measure = stream.Measure()
                beat_count = 0
            current_measure.append(n)
            beat_count += dur_beats

        if len(current_measure.notes) > 0 or len(current_measure.notesAndRests) > 0:
            # Pad final measure with rests if needed
            remaining = beats_per_measure - beat_count
            if remaining > 0 and remaining < beats_per_measure:
                r = note.Rest()
                r.duration.quarterLength = remaining
                current_measure.append(r)
            part.append(current_measure)

        score.append(part)

    return score

def save(score, filename):
    path = os.path.join(OUT, filename)
    score.write('musicxml', fp=path)
    print(f"  Created: {filename}")


# ════════════════════════════════════════════════════════════
# FILE 1: LATIN JAZZ RIFFS OVER MINOR VAMPS (D Dorian)
# ════════════════════════════════════════════════════════════
print("Generating Latin Jazz Minor Vamp Riffs...")

riffs = []

# Riff 1: Pentatonic Call
notes1 = [make_note('D4','eighth'), make_note('F4','eighth'),
          make_note('G4','eighth'), make_note('A4','eighth'),
          make_note('C5','eighth'), make_note('D5','quarter', dots=1)]
riffs.append(("1. Pentatonic Call (D Dorian)", notes1))

# Riff 2: Falling Answer
notes2 = [make_note('C5','eighth'), make_note('A4','eighth'),
          make_note('G4','eighth'), make_note('F4','eighth'),
          make_note('D4','half')]
riffs.append(("2. Falling Answer", notes2))

# Riff 3: The Montuno Riff
notes3 = [make_note('D4','eighth'), make_note('F4','eighth'),
          make_note('A4','quarter'),
          make_note('C5','eighth'), make_note('A4','eighth'),
          make_note('F4','quarter')]
riffs.append(("3. The Montuno Riff", notes3))

# Riff 4: Root-5th Anchor
notes4 = [make_note('D4','quarter'), make_rest('quarter'),
          make_note('A4','quarter'), make_rest('quarter'),
          make_note('D5','quarter'), make_rest('quarter'),
          make_note('A4','quarter'), make_note('D4','quarter')]
riffs.append(("4. Root-5th Anchor (marcato)", notes4))

# Riff 5: Dorian Signature
notes5 = [make_note('D4','eighth'), make_note('E4','eighth'),
          make_note('F4','eighth'), make_note('A4','eighth'),
          make_note('G4','eighth'), make_note('E4','eighth'),
          make_note('D4','quarter')]
riffs.append(("5. Dorian Signature (1-2-b3-5-4-2-1)", notes5))

# Riff 6: Blue Note Dip
notes6 = [make_note('D4','eighth'), make_note('F4','eighth'),
          make_note('G4','eighth'), make_note('G#4','eighth'),
          make_note('A4','eighth'), make_note('C5','eighth'),
          make_note('D5','quarter')]
riffs.append(("6. Blue Note Dip (with b5 passing tone)", notes6))

# Riff 7: Clave Melody (notes on clave hits, rests between)
notes7 = [make_note('D4','quarter', dots=1), make_note('F4','quarter', dots=1),
          make_note('A4','quarter'),
          make_rest('quarter'), make_rest('eighth'),
          make_note('G4','quarter', dots=1), make_note('D4','quarter')]
riffs.append(("7. Clave Melody (notes on clave hits)", notes7))

# Riff 8: Syncopated 3rds
notes8 = [make_rest('eighth'), make_note('D4','eighth'), make_note('F4','eighth'), make_rest('eighth'),
          make_rest('eighth'), make_note('E4','eighth'), make_note('G4','eighth'), make_rest('eighth'),
          make_rest('eighth'), make_note('F4','eighth'), make_note('A4','eighth'), make_rest('eighth'),
          make_rest('eighth'), make_note('G4','eighth'), make_note('B-4','eighth'), make_rest('eighth')]
riffs.append(("8. Syncopated 3rds (upbeat pairs)", notes8))

s1 = build_score(
    "Latin Jazz Riffs - Minor Vamps",
    "D Dorian (concert F/C) - Transpose to all 12 keys",
    riffs, bpm=110
)
save(s1, "01_latin_jazz_minor_vamp_riffs.musicxml")


# ════════════════════════════════════════════════════════════
# FILE 2: ii-V-i LICKS (Dm7 - G7b9 - Cm)
# ════════════════════════════════════════════════════════════
print("Generating ii-V-i Licks...")

licks = []

# Lick 1: Smooth Dorian-Spanish
l1 = [make_note('D4','eighth'), make_note('E4','eighth'),
      make_note('F4','eighth'), make_note('G4','eighth'),  # Dm7
      make_note('A-4','eighth'), make_note('B4','eighth'),
      make_note('D5','eighth'), make_note('F5','eighth'),  # G7b9
      make_note('E-5','quarter'), make_note('D5','quarter'),
      make_note('C5','half')]  # Cm
licks.append(("1. Smooth Dorian-Spanish", l1))

# Lick 2: Bebop Connector
l2 = [make_note('A4','eighth'), make_note('G4','eighth'),
      make_note('F4','eighth'), make_note('E4','eighth'),  # Dm7
      make_note('F4','eighth'), make_note('A-4','eighth'),
      make_note('B4','eighth'), make_note('D5','eighth'),  # G7b9
      make_note('E-5','quarter'), make_note('C5','half')]  # Cm
licks.append(("2. Bebop Connector (descending into tension)", l2))

# Lick 3: Enclosure Lick
l3 = [make_note('E4','eighth'), make_note('D4','eighth'),
      make_note('F4','eighth'), make_note('E4','eighth'),  # Dm7
      make_note('A-4','eighth'), make_note('G4','eighth'),
      make_note('B4','eighth'), make_note('A-4','eighth'),  # G7b9
      make_note('G4','eighth'), make_note('E-4','eighth'),
      make_note('D4','eighth'), make_note('C4','quarter', dots=1)]  # Cm
licks.append(("3. Enclosure Lick (surround target notes)", l3))

# Lick 4: Arpeggio + Scale
l4 = [make_note('D4','eighth'), make_note('F4','eighth'),
      make_note('A4','eighth'), make_note('C5','eighth'),  # Dm7 arp
      make_note('B4','eighth'), make_note('D5','eighth'),
      make_note('F5','eighth'), make_note('A-4','eighth'),  # G7b9 arp
      make_note('G4','eighth'), make_note('E-4','eighth'),
      make_note('D4','eighth'), make_note('C4','quarter', dots=1)]  # Cm
licks.append(("4. Arpeggio + Scale Fill", l4))

# Lick 5: Altered Tension
l5 = [make_note('D4','eighth'), make_note('F4','eighth'),
      make_note('G4','eighth'), make_note('A4','eighth'),  # Dm7
      make_note('A-4','eighth'), make_note('B-4','eighth'),
      make_note('D-5','eighth'), make_note('E5','eighth'),  # G7 altered
      make_note('E-5','quarter'), make_note('D5','quarter'),
      make_note('C5','half')]  # Cm
licks.append(("5. Altered Tension (max tension on V)", l5))

# Lick 6: Pentatonic Shift
l6 = [make_note('D4','eighth'), make_note('F4','eighth'),
      make_note('G4','eighth'), make_note('A4','eighth'),
      make_note('C5','eighth'),  # Dm pent
      make_note('D-5','eighth'), make_note('A-4','eighth'),
      make_note('G-4','eighth'),  # Db pent over G7
      make_note('C4','half'),  # Cm
      make_note('E-4','quarter'), make_note('G4','quarter')]
licks.append(("6. Pentatonic Shift (Dm pent -> Db pent -> Cm)", l6))

# Lick 7: Chromatic Approach
l7 = [make_note('A4','eighth'), make_note('G4','eighth'),
      make_note('F4','eighth'), make_note('E4','eighth'),  # Dm7
      make_note('E-4','eighth'), make_note('D4','eighth'),
      make_note('D-4','eighth'), make_note('C4','eighth'),
      make_note('B3','eighth'),  # chromatic descent to...
      make_note('C4','quarter', dots=1)]  # Cm
licks.append(("7. Chromatic Approach (half steps into resolution)", l7))

# Lick 8: Spanish Signature Run
l8 = [make_note('D4','eighth'), make_note('E4','eighth'),
      make_note('F4','eighth'), make_note('G4','eighth'),  # Dm7
      make_note('G4','eighth'), make_note('A-4','eighth'),
      make_note('B4','eighth'), make_note('C5','eighth'),
      make_note('D5','eighth'), make_note('E-5','eighth'),
      make_note('F5','eighth'),  # G Spanish run
      make_note('E-5','eighth'),
      make_note('D5','quarter'), make_note('C5','half')]  # Cm
licks.append(("8. Spanish Signature (full Spanish run on V)", l8))

s2 = build_score(
    "ii-V-i Licks",
    "Dm7 - G7b9 - Cm (transpose to all 12 minor keys)",
    licks, bpm=100
)
save(s2, "02_ii_V_i_licks.musicxml")


# ════════════════════════════════════════════════════════════
# FILE 3: DOMINANT 7th FLAVOR COMPARISON (all over G7 -> Cm)
# ════════════════════════════════════════════════════════════
print("Generating Dominant Flavor Comparison...")

dom_flavors = []

# Mixolydian (vanilla)
df1 = [make_note('G4','eighth'), make_note('A4','eighth'),
       make_note('B4','eighth'), make_note('D5','eighth'),
       make_note('C5','eighth'), make_note('B4','eighth'),
       make_note('A4','eighth'), make_note('G4','eighth')]
dom_flavors.append(("1. Mixolydian (vanilla)", df1))

# Spanish/Jewish (salsa fire)
df2 = [make_note('G4','eighth'), make_note('A-4','eighth'),
       make_note('B4','eighth'), make_note('C5','eighth'),
       make_note('D5','eighth'), make_note('E-5','eighth'),
       make_note('F5','eighth'), make_note('G5','eighth')]
dom_flavors.append(("2. Spanish/Jewish (salsa fire)", df2))

# Bebop Dominant
df3 = [make_note('G4','eighth'), make_note('A4','eighth'),
       make_note('B4','eighth'), make_note('C5','eighth'),
       make_note('D5','eighth'), make_note('E5','eighth'),
       make_note('F5','eighth'), make_note('F#5','eighth')]
dom_flavors.append(("3. Bebop Dominant (smooth 8ths)", df3))

# Diminished H-W
df4 = [make_note('G4','eighth'), make_note('A-4','eighth'),
       make_note('A#4','eighth'), make_note('B4','eighth'),
       make_note('C#5','eighth'), make_note('D5','eighth'),
       make_note('E5','eighth'), make_note('F5','eighth')]
dom_flavors.append(("4. Diminished H-W (angular, symmetric)", df4))

# Altered
df5 = [make_note('G4','eighth'), make_note('A-4','eighth'),
       make_note('B-4','eighth'), make_note('B4','eighth'),
       make_note('D-5','eighth'), make_note('E-5','eighth'),
       make_note('F5','quarter')]
dom_flavors.append(("5. Altered (maximum heat)", df5))

# Whole Tone
df6 = [make_note('G4','eighth'), make_note('A4','eighth'),
       make_note('B4','eighth'), make_note('C#5','eighth'),
       make_note('D#5','eighth'), make_note('F5','quarter', dots=1)]
dom_flavors.append(("6. Whole Tone (floating, dreamy)", df6))

# Blues
df7 = [make_note('G4','eighth'), make_note('B-4','eighth'),
       make_note('C5','eighth'), make_note('C#5','eighth'),
       make_note('D5','quarter'),
       make_note('F5','eighth'), make_note('D5','eighth')]
dom_flavors.append(("7. Blues (earthy, soulful)", df7))

# Lydian Dominant
df8 = [make_note('G4','eighth'), make_note('A4','eighth'),
       make_note('B4','eighth'), make_note('C#5','eighth'),
       make_note('D5','eighth'), make_note('E5','eighth'),
       make_note('F5','quarter')]
dom_flavors.append(("8. Lydian Dominant (bright, non-resolving)", df8))

s3 = build_score(
    "Dominant 7th Flavor Comparison",
    "8 ways to play over G7 -> Cm",
    dom_flavors, bpm=110
)
save(s3, "03_dominant_flavor_comparison.musicxml")


# ════════════════════════════════════════════════════════════
# FILE 4: PENTATONIC TRICKS (D minor pentatonic)
# ════════════════════════════════════════════════════════════
print("Generating Pentatonic Tricks...")

pent = []

# Ascending 4ths
p1 = [make_note('D4','eighth'), make_note('G4','eighth'),
      make_note('F4','eighth'), make_note('A4','eighth'),
      make_note('G4','eighth'), make_note('C5','eighth'),
      make_note('A4','eighth'), make_note('D5','eighth')]
pent.append(("1. Ascending 4ths", p1))

# Falling 3rds
p2 = [make_note('A4','eighth'), make_note('F4','eighth'),
      make_note('G4','eighth'), make_note('D4','eighth'),
      make_note('F4','eighth'), make_note('C4','eighth'),
      make_note('D4','half')]
pent.append(("2. Falling 3rds", p2))

# Skip Pattern (zigzag)
p3 = [make_note('D4','eighth'), make_note('G4','eighth'),
      make_note('F4','eighth'), make_note('A4','eighth'),
      make_note('G4','eighth'), make_note('C5','eighth'),
      make_note('A4','eighth'), make_note('D5','eighth')]
pent.append(("3. Skip Pattern (zigzag)", p3))

# Repeated Cell (3-note groups)
p4 = [make_note('D4','eighth'), make_note('F4','eighth'),
      make_note('G4','eighth'),
      make_note('F4','eighth'), make_note('G4','eighth'),
      make_note('A4','eighth'),
      make_note('G4','eighth'), make_note('A4','eighth'),
      make_note('C5','eighth'),
      make_note('A4','eighth'), make_note('C5','eighth'),
      make_note('D5','quarter')]
pent.append(("4. Repeated Cell (3-note groups shifting up)", p4))

# Call & Response
p5 = [make_note('D4','eighth'), make_note('F4','eighth'),
      make_note('G4','eighth'), make_note('A4','quarter', dots=1),
      make_rest('quarter'),
      make_note('C5','eighth'), make_note('A4','eighth'),
      make_note('G4','eighth'), make_note('F4','quarter', dots=1)]
pent.append(("5. Call & Response (leave space!)", p5))

# Octave Displacement
p6 = [make_note('D3','eighth'), make_note('F4','eighth'),
      make_note('G3','eighth'), make_note('A4','eighth'),
      make_note('C4','eighth'), make_note('D5','eighth'),
      make_rest('quarter')]
pent.append(("6. Octave Displacement (dramatic jumps)", p6))

# Clave Pentatonic
p7 = [make_note('D4','quarter', dots=1), make_note('F4','quarter', dots=1),
      make_note('G4','quarter'),
      make_rest('quarter'), make_rest('eighth'),
      make_note('A4','quarter', dots=1), make_note('C5','quarter')]
pent.append(("7. Clave Pentatonic (notes on clave)", p7))

# Pent over V7 substitution
p8_notes = [make_note('A-4','eighth'), make_note('C-5','eighth'),
            make_note('D-5','eighth'), make_note('E-5','eighth'),
            make_note('G-5','eighth'), make_note('A-5','eighth'),
            make_note('G5','quarter')]  # resolve
pent.append(("8. Ab minor pent over G7 (b9-3-b5-b13-b7)", p8_notes))

s4 = build_score(
    "Pentatonic Tricks",
    "D minor pentatonic patterns - Transpose to all keys",
    pent, bpm=110
)
save(s4, "04_pentatonic_tricks.musicxml")


# ════════════════════════════════════════════════════════════
# FILE 5: TANGO MELODIC PATTERNS (A harmonic minor)
# ════════════════════════════════════════════════════════════
print("Generating Tango Melodic Patterns...")

tango = []

# The Tango Sigh
t1 = [make_note('B4','eighth'), make_note('C5','eighth'),
      make_note('B4','quarter'),
      make_note('A4','eighth'), make_note('G#4','eighth'),
      make_note('A4','half')]
tango.append(("1. The Tango Sigh (upper neighbor, fall back)", t1))

# Dramatic Leap + Descent
t2 = [make_note('A3','quarter'),
      make_note('E4','eighth'), make_note('D4','eighth'),
      make_note('C4','eighth'), make_note('B3','eighth'),
      make_note('A3','quarter')]
tango.append(("2. Dramatic Leap + Stepwise Descent", t2))

# Augmented 2nd Cry
t3 = [make_note('F4','quarter'), make_note('G#4','quarter'),
      make_note('A4','half'),
      make_note('F4','quarter'), make_note('G#4','eighth'),
      make_note('A4','eighth'), make_note('B4','half')]
tango.append(("3. Augmented 2nd Cry (F-G#-A = tango DNA)", t3))

# Chromatic Approach
t4 = [make_note('G#3','eighth'), make_note('A3','eighth'),
      make_note('B#3','eighth'), make_note('C4','eighth'),
      make_note('D#4','eighth'), make_note('E4','eighth'),
      make_note('F4','eighth'), make_note('G#4','eighth'),
      make_note('A4','half')]
tango.append(("4. Chromatic Approach (half step below each note)", t4))

# Phrygian Cadence Lick
t5 = [make_note('B-4','eighth'), make_note('A4','eighth'),
      make_note('G#4','eighth'), make_note('A4','quarter', dots=1),
      make_note('F4','eighth'), make_note('E4','eighth'),
      make_note('D#4','eighth'), make_note('E4','half')]
tango.append(("5. Phrygian Cadence Lick (bII melting to V to i)", t5))

# Bandoneon Imitation
t6 = [make_note('A4','eighth'), make_note('E4','eighth'),
      make_note('C4','eighth'), make_note('A3','eighth'),
      make_note('E4','eighth'), make_note('C4','eighth'),
      make_note('A3','quarter')]
tango.append(("6. Bandoneon Imitation (descending arp, staccato)", t6))

# 3-3-2 Harmonic Minor
t7 = [make_note('A4','eighth'), make_note('B4','eighth'),
      make_note('C5','eighth'),
      make_note('D5','eighth'), make_note('E5','eighth'),
      make_note('F5','eighth'),
      make_note('G#5','quarter'), make_note('A5','quarter')]
tango.append(("7. 3-3-2 Harmonic Minor grouping", t7))

# Double Neighbor
t8 = [make_note('G#4','eighth'), make_note('B-4','eighth'),
      make_note('A4','quarter'),
      make_note('D#4','eighth'), make_note('F4','eighth'),
      make_note('E4','half')]
tango.append(("8. Double Neighbor (surround from above & below)", t8))

# Piazzolla Sequence (rising 3rds)
t9 = [make_note('A3','eighth'), make_note('C4','eighth'),
      make_note('E4','eighth'),
      make_note('B3','eighth'), make_note('D4','eighth'),
      make_note('F4','eighth'),
      make_note('C4','eighth'), make_note('E4','eighth'),
      make_note('G#4','eighth'),
      make_note('A4','quarter', dots=1)]
tango.append(("9. Piazzolla Sequence (rising 3rds through harm. minor)", t9))

# Tango Ending
t10 = [make_note('E4','eighth'), make_note('D#4','eighth'),
       make_note('E4','quarter'),
       make_note('F4','eighth'), make_note('E4','eighth'),
       make_note('D4','eighth'), make_note('C4','eighth'),
       make_note('B3','eighth'), make_note('A3','quarter', dots=1)]
tango.append(("10. Tango Ending (turn on 5th, descend to tonic)", t10))

s5 = build_score(
    "Tango Melodic Patterns",
    "A harmonic minor (concert C/G) - Use 3-3-2 rhythmic feel",
    tango, bpm=90
)
save(s5, "05_tango_melodic_patterns.musicxml")


# ════════════════════════════════════════════════════════════
# FILE 6: RHYTHMIC PATTERNS (applied to D Dorian)
# ════════════════════════════════════════════════════════════
print("Generating Rhythmic Patterns...")

rhythm = []

# Son Clave Melody
r1 = [make_note('D4','quarter',dots=1), make_note('F4','quarter',dots=1),
      make_note('A4','quarter'),
      make_rest('quarter'), make_rest('eighth'),
      make_note('G4','quarter',dots=1), make_note('D4','quarter')]
rhythm.append(("1. Son Clave 3-2 Melody", r1))

# Anticipated downbeat
r2 = [make_rest('quarter'), make_rest('eighth'),
      make_note('D4','eighth'), make_note('F4','quarter'),
      make_rest('quarter'),
      make_rest('quarter'), make_rest('eighth'),
      make_note('A4','eighth'), make_note('G4','quarter'),
      make_rest('quarter')]
rhythm.append(("2. Anticipated Downbeat (push the 'one')", r2))

# Tresillo 3+3+2
r3 = [make_note('D4','quarter',dots=1),
      make_note('F4','quarter',dots=1),
      make_note('A4','quarter'),
      make_note('C5','quarter',dots=1),
      make_note('A4','quarter',dots=1),
      make_note('G4','quarter')]
rhythm.append(("3. Tresillo (3+3+2)", r3))

# Habanera
r4 = [make_note('D4','quarter',dots=1), make_note('F4','eighth'),
      make_note('G4','quarter'), make_note('A4','quarter'),
      make_note('D4','quarter',dots=1), make_note('F4','eighth'),
      make_note('G4','quarter'), make_note('A4','quarter')]
rhythm.append(("4. Habanera (dotted quarter + eighth)", r4))

# Cinquillo
r5 = [make_note('D4','eighth'), make_rest('eighth'),
      make_note('F4','eighth'), make_note('G4','eighth'),
      make_rest('eighth'), make_note('A4','eighth'),
      make_note('C5','eighth'), make_rest('eighth')]
rhythm.append(("5. Cinquillo (5-note Afro-Cuban pattern)", r5))

# Off-beat accent
r6 = [make_rest('eighth'), make_note('D4','eighth'),
      make_rest('eighth'), make_note('F4','eighth'),
      make_rest('eighth'), make_note('G4','eighth'),
      make_rest('eighth'), make_note('A4','eighth')]
rhythm.append(("6. Off-Beat Accents (all upbeats)", r6))

# 3 over 4
r7 = [make_note('D4','quarter',dots=1),
      make_note('G4','quarter',dots=1),
      make_note('C5','quarter',dots=1),
      make_note('A4','quarter',dots=1),
      make_note('F4','quarter',dots=1),
      make_note('D4','quarter',dots=1)]
rhythm.append(("7. 3 over 4 Polyrhythm (dotted quarters)", r7))

# Cascara-inspired
r8 = [make_note('D4','eighth'), make_rest('eighth'),
      make_note('F4','eighth'), make_rest('eighth'),
      make_note('G4','eighth'), make_note('A4','eighth'),
      make_rest('eighth'), make_note('C5','eighth'),
      make_rest('eighth'), make_note('A4','eighth'),
      make_rest('eighth'), make_note('G4','eighth'),
      make_note('F4','eighth'), make_rest('eighth'),
      make_note('D4','eighth'), make_rest('eighth')]
rhythm.append(("8. Cascara-Inspired (timbale shell rhythm)", r8))

s6 = build_score(
    "Rhythmic Patterns",
    "Applied to D Dorian - Use these rhythms with ANY scale",
    rhythm, bpm=100
)
save(s6, "06_rhythmic_patterns.musicxml")


# ════════════════════════════════════════════════════════════
# FILE 7: ii-V-i LICKS TRANSPOSED TO 4 COMMON KEYS
# ════════════════════════════════════════════════════════════
print("Generating ii-V-i in 4 common keys...")

def make_lick_in_key(root_offset, label):
    """Transpose lick 1 (Smooth Dorian-Spanish) by semitones."""
    from music21 import interval
    # Original: D E F G | Ab B D F | Eb D C (in Dm7-G7b9-Cm)
    pitches_str = ['D4','E4','F4','G4','A-4','B4','D5','F5','E-5','D5','C5']
    durs = ['eighth']*8 + ['quarter','quarter','half']

    notes = []
    for ps, d in zip(pitches_str, durs):
        n = make_note(ps, d)
        n.transpose(root_offset, inPlace=True)
        notes.append(n)
    return (label, notes)

transposed_licks = [
    make_lick_in_key(0, "C minor: Dm7 - G7b9 - Cm"),
    make_lick_in_key(5, "F minor: Gm7 - C7b9 - Fm"),
    make_lick_in_key(7, "G minor: Am7 - D7b9 - Gm"),
    make_lick_in_key(2, "D minor: Em7 - A7b9 - Dm"),
]

s7 = build_score(
    "ii-V-i Lick #1 Transposed",
    "Smooth Dorian-Spanish lick in 4 common latin keys",
    transposed_licks, bpm=100
)
save(s7, "07_ii_V_i_transposed_4_keys.musicxml")


print("\n" + "="*50)
print("ALL FILES GENERATED!")
print("="*50)
print(f"\nOutput directory: {OUT}")
print("\nOpen these .musicxml files in:")
print("  - MuseScore (free, download from musescore.org)")
print("  - Flat.io (free, works in browser)")
print("  - Finale, Sibelius, Dorico")
print("  - Any MusicXML-compatible notation app")
