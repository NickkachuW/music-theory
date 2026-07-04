"""
Generate a polished PDF for the Latin Jazz & Tango Saxophone Improvisation Syllabus.
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether
)

# ── Colors ──────────────────────────────────────────────
DARK = HexColor("#1a1a2e")
ACCENT = HexColor("#e94560")
ACCENT2 = HexColor("#0f3460")
LIGHT_BG = HexColor("#f5f5f5")
WHITE = HexColor("#ffffff")
TABLE_HEADER = HexColor("#1a1a2e")
TABLE_ALT = HexColor("#f0f0f8")
MUTED = HexColor("#666666")

# ── Styles ──────────────────────────────────────────────
styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    name='CoverTitle',
    fontName='Helvetica-Bold',
    fontSize=28,
    textColor=DARK,
    alignment=TA_CENTER,
    spaceAfter=6,
    leading=34,
))
styles.add(ParagraphStyle(
    name='CoverSubtitle',
    fontName='Helvetica',
    fontSize=16,
    textColor=ACCENT,
    alignment=TA_CENTER,
    spaceAfter=4,
    leading=20,
))
styles.add(ParagraphStyle(
    name='CoverDetail',
    fontName='Helvetica',
    fontSize=11,
    textColor=MUTED,
    alignment=TA_CENTER,
    spaceAfter=4,
))
styles.add(ParagraphStyle(
    name='PhaseTitle',
    fontName='Helvetica-Bold',
    fontSize=22,
    textColor=ACCENT,
    spaceBefore=0,
    spaceAfter=4,
))
styles.add(ParagraphStyle(
    name='PhaseSubtitle',
    fontName='Helvetica',
    fontSize=12,
    textColor=MUTED,
    spaceAfter=12,
))
styles.add(ParagraphStyle(
    name='SectionHead',
    fontName='Helvetica-Bold',
    fontSize=14,
    textColor=ACCENT2,
    spaceBefore=16,
    spaceAfter=6,
))
styles.add(ParagraphStyle(
    name='SubSection',
    fontName='Helvetica-Bold',
    fontSize=11,
    textColor=DARK,
    spaceBefore=10,
    spaceAfter=4,
))
styles.add(ParagraphStyle(
    name='Body',
    fontName='Helvetica',
    fontSize=9.5,
    textColor=DARK,
    spaceBefore=2,
    spaceAfter=4,
    leading=13,
))
styles.add(ParagraphStyle(
    name='BodyBold',
    fontName='Helvetica-Bold',
    fontSize=9.5,
    textColor=DARK,
    spaceBefore=2,
    spaceAfter=4,
    leading=13,
))
styles.add(ParagraphStyle(
    name='BulletCustom',
    fontName='Helvetica',
    fontSize=9.5,
    textColor=DARK,
    leftIndent=18,
    spaceBefore=1,
    spaceAfter=1,
    leading=13,
))
styles.add(ParagraphStyle(
    name='SmallNote',
    fontName='Helvetica-Oblique',
    fontSize=8.5,
    textColor=MUTED,
    spaceBefore=2,
    spaceAfter=4,
))
styles.add(ParagraphStyle(
    name='TableCell',
    fontName='Helvetica',
    fontSize=8,
    textColor=DARK,
    leading=10,
))
styles.add(ParagraphStyle(
    name='TableHeader',
    fontName='Helvetica-Bold',
    fontSize=8,
    textColor=WHITE,
    leading=10,
))

# ── Helpers ─────────────────────────────────────────────
def make_table(headers, rows, col_widths=None):
    """Build a styled Table from header list and row list-of-lists."""
    data = [[Paragraph(h, styles['TableHeader']) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), styles['TableCell']) for c in row])

    if col_widths is None:
        col_widths = [None] * len(headers)

    t = Table(data, colWidths=col_widths, repeatRows=1)
    cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 4),
        ('TOPPADDING', (0, 1), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#cccccc")),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            cmds.append(('BACKGROUND', (0, i), (-1, i), TABLE_ALT))
    t.setStyle(TableStyle(cmds))
    return t

def P(text, style='Body'):
    return Paragraph(text, styles[style])

def Bul(text):
    return Paragraph(text, styles['BulletCustom'])

def sp(pts=6):
    return Spacer(1, pts)

# ── Build the document ──────────────────────────────────
output_path = r"C:\Users\nicwo\Projects\music theory\latin-jazz-syllabus\Latin_Jazz_Tango_Syllabus.pdf"

doc = SimpleDocTemplate(
    output_path,
    pagesize=letter,
    topMargin=0.6*inch,
    bottomMargin=0.6*inch,
    leftMargin=0.65*inch,
    rightMargin=0.65*inch,
    title="Latin Jazz & Tango Improvisation Syllabus",
    author="Saxophone Practice Guide",
)

story = []
W = letter[0] - 1.3*inch  # usable width

# ════════════════════════════════════════════════════════
# COVER PAGE
# ════════════════════════════════════════════════════════
story.append(Spacer(1, 2*inch))
story.append(P("Latin Jazz &amp; Tango", 'CoverTitle'))
story.append(P("Improvisation Syllabus", 'CoverTitle'))
story.append(sp(12))
story.append(P("For Alto &amp; Tenor Saxophone", 'CoverSubtitle'))
story.append(sp(20))
story.append(P("A 16-Week Practice Program", 'CoverDetail'))
story.append(P("Scales in All 12 Keys  |  ii-V-i Progressions  |  Tango Cadences", 'CoverDetail'))
story.append(sp(30))
story.append(P("Companion to the FQBK Scale &amp; Chord Reference", 'CoverDetail'))
story.append(PageBreak())

# ════════════════════════════════════════════════════════
# TABLE OF CONTENTS
# ════════════════════════════════════════════════════════
story.append(P("Table of Contents", 'PhaseTitle'))
story.append(sp(12))
toc_items = [
    "Phase 1: Foundation (Weeks 1-4) - Dorian, Mixolydian, Pentatonic, Blues",
    "Phase 2: Harmonic Depth (Weeks 5-8) - Spanish/Jewish, Harmonic Minor, Melodic Minor, Bebop, Lydian Dominant",
    "Phase 3: Color &amp; Tension (Weeks 9-12) - Altered, Whole Tone, Diminished, Phrygian",
    "Phase 4: Advanced &amp; Tango (Weeks 13-16) - Lydian Augmented, Locrian #2, Hindu, Tango Cadences",
    "Riffs, Licks &amp; Melodic Patterns - Latin Jazz Riffs, ii-V-i Licks, Dominant Flavors, Pentatonic Tricks, Tango Patterns, Rhythmic Patterns",
    "Daily Routine Quick Reference Card",
    "Scale Cheat Sheet: What to Play Over What",
    "Listening Homework &amp; Progress Tracker",
]
for i, item in enumerate(toc_items, 1):
    story.append(P(f"<b>{i}.</b>  {item}", 'Body'))
    story.append(sp(4))
story.append(PageBreak())

# ════════════════════════════════════════════════════════
# PHASE 1
# ════════════════════════════════════════════════════════
story.append(P("Phase 1: Foundation", 'PhaseTitle'))
story.append(P("Weeks 1-4  |  Goal: Core scale fluency in common Latin jazz keys  |  30-45 min/day", 'PhaseSubtitle'))
story.append(P("Always practice with a <b>clave pattern</b> (son clave 3-2 or 2-3). Tap the clave with your foot.", 'SmallNote'))

# Dorian
story.append(P("Scale 1: DORIAN (Minor) - The Latin Jazz Workhorse", 'SectionHead'))
story.append(P("<b>Use over:</b> minor 7th vamps, montuno grooves, ii chords  |  <b>Formula:</b> W H W W W H W", 'Body'))
story.append(make_table(
    ["Key", "Notes", "Concert (Alto)", "Concert (Tenor)", "Context"],
    [
        ["C-7", "C D Eb F G A Bb", "Eb min", "Bb min", ""],
        ["Db-7", "Db Eb Fb Gb Ab Bb Cb", "E min", "B min", ""],
        ["D-7", "D E F G A B C", "F min", "C min", "Very common"],
        ["Eb-7", "Eb F Gb Ab Bb C Db", "Gb min", "Db min", ""],
        ["E-7", "E F# G A B C# D", "G min", "D min", "Very common"],
        ["F-7", "F G Ab Bb C D Eb", "Ab min", "Eb min", "Common"],
        ["F#-7", "F# G# A B C# D# E", "A min", "E min", ""],
        ["G-7", "G A Bb C D E F", "Bb min", "F min", "Very common"],
        ["Ab-7", "Ab Bb Cb Db Eb F Gb", "B min", "Gb min", ""],
        ["A-7", "A B C D E F# G", "C min", "G min", "Very common"],
        ["Bb-7", "Bb C Db Eb F G Ab", "Db min", "Ab min", "Common"],
        ["B-7", "B C# D E F# G# A", "D min", "A min", "Common"],
    ],
    col_widths=[0.5*inch, 1.8*inch, 0.9*inch, 0.9*inch, 0.9*inch],
))
story.append(sp(6))
story.append(P("Priority Practice Order", 'SubSection'))
for i, item in enumerate([
    "D Dorian (concert F/C minor)", "G Dorian (concert Bb/F minor)",
    "A Dorian (concert C/G minor)", "E Dorian (concert G/D minor)",
    "C Dorian (concert Eb/Bb minor)", "F Dorian (concert Ab/Eb minor)",
    "Bb Dorian (concert Db/Ab minor)", "Then fill in remaining keys",
], 1):
    story.append(Bul(f"{i}. {item}"))

# Mixolydian
story.append(P("Scale 2: MIXOLYDIAN - Over Dominant Chords", 'SectionHead'))
story.append(P("<b>Use over:</b> dominant 7th chords, V7 chords  |  <b>Formula:</b> W W H W W H W", 'Body'))
story.append(make_table(
    ["Key", "Notes", "Concert (Alto)", "Concert (Tenor)"],
    [
        ["C7", "C D E F G A Bb", "Eb7", "Bb7"],
        ["Db7", "Db Eb F Gb Ab Bb Cb", "E7", "B7"],
        ["D7", "D E F# G A B C", "F7", "C7"],
        ["Eb7", "Eb F G Ab Bb C Db", "Gb7", "Db7"],
        ["E7", "E F# G# A B C# D", "G7", "D7"],
        ["F7", "F G A Bb C D Eb", "Ab7", "Eb7"],
        ["F#7", "F# G# A# B C# D# E", "A7", "E7"],
        ["G7", "G A B C D E F", "Bb7", "F7"],
        ["Ab7", "Ab Bb C Db Eb F Gb", "B7", "Gb7"],
        ["A7", "A B C# D E F# G", "C7", "G7"],
        ["Bb7", "Bb C D Eb F G Ab", "Db7", "Ab7"],
        ["B7", "B C# D# E F# G# A", "D7", "A7"],
    ],
    col_widths=[0.5*inch, 2*inch, 1*inch, 1*inch],
))

# Minor Pentatonic
story.append(P("Scale 3: MINOR PENTATONIC - Clean Rhythmic Lines", 'SectionHead'))
story.append(P("<b>Use over:</b> minor vamps, simple blowing sections  |  <b>Formula:</b> m3 W W m3 W", 'Body'))
story.append(make_table(
    ["Key", "Notes (5 notes)"],
    [["C", "C Eb F G Bb"], ["Db", "Db Fb Gb Ab Cb"], ["D", "D F G A C"],
     ["Eb", "Eb Gb Ab Bb Db"], ["E", "E G A B D"], ["F", "F Ab Bb C Eb"],
     ["F#", "F# A B C# E"], ["G", "G Bb C D F"], ["Ab", "Ab Cb Db Eb Gb"],
     ["A", "A C D E G"], ["Bb", "Bb Db Eb F Ab"], ["B", "B D E F# A"]],
    col_widths=[0.5*inch, 3*inch],
))

# Blues Scale
story.append(P("Scale 4: BLUES SCALE - Grit and Soul", 'SectionHead'))
story.append(P("<b>Use over:</b> everything!  |  <b>Formula:</b> m3 W H H m3 W", 'Body'))
story.append(make_table(
    ["Key", "Notes (6 notes)"],
    [["C", "C Eb F F# G Bb"], ["Db", "Db Fb Gb G Ab Cb"], ["D", "D F G G# A C"],
     ["Eb", "Eb Gb Ab A Bb Db"], ["E", "E G A A# B D"], ["F", "F Ab Bb B C Eb"],
     ["F#", "F# A B B# C# E"], ["G", "G Bb C C# D F"], ["Ab", "Ab Cb Db D Eb Gb"],
     ["A", "A C D D# E G"], ["Bb", "Bb Db Eb E F Ab"], ["B", "B D E E# F# A"]],
    col_widths=[0.5*inch, 3*inch],
))

# Weekly schedule
story.append(P("Week-by-Week Schedule", 'SectionHead'))
story.append(P("<b>Week 1:</b> D Dorian + G Mixolydian + D Minor Pentatonic (ii-V in C minor)", 'Body'))
story.append(P("<b>Week 2:</b> G Dorian + C Mixolydian + G Minor Pentatonic (ii-V in F minor)", 'Body'))
story.append(P("<b>Week 3:</b> A Dorian + D Mixolydian + A Minor Pentatonic (ii-V in G minor)", 'Body'))
story.append(P("<b>Week 4:</b> Review all 3 key centers + add E, C, F Dorian. Record yourself.", 'Body'))

# Clave
story.append(P("Clave Rhythm Reference", 'SectionHead'))
story.append(P("<b>Son Clave 3-2:</b>  X . . X . . X .  |  . . X . . X . .", 'Body'))
story.append(P("<b>Son Clave 2-3:</b>  . . X . . X . .  |  X . . X . . X .", 'Body'))
story.append(P("<b>Rumba Clave 3-2:</b>  X . . X . . . X  |  . . X . . X . .", 'Body'))
story.append(PageBreak())

# ════════════════════════════════════════════════════════
# PHASE 2
# ════════════════════════════════════════════════════════
story.append(P("Phase 2: Harmonic Depth", 'PhaseTitle'))
story.append(P("Weeks 5-8  |  Goal: Navigate ii-V-i progressions  |  30-45 min/day", 'PhaseSubtitle'))

# Spanish/Jewish
story.append(P("Spanish / Jewish (Phrygian Dominant) - THE Latin Dominant Sound", 'SectionHead'))
story.append(P("<b>Use over:</b> V7b9 chords resolving to minor  |  <b>Formula:</b> H m3 H W H W W", 'Body'))
story.append(P("5th mode of Harmonic Minor. The b9 interval is what makes salsa, mambo, and tango distinctive.", 'SmallNote'))
story.append(make_table(
    ["Key", "Notes", "Resolves to"],
    [
        ["C7b9", "C Db E F G Ab Bb", "F minor"],
        ["Db7b9", "Db Ebb F Gb Ab Bbb Cb", "Gb minor"],
        ["D7b9", "D Eb F# G A Bb C", "G minor"],
        ["Eb7b9", "Eb Fb G Ab Bb Cb Db", "Ab minor"],
        ["E7b9", "E F G# A B C D", "A minor"],
        ["F7b9", "F Gb A Bb C Db Eb", "Bb minor"],
        ["F#7b9", "F# G A# B C# D E", "B minor"],
        ["G7b9", "G Ab B C D Eb F", "C minor"],
        ["Ab7b9", "Ab Bbb C Db Eb Fb Gb", "Db minor"],
        ["A7b9", "A Bb C# D E F G", "D minor"],
        ["Bb7b9", "Bb Cb D Eb F Gb Ab", "Eb minor"],
        ["B7b9", "B C D# E F# G A", "E minor"],
    ],
    col_widths=[0.6*inch, 2.2*inch, 1*inch],
))

# Harmonic Minor
story.append(P("Harmonic Minor - Dramatic Resolutions &amp; Tango", 'SectionHead'))
story.append(P("<b>Use over:</b> minor tonic, V7-i cadences  |  <b>Formula:</b> W H W W H m3 H", 'Body'))
story.append(make_table(
    ["Key", "Notes", "Augmented 2nd"],
    [
        ["C", "C D Eb F G Ab B", "Ab-B"],
        ["Db", "Db Eb Fb Gb Ab Bbb C", ""],
        ["D", "D E F G A Bb C#", "Bb-C#"],
        ["Eb", "Eb F Gb Ab Bb Cb D", ""],
        ["E", "E F# G A B C D#", "C-D#"],
        ["F", "F G Ab Bb C Db E", "Db-E"],
        ["F#", "F# G# A B C# D E#", ""],
        ["G", "G A Bb C D Eb F#", "Eb-F#"],
        ["Ab", "Ab Bb Cb Db Eb Fb G", ""],
        ["A", "A B C D E F G#", "F-G#"],
        ["Bb", "Bb C Db Eb F Gb A", "Gb-A"],
        ["B", "B C# D E F# G A#", "G-A#"],
    ],
    col_widths=[0.5*inch, 2.2*inch, 0.9*inch],
))

# Melodic Minor
story.append(P("Melodic Minor - Modern Tango Tonic", 'SectionHead'))
story.append(P("<b>Use over:</b> minor-major7 chords  |  <b>Formula:</b> W H W W W W H", 'Body'))
story.append(make_table(
    ["Key", "Notes (ascending)"],
    [
        ["C", "C D Eb F G A B"], ["Db", "Db Eb Fb Gb Ab Bb C"],
        ["D", "D E F G A B C#"], ["Eb", "Eb F Gb Ab Bb C D"],
        ["E", "E F# G A B C# D#"], ["F", "F G Ab Bb C D E"],
        ["F#", "F# G# A B C# D# E#"], ["G", "G A Bb C D E F#"],
        ["Ab", "Ab Bb Cb Db Eb F G"], ["A", "A B C D E F# G#"],
        ["Bb", "Bb C Db Eb F G A"], ["B", "B C# D E F# G# A#"],
    ],
    col_widths=[0.5*inch, 3*inch],
))

# Bebop Dominant
story.append(P("Bebop Dominant - Smooth Eighth-Note Lines", 'SectionHead'))
story.append(P("<b>Use over:</b> dominant 7th chords  |  <b>Formula:</b> W W H W W H H H (8 notes)", 'Body'))
story.append(make_table(
    ["Key", "Notes (8 notes)"],
    [
        ["C7", "C D E F G A Bb B"], ["Db7", "Db Eb F Gb Ab Bb Cb C"],
        ["D7", "D E F# G A B C C#"], ["Eb7", "Eb F G Ab Bb C Db D"],
        ["E7", "E F# G# A B C# D D#"], ["F7", "F G A Bb C D Eb E"],
        ["F#7", "F# G# A# B C# D# E E#"], ["G7", "G A B C D E F F#"],
        ["Ab7", "Ab Bb C Db Eb F Gb G"], ["A7", "A B C# D E F# G G#"],
        ["Bb7", "Bb C D Eb F G Ab A"], ["B7", "B C# D# E F# G# A A#"],
    ],
    col_widths=[0.5*inch, 3.5*inch],
))

# Lydian Dominant
story.append(P("Lydian Dominant - Static Dominant Chords", 'SectionHead'))
story.append(P("<b>Use over:</b> dominant chords that don't resolve down a 5th  |  <b>Formula:</b> W W W H W H W", 'Body'))
story.append(make_table(
    ["Key", "Notes"],
    [
        ["C7#4", "C D E F# G A Bb"], ["Db7#4", "Db Eb F G Ab Bb Cb"],
        ["D7#4", "D E F# G# A B C"], ["Eb7#4", "Eb F G A Bb C Db"],
        ["E7#4", "E F# G# A# B C# D"], ["F7#4", "F G A B C D Eb"],
        ["F#7#4", "F# G# A# B# C# D# E"], ["G7#4", "G A B C# D E F"],
        ["Ab7#4", "Ab Bb C D Eb F Gb"], ["A7#4", "A B C# D# E F# G"],
        ["Bb7#4", "Bb C D E F G Ab"], ["B7#4", "B C# D# E# F# G# A"],
    ],
    col_widths=[0.6*inch, 3*inch],
))

# ii-V-i Master Chart
story.append(P("MASTER CHART: ii-V-i in All 12 Minor Keys", 'SectionHead'))
story.append(P("The core latin jazz progression. Practice each row as a unit.", 'SmallNote'))
story.append(make_table(
    ["Key", "ii (Dorian)", "V (Spanish/Jewish)", "i (Harmonic Minor)"],
    [
        ["C min", "D: D E F G A B C", "G7b9: G Ab B C D Eb F", "C: C D Eb F G Ab B"],
        ["Db min", "Eb: Eb F Gb Ab Bb C Db", "Ab7b9: Ab Bbb C Db Eb Fb Gb", "Db: Db Eb Fb Gb Ab Bbb C"],
        ["D min", "E: E F# G A B C# D", "A7b9: A Bb C# D E F G", "D: D E F G A Bb C#"],
        ["Eb min", "F: F G Ab Bb C D Eb", "Bb7b9: Bb Cb D Eb F Gb Ab", "Eb: Eb F Gb Ab Bb Cb D"],
        ["E min", "F#: F# G# A B C# D# E", "B7b9: B C D# E F# G A", "E: E F# G A B C D#"],
        ["F min", "G: G A Bb C D E F", "C7b9: C Db E F G Ab Bb", "F: F G Ab Bb C Db E"],
        ["F# min", "G#: G# A# B C# D# E# F#", "C#7b9: C# D E# F# G# A B", "F#: F# G# A B C# D E#"],
        ["G min", "A: A B C D E F# G", "D7b9: D Eb F# G A Bb C", "G: G A Bb C D Eb F#"],
        ["Ab min", "Bb: Bb C Db Eb F G Ab", "Eb7b9: Eb Fb G Ab Bb Cb Db", "Ab: Ab Bb Cb Db Eb Fb G"],
        ["A min", "B: B C# D E F# G# A", "E7b9: E F G# A B C D", "A: A B C D E F G#"],
        ["Bb min", "C: C D Eb F G A Bb", "F7b9: F Gb A Bb C Db Eb", "Bb: Bb C Db Eb F Gb A"],
        ["B min", "C#: C# D# E F# G# A# B", "F#7b9: F# G A# B C# D E", "B: B C# D E F# G A#"],
    ],
    col_widths=[0.6*inch, 1.6*inch, 1.8*inch, 1.7*inch],
))
story.append(sp(8))
story.append(P("<b>Practice Method:</b> 4 beats Dorian, 4 beats Spanish/Jewish, 8 beats Harmonic Minor. Repeat.", 'Body'))

# Weekly schedule
story.append(P("Week-by-Week Schedule", 'SectionHead'))
story.append(P("<b>Week 5:</b> Spanish/Jewish in 4 keys (G, D, A, C). Compare to Mixolydian.", 'Body'))
story.append(P("<b>Week 6:</b> Add Harmonic Minor. Connect full ii-V-i in C, G, D, F minor.", 'Body'))
story.append(P("<b>Week 7:</b> Add Melodic Minor + Bebop Dominant for flowing lines.", 'Body'))
story.append(P("<b>Week 8:</b> All 12 keys. Add Lydian Dominant over static vamps. Record yourself.", 'Body'))
story.append(PageBreak())

# ════════════════════════════════════════════════════════
# PHASE 3
# ════════════════════════════════════════════════════════
story.append(P("Phase 3: Color &amp; Tension", 'PhaseTitle'))
story.append(P("Weeks 9-12  |  Goal: Tension, release, and outside playing  |  30-45 min/day", 'PhaseSubtitle'))

# Altered
story.append(P("Altered Scale (Diminished Whole Tone) - Maximum Tension", 'SectionHead'))
story.append(P("<b>Use over:</b> V7#9, V7b9, V7#5  |  <b>Formula:</b> H W H W W W W  |  Contains: root, b9, #9, 3, #11, b13, b7", 'Body'))
story.append(make_table(
    ["Key", "Notes"],
    [
        ["C7alt", "C Db D# E F# G# Bb"], ["Db7alt", "Db Ebb E F G A Cb"],
        ["D7alt", "D Eb E# F# G# A# C"], ["Eb7alt", "Eb Fb F# G A B Db"],
        ["E7alt", "E F F## G# A# B# D"], ["F7alt", "F Gb G# A B C# Eb"],
        ["F#7alt", "F# G A Bb C D E"], ["G7alt", "G Ab A# B C# D# F"],
        ["Ab7alt", "Ab Bbb B C D E Gb"], ["A7alt", "A Bb B# C# D# E# G"],
        ["Bb7alt", "Bb Cb C# D E F# Ab"], ["B7alt", "B C C## D# E# F## A"],
    ],
    col_widths=[0.6*inch, 3.5*inch],
))

# Whole Tone
story.append(P("Whole Tone - Dreamy Floating Sound", 'SectionHead'))
story.append(P("<b>Use over:</b> V7#5  |  <b>Formula:</b> W W W W W W  |  Only 2 unique whole tone scales exist", 'Body'))
story.append(make_table(
    ["Key", "Notes", "WT Scale"],
    [
        ["C7#5", "C D E F# G# Bb", "1"], ["Db7#5", "Db Eb F G A Cb", "2"],
        ["D7#5", "D E F# G# A# C", "1"], ["Eb7#5", "Eb F G A B Db", "2"],
        ["E7#5", "E F# G# A# B# D", "1"], ["F7#5", "F G A B C# Eb", "2"],
        ["Gb7#5", "Gb Ab Bb C D Fb", "1"],
        ["G7#5", "G A B C# D# F", "2"], ["Ab7#5", "Ab Bb C D E Gb", "1"],
        ["A7#5", "A B C# D# E# G", "2"], ["Bb7#5", "Bb C D E F# Ab", "1"],
        ["B7#5", "B C# D# E# F## A", "2"],
    ],
    col_widths=[0.6*inch, 2.5*inch, 0.6*inch],
))

# Diminished H-W
story.append(P("Diminished (begin with H) - Angular Dominant Sound", 'SectionHead'))
story.append(P("<b>Use over:</b> V7b9  |  <b>Formula:</b> H W H W H W H W (8 notes, symmetric)", 'Body'))
story.append(make_table(
    ["Key", "Notes (8 notes)"],
    [
        ["C7b9", "C Db D# E F# G A Bb"], ["Db7b9", "Db Ebb E F G Ab Bb Cb"],
        ["D7b9", "D Eb E# F# G# A B C"], ["Eb7b9", "Eb Fb F# G A Bb C Db"],
        ["E7b9", "E F F## G# A# B C# D"], ["F7b9", "F Gb G# A B C D Eb"],
        ["G7b9", "G Ab A# B C# D E F"], ["Ab7b9", "Ab Bbb B C D Eb F Gb"],
        ["A7b9", "A Bb B# C# D# E F# G"], ["Bb7b9", "Bb Cb C# D E F G Ab"],
        ["B7b9", "B C C## D# E# F# G# A"],
    ],
    col_widths=[0.6*inch, 3.5*inch],
))

# Phrygian
story.append(P("Phrygian - Dark Modal Vamps", 'SectionHead'))
story.append(P("<b>Use over:</b> modal minor sections, descarga grooves  |  <b>Formula:</b> H W W W H W W", 'Body'))
story.append(make_table(
    ["Key", "Notes"],
    [
        ["C", "C Db Eb F G Ab Bb"], ["C#", "C# D E F# G# A B"],
        ["D", "D Eb F G A Bb C"], ["Eb", "Eb Fb Gb Ab Bb Cb Db"],
        ["E", "E F G A B C D"], ["F", "F Gb Ab Bb C Db Eb"],
        ["F#", "F# G A B C# D E"], ["G", "G Ab Bb C D Eb F"],
        ["G#", "G# A B C# D# E F#"], ["A", "A Bb C D E F G"],
        ["Bb", "Bb Cb Db Eb F Gb Ab"], ["B", "B C D E F# G A"],
    ],
    col_widths=[0.5*inch, 3*inch],
))

# Tension-Resolution
story.append(P("Tension-Resolution Exercise (All 12 Keys)", 'SectionHead'))
story.append(P("Practice: 2 bars tension (Altered) then 2 bars resolution (Dorian)", 'SmallNote'))
story.append(make_table(
    ["Resolve to", "V7 Altered Scale", "i Dorian Scale"],
    [
        ["C min", "G: G Ab A# B C# D# F", "C: C D Eb F G A Bb"],
        ["D min", "A: A Bb B# C# D# E# G", "D: D E F G A B C"],
        ["E min", "B: B C C## D# E# F## A", "E: E F# G A B C# D"],
        ["F min", "C: C Db D# E F# G# Bb", "F: F G Ab Bb C D Eb"],
        ["G min", "D: D Eb E# F# G# A# C", "G: G A Bb C D E F"],
        ["A min", "E: E F F## G# A# B# D", "A: A B C D E F# G"],
        ["Bb min", "F: F Gb G# A B C# Eb", "Bb: Bb C Db Eb F G Ab"],
        ["B min", "F#: F# G A Bb C D E", "B: B C# D E F# G# A"],
    ],
    col_widths=[0.7*inch, 2.2*inch, 2.2*inch],
))

story.append(P("Week-by-Week Schedule", 'SectionHead'))
story.append(P("<b>Week 9:</b> Altered Scale in 4 keys + tension-resolution exercise.", 'Body'))
story.append(P("<b>Week 10:</b> Whole Tone + Diminished. Compare all dominant tensions.", 'Body'))
story.append(P("<b>Week 11:</b> Phrygian over dark vamps + Diminished (W-H) for outside color.", 'Body'))
story.append(P("<b>Week 12:</b> Integration. Improvise over full tunes with ALL tension scales.", 'Body'))
story.append(PageBreak())

# ════════════════════════════════════════════════════════
# PHASE 4
# ════════════════════════════════════════════════════════
story.append(P("Phase 4: Advanced &amp; Tango", 'PhaseTitle'))
story.append(P("Weeks 13-16  |  Goal: Real-world application + tango vocabulary  |  45-60 min/day", 'PhaseSubtitle'))

# Lydian Augmented
story.append(P("Lydian Augmented", 'SectionHead'))
story.append(P("<b>Use over:</b> Major #5 chords, III chords in minor  |  <b>Formula:</b> W W W W H W H", 'Body'))
story.append(make_table(
    ["Key", "Notes"],
    [["C", "C D E F# G# A B"], ["D", "D E F# G# A# B C#"],
     ["E", "E F# G# A# B# C# D#"], ["F", "F G A B C# D E"],
     ["G", "G A B C# D# E F#"], ["A", "A B C# D# E# F# G#"],
     ["Bb", "Bb C D E F# G A"], ["B", "B C# D# E# F## G# A#"]],
    col_widths=[0.5*inch, 3.5*inch],
))

# Locrian #2
story.append(P("Locrian #2 - Smooth Half-Diminished", 'SectionHead'))
story.append(P("<b>Use over:</b> half-diminished chords  |  <b>Formula:</b> W H W H W W W", 'Body'))
story.append(make_table(
    ["Key", "Notes"],
    [["C", "C D Eb F Gb Ab Bb"], ["D", "D E F G Ab Bb C"],
     ["E", "E F# G A Bb C D"], ["F", "F G Ab Bb Cb Db Eb"],
     ["G", "G A Bb C Db Eb F"], ["A", "A B C D Eb F G"],
     ["Bb", "Bb C Db Eb Fb Gb Ab"], ["B", "B C# D E F G A"]],
    col_widths=[0.5*inch, 3.5*inch],
))

# Hindu
story.append(P("Hindu (Mixolydian b6) - Melancholic Dominant", 'SectionHead'))
story.append(P("<b>Use over:</b> dominant b6 chords  |  <b>Formula:</b> W W H W H W W", 'Body'))
story.append(make_table(
    ["Key", "Notes"],
    [["C7b6", "C D E F G Ab Bb"], ["D7b6", "D E F# G A Bb C"],
     ["E7b6", "E F# G# A B C D"], ["F7b6", "F G A Bb C Db Eb"],
     ["G7b6", "G A B C D Eb F"], ["A7b6", "A B C# D E F G"],
     ["Bb7b6", "Bb C D Eb F Gb Ab"], ["B7b6", "B C# D# E F# G A"]],
    col_widths=[0.6*inch, 3.5*inch],
))

# Tango Section
story.append(P("TANGO-SPECIFIC PRACTICE", 'SectionHead'))
story.append(P("The Tango Scale Palette", 'SubSection'))
story.append(make_table(
    ["Scale", "Tango Function", "Emotional Quality"],
    [
        ["Harmonic Minor", "Primary tonic scale", "Dramatic, passionate"],
        ["Spanish/Jewish", "Over V7b9", "Yearning, bittersweet"],
        ["Melodic Minor", "Modern tango tonic", "Sophisticated, smooth"],
        ["Diminished (H-W)", "Passing diminished chords", "Mysterious, tense"],
        ["Phrygian", "Dark modal sections", "Brooding, intense"],
        ["Natural Minor", "Folk tango", "Simple, melancholic"],
    ],
    col_widths=[1.3*inch, 1.8*inch, 1.8*inch],
))

story.append(P("Tango Phrygian Cadence: bII - V7b9 - i (All Keys)", 'SubSection'))
story.append(P("The signature tango resolution pattern.", 'SmallNote'))
story.append(make_table(
    ["Key", "bII (Lydian)", "V7b9 (Spanish)", "i (Harm. Minor)"],
    [
        ["C min", "Db: Db Eb F G Ab Bb C", "G7b9: G Ab B C D Eb F", "C: C D Eb F G Ab B"],
        ["D min", "Eb: Eb F G A Bb C D", "A7b9: A Bb C# D E F G", "D: D E F G A Bb C#"],
        ["E min", "F: F G A B C D E", "B7b9: B C D# E F# G A", "E: E F# G A B C D#"],
        ["F min", "Gb: Gb Ab Bb C Db Eb F", "C7b9: C Db E F G Ab Bb", "F: F G Ab Bb C Db E"],
        ["G min", "Ab: Ab Bb C D Eb F G", "D7b9: D Eb F# G A Bb C", "G: G A Bb C D Eb F#"],
        ["A min", "Bb: Bb C D E F G A", "E7b9: E F G# A B C D", "A: A B C D E F G#"],
        ["Bb min", "Cb: Cb Db Eb F Gb Ab Bb", "F7b9: F Gb A Bb C Db Eb", "Bb: Bb C Db Eb F Gb A"],
        ["B min", "C: C D E F# G A B", "F#7b9: F# G A# B C# D E", "B: B C# D E F# G A#"],
    ],
    col_widths=[0.55*inch, 1.55*inch, 1.7*inch, 1.6*inch],
))

story.append(P("Tango Melodic Vocabulary", 'SubSection'))
story.append(Bul("<b>Chromatic Neighbors:</b> Approach each harmonic minor note from a half step below."))
story.append(Bul("<b>Dramatic Leaps:</b> Jump up a 6th or 7th, then walk back down stepwise."))
story.append(Bul("<b>3-3-2 Rhythm:</b> X . . X . . X . over 4/4 - the tango rhythmic DNA."))
story.append(Bul("<b>Marcato vs Sincopa:</b> Heavy quarter notes vs syncopated push. Switch mid-phrase."))

story.append(P("Week-by-Week Schedule", 'SectionHead'))
story.append(P("<b>Week 13:</b> Tango cadences in C, D, G, A minor. Chromatic neighbor exercise.", 'Body'))
story.append(P("<b>Week 14:</b> Lydian Augmented, Locrian #2, Hindu over specific chord types.", 'Body'))
story.append(P("<b>Week 15:</b> Pick 3 latin jazz standards. Map every chord to a scale. Improvise.", 'Body'))
story.append(P("<b>Week 16:</b> All tango cadences in 12 keys. 3-3-2 rhythm. Transcribe Piazzolla.", 'Body'))
story.append(PageBreak())

# ════════════════════════════════════════════════════════
# RIFFS, LICKS & MELODIC PATTERNS
# ════════════════════════════════════════════════════════
story.append(P("Riffs, Licks &amp; Melodic Patterns", 'PhaseTitle'))
story.append(P("Common vocabulary for Latin Jazz &amp; Tango improvisation. Learn in C, then transpose to all keys.", 'PhaseSubtitle'))

# --- Section 1: Latin Jazz Riffs over Minor Vamps ---
story.append(P("1. LATIN JAZZ RIFFS - Over Minor Vamps (Dorian)", 'SectionHead'))
story.append(P("Play these over a Dm7 or Cm7 montuno groove with clave. Written in D Dorian (concert F/C).", 'SmallNote'))

story.append(make_table(
    ["Riff", "Notes (in D Dorian)", "Rhythm Feel", "Technique"],
    [
        ["Pentatonic Call", "D F G A C D", "Ascending burst on 3-side of clave", "Strong attack, let last note ring"],
        ["Falling Answer", "C A G F D", "Descending on 2-side of clave", "Softer, legato response"],
        ["The Montuno Riff", "D F A - C A F", "Up in 3rds, back down", "Staccato, match piano montuno rhythm"],
        ["Root-5th Anchor", "D . A . D' . A . D", "Quarter notes, marcato", "Strong foundation riff"],
        ["Dorian Signature", "D E F A G E D", "1-2-b3-5-4-2-1 shape", "Emphasize the natural 6th (B)"],
        ["Blue Note Dip", "D F G G# A C D", "Add blues b5 passing tone", "Bend into the G#, slide to A"],
        ["Clave Melody", "D . . F . . A .", "Notes on clave hits only", "Let space do the work"],
        ["Syncopated 3rds", "D-F . E-G . F-A . G-Bb", "Pairs on upbeats", "Push ahead of the beat"],
    ],
    col_widths=[1.1*inch, 1.7*inch, 1.5*inch, 1.5*inch],
))

# --- Section 2: ii-V-i Licks ---
story.append(P("2. ii-V-i LICKS - The Core Latin Jazz Vocabulary", 'SectionHead'))
story.append(P("Written for ii-V-i in C minor: Dm7 - G7b9 - Cm. Transpose to all 12 keys.", 'SmallNote'))

story.append(make_table(
    ["Lick", "Dm7 (beats 1-2)", "G7b9 (beats 3-4)", "Cm (bar 2)", "Character"],
    [
        ["Smooth Dorian-Spanish",
         "D E F G",
         "Ab B D F",
         "Eb D C",
         "Classic, clean"],
        ["Bebop Connector",
         "A G F E",
         "F Ab B D",
         "Eb C",
         "Descending into tension"],
        ["Enclosure Lick",
         "E D F E",
         "Ab G B Ab",
         "G Eb D C",
         "Surround target notes"],
        ["Arpeggio + Scale",
         "D F A C",
         "B D F Ab",
         "G Eb D C",
         "Chord tones then fill"],
        ["Altered Tension",
         "D F G A",
         "Ab Bb Db E (altered)",
         "Eb D C",
         "Max tension on V"],
        ["Pentatonic Shift",
         "D F G A C",
         "Db Fb Gb Ab (Db pent)",
         "C Eb G",
         "Pentatonic substitution"],
        ["Chromatic Approach",
         "A G F E",
         "Eb D Db C B",
         "C",
         "Half steps into resolution"],
        ["Spanish Signature",
         "D E F G",
         "G Ab B C D Eb F",
         "Eb D C",
         "Full Spanish run on V"],
    ],
    col_widths=[1*inch, 1.1*inch, 1.3*inch, 0.9*inch, 1.2*inch],
))

story.append(sp(6))
story.append(P("<b>How to practice:</b> Play each lick slowly with a metronome. Then loop a Dm7-G7-Cm backing track and cycle through all 8 licks. Once comfortable, transpose to G minor (Am7-D7b9-Gm), then all keys.", 'Body'))

# --- Section 3: Dominant Riffs ---
story.append(P("3. DOMINANT 7th RIFFS - Spicing Up the V Chord", 'SectionHead'))
story.append(P("Different ways to play over G7 resolving to C minor. Each gives a different flavor.", 'SmallNote'))

story.append(make_table(
    ["Flavor", "Scale Used", "Example Riff (over G7)", "Sound"],
    [
        ["Vanilla", "G Mixolydian", "G A B D C B A G", "Safe, consonant"],
        ["Salsa Fire", "G Spanish/Jewish", "G Ab B C D Eb F G", "Classic Afro-Cuban"],
        ["Bebop Flow", "G Bebop Dominant", "G A B C D E F F# G", "Smooth 8th notes"],
        ["Dark Mystery", "G Dim (H-W)", "G Ab A# B C# D E F", "Angular, symmetric"],
        ["Maximum Heat", "G Altered", "G Ab Bb B Db Eb F", "Outside, unresolved"],
        ["Floating", "G Whole Tone", "G A B C# D# F", "Dreamy, suspended"],
        ["Blues Grit", "G Blues", "G Bb C C# D F", "Earthy, soulful"],
        ["Lydian Static", "G Lydian Dom", "G A B C# D E F", "Bright, non-resolving"],
    ],
    col_widths=[0.9*inch, 1.2*inch, 2*inch, 1.2*inch],
))

# --- Section 4: Pentatonic Tricks ---
story.append(P("4. PENTATONIC TRICKS - Simple but Powerful", 'SectionHead'))
story.append(P("The minor pentatonic is the secret weapon of latin jazz. These patterns work in any key.", 'SmallNote'))

story.append(make_table(
    ["Pattern Name", "Shape (in D minor pent: D F G A C)", "Application"],
    [
        ["Ascending 4ths", "D-G, F-A, G-C, A-D", "Strong, angular, modern"],
        ["Falling 3rds", "A-F, G-D, F-C, D-A", "Smooth, flowing descent"],
        ["Skip Pattern", "D G F A G C A D'", "Zigzag through the scale"],
        ["Repeated Cell", "D F G - F G A - G A C", "3-note groups, shifting up"],
        ["Call &amp; Response", "D F G A (high) ... C A G F (answer)", "Leave space between phrases"],
        ["Octave Displacement", "D(low) F(high) G(low) A(high)", "Jump octaves for drama"],
        ["Clave Pentatonic", "D . . F . . G . / . . A . . C . .", "Place notes only on clave hits"],
        ["Pent over V7", "Play Ab min pent over G7", "Ab Cb Db Eb Gb = b9 3 b5 b13 b7 of G7"],
    ],
    col_widths=[1.1*inch, 2.6*inch, 2.1*inch],
))

# --- Section 5: Tango Melodic Patterns ---
story.append(P("5. TANGO MELODIC PATTERNS", 'SectionHead'))
story.append(P("Signature tango gestures. Written in A minor (concert C/G). Use 3-3-2 rhythmic feel.", 'SmallNote'))

story.append(make_table(
    ["Pattern", "Notes", "Description"],
    [
        ["The Tango Sigh", "B C B A G# A", "Upper neighbor, fall back - yearning quality"],
        ["Dramatic Leap + Descent", "A(low) - F(up 6th) E D C B A", "Jump up, walk down stepwise"],
        ["Augmented 2nd Cry", "E F G# A G# F E", "Mirror around the F-G# aug 2nd interval"],
        ["Chromatic Approach", "G G# A - B C - D D# E", "Lead into each chord tone from below"],
        ["Phrygian Cadence Lick", "Bb A G# A - F E D# E", "bII sound melting into V then i"],
        ["Bandoneon Imitation", "A E' C A E C A", "Descending arpeggiated pattern, staccato"],
        ["3-3-2 Harmonic Minor", "A B C / D E F / G# A", "Group harmonic minor in 3-3-2"],
        ["Double Neighbor", "G# Bb A  -  D# F E", "Surround from above and below"],
        ["Piazzolla Sequence", "A C E - B D F - C E G#", "Rising 3rds through harmonic minor"],
        ["Tango Ending", "E D# E - F E D C B A", "Turn on the 5th, descend to tonic"],
    ],
    col_widths=[1.2*inch, 2*inch, 2.6*inch],
))

# --- Section 6: Rhythmic Patterns ---
story.append(P("6. RHYTHMIC PATTERNS TO APPLY TO ANY SCALE", 'SectionHead'))
story.append(P("Apply these rhythms to any of the scales above. X = play note, . = rest, &gt; = accent", 'SmallNote'))

story.append(make_table(
    ["Pattern", "Rhythm (over 2 bars of 4/4)", "Style"],
    [
        ["Son Clave Melody", "X . . X . . X . | . . X . . X . .", "Fundamental latin jazz phrasing"],
        ["Anticipated Downbeat", ". . . X | X . . . | . . . X | X . . .", "Push the 'one' - syncopated salsa feel"],
        ["Tresillo", "X . . X . . X . | X . . X . . X .", "3+3+2 repeated - Afro-Cuban DNA"],
        ["Habanera", "X . . X . X . . | X . . X . X . .", "Dotted quarter + eighth feel - tango base"],
        ["Cinquillo", "X . X X . X X .", "5-note Afro-Cuban pattern in 8 pulses"],
        ["Cascara", "X . X . X X . X | . X . X X . X .", "Rhythmic shell pattern from timbales"],
        ["Off-Beat Accent", ". X . X . X . X", "All upbeats - floating feel"],
        ["3 over 4", "X . . X . . X . . X . . | X . . X", "Polyrhythmic grouping for tension"],
    ],
    col_widths=[1.2*inch, 2.8*inch, 1.8*inch],
))

# --- Section 7: Transposition Guide ---
story.append(P("7. TRANSPOSITION GUIDE - Move Any Riff to All 12 Keys", 'SectionHead'))
story.append(P("Take any lick above and shift it by these intervals. Example: the Dorian riff D-F-A-C-A-F becomes:", 'SmallNote'))
story.append(make_table(
    ["Key", "Root-b3-5-b7-5-b3", "Key", "Root-b3-5-b7-5-b3"],
    [
        ["D min", "D F A C A F",     "Ab min", "Ab Cb Eb Gb Eb Cb"],
        ["Eb min", "Eb Gb Bb Db Bb Gb", "A min", "A C E G E C"],
        ["E min", "E G B D B G",     "Bb min", "Bb Db F Ab F Db"],
        ["F min", "F Ab C Eb C Ab",   "B min", "B D F# A F# D"],
        ["F# min", "F# A C# E C# A", "C min", "C Eb G Bb G Eb"],
        ["G min", "G Bb D F D Bb",   "C# min", "C# E G# B G# E"],
    ],
    col_widths=[0.6*inch, 2*inch, 0.6*inch, 2*inch],
))

story.append(sp(8))
story.append(P("<b>Practice method:</b> Pick ONE riff per day. Play it in the original key 5 times, then move it through the cycle of 4ths: D - G - C - F - Bb - Eb - Ab - Db - F# - B - E - A. Use a metronome starting at 80 BPM.", 'Body'))

story.append(PageBreak())

# ════════════════════════════════════════════════════════
# DAILY ROUTINE + CHEAT SHEET
# ════════════════════════════════════════════════════════
story.append(P("Daily Routine - Quick Reference", 'PhaseTitle'))
story.append(sp(8))

story.append(P("10-Minute Warm-Up (Every Day)", 'SectionHead'))
story.append(Bul("1. Long tones on the tonic of today's key (2 min)"))
story.append(Bul("2. Major scale ascending/descending, full range (2 min)"))
story.append(Bul("3. Dorian scale in today's key with clave foot tap (3 min)"))
story.append(Bul("4. Minor pentatonic in today's key, varying rhythms (3 min)"))

story.append(P("Phase Routines", 'SectionHead'))
story.append(make_table(
    ["Phase", "Time", "Blocks"],
    [
        ["Phase 1 (Wk 1-4)", "30 min", "Scales 10m + Patterns 10m + Improvise 10m"],
        ["Phase 2 (Wk 5-8)", "35 min", "New scales 10m + ii-V-i 10m + Bebop 5m + Improv 10m"],
        ["Phase 3 (Wk 9-12)", "40 min", "Altered 10m + Tension compare 10m + Phrygian 5m + Transcribe 5m + Improv 10m"],
        ["Phase 4 (Wk 13-16)", "45 min", "Tango cadences 10m + Adv. scales 10m + Tango vocab 10m + Transcribe 5m + Improv 10m"],
    ],
    col_widths=[1.2*inch, 0.6*inch, 4*inch],
))

# Scale cheat sheet
story.append(P("SCALE CHEAT SHEET: What to Play Over What", 'SectionHead'))
story.append(make_table(
    ["Chord Type", "First Choice", "Second Choice", "Third Choice"],
    [
        ["Major 7", "Major", "Lydian", "Lydian Augmented"],
        ["Dominant 7", "Mixolydian", "Bebop Dominant", "Lydian Dominant"],
        ["Dominant 7b9", "Spanish/Jewish", "Diminished (H-W)", "Altered"],
        ["Dominant 7#9", "Altered", "Diminished (H-W)", "Blues Scale"],
        ["Dominant 7#5", "Whole Tone", "Altered", ""],
        ["Dominant 7sus4", "Mixolydian (avoid 3rd)", "Pentatonic on b7", "Bebop"],
        ["Dominant 7b6", "Hindu", "", ""],
        ["Minor 7", "Dorian", "Minor Pentatonic", "Blues Scale"],
        ["Minor-Major 7", "Melodic Minor", "Harmonic Minor", ""],
        ["Minor b9 b6", "Phrygian", "", ""],
        ["Half-diminished", "Locrian #2", "Locrian", ""],
        ["Diminished 7", "Diminished (W-H)", "", ""],
    ],
    col_widths=[1.2*inch, 1.4*inch, 1.4*inch, 1.2*inch],
))

# Listening
story.append(P("Listening Homework", 'SectionHead'))
story.append(P("<b>Latin Jazz:</b>", 'SubSection'))
story.append(Bul("Paquito D'Rivera (alto sax model) | David Sanchez - Obsesion (tenor model)"))
story.append(Bul("Jerry Gonzalez &amp; Fort Apache Band | Chucho Valdes | Eddie Palmieri"))
story.append(Bul("Mongo Santamaria | Michel Camilo"))
story.append(P("<b>Tango:</b>", 'SubSection'))
story.append(Bul("Gato Barbieri - Chapter One: Latin America (tenor sax + tango)"))
story.append(Bul("Astor Piazzolla - Tango: Zero Hour | Libertango | Oblivion | Adios Nonino"))
story.append(Bul("Javier Girotto - Aires Tangueros (sax + modern tango)"))

# Progress tracker
story.append(P("16-Week Progress Tracker", 'SectionHead'))
story.append(make_table(
    ["Week", "Keys Mastered", "Scales Added", "Tunes Learned", "Solos Transcribed"],
    [[str(i), "", "", "", ""] for i in range(1, 17)],
    col_widths=[0.5*inch, 1.3*inch, 1.3*inch, 1.3*inch, 1.3*inch],
))

# ── Build ───────────────────────────────────────────────
doc.build(story)
print(f"PDF created: {output_path}")
