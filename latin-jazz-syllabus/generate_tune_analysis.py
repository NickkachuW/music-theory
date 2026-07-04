"""
Generate the Tune Analysis section for the Latin Jazz syllabus PDF.
Maps every chord to recommended scales from the syllabus.
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

DARK = HexColor("#1a1a2e")
ACCENT = HexColor("#e94560")
ACCENT2 = HexColor("#0f3460")
LIGHT_BG = HexColor("#f5f5f5")
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
    ('BB', dict(fontName='Helvetica-Bold', fontSize=9.5, textColor=DARK, spaceBefore=2, spaceAfter=4, leading=13)),
    ('BulC', dict(fontName='Helvetica', fontSize=9.5, textColor=DARK, leftIndent=18, spaceBefore=1, spaceAfter=1, leading=13)),
    ('SN', dict(fontName='Helvetica-Oblique', fontSize=8.5, textColor=MUTED, spaceBefore=2, spaceAfter=4)),
    ('TC', dict(fontName='Helvetica', fontSize=8, textColor=DARK, leading=10)),
    ('TH', dict(fontName='Helvetica-Bold', fontSize=8, textColor=WHITE, leading=10)),
    ('TuneTitle', dict(fontName='Helvetica-Bold', fontSize=16, textColor=ACCENT2, spaceBefore=4, spaceAfter=2)),
    ('TuneInfo', dict(fontName='Helvetica', fontSize=10, textColor=MUTED, spaceAfter=8)),
    ('ScaleRec', dict(fontName='Helvetica-Bold', fontSize=9, textColor=GREEN, spaceBefore=2, spaceAfter=2, leading=12)),
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
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
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

W = letter[0] - 1.3*inch

output_path = r"C:\Users\nicwo\Projects\music theory\latin-jazz-syllabus\tune_analysis.pdf"
doc = SimpleDocTemplate(output_path, pagesize=letter,
    topMargin=0.6*inch, bottomMargin=0.6*inch,
    leftMargin=0.65*inch, rightMargin=0.65*inch,
    title="Tune Analysis - Latin Jazz & Tango",
)

story = []

# ── TITLE ──
story.append(P("Tune Analysis", 'PT'))
story.append(P("10 Latin Jazz &amp; Tango Standards — Chord-to-Scale Mapping", 'PSub'))
story.append(P("For each chord, the recommended scale from your syllabus is shown. Practice the tune by playing through the form using these scale choices.", 'SN'))
story.append(sp(8))

# ════════════════════════════════════════════
# TUNE 1: OYE COMO VA
# ════════════════════════════════════════════
story.append(P("1. Oye Como Va", 'TuneTitle'))
story.append(P("Tito Puente  |  Key: A Dorian  |  Form: 2-chord vamp (open)  |  Time: 4/4 Cha-cha  |  Difficulty: Beginner", 'TuneInfo'))

story.append(make_table(
    ["Bars", "Chord", "Scale Choice", "Notes"],
    [
        ["1-2", "Am7", "A Dorian: A B C D E F# G", "The workhorse — emphasize the F# (natural 6th)"],
        ["3-4", "D9", "D Mixolydian: D E F# G A B C", "Or stay on A Dorian — same notes!"],
    ],
    col_widths=[0.5*inch, 0.6*inch, 2.2*inch, 2.5*inch],
))
story.append(sp(4))
story.append(P("<b>Why this tune:</b> Perfect beginner tune. Two chords, infinite possibilities. Am7-D9 is a i-IV vamp in A Dorian. Since both chords share the same notes (A Dorian = D Mixolydian), you can play A Dorian or A minor pentatonic over the entire tune.", 'B'))
story.append(P("<b>Practice tip:</b> Start with A minor pentatonic only. Then add the F# (Dorian 6th). Then try A Blues scale for grit. Focus on RHYTHM over note choice — this tune is all about the groove.", 'ScaleRec'))

# ════════════════════════════════════════════
# TUNE 2: SENOR BLUES
# ════════════════════════════════════════════
story.append(P("2. Senor Blues", 'TuneTitle'))
story.append(P("Horace Silver  |  Key: Eb minor  |  Form: 12-bar minor blues  |  Time: 6/8 Afro-Cuban  |  Difficulty: Beginner-Intermediate", 'TuneInfo'))

story.append(make_table(
    ["Bars", "Chord", "Function", "Scale Choice"],
    [
        ["1-2", "Ebm6/9", "i", "Eb Dorian: Eb F Gb Ab Bb C Db"],
        ["3-4", "Ebm6/9", "i", "Eb Minor Pentatonic: Eb Gb Ab Bb Db"],
        ["5-6", "Cb9 (B9)", "bVI", "Cb Mixolydian: Cb Db Eb Fb Gb Ab Bbb"],
        ["7-8", "Ebm6/9", "i", "Eb Blues: Eb Gb Ab A Bb Db"],
        ["9", "Bb7", "V", "Bb Spanish/Jewish: Bb Cb D Eb F Gb Ab"],
        ["10", "Ab7", "IV", "Ab Mixolydian: Ab Bb C Db Eb F Gb"],
        ["11-12", "Ebm6/9", "i", "Eb Dorian or Eb Minor Pentatonic"],
    ],
    col_widths=[0.5*inch, 0.8*inch, 0.4*inch, 3.1*inch],
))
story.append(sp(4))
story.append(P("<b>Why this tune:</b> Bridges blues and latin jazz vocabulary. The 6/8 Afro-Cuban feel teaches you to think in a different rhythmic grid. The bVI chord (Cb9) is a classic minor blues move.", 'B'))
story.append(P("<b>Practice tip:</b> Eb minor pentatonic works over the entire form. Add Dorian for color. On the Bb7 (bar 9), try Spanish/Jewish for that latin V7 sound. The 6/8 feel means thinking in groups of 3.", 'ScaleRec'))

# ════════════════════════════════════════════
# TUNE 3: STOLEN MOMENTS
# ════════════════════════════════════════════
story.append(P("3. Stolen Moments", 'TuneTitle'))
story.append(P("Oliver Nelson  |  Key: C minor  |  Form: 12-bar minor blues + chromatic passage  |  Time: 4/4  |  Difficulty: Intermediate", 'TuneInfo'))

story.append(make_table(
    ["Bars", "Chord", "Function", "Scale Choice"],
    [
        ["1-4", "Cm7 / Cm6", "i", "C Dorian: C D Eb F G A Bb"],
        ["5-6", "Fm7 / Fm6", "iv", "F Dorian: F G Ab Bb C D Eb"],
        ["7-8", "Cm7 / Cm6", "i", "C Dorian or C Minor Pentatonic"],
        ["9", "Dm7(b5)", "ii (of V)", "D Locrian #2: D E F G Ab Bb C"],
        ["10", "G7(b13)", "V", "G Spanish/Jewish: G Ab B C D Eb F"],
        ["11-12", "Cm7 / Cm6", "i", "C Dorian"],
    ],
    col_widths=[0.5*inch, 0.9*inch, 0.6*inch, 2.8*inch],
))
story.append(sp(2))
story.append(P("Chromatic Passage (the signature section):", 'SS'))
story.append(make_table(
    ["Bar", "Chord", "Scale Choice"],
    [
        ["13", "Dm11 / Ebm11", "D Dorian / Eb Dorian (shift up a half step)"],
        ["14", "Em11 / Fm11", "E Dorian / F Dorian (shift up a half step)"],
        ["15", "F#m11 / Fm11", "F# Dorian / F Dorian (shift back down)"],
        ["16", "Em11 / Ebm11", "E Dorian / Eb Dorian (continue descent)"],
    ],
    col_widths=[0.5*inch, 1.2*inch, 3.5*inch],
))
story.append(P("<b>Practice tip:</b> The chromatic passage is a Dorian scale shifting up by half steps then back down. Practice Dorian in ALL keys — this tune tests whether you can move between them fluidly.", 'ScaleRec'))

# ════════════════════════════════════════════
# TUNE 4: BESAME MUCHO
# ════════════════════════════════════════════
story.append(P("4. Besame Mucho", 'TuneTitle'))
story.append(P("Consuelo Velazquez  |  Key: D minor  |  Form: ABA  |  Time: 4/4 Bolero  |  Difficulty: Intermediate", 'TuneInfo'))

story.append(make_table(
    ["Bars", "Chord", "Function", "Scale Choice"],
    [
        ["A: 1-2", "Dm6", "i", "D Harmonic Minor: D E F G A Bb C#"],
        ["3-4", "Gm6", "iv", "G Dorian: G A Bb C D E F"],
        ["5-6", "Gm6 / D7(b9)", "iv / V/iv", "D7b9: D Spanish/Jewish: D Eb F# G A Bb C"],
        ["7-8", "Em7(b5) / A7(b9)", "ii-V", "Em7b5: E Locrian #2 / A7b9: A Spanish/Jewish"],
        ["9-10", "Dm6", "i", "D Melodic Minor: D E F G A B C#"],
        ["11-12", "A7(b9) / D7(b9)", "V / V/iv", "A Spanish: A Bb C# D E F G"],
        ["13-14", "Gm6", "iv", "G Harmonic Minor: G A Bb C D Eb F#"],
        ["15-16", "Bm7(b5) / E7(b9) / A7(b9)", "ii-V-V", "B Locrian #2 / E Spanish / A Spanish"],
    ],
    col_widths=[0.5*inch, 1.3*inch, 0.5*inch, 2.5*inch],
))
story.append(sp(2))
story.append(make_table(
    ["Bars", "Chord", "Function", "Scale Choice"],
    [
        ["B: 1-2", "Gm6", "iv", "G Dorian: G A Bb C D E F"],
        ["3-4", "Dm6", "i", "D Harmonic Minor"],
        ["5-6", "Em7(b5) / A7(b9)", "ii-V", "E Locrian #2 / A Spanish/Jewish"],
        ["7-8", "Dm6 / D7(b9)", "i / V/iv", "D Harm Minor / D Spanish"],
    ],
    col_widths=[0.5*inch, 1.3*inch, 0.5*inch, 2.5*inch],
))
story.append(P("<b>Why this tune:</b> A masterclass in minor key harmony. Almost every dominant chord is a V7(b9) — perfect for drilling Spanish/Jewish scale. The Dm6 tonic invites both Harmonic Minor and Melodic Minor.", 'B'))
story.append(P("<b>Practice tip:</b> This tune is FULL of Spanish/Jewish opportunities. Practice A Spanish (A Bb C# D E F G) and D Spanish (D Eb F# G A Bb C) until they are automatic. The Em7(b5)-A7(b9)-Dm cadence appears repeatedly — this is the minor ii-V-i from Phase 2.", 'ScaleRec'))

# ════════════════════════════════════════════
# TUNE 5: TIN TIN DEO
# ════════════════════════════════════════════
story.append(P("5. Tin Tin Deo", 'TuneTitle'))
story.append(P("Chano Pozo / Gil Fuller / Dizzy Gillespie  |  Key: C minor  |  Form: AABA (32 bars)  |  Time: 4/4 Afro-Cuban  |  Difficulty: Intermediate", 'TuneInfo'))

story.append(P("Intro Vamp (Latin feel):", 'SS'))
story.append(make_table(
    ["Bars", "Chord", "Scale Choice"],
    [
        ["1-2", "Cm7", "C Dorian: C D Eb F G A Bb"],
        ["3-4", "Dm7(b5) / G7(b9)", "D Locrian #2: D E F G Ab Bb C / G Spanish: G Ab B C D Eb F"],
    ],
    col_widths=[0.5*inch, 1.5*inch, 3.8*inch],
))
story.append(P("A Section:", 'SS'))
story.append(make_table(
    ["Bars", "Chord", "Function", "Scale Choice"],
    [
        ["1-2", "Cm7", "i", "C Dorian"],
        ["3-4", "Fm7", "iv", "F Dorian: F G Ab Bb C D Eb"],
        ["5", "Dm7(b5)", "ii", "D Locrian #2: D E F G Ab Bb C"],
        ["6", "G7(b9)", "V", "G Spanish/Jewish: G Ab B C D Eb F"],
        ["7-8", "Cm7", "i", "C Minor Pentatonic: C Eb F G Bb"],
    ],
    col_widths=[0.5*inch, 0.9*inch, 0.4*inch, 3*inch],
))
story.append(P("B Section (Bridge):", 'SS'))
story.append(make_table(
    ["Bars", "Chord", "Function", "Scale Choice"],
    [
        ["1-2", "Ebmaj7", "III", "Eb Major: Eb F G Ab Bb C D"],
        ["3-4", "Abmaj7", "VI", "Ab Lydian: Ab Bb C D Eb F G"],
        ["5-6", "Dm7(b5)", "ii", "D Locrian #2"],
        ["7-8", "G7(b9)", "V", "G Spanish/Jewish or G Altered"],
    ],
    col_widths=[0.5*inch, 0.9*inch, 0.4*inch, 3*inch],
))
story.append(P("<b>Practice tip:</b> The A section is a textbook minor jazz progression: i-iv-ii-V-i. The bridge lifts to the relative major (Eb). Practice switching between C Dorian (A section) and Eb Major (bridge) smoothly.", 'ScaleRec'))

# ════════════════════════════════════════════
# TUNE 6: OBSESION
# ════════════════════════════════════════════
story.append(P("6. Obsesion", 'TuneTitle'))
story.append(P("Pedro Flores  |  Key: A minor  |  Form: AB (32 bars)  |  Time: 4/4 Bolero  |  Difficulty: Intermediate", 'TuneInfo'))

story.append(make_table(
    ["Bars", "Chord", "Function", "Scale Choice"],
    [
        ["A: 1-2", "Am", "i", "A Harmonic Minor: A B C D E F G#"],
        ["3-4", "F", "VI", "F Major: F G A Bb C D E"],
        ["5-6", "E7", "V", "E Spanish/Jewish: E F G# A B C D"],
        ["7-8", "Am", "i", "A Dorian: A B C D E F# G"],
        ["9-10", "Am", "i", "A Minor Pentatonic: A C D E G"],
        ["11-12", "G7", "VII", "G Mixolydian: G A B C D E F"],
        ["13-14", "C", "III", "C Major: C D E F G A B"],
        ["15-16", "Dm / Am", "iv / i", "D Dorian / A Harmonic Minor"],
    ],
    col_widths=[0.5*inch, 0.8*inch, 0.5*inch, 2.8*inch],
))
story.append(sp(2))
story.append(make_table(
    ["Bars", "Chord", "Function", "Scale Choice"],
    [
        ["B: 1-4", "Am / F", "i / VI", "A Harm Minor / F Major"],
        ["5-6", "E7", "V", "E Spanish/Jewish"],
        ["7-8", "Am", "i", "A Harmonic Minor"],
        ["9-10", "A7", "V/iv", "A Mixolydian: A B C# D E F# G"],
        ["11-12", "G7", "VII", "G Mixolydian"],
        ["13-14", "C", "III", "C Major"],
        ["15-16", "E7 / Am", "V / i", "E Spanish / A Harmonic Minor"],
    ],
    col_widths=[0.5*inch, 0.8*inch, 0.5*inch, 2.8*inch],
))
story.append(P("<b>Practice tip:</b> The bVI-V-i movement (F-E7-Am) is a classic tango/bolero cadence. Emphasize the G# in E Spanish/Jewish — it's the leading tone that pulls everything home to Am.", 'ScaleRec'))

# ════════════════════════════════════════════
# TUNE 7: CARAVAN
# ════════════════════════════════════════════
story.append(P("7. Caravan", 'TuneTitle'))
story.append(P("Juan Tizol / Duke Ellington  |  Key: Fm / Ab major  |  Form: AABA (32 bars)  |  Time: 4/4 Latin/Swing  |  Difficulty: Intermediate", 'TuneInfo'))

story.append(P("A Section (8 bars) — The exotic vamp:", 'SS'))
story.append(make_table(
    ["Bars", "Chord", "Scale Choice", "Notes"],
    [
        ["1-6", "C7(b9)", "C Spanish/Jewish: C Db E F G Ab Bb", "THIS is the Caravan sound — Spanish scale for 6 bars"],
        ["7-8", "Fm6", "F Harmonic Minor: F G Ab Bb C Db E", "Resolution — the E natural pulls to F"],
    ],
    col_widths=[0.5*inch, 0.7*inch, 2.5*inch, 2.1*inch],
))
story.append(P("B Section / Bridge (8 bars) — Swing feel, cycle of dominants:", 'SS'))
story.append(make_table(
    ["Bars", "Chord", "Function", "Scale Choice"],
    [
        ["1-2", "F7", "V/ii", "F Mixolydian: F G A Bb C D Eb"],
        ["3-4", "Bb7", "V/V", "Bb Mixolydian: Bb C D Eb F G Ab"],
        ["5-6", "Eb7", "V", "Eb Mixolydian: Eb F G Ab Bb C Db"],
        ["7-8", "Ab6", "I", "Ab Major: Ab Bb C Db Eb F G"],
    ],
    col_widths=[0.5*inch, 0.7*inch, 0.5*inch, 3.1*inch],
))
story.append(P("<b>Why this tune:</b> THE Spanish/Jewish scale showcase. You sit on C7(b9) for 6 bars — pure Phrygian Dominant territory. The bridge shifts to Ab major with a cycle of dominants (Mixolydian practice). Two completely different sounds in one tune.", 'B'))
story.append(P("<b>Practice tip:</b> On the A section, learn to milk the C Spanish scale: C Db E F G Ab Bb. The Db-E augmented 2nd IS the Caravan sound. On the bridge, switch to Mixolydian mode thinking. Try Bebop Dominant for flowing lines over the cycle.", 'ScaleRec'))

# ════════════════════════════════════════════
# TUNE 8: LIBERTANGO
# ════════════════════════════════════════════
story.append(P("8. Libertango", 'TuneTitle'))
story.append(P("Astor Piazzolla  |  Key: A minor  |  Form: AB (repeating)  |  Time: 4/4 Tango (136 BPM)  |  Difficulty: Intermediate", 'TuneInfo'))

story.append(P("A Section (8 bars) — The iconic tango riff:", 'SS'))
story.append(make_table(
    ["Bars", "Chord", "Function", "Scale Choice"],
    [
        ["1-2", "Am", "i", "A Harmonic Minor: A B C D E F G#"],
        ["3-4", "E7", "V", "E Spanish/Jewish: E F G# A B C D"],
        ["5-6", "Dm", "iv", "D Dorian: D E F G A B C"],
        ["7-8", "Am", "i", "A Minor Pentatonic: A C D E G"],
    ],
    col_widths=[0.5*inch, 0.7*inch, 0.4*inch, 3.2*inch],
))
story.append(P("B Section (8 bars) — Opens up to relative major area:", 'SS'))
story.append(make_table(
    ["Bars", "Chord", "Function", "Scale Choice"],
    [
        ["1-2", "Dm", "iv", "D Dorian or D Melodic Minor"],
        ["3-4", "G7", "VII", "G Mixolydian: G A B C D E F"],
        ["5-6", "C (Cmaj7)", "III", "C Major: C D E F G A B"],
        ["7-8", "E7", "V", "E Spanish/Jewish or E Altered"],
    ],
    col_widths=[0.5*inch, 0.9*inch, 0.4*inch, 3*inch],
))
story.append(P("The A section bass line descends chromatically: A - G# - G - F# - F - E. This implies passing diminished chords. Over the chromatic descent, use A Harmonic Minor throughout.", 'SN'))
story.append(P("<b>Practice tip:</b> Use 3-3-2 rhythmic grouping. The B section Dm-G7-C is a ii-V-I in C major — contrast the tango A with a jazzier B section. On the final E7, try E Altered for maximum tension before returning to Am.", 'ScaleRec'))

# ════════════════════════════════════════════
# TUNE 9: OBLIVION
# ════════════════════════════════════════════
story.append(P("9. Oblivion", 'TuneTitle'))
story.append(P("Astor Piazzolla  |  Key: C minor  |  Form: ABA  |  Time: 4/4 Slow milonga  |  Difficulty: Intermediate-Advanced", 'TuneInfo'))

story.append(P("A Section (16 bars) — Descending minor cycle:", 'SS'))
story.append(make_table(
    ["Bars", "Chord", "Function", "Scale Choice"],
    [
        ["1-2", "Cm", "i", "C Melodic Minor: C D Eb F G A B"],
        ["3-4", "Fm7", "iv", "F Dorian: F G Ab Bb C D Eb"],
        ["5-6", "Bb7", "VII", "Bb Mixolydian: Bb C D Eb F G Ab"],
        ["7-8", "Ebmaj7", "III", "Eb Major: Eb F G Ab Bb C D"],
        ["9-10", "Abmaj7", "VI", "Ab Lydian: Ab Bb C D Eb F G"],
        ["11-12", "Dm7(b5)", "ii", "D Locrian #2: D E F G Ab Bb C"],
        ["13-14", "G7", "V", "G Spanish/Jewish: G Ab B C D Eb F"],
        ["15-16", "Cm", "i", "C Harmonic Minor: C D Eb F G Ab B"],
    ],
    col_widths=[0.5*inch, 0.85*inch, 0.4*inch, 3*inch],
))
story.append(P("B Section (16 bars):", 'SS'))
story.append(make_table(
    ["Bars", "Chord", "Function", "Scale Choice"],
    [
        ["1-2", "Cm", "i", "C Dorian: C D Eb F G A Bb"],
        ["3-4", "Fm", "iv", "F Dorian or F Harmonic Minor"],
        ["5-6", "G7(sus4) / G7", "V", "G Mixolydian then G Spanish"],
        ["7-8", "Cm", "i", "C Melodic Minor"],
        ["9-10", "Abmaj7", "VI", "Ab Major or Ab Lydian"],
        ["11-12", "Bb7", "VII", "Bb Bebop Dominant"],
        ["13-14", "Ebmaj7", "III", "Eb Major"],
        ["15-16", "G7", "V", "G Altered: G Ab Bb B Db Eb F"],
    ],
    col_widths=[0.5*inch, 1*inch, 0.4*inch, 2.8*inch],
))
story.append(P("<b>Why this tune:</b> A masterpiece of tango harmony. The A section is a full cycle through the key of C minor (i-iv-VII-III-VI-ii-V-i) — you touch almost every diatonic chord. This is the ultimate minor key navigation exercise.", 'B'))
story.append(P("<b>Practice tip:</b> Play slowly (this is a milonga, not a fast tango). Use Melodic Minor on the tonic for a smooth, modern sound. Switch to Harmonic Minor at the end of the A section for dramatic resolution. The Dm7(b5)-G7 is your Phase 2 ii-V in minor.", 'ScaleRec'))

# ════════════════════════════════════════════
# TUNE 10: DESAFINADO
# ════════════════════════════════════════════
story.append(P("10. Desafinado", 'TuneTitle'))
story.append(P("Antonio Carlos Jobim  |  Key: F major  |  Form: AABC (68 bars)  |  Time: 4/4 Bossa nova  |  Difficulty: Advanced", 'TuneInfo'))

story.append(P("A Section (16 bars) — Chromatic ii-V motion:", 'SS'))
story.append(make_table(
    ["Bars", "Chord", "Function", "Scale Choice"],
    [
        ["1-2", "Fmaj7", "I", "F Major: F G A Bb C D E"],
        ["3-4", "G7(b5)", "subV/vi", "G Lydian Dominant: G A B C# D E F"],
        ["5-6", "Gm7 / C7", "ii-V", "G Dorian / C Bebop Dominant"],
        ["7-8", "Am7(b5) / D7(b9)", "iii-VI(alt)", "A Locrian #2 / D Spanish/Jewish"],
        ["9-10", "Gm7 / A7(b13)", "ii / V/ii", "G Dorian / A Altered"],
        ["11-12", "Bbmaj7 / Bbm6", "IV / iv", "Bb Major / Bb Dorian"],
        ["13-14", "Fmaj7", "I", "F Major or F Lydian"],
        ["15-16", "G7(b5) / Gb7", "subV / bII7", "G Lyd Dom / Gb Lydian Dominant"],
    ],
    col_widths=[0.5*inch, 1.2*inch, 0.6*inch, 2.5*inch],
))
story.append(P("B Section — Modulation to A major then Ab major:", 'SS'))
story.append(make_table(
    ["Bars", "Chord", "Function", "Scale Choice"],
    [
        ["17-18", "Fmaj7", "I (home)", "F Major"],
        ["19-20", "E7(#9)", "V/iii (to A)", "E Altered: E F G G# Bb C D"],
        ["21-22", "Amaj7", "new I", "A Major: A B C# D E F# G#"],
        ["23-24", "Bb7(#11)", "subV (to A)", "Bb Lydian Dominant: Bb C D E F G Ab"],
        ["25-26", "Amaj7", "I (A major)", "A Major"],
        ["27-28", "Bbm7 / Eb7", "ii-V (to Ab)", "Bb Dorian / Eb Bebop Dominant"],
        ["29-30", "Abmaj7", "new I", "Ab Major: Ab Bb C Db Eb F G"],
        ["31-32", "Db7", "subV (to C)", "Db Lydian Dominant"],
        ["33-36", "Cmaj7 / C#dim7 / Dm7 / G7", "V area", "C Major / Dim / G Dorian / G Bebop Dom"],
    ],
    col_widths=[0.5*inch, 1.3*inch, 0.7*inch, 2.3*inch],
))
story.append(P("C Section returns to F major with the same A-section material, resolving through Am7(b5)-D7(b9)-Gm7 cadences.", 'SN'))
story.append(P("<b>Why this tune:</b> The harmonic Everest of bossa nova. It modulates through F, A, and Ab major using tritone substitutions (Lydian Dominant territory) and altered dominants. This tune uses nearly EVERY scale in your syllabus.", 'B'))
story.append(P("<b>Practice tip:</b> Break it into 8-bar chunks. Master each modulation separately. The Lydian Dominant scale is crucial here — use it on every b5 or #11 dominant. The E7(#9) to Amaj7 is a classic altered dominant resolution. This is a Phase 4 tune — don't rush to it.", 'ScaleRec'))

# ── Summary Page ──
story.append(PageBreak())
story.append(P("Tune Difficulty Progression", 'SH'))
story.append(P("Suggested order for learning these tunes:", 'SN'))
story.append(make_table(
    ["Order", "Tune", "Key Concept Practiced", "Phase"],
    [
        ["1", "Oye Como Va", "Dorian vamp, pentatonic, rhythm focus", "Phase 1"],
        ["2", "Senor Blues", "Minor blues, Dorian + pentatonic, 6/8 feel", "Phase 1"],
        ["3", "Stolen Moments", "Minor blues + chromatic Dorian shifts", "Phase 1-2"],
        ["4", "Libertango", "Harmonic minor, tango rhythm, Spanish/Jewish", "Phase 2"],
        ["5", "Caravan", "Spanish/Jewish vamp, cycle of dominants", "Phase 2"],
        ["6", "Besame Mucho", "Minor ii-V-i, Spanish/Jewish everywhere", "Phase 2"],
        ["7", "Tin Tin Deo", "Full minor jazz form, Afro-Cuban", "Phase 2-3"],
        ["8", "Obsesion", "Bolero, bVI-V-i cadences", "Phase 2-3"],
        ["9", "Oblivion", "Full minor cycle, Melodic Minor, tango phrasing", "Phase 3"],
        ["10", "Desafinado", "Modulations, Lydian Dominant, Altered, all scales", "Phase 4"],
    ],
    col_widths=[0.4*inch, 1.2*inch, 2.8*inch, 0.8*inch],
))

doc.build(story)
print(f"PDF created: {output_path}")
