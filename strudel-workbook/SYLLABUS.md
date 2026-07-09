# Strudel Syllabus — Music Theory Lab for Saxophone

**Goal:** learn [Strudel](https://strudel.cc) as a *theory instrument* — a way to hear, build, and
internalize the scales, chords, and rhythms from the Scale & Chord Reference and the Latin Jazz &
Tango Syllabus. Every module ends with something you can play alto or tenor sax over.

**Why Strudel for theory:** in Strudel a scale is `n("0 2 4 6").scale("C:dorian")` — you literally
type scale degrees and hear them. Chord symbols become sound via `chord("Dm7 G7").voicing()`. The
theory *is* the code, so writing patterns forces you to think in degrees, intervals, and chord-scale
relationships rather than finger patterns.

**Format:** 6 modules, each split into short sessions (~20–30 min at the laptop, plus sax time).
Fully self-paced — sessions are numbered, not scheduled. Each session in the workbook will have:
a concept, runnable code you type yourself (not paste), 2–3 modification challenges, and a
"now pick up the horn" exercise. All sounds are Strudel built-ins — everything runs in the browser
with zero setup.

**Transposition note:** Strudel plays **concert pitch**. Your reference book is in *written* keys.
Every play-along states both: e.g. "track in concert D minor → alto plays B minor, tenor plays
E minor." This is deliberate — constant gentle transposition practice.

---

## Module 1 — First Loops: Rhythm Before Notes

*Strudel fundamentals through latin rhythm — no pitches yet, so all attention goes to time.
Compressed: you already code, so this moves fast and treats mini-notation as a small DSL to absorb,
not a programming lesson.*

| Session | Strudel concepts | Theory anchor |
|---|---|---|
| 1.1 The REPL & mini-notation | `sound()`, `setcpm()`, sequences, `~` rests, `[]` grouping, `*` speed | pulse, tempo, subdivision: quarters → eighths → sixteenths |
| 1.2 Tresillo & clave | `<>` alternation, `,` layering, `.bank()` drum sounds | tresillo (3+3+2); son clave 3-2 vs 2-3, layered together |
| 1.3 Habanera & marcato | `.gain()` accents, euclidean `(3,8)` | habanera (tango base), marcato vs sincopa feels |

**Sax integration:** clap/play single-note rhythms (one comfortable note) against your own clave loop.

**Milestone:** a four-layer percussion groove — clave + tresillo + pulse + accent layer — coded from scratch.

---

## Module 2 — Scale Lab: Degrees You Can Hear

*The `n()`/`scale()` workflow. Scales from Category 1 & 3 of your reference, thought of as degree patterns, not note names.*

| Session | Strudel concepts | Theory anchor |
|---|---|---|
| 2.1 Numbers into notes | `n()`, `note()`, `.scale()`, octaves | major scale as degrees 0–7; W-W-H-W-W-W-H |
| 2.2 Scale degrees as melody | degree patterns, negative numbers (below root) | pentatonics: why 5 notes never clash |
| 2.3 The minor family | swapping scale names on one pattern | dorian vs aeolian vs harmonic minor — *same code, different scale* — hear exactly which degrees differ |
| 2.4 The tango scale | `.scale("<...>")` alternation | harmonic minor and its augmented 2nd; melodic minor ascending |
| 2.5 Modes as rotations | same degrees, shifted root | dorian = major from degree 2; phrygian's b9 color |
| 2.6 Scale patterns (technique lab) | `.add()`, `.off()`, `.rev()` | thirds, enclosures, 1235 cells — the patterns you drill on sax, generated |

**Sax integration:** Strudel drones the root + plays the degree pattern; you echo it on sax in the
written key (reference book page cited per exercise).

**Milestone:** one pattern (e.g. `n("0 2 4 3")`) run through 6 scales in 3 keys — describe what each
scale color does to it.

---

## Module 3 — Chord Lab: The Five Chord Types

*Category-by-category from the chord reference: Δ, 7, –7, ø, °7 — built, arpeggiated, voiced.*

| Session | Strudel concepts | Theory anchor |
|---|---|---|
| 3.1 Building chords from degrees | stacking with `,` inside `[]`, `.struct()` | chord = degrees 0-2-4-6 of a scale; hear Δ7 emerge from major |
| 3.2 Chord symbols | `chord()`, `.voicing()`, `.anchor()` | the five types in all inversions; smooth voice leading (why voicings ≠ root position) |
| 3.3 Arpeggios vs scales | `.arp()`, arpeggio patterns | chord tones vs passing tones; targeting 3rds and 7ths |
| 3.4 Roots and bass | `rootNotes()`, layering bass + voicing | hearing root motion as its own melody |
| 3.5 Chord-scale pairs | chord layer + scale-degree melody layer together | the mapping table from LEARNINGS.md: Δ→lydian, 7→mixolydian/lydian dominant, –7→dorian, ø→locrian #2 |

**Sax integration:** arpeggio drills over your own chord loops; "guide tone" exercise — play only
3rds and 7ths while the loop cycles.

**Milestone:** a two-chord vamp (Dm7 → G7) with bass, voicings, and clave, plus a degree-map of
which melody notes are chord tones.

---

## Module 4 — Progressions: ii-V-i and the Tango Cadences

*The harmonic core of the latin syllabus, now as loops you build and hear.*

| Session | Strudel concepts | Theory anchor |
|---|---|---|
| 4.1 The minor ii-V-i | chord sequences `<>`, slow harmonic rhythm | iiø → V7b9 → i– in D minor; which scale over which chord (dorian/locrian#2 → spanish → harmonic minor) |
| 4.2 Five priority keys | pattern reuse, transposition by code | ii-V-i in Dm, Gm, Cm, Fm, Am (the latin priority keys) |
| 4.3 The Phrygian cadence | writing bII → V7b9 → i | the signature tango resolution; bII as lydian |
| 4.4 bVI → V → i and minor vamps | longer forms, `.slow()`, section switching | second tango cadence; i–iv montuno vamps |
| 4.5 Dominant colors | one V7 chord, four scales | mixolydian → spanish → altered → whole tone over the same V7 — tension ladder from LEARNINGS.md |
| 4.6 The pentatonic trick | superimposition patterns | Ab minor pentatonic over G7 = instant altered sound; hear *why* it works, degree by degree |

**Sax integration:** every session's loop is a practice track. Written-key cheat line included for
alto and tenor per exercise.

**Milestone:** a 16-bar tango progression (Phrygian cadence form) that you can solo over comfortably
in two keys.

---

## Module 5 — Groove Engineering: Full Latin Rhythm Section

*Make loops that feel good enough to actually practice with — this is where Strudel replaces canned backing tracks.*

| Session | Strudel concepts | Theory anchor |
|---|---|---|
| 5.1 Montuno patterns | offset melodic ostinati, `.off()`, `.late()` | the piano montuno: syncopated arpeggiation locked to clave |
| 5.2 Bass tumbao | dotted rhythms against the voicing layer | tumbao anticipates the downbeat — hear beat-3 anticipation |
| 5.3 Tango accompaniment | marcato vs sincopa sections, `.arrange()` | 3-3-2 grouping; heavy quarter marcato under harmonic minor melody |
| 5.4 Dynamics & space | `.velocity()`/`.gain()` shaping, filters, `.room()` | phrasing: where latin players breathe; call-and-response space |
| 5.5 Song forms | `.arrange()` sections: intro/vamp/head/solo | AABA and verse-vamp forms; structuring a practice track |

**Sax integration:** long-form practice — 5+ minute structured tracks with a solo section that
opens up (fewer layers) and a head section (full groove).

**Milestone:** two reusable backing-track templates: one salsa-ish minor vamp, one tango.

---

## Module 6 — Capstone: The Personal Practice System

*Turn everything into a small library of practice tools you'll keep using.*

| Session | Deliverable |
|---|---|
| 6.1 Scale-drill machine | a parameterized loop: pick scale + key + tempo at the top of the file, get a drone + degree patterns — your reference book, audible |
| 6.2 ii-V-i trainer | cycles ii-V-i through the five priority keys automatically, 8 bars each |
| 6.3 Tune backing track | build a full backing track for a Piazzolla tune (working target: **Libertango** — iconic 3-3-2 groove, harmonic minor territory) |
| 6.4 (stretch) Live tweaking | change the loop *while playing* — the live-coding skill: swap scales/densities mid-practice |

**Final milestone:** a `tracks/` folder of Strudel files you actually reach for when the horn comes out.

---

## Workbook plan (once syllabus is agreed)

- One markdown file per module: concept → typed code → challenges → sax exercise, with a
  strudel.cc share-link per snippet so each is one click from playing.
- Every exercise cross-references the Scale & Chord Reference (scale + written key for alto/tenor)
  and, where relevant, the Latin Jazz & Tango Syllabus phase it supports.
- Solutions in a collapsible section, because typing-then-checking beats reading.

## Agreed decisions (2026-07-09)

- Module 1 compressed to 3 sessions — Nic codes, fundamentals move fast.
- No schedule attached — sessions numbered, fully self-paced.
- Built-in Strudel sounds only; no MIDI-out.
- Capstone tune: Piazzolla — working target Libertango.
