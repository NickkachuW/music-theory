"""
Generate the Common Latin Jazz Chord Progressions section.
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
)

DARK = HexColor("#1a1a2e")
ACCENT = HexColor("#e94560")
ACCENT2 = HexColor("#0f3460")
WHITE = HexColor("#ffffff")
TABLE_HEADER = HexColor("#1a1a2e")
TABLE_ALT = HexColor("#f0f0f8")
MUTED = HexColor("#666666")
GREEN = HexColor("#2d6a4f")

styles = getSampleStyleSheet()
for name, conf in [
    ('PT', dict(fontName='Helvetica-Bold', fontSize=22, textColor=ACCENT, spaceAfter=4)),
    ('PSub', dict(fontName='Helvetica', fontSize=12, textColor=MUTED, spaceAfter=12)),
    ('SH', dict(fontName='Helvetica-Bold', fontSize=14, textColor=ACCENT2, spaceBefore=16, spaceAfter=6)),
    ('SS', dict(fontName='Helvetica-Bold', fontSize=11, textColor=DARK, spaceBefore=10, spaceAfter=4)),
    ('B', dict(fontName='Helvetica', fontSize=9.5, textColor=DARK, spaceBefore=2, spaceAfter=4, leading=13)),
    ('BulC', dict(fontName='Helvetica', fontSize=9.5, textColor=DARK, leftIndent=18, spaceBefore=1, spaceAfter=1, leading=13)),
    ('SN', dict(fontName='Helvetica-Oblique', fontSize=8.5, textColor=MUTED, spaceBefore=2, spaceAfter=4)),
    ('TC', dict(fontName='Helvetica', fontSize=8, textColor=DARK, leading=10)),
    ('TH', dict(fontName='Helvetica-Bold', fontSize=8, textColor=WHITE, leading=10)),
    ('ScaleRec', dict(fontName='Helvetica-Bold', fontSize=9, textColor=GREEN, spaceBefore=2, spaceAfter=2, leading=12)),
    ('ProgTitle', dict(fontName='Helvetica-Bold', fontSize=12, textColor=ACCENT2, spaceBefore=14, spaceAfter=2)),
    ('ProgSub', dict(fontName='Helvetica-Oblique', fontSize=9.5, textColor=MUTED, spaceAfter=6)),
]:
    styles.add(ParagraphStyle(name=name, **conf))

def make_table(headers, rows, col_widths=None):
    data = [[Paragraph(h, styles['TH']) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), styles['TC']) for c in row])
    if col_widths is None:
        col_widths = [None] * len(headers)
    t = Table(data, colWidths=col_widths, repeatRows=1)
    cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 3),
        ('TOPPADDING', (0, 1), (-1, -1), 3),
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

def P(text, style='B'):
    return Paragraph(text, styles[style])
def Bul(text):
    return Paragraph(text, styles['BulC'])
def sp(pts=6):
    return Spacer(1, pts)

output_path = r"C:\Users\nicwo\Projects\music theory\latin-jazz-syllabus\chord_progressions.pdf"
doc = SimpleDocTemplate(output_path, pagesize=letter,
    topMargin=0.6*inch, bottomMargin=0.6*inch,
    leftMargin=0.65*inch, rightMargin=0.65*inch,
    title="Common Latin Jazz Chord Progressions",
)

story = []

story.append(P("Common Latin Jazz Chord Progressions", 'PT'))
story.append(P("Harmonic templates used across salsa, Afro-Cuban jazz, bossa nova, and tango", 'PSub'))
story.append(P("Each progression is shown in a common key with scale recommendations, then transposed to all 12 keys. Use these as vamp tracks for practicing your scales and riffs.", 'SN'))

# ════════════════════════════════════════════
# 1. MINOR DORIAN VAMP (i - IV)
# ════════════════════════════════════════════
story.append(P("1. The Dorian Vamp (i7 - IV7)", 'ProgTitle'))
story.append(P("Style: Salsa, Latin rock, cha-cha  |  Think: Oye Como Va, Evil Ways, Black Magic Woman", 'ProgSub'))

story.append(make_table(
    ["Bar", "Chord", "Scale", "Notes"],
    [
        ["1-2", "Am7", "A Dorian: A B C D E F# G", "Home base — emphasize F# (natural 6th)"],
        ["3-4", "D9", "D Mixolydian: D E F# G A B C", "Same notes as A Dorian — one scale fits all"],
    ],
    col_widths=[0.4*inch, 0.6*inch, 2.2*inch, 2.6*inch],
))
story.append(sp(4))
story.append(P("<b>Why it works:</b> Am7 and D9 share the same notes (A Dorian = D Mixolydian). You can solo with one scale over the entire vamp. This is the simplest latin jazz progression and the best place to start.", 'B'))
story.append(P("<b>Also try:</b> A minor pentatonic, A blues scale, or switch between Dorian and pentatonic.", 'ScaleRec'))
story.append(P("In all 12 keys:", 'SS'))
story.append(make_table(
    ["Key", "i7", "IV7", "Dorian Scale"],
    [
        ["A", "Am7", "D9", "A B C D E F# G"],
        ["Bb", "Bbm7", "Eb9", "Bb C Db Eb F G Ab"],
        ["B", "Bm7", "E9", "B C# D E F# G# A"],
        ["C", "Cm7", "F9", "C D Eb F G A Bb"],
        ["C#", "C#m7", "F#9", "C# D# E F# G# A# B"],
        ["D", "Dm7", "G9", "D E F G A B C"],
        ["Eb", "Ebm7", "Ab9", "Eb F Gb Ab Bb C Db"],
        ["E", "Em7", "A9", "E F# G A B C# D"],
        ["F", "Fm7", "Bb9", "F G Ab Bb C D Eb"],
        ["F#", "F#m7", "B9", "F# G# A B C# D# E"],
        ["G", "Gm7", "C9", "G A Bb C D E F"],
        ["Ab", "Abm7", "Db9", "Ab Bb Cb Db Eb F Gb"],
    ],
    col_widths=[0.4*inch, 0.7*inch, 0.6*inch, 2.5*inch],
))

# ════════════════════════════════════════════
# 2. MINOR ii-V-i
# ════════════════════════════════════════════
story.append(P("2. The Minor ii-V-i", 'ProgTitle'))
story.append(P("Style: The backbone of ALL latin jazz harmony  |  Think: Besame Mucho, Tin Tin Deo, Blue Bossa", 'ProgSub'))

story.append(make_table(
    ["Bar", "Chord", "Function", "Scale", "Tension Level"],
    [
        ["1-2", "Dm7(b5)", "ii", "D Locrian #2: D E F G Ab Bb C", "Low"],
        ["3-4", "G7(b9)", "V", "G Spanish/Jewish: G Ab B C D Eb F", "Medium-High"],
        ["5-8", "Cm6", "i", "C Harmonic Minor: C D Eb F G Ab B", "Resolution"],
    ],
    col_widths=[0.4*inch, 0.7*inch, 0.3*inch, 2.3*inch, 0.8*inch],
))
story.append(sp(4))
story.append(P("<b>Dominant substitutions</b> (try these on the V chord for different flavors):", 'SS'))
story.append(make_table(
    ["V Chord Scale", "Sound", "When to Use"],
    [
        ["G Spanish/Jewish", "Classic latin, Afro-Cuban", "Default choice — always works"],
        ["G Altered (Dim WT)", "Maximum tension, modern jazz", "When you want to push outside"],
        ["G Diminished (H-W)", "Angular, symmetric", "Over G7b9 for a jazzy edge"],
        ["G Bebop Dominant", "Smooth eighth-note lines", "For flowing bebop-style lines"],
        ["G Whole Tone", "Floating, dreamy", "Over G7#5 voicings"],
    ],
    col_widths=[1.3*inch, 1.5*inch, 2.5*inch],
))
story.append(P("In all 12 minor keys:", 'SS'))
story.append(make_table(
    ["Key", "ii (half-dim)", "V7(b9)", "i"],
    [
        ["Cm", "Dm7(b5)", "G7(b9)", "Cm"],
        ["C#m", "D#m7(b5)", "G#7(b9)", "C#m"],
        ["Dm", "Em7(b5)", "A7(b9)", "Dm"],
        ["Ebm", "Fm7(b5)", "Bb7(b9)", "Ebm"],
        ["Em", "F#m7(b5)", "B7(b9)", "Em"],
        ["Fm", "Gm7(b5)", "C7(b9)", "Fm"],
        ["F#m", "G#m7(b5)", "C#7(b9)", "F#m"],
        ["Gm", "Am7(b5)", "D7(b9)", "Gm"],
        ["Abm", "Bbm7(b5)", "Eb7(b9)", "Abm"],
        ["Am", "Bm7(b5)", "E7(b9)", "Am"],
        ["Bbm", "Cm7(b5)", "F7(b9)", "Bbm"],
        ["Bm", "C#m7(b5)", "F#7(b9)", "Bm"],
    ],
    col_widths=[0.5*inch, 1.1*inch, 0.9*inch, 0.6*inch],
))

# ════════════════════════════════════════════
# 3. MAJOR ii-V-I
# ════════════════════════════════════════════
story.append(P("3. The Major ii-V-I", 'ProgTitle'))
story.append(P("Style: Bossa nova, Latin jazz standards  |  Think: Desafinado, Girl from Ipanema, Corcovado", 'ProgSub'))

story.append(make_table(
    ["Bar", "Chord", "Function", "Scale"],
    [
        ["1-2", "Dm7", "ii", "D Dorian: D E F G A B C"],
        ["3-4", "G7", "V", "G Mixolydian: G A B C D E F (or Bebop Dom)"],
        ["5-8", "Cmaj7", "I", "C Major: C D E F G A B (or C Lydian)"],
    ],
    col_widths=[0.4*inch, 0.7*inch, 0.4*inch, 3.3*inch],
))
story.append(P("In all 12 major keys:", 'SS'))
story.append(make_table(
    ["Key", "ii", "V7", "I"],
    [
        ["C", "Dm7", "G7", "Cmaj7"], ["Db", "Ebm7", "Ab7", "Dbmaj7"],
        ["D", "Em7", "A7", "Dmaj7"], ["Eb", "Fm7", "Bb7", "Ebmaj7"],
        ["E", "F#m7", "B7", "Emaj7"], ["F", "Gm7", "C7", "Fmaj7"],
        ["F#", "G#m7", "C#7", "F#maj7"], ["G", "Am7", "D7", "Gmaj7"],
        ["Ab", "Bbm7", "Eb7", "Abmaj7"], ["A", "Bm7", "E7", "Amaj7"],
        ["Bb", "Cm7", "F7", "Bbmaj7"], ["B", "C#m7", "F#7", "Bmaj7"],
    ],
    col_widths=[0.4*inch, 0.8*inch, 0.7*inch, 0.8*inch],
))

# ════════════════════════════════════════════
# 4. CYCLE OF DOMINANTS
# ════════════════════════════════════════════
story.append(P("4. Cycle of Dominants", 'ProgTitle'))
story.append(P("Style: Swing/latin bridge sections  |  Think: Caravan bridge, Autumn Leaves, rhythm changes bridge", 'ProgSub'))

story.append(make_table(
    ["Bar", "Chord", "Resolves to", "Scale"],
    [
        ["1-2", "F7", "Bb7", "F Mixolydian (or Bebop Dominant)"],
        ["3-4", "Bb7", "Eb7", "Bb Mixolydian"],
        ["5-6", "Eb7", "Abmaj7", "Eb Mixolydian"],
        ["7-8", "Abmaj7", "(home)", "Ab Major or Ab Lydian"],
    ],
    col_widths=[0.4*inch, 0.6*inch, 0.7*inch, 2.8*inch],
))
story.append(P("<b>Pattern:</b> Each dominant 7th resolves down a perfect 5th to the next. Use Mixolydian or Bebop Dominant on each chord. This pattern appears in bridges of many standards.", 'B'))
story.append(P("<b>Advanced:</b> Try Spanish/Jewish on each dominant for a latin flavor, or Altered for maximum tension.", 'ScaleRec'))

# ════════════════════════════════════════════
# 5. PHRYGIAN CADENCE (bII - V7b9 - i)
# ════════════════════════════════════════════
story.append(P("5. Phrygian Cadence (bII - V7b9 - i)", 'ProgTitle'))
story.append(P("Style: Tango, flamenco-jazz, dramatic latin  |  Think: Piazzolla, Caravan intro, Spanish-tinged jazz", 'ProgSub'))

story.append(make_table(
    ["Bar", "Chord", "Function", "Scale"],
    [
        ["1-2", "Dbmaj7", "bII", "Db Lydian: Db Eb F G Ab Bb C"],
        ["3-4", "G7(b9)", "V", "G Spanish/Jewish: G Ab B C D Eb F"],
        ["5-8", "Cm", "i", "C Harmonic Minor: C D Eb F G Ab B"],
    ],
    col_widths=[0.4*inch, 0.7*inch, 0.4*inch, 3.3*inch],
))
story.append(P("<b>The tango signature:</b> The bII chord (a half step above the tonic) slides down to the V7(b9), then resolves to i. The augmented 2nd interval in the Spanish scale IS the sound of tango.", 'B'))
story.append(P("In all 12 minor keys:", 'SS'))
story.append(make_table(
    ["i", "bII", "V7(b9)", "i"],
    [
        ["Cm", "Dbmaj7", "G7(b9)", "Cm"],
        ["C#m", "Dmaj7", "G#7(b9)", "C#m"],
        ["Dm", "Ebmaj7", "A7(b9)", "Dm"],
        ["Ebm", "Emaj7 (Fbmaj7)", "Bb7(b9)", "Ebm"],
        ["Em", "Fmaj7", "B7(b9)", "Em"],
        ["Fm", "Gbmaj7", "C7(b9)", "Fm"],
        ["F#m", "Gmaj7", "C#7(b9)", "F#m"],
        ["Gm", "Abmaj7", "D7(b9)", "Gm"],
        ["Abm", "Amaj7 (Bbbmaj7)", "Eb7(b9)", "Abm"],
        ["Am", "Bbmaj7", "E7(b9)", "Am"],
        ["Bbm", "Cbmaj7 (Bmaj7)", "F7(b9)", "Bbm"],
        ["Bm", "Cmaj7", "F#7(b9)", "Bm"],
    ],
    col_widths=[0.5*inch, 1.3*inch, 0.9*inch, 0.5*inch],
))

# ════════════════════════════════════════════
# 6. bVI - V7 - i
# ════════════════════════════════════════════
story.append(P("6. bVI - V7(b9) - i (Dramatic Minor Cadence)", 'ProgTitle'))
story.append(P("Style: Bolero, tango, dramatic ballads  |  Think: Besame Mucho, Obsesion", 'ProgSub'))

story.append(make_table(
    ["Bar", "Chord", "Function", "Scale"],
    [
        ["1-2", "Abmaj7", "bVI", "Ab Major: Ab Bb C Db Eb F G"],
        ["3-4", "G7(b9)", "V", "G Spanish/Jewish: G Ab B C D Eb F"],
        ["5-8", "Cm", "i", "C Harmonic Minor: C D Eb F G Ab B"],
    ],
    col_widths=[0.4*inch, 0.7*inch, 0.4*inch, 3.3*inch],
))
story.append(P("<b>This cadence</b> is extremely common in bolero and tango. The bVI chord shares two notes with the i chord (Ab and C in Cm), creating a smooth voice-leading descent: Ab -> G -> G (bVI root drops to V root to resolve).", 'B'))
story.append(P("In all 12 keys:", 'SS'))
story.append(make_table(
    ["i", "bVI", "V7(b9)"],
    [
        ["Cm", "Abmaj7", "G7(b9)"], ["Dm", "Bbmaj7", "A7(b9)"],
        ["Em", "Cmaj7", "B7(b9)"], ["Fm", "Dbmaj7", "C7(b9)"],
        ["Gm", "Ebmaj7", "D7(b9)"], ["Am", "Fmaj7", "E7(b9)"],
        ["Bbm", "Gbmaj7", "F7(b9)"], ["Bm", "Gmaj7", "F#7(b9)"],
    ],
    col_widths=[0.6*inch, 1*inch, 0.9*inch],
))

# ════════════════════════════════════════════
# 7. SALSA MONTUNO VAMP (I - IV - V - IV)
# ════════════════════════════════════════════
story.append(P("7. Salsa Montuno Vamp (I - IV - V - IV)", 'ProgTitle'))
story.append(P("Style: Salsa, son montuno, descarga  |  The dance floor groove", 'ProgSub'))

story.append(make_table(
    ["Bar", "Chord", "Scale"],
    [
        ["1", "C", "C Major: C D E F G A B"],
        ["2", "F", "F Major (or F Lydian)"],
        ["3", "G7", "G Mixolydian: G A B C D E F"],
        ["4", "F", "F Major"],
    ],
    col_widths=[0.4*inch, 0.6*inch, 3.5*inch],
))
story.append(P("<b>Simplicity is power:</b> This I-IV-V-IV loop drives hundreds of salsa tunes. Use C major pentatonic over the whole thing. Add blues notes for flavor. Focus on RHYTHM, not note complexity.", 'B'))

# ════════════════════════════════════════════
# 8. GUAJIRA (6/8 - 3/4 hemiola, Cuban countryside)
# ════════════════════════════════════════════
story.append(P("8. Guajira (Cuban 6/8-3/4 Hemiola)", 'ProgTitle'))
story.append(P("Style: Traditional Cuban, guajira-son  |  Think: Guantanamera, Paquito D'Rivera's guajiras, Bebo Valdes", 'ProgSub'))

story.append(P("<b>The signature sound:</b> The guajira alternates between <b>6/8</b> and <b>3/4</b> feel — the same 6 eighth notes can be grouped as 2 groups of 3 (compound duple) or 3 groups of 2 (simple triple). This creates a rolling, rural, lyrical feel unlike anything else in latin music.", 'B'))

story.append(P("Classic Guajira Form (16 bars, alternating major/relative minor):", 'SS'))
story.append(make_table(
    ["Bars", "Chord", "Feel", "Scale"],
    [
        ["1-2", "C", "I (major, 6/8)", "C Major Pentatonic: C D E G A"],
        ["3-4", "G7", "V", "G Mixolydian: G A B C D E F"],
        ["5-6", "C", "I", "C Major: C D E F G A B"],
        ["7-8", "G7", "V", "G Mixolydian"],
        ["9-10", "Am", "vi (shift to minor)", "A Natural Minor: A B C D E F G"],
        ["11-12", "E7", "V/vi", "E Spanish/Jewish: E F G# A B C D"],
        ["13-14", "Am / Dm", "vi / ii", "A Aeolian / D Dorian"],
        ["15-16", "G7 / C", "V / I (back home)", "G Mixolydian / C Major"],
    ],
    col_widths=[0.5*inch, 0.8*inch, 1.2*inch, 2.3*inch],
))
story.append(sp(4))
story.append(P("<b>Scale strategy:</b> Keep it simple and lyrical. Use major pentatonic in the major sections, natural minor (Aeolian) in the minor sections. The E7 to Am is the only dramatic moment — use E Spanish/Jewish here for the traditional Cuban flavor.", 'ScaleRec'))

story.append(P("The 6/8 vs 3/4 Hemiola:", 'SS'))
story.append(make_table(
    ["Feel", "Grouping", "Accent Pattern", "Character"],
    [
        ["6/8", "Two groups of 3: (1-2-3)(4-5-6)", "&gt; . . &gt; . .", "Flowing, rolling, pastoral"],
        ["3/4", "Three groups of 2: (1-2)(3-4)(5-6)", "&gt; . &gt; . &gt; .", "March-like, lilting, Spanish"],
        ["Combined", "Alternate between them", "Shifting accents", "THE guajira sound"],
    ],
    col_widths=[0.5*inch, 2*inch, 1.2*inch, 1.5*inch],
))
story.append(P("<b>Practice tip:</b> Play a C major scale for 6 beats. First pass in 6/8 (accent beats 1 and 4). Second pass in 3/4 (accent beats 1, 3, and 5). Once you can switch smoothly, you've got the guajira feel.", 'B'))

story.append(P("Simplified Guajira Vamp (for practice):", 'SS'))
story.append(make_table(
    ["Bars", "Chord", "Scale"],
    [
        ["1-4", "C", "C Major Pentatonic"],
        ["5-8", "Am", "A Natural Minor"],
        ["9-12", "Dm", "D Dorian: D E F G A B C"],
        ["13-16", "G7 / C", "G Mixolydian resolving to C Major"],
    ],
    col_widths=[0.5*inch, 1*inch, 3.3*inch],
))

story.append(P("In all 12 keys (simplified I - V7 - vi - V/vi pattern):", 'SS'))
story.append(make_table(
    ["Major Key", "I", "V7", "vi", "V7/vi"],
    [
        ["C", "C", "G7", "Am", "E7"],
        ["Db", "Db", "Ab7", "Bbm", "F7"],
        ["D", "D", "A7", "Bm", "F#7"],
        ["Eb", "Eb", "Bb7", "Cm", "G7"],
        ["E", "E", "B7", "C#m", "G#7"],
        ["F", "F", "C7", "Dm", "A7"],
        ["F#", "F#", "C#7", "D#m", "A#7"],
        ["G", "G", "D7", "Em", "B7"],
        ["Ab", "Ab", "Eb7", "Fm", "C7"],
        ["A", "A", "E7", "F#m", "C#7"],
        ["Bb", "Bb", "F7", "Gm", "D7"],
        ["B", "B", "F#7", "G#m", "D#7"],
    ],
    col_widths=[0.6*inch, 0.6*inch, 0.7*inch, 0.7*inch, 0.8*inch],
))

story.append(P("<b>Why this matters:</b> The guajira is the countryside soul of Cuban music — simpler and more melodic than the urban son montuno. Learning it gives you access to the lyrical, singable side of latin jazz. 'Guantanamera' is the most famous example — if you can play over its changes, you understand the guajira.", 'B'))

# ════════════════════════════════════════════
# 9. MINOR DESCENDING CYCLE
# ════════════════════════════════════════════
story.append(P("9. Minor Descending Cycle (i - iv - VII - III - VI - ii - V - i)", 'ProgTitle'))
story.append(P("Style: Tango nuevo, sophisticated jazz  |  Think: Oblivion (Piazzolla), Autumn Leaves", 'ProgSub'))

story.append(make_table(
    ["Bar", "Chord", "Function", "Scale"],
    [
        ["1-2", "Cm", "i", "C Dorian (or Melodic Minor)"],
        ["3-4", "Fm7", "iv", "F Dorian: F G Ab Bb C D Eb"],
        ["5-6", "Bb7", "VII", "Bb Mixolydian: Bb C D Eb F G Ab"],
        ["7-8", "Ebmaj7", "III", "Eb Major: Eb F G Ab Bb C D"],
        ["9-10", "Abmaj7", "VI", "Ab Lydian: Ab Bb C D Eb F G"],
        ["11-12", "Dm7(b5)", "ii", "D Locrian #2: D E F G Ab Bb C"],
        ["13-14", "G7(b9)", "V", "G Spanish/Jewish: G Ab B C D Eb F"],
        ["15-16", "Cm", "i", "C Harmonic Minor: C D Eb F G Ab B"],
    ],
    col_widths=[0.5*inch, 0.8*inch, 0.4*inch, 2.8*inch],
))
story.append(P("<b>The complete minor key journey:</b> This cycle touches every diatonic chord in C minor. It descends by 4ths (C-F-Bb-Eb-Ab-D-G-C). This is the progression in Piazzolla's Oblivion and many jazz standards.", 'B'))
story.append(P("<b>Scale strategy:</b> Use Dorian/Melodic Minor on i, Dorian on iv, Mixolydian on VII and III area, Locrian #2 on ii, Spanish/Jewish on V, Harmonic Minor for final resolution.", 'ScaleRec'))

# ════════════════════════════════════════════
# 10. STATIC DOMINANT VAMP
# ════════════════════════════════════════════
story.append(P("10. Static Dominant Vamp", 'ProgTitle'))
story.append(P("Style: Afro-Cuban, descarga, guaguanco  |  Think: Manteca A section, rumba jams", 'ProgSub'))

story.append(make_table(
    ["Bar", "Chord", "Scale Options"],
    [
        ["1-8+", "Bb7 (static, no resolution)", "Bb Mixolydian — safe, consonant\n"
         "Bb Lydian Dominant — bright #4 color\n"
         "Bb Blues — earthy, soulful\n"
         "Bb Bebop Dominant — smooth 8th-note lines"],
    ],
    col_widths=[0.4*inch, 1.5*inch, 3.9*inch],
))
story.append(P("<b>When the dominant doesn't resolve:</b> Use Lydian Dominant instead of Mixolydian. The #4 prevents the chord from wanting to resolve, matching the static harmony. This is common in Afro-Cuban vamps where a dominant chord just grooves indefinitely.", 'B'))

# ════════════════════════════════════════════
# 10. COLTRANE CHANGES (Latin application)
# ════════════════════════════════════════════
story.append(P("11. Tritone Substitution Turnaround", 'ProgTitle'))
story.append(P("Style: Modern bossa, sophisticated latin jazz  |  Think: Desafinado, jobim ballads", 'ProgSub'))

story.append(make_table(
    ["Bar", "Chord", "Function", "Scale"],
    [
        ["1", "Cmaj7", "I", "C Major"],
        ["2", "Db7(#11)", "subV/I (tritone sub of G7)", "Db Lydian Dominant: Db Eb F G Ab Bb Cb"],
        ["3", "Cmaj7", "I", "C Lydian: C D E F# G A B"],
        ["4", "B7(#11)", "subV/ii (tritone sub of F7)", "B Lydian Dominant: B C# D# E# F# G# A"],
    ],
    col_widths=[0.4*inch, 1*inch, 1.3*inch, 2.1*inch],
))
story.append(P("<b>Tritone substitutions</b> replace a V7 chord with a dominant 7th a tritone away (e.g., Db7 replaces G7). The Lydian Dominant scale is THE scale for these chords. This is the sound of sophisticated bossa nova harmony (Jobim used this constantly).", 'B'))
story.append(P("<b>Rule of thumb:</b> See a dominant 7th with a #11 or b5? Use Lydian Dominant every time.", 'ScaleRec'))

# ════════════════════════════════════════════
# 11. MINOR BLUES
# ════════════════════════════════════════════
story.append(P("12. Latin Minor Blues (12-bar)", 'ProgTitle'))
story.append(P("Style: Latin blues, Afro-Cuban blues  |  Think: Senor Blues, Blue Monk (latin arrangement)", 'ProgSub'))

story.append(make_table(
    ["Bar", "Chord", "Function", "Scale"],
    [
        ["1-4", "Cm7", "i", "C Dorian, C Minor Pentatonic, C Blues"],
        ["5-6", "Fm7", "iv", "F Dorian: F G Ab Bb C D Eb"],
        ["7-8", "Cm7", "i", "C Dorian or C Blues"],
        ["9", "Dm7(b5)", "ii", "D Locrian #2: D E F G Ab Bb C"],
        ["10", "G7(b9)", "V", "G Spanish/Jewish or G Altered"],
        ["11-12", "Cm7", "i", "C Minor Pentatonic (turnaround)"],
    ],
    col_widths=[0.4*inch, 0.7*inch, 0.4*inch, 3.1*inch],
))
story.append(P("<b>The minor blues</b> is a 12-bar form that bridges blues and jazz. You can play minor pentatonic or blues scale over the entire form, then get more specific with Dorian on the i, Spanish/Jewish on the V. Latin feel comes from the rhythm, not the harmony.", 'B'))

# ════════════════════════════════════════════
# 12. PIAZZOLLA HARMONIC SEQUENCE
# ════════════════════════════════════════════
story.append(P("13. Piazzolla Tango Sequence (chromatic bass descent)", 'ProgTitle'))
story.append(P("Style: Tango nuevo  |  Think: Libertango, Adios Nonino, Buenos Aires Hora Cero", 'ProgSub'))

story.append(make_table(
    ["Bar", "Chord (over bass)", "Bass Note", "Scale"],
    [
        ["1", "Am", "A", "A Harmonic Minor"],
        ["2", "Am/G#", "G# (descending)", "A Harmonic Minor (G# is the leading tone)"],
        ["3", "Am/G", "G natural", "A Dorian (G natural implies natural 7th descent)"],
        ["4", "Am/F#", "F#", "D Lydian Dominant or passing diminished"],
        ["5", "Dm/F", "F", "D Dorian or D Harmonic Minor"],
        ["6", "E7", "E", "E Spanish/Jewish: E F G# A B C D"],
        ["7-8", "Am", "A", "A Harmonic Minor (resolution)"],
    ],
    col_widths=[0.4*inch, 1*inch, 0.8*inch, 2.6*inch],
))
story.append(P("<b>The chromatic descending bass line</b> (A - G# - G - F# - F - E) is the DNA of tango nuevo. While the bass descends chromatically, the upper harmony shifts between harmonic minor, dorian, and passing diminished sounds. This creates the dramatic, cinematic quality of Piazzolla.", 'B'))
story.append(P("<b>Practice tip:</b> Play A harmonic minor over the first 2 bars, then let your ear guide you through the chromatic descent. The E7 at the end is pure Spanish/Jewish territory.", 'ScaleRec'))

# ── Summary ──
story.append(PageBreak())
story.append(P("Quick Reference: All 13 Progressions", 'SH'))
story.append(make_table(
    ["#", "Progression", "Style", "Key Scale(s)"],
    [
        ["1", "i7 - IV7 (Dorian Vamp)", "Salsa, cha-cha", "Dorian, Minor Pentatonic"],
        ["2", "ii(b5) - V7(b9) - i (Minor ii-V-i)", "All latin jazz", "Locrian #2, Spanish/Jewish, Harm Minor"],
        ["3", "ii - V7 - I (Major ii-V-I)", "Bossa nova", "Dorian, Mixolydian, Major"],
        ["4", "V7/ii - V7/V - V7 - I (Cycle of Doms)", "Swing/latin bridges", "Mixolydian on each"],
        ["5", "bII - V7(b9) - i (Phrygian Cadence)", "Tango, flamenco", "Lydian, Spanish/Jewish, Harm Minor"],
        ["6", "bVI - V7(b9) - i", "Bolero, tango", "Major, Spanish/Jewish, Harm Minor"],
        ["7", "I - IV - V - IV (Montuno Vamp)", "Salsa, son", "Major Pentatonic"],
        ["8", "Guajira (6/8-3/4 hemiola, I-V-vi-E7)", "Cuban countryside", "Major Pentatonic, Natural Minor, Spanish"],
        ["9", "i-iv-VII-III-VI-ii-V-i (Minor Cycle)", "Tango nuevo, jazz", "Dorian, Mixolydian, Spanish"],
        ["10", "Static V7 (Dominant Vamp)", "Afro-Cuban, descarga", "Lydian Dominant, Mixolydian"],
        ["11", "I - subV - I (Tritone Sub)", "Modern bossa", "Lydian Dominant"],
        ["12", "12-bar Minor Blues", "Latin blues", "Blues, Dorian, Spanish"],
        ["13", "Chromatic Bass Descent", "Tango nuevo", "Harmonic Minor, Spanish"],
    ],
    col_widths=[0.3*inch, 1.8*inch, 1.1*inch, 2.2*inch],
))

doc.build(story)
print(f"PDF created: {output_path}")
