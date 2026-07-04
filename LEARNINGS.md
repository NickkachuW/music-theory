# Learnings from Scale & Chord Reference PDF Project

## Music Theory — Fundamentals

### Transposing Instruments
- **Alto Saxophone** (Eb): written C sounds concert Eb. To write concert C, write A (up a major 6th).
- **Tenor Saxophone** (Bb): written C sounds concert Bb. To write concert C, write D (up a major 2nd).
- Practice references should present scales in **written keys** (what the musician reads), not concert pitch.

### Scale Categories (FQBK Handbook)
Five categories with multiple scale choices each:

| Category | Scale Choices |
|----------|--------------|
| **Major** | Major, Major Pentatonic, Lydian, Bebop (Major), Harmonic Major, Lydian Augmented, Augmented, 6th Mode of Harmonic Minor, Diminished (begin H), Blues |
| **Dominant 7th** | Mixolydian, Major Pentatonic, Bebop (Dominant), Spanish/Jewish, Lydian Dominant, Hindu, Whole Tone, Diminished (begin H), Diminished Whole Tone, Blues |
| **Dom 7sus4** | Mixolydian (avoid 3rd), Major Pentatonic built on b7, Bebop |
| **Minor** | Dorian, Minor Pentatonic, Bebop (Minor), Melodic Minor, Bebop Minor No. 2, Blues, Harmonic Minor, Diminished (begin W), Phrygian, Natural Minor (Aeolian) |
| **Half Diminished** | Locrian, Locrian #2, Bebop |
| **Diminished** | Diminished (8-tone) |

### Step Notation
- W = whole step (2 semitones), H = half step (1 semitone), m3 = minor third (3 semitones)

### Melodic Minor Uniqueness
- Ascends with raised 6th and 7th, descends using natural minor. No other common scale has different ascending/descending forms.

### Enharmonic Spelling
- Wrong enharmonic root cascades into double sharps/flats. **Gb is preferable to F#** for sax transpositions (produces cleaner key signatures).
- Concert key labels need normalization: "Fb" should display as "E", "Cb" as "B".

### Chord Types
- Five basic types: Major 7th, Dominant 7th, Minor 7th, Half Diminished, Diminished 7th — each transposable to all 12 keys.

---

## Music Theory — Latin Jazz & Tango Improvisation

### Latin Jazz Scale-Chord Mapping
The core principle: each chord type gets specific scale colors, from consonant to maximum tension.

| Chord Type | Conservative | Medium | Maximum Tension |
|-----------|-------------|--------|----------------|
| Major 7 | Major | Lydian | Lydian Augmented |
| Dominant 7 | Mixolydian | Bebop Dominant | Lydian Dominant |
| Dominant 7b9 | Spanish/Jewish | Diminished (H-W) | Altered (Dim Whole Tone) |
| Dominant 7#5 | Whole Tone | Altered | |
| Minor 7 | Dorian | Minor Pentatonic | Blues |
| Minor-Major 7 | Melodic Minor | Harmonic Minor | |
| Half-dim | Locrian #2 | Locrian | |

### The ii-V-i Progression (Core of Latin Jazz)
- **ii chord:** Dorian scale
- **V chord:** Spanish/Jewish (Phrygian Dominant) for traditional latin; Altered for modern tension
- **i chord:** Harmonic Minor (dramatic) or Melodic Minor (smooth)
- Practice as a unit: 4 beats Dorian, 4 beats Spanish, 8 beats Harmonic Minor

### Key Scales for Latin Jazz
- **Dorian** — the workhorse for minor vamps and montuno grooves
- **Spanish/Jewish (Phrygian Dominant)** — THE latin dominant sound; 5th mode of Harmonic Minor; the b9 interval defines salsa, mambo, and tango
- **Bebop Dominant** — added natural 7th puts chord tones on downbeats in continuous eighth notes
- **Minor Pentatonic** — simple but powerful for rhythmic improvisation
- **Blues Scale** — adds character over any context

### Key Scales for Tango
- **Harmonic Minor** — primary tonic scale (dramatic, passionate)
- **Spanish/Jewish** — over V7b9 (yearning, bittersweet)
- **Melodic Minor** — modern tango tonic (sophisticated)
- **Phrygian** — dark modal sections (brooding)
- The **augmented 2nd interval** (e.g., F to G# in A harmonic minor) is the defining tango sound

### Tango Cadence Patterns
- **Phrygian Cadence:** bII (Lydian) → V7b9 (Spanish/Jewish) → i (Harmonic Minor) — the signature tango resolution
- **bVI → V7b9 → i** — another classic tango cadence

### Rhythmic Concepts
- **Clave** (son clave 3-2 and 2-3) is the rhythmic foundation of all latin jazz; phrasing should relate to clave
- **Tresillo** (3+3+2) is the fundamental Afro-Cuban rhythmic cell
- **Habanera** (dotted quarter + eighth) is the tango rhythmic base
- **3-3-2 grouping** is tango's rhythmic DNA
- **Marcato** (heavy quarter notes) vs **Sincopa** (syncopated, pushing ahead) are tango's two main rhythmic feels

### Pentatonic Substitution Trick
- Playing Ab minor pentatonic over G7 yields: b9, 3, b5, b13, b7 — an instant altered dominant sound without learning the altered scale

### Latin Jazz Priority Keys
- Most common minor key centers: D minor, G minor, C minor, F minor, A minor
- Practice ii-V-i in these keys first, then expand to all 12

### Recommended Listening
- **Latin Jazz sax models:** Paquito D'Rivera (alto), David Sanchez (tenor)
- **Tango sax models:** Gato Barbieri (tenor), Javier Girotto (modern tango)
- **Essential tango composer:** Astor Piazzolla — bandoneon lines translate well to saxophone

---

## Technical — PDF Generation

### reportlab
- Standard fonts (Helvetica, Times, Courier) use WinAnsiEncoding and **cannot render music symbols**.
- **Segoe UI Symbol** (`seguisym.ttf`) on Windows contains treble clef (U+1D11E), sharp (U+266F), flat (U+266D), natural (U+266E).
- Treble clef baseline doesn't match musical position — requires empirical y-offset to wrap around the G line.

### Music Notation Drawing (in reportlab)
- Staff: 5 horizontal lines with equal spacing.
- Note position determined by letter name + octave (diatonic), not chromatic pitch. Accidentals don't change vertical position.
- Ledger lines needed above F5 or below C4 in treble clef.
- Stemless filled noteheads work well for scale references (no rhythm needed).

### LilyPond (Music Engraving)
- **LilyPond** (`lilypond.exe`) generates publication-quality sheet music PDFs from text input files (`.ly`).
- Install via `winget install --id LilyPond.LilyPond`.
- On this system, installed to: `C:\Users\nicwo\AppData\Local\Microsoft\WinGet\Packages\LilyPond.LilyPond_Microsoft.Winget.Source_8wekyb3d8bbwe\lilypond-2.24.4\bin\lilypond.exe`
- Syntax: `\relative c' { c d e f g a b c }` for a C major scale.
- Chord symbols above notes: `c8^\markup{\small "Cm7"}`.
- Articulations: `-^` for marcato, `->` for accent, `-.` for staccato.
- Beaming groups: `a8[ b c]` forces beaming.
- Key signatures: `\key f \major`, `\key a \minor`.

### music21 (Python)
- Python library for music theory and notation: `pip install music21`.
- Can generate MusicXML files (`.musicxml`) openable in MuseScore, Finale, Sibelius, Flat.io.
- Useful for programmatic transposition and music analysis, but needs an external renderer (LilyPond or MuseScore) for PDF output.

### Two-Pass PDF Generation
- For a table of contents with correct page numbers: first pass collects page counts, second pass generates final PDF with TOC offset.

### Merging PDFs (pypdf)
- Use `pypdf` to combine multiple PDFs: `PdfWriter` + `add_page()` from multiple `PdfReader` objects.
- Useful for combining reportlab-generated content with LilyPond sheet music into a single document.
