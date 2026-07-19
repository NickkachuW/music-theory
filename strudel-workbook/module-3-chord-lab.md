# Module 3 — Chord Lab: The Five Chord Types

Module 1: time. Module 2: melody. This module adds the third layer — **harmony** — and with it the
last section of your Scale & Chord Reference: the five chord types (Δ, 7, –7, ø, °7) with their
tones in all 12 keys. By the end you'll build chords three different ways (from degrees, from
symbols, from arps), lay bass under them, and know which scale to reach for over each chord —
which is the doorway to Module 4's progressions.

**Reference book tie-in:** the *Chord Reference* tables at the back of the
[Scale & Chord Reference](../Scale_and_Chord_Reference_Saxophones.pdf) — plus the chord symbols
printed above every scale in Categories 1–5.

> **Piano roll advice for this module:** keep `._pianoroll()` on the harmony line. Chords appear
> as note *columns*; good voice leading appears as those columns connecting into nearly-horizontal
> lines. You'll literally watch harmony turn from blocks into voices.

---

## Session 3.1 — Chords from degrees

### 3.1.1 A chord is a scale, skipping

Stack degrees with commas (Module 2's `n("0,2")` trick, now with more floors). Every-other-degree
of any scale = that scale's chord:

```js
setcpm(80/4)
$: n("<[0,2,4] [0,2,4,6]>").scale("C4:major").sound("piano")
$: note("c2").sound("sawtooth").lpf(400).gain(.3)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDgwLzQpCiQ6IG4oIjxbMCwyLDRdIFswLDIsNCw2XT4iKS5zY2FsZSgiQzQ6bWFqb3IiKS5zb3VuZCgicGlhbm8iKQokOiBub3RlKCJjMiIpLnNvdW5kKCJzYXd0b290aCIpLmxwZig0MDApLmdhaW4oLjMp)

Bar 1: `0,2,4` — root, third, fifth: a **triad**. Bar 2: add `6` — the seventh: a **major 7th
chord**, the book's `CΔ`. That's the recipe for every chord in the book: take a scale, keep the
even-numbered degrees, play them together. Harmony isn't separate from scales — it's scales,
compressed.

### 3.1.2 The diatonic chord walk

Now slide the whole stack up the scale, one degree per bar — the same climbing trick as Module 2's
cell, applied to a chord:

```js
setcpm(80/4)
$: n("<[0,2,4,6] [1,3,5,7] [2,4,6,8] [3,5,7,9] [4,6,8,10] [5,7,9,11] [6,8,10,12] [7,9,11,13]>")
   .scale("C4:major").sound("piano")._pianoroll()
$: note("c2").sound("sawtooth").lpf(400).gain(.25)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDgwLzQpCiQ6IG4oIjxbMCwyLDQsNl0gWzEsMyw1LDddIFsyLDQsNiw4XSBbMyw1LDcsOV0gWzQsNiw4LDEwXSBbNSw3LDksMTFdIFs2LDgsMTAsMTJdIFs3LDksMTEsMTNdPiIpCiAgIC5zY2FsZSgiQzQ6bWFqb3IiKS5zb3VuZCgicGlhbm8iKS5fcGlhbm9yb2xsKCkKJDogbm90ZSgiYzIiKS5zb3VuZCgic2F3dG9vdGgiKS5scGYoNDAwKS5nYWluKC4yNSk%3D)

Eight bars, eight chords, *one scale* — and listen to the qualities change even though the recipe
never does: **Δ7, m7, m7, Δ7, 7, m7, ø, Δ7**. The scale's half-step positions (Module 2's
fingerprint) decide each chord's flavor. Two residents of this walk matter enormously: bar 2
(built on degree 1) is the **ii chord — always m7**, and bar 5 (degree 4) is the **V chord —
always a dominant 7**. The ii-V, the engine of jazz and latin harmony, lives natively inside every
major scale. Module 4 is entirely about it.

### 3.1.3 Chords in time — `.struct()`

`.struct()` stamps a rhythm onto anything. Chord meets tresillo:

```js
setcpm(90/4)
$: n("[0,2,4,6]").scale("D4:dorian").struct("x ~ ~ x ~ ~ x ~").sound("piano")
$: sound("bd*4, hh*8").gain(.4)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCiQ6IG4oIlswLDIsNCw2XSIpLnNjYWxlKCJENDpkb3JpYW4iKS5zdHJ1Y3QoInggfiB%2BIHggfiB%2BIHggfiIpLnNvdW5kKCJwaWFubyIpCiQ6IHNvdW5kKCJiZCo0LCBoaCo4IikuZ2FpbiguNCk%3D)

`x` = play, `~` = don't. The pitch material and the rhythm are now separate decisions — which is
exactly how a comping pianist thinks: *what* to press and *when* to press it.

### Challenges 3.1

1. Build all five book chord types with one stack and five scales:
   `[0,2,4,6]` over major → Δ7, dorian → –7, mixolydian → 7, locrian → ø… and for °7, the
   diminished scale. One `< >` list, five bars, the whole back of your book.
2. In the diatonic walk, find the two bars that sound *restless* (hint: one is the V7, one the ø).
   What do they share? (Both contain the scale's two half-step neighbors — that's the tension.)
3. Give the 3.1.3 comp a 2-3 clave rhythm instead of the tresillo.

<details><summary>Solution for 1</summary>

```js
setcpm(60/4)
$: n("[0,2,4,6]").scale("<C4:major C4:dorian C4:mixolydian C4:locrian C4:diminished>").sound("piano")._pianoroll()
$: note("c2").sound("sawtooth").lpf(400).gain(.3)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDYwLzQpCiQ6IG4oIlswLDIsNCw2XSIpLnNjYWxlKCI8QzQ6bWFqb3IgQzQ6ZG9yaWFuIEM0Om1peG9seWRpYW4gQzQ6bG9jcmlhbiBDNDpkaW1pbmlzaGVkPiIpLnNvdW5kKCJwaWFubyIpLl9waWFub3JvbGwoKQokOiBub3RlKCJjMiIpLnNvdW5kKCJzYXd0b290aCIpLmxwZig0MDApLmdhaW4oLjMp)

CΔ7 → C–7 → C7 → Cø → C°7: same root, five colors — this is the exact layout of the book's chord
reference, one row per bar. The piano roll shows chord quality as *shape*: watch the middle notes
sag flat one by one.

</details>

### 🎷 Horn time 3.1

Loop challenge 1's five-color bar cycle slowly. On the horn, arpeggiate each chord as it sounds —
**written C on tenor is this exact exercise in D; on alto it's in A** — reading the tones from the
book's Chord Reference table (tenor: D row, alto: A row). The exercise: between each neighboring
pair of chords, find *which single note changed* — every transition in the cycle moves exactly one
tone. Say the change out loud as you play it ("the 3rd went flat").

---

## Session 3.2 — Chord symbols & voicings

### 3.2.1 Speaking symbol

Strudel reads chord symbols directly — `chord()` names them, `.voicing()` turns them into
well-arranged notes:

```js
setcpm(80/4)
$: chord("<Dm7 G7 C^7 A7>").voicing().sound("piano")._pianoroll()
$: sound("bd ~ sd ~").bank("RolandTR808").gain(.5)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDgwLzQpCiQ6IGNob3JkKCI8RG03IEc3IENeNyBBNz4iKS52b2ljaW5nKCkuc291bmQoInBpYW5vIikuX3BpYW5vcm9sbCgpCiQ6IHNvdW5kKCJiZCB%2BIHNkIH4iKS5iYW5rKCJSb2xhbmRUUjgwOCIpLmdhaW4oLjUp)

Translation table for your book's symbols:

| Book | Strudel | Example |
|---|---|---|
| CΔ (major 7th) | `^7` | `C^7` |
| C7 (dominant) | `7` | `C7`, and alterations: `G7b9`, `C7#5` |
| C–7 (minor 7th) | `m7` or `-7` | `Dm7` / `D-7` |
| Cø (half-dim) | `m7b5` | `Bm7b5` |
| C°7 (dim 7th) | `o7` | `Co7` |
| C7sus4 | `7sus` | `C7sus` |

> **The silent-symbol gotcha.** A symbol Strudel doesn't recognize produces **silence, not an
> error** — `Cmaj7` and `Cdim7` both fail quietly (use `C^7` and `Co7`). Same failure mode as
> Module 2's bare `.add()`: if a chord line goes mute, check your spelling against this table
> first.

### 3.2.2 Why voicings — the proof

Play the ii-V-I both ways and watch the piano roll:

```js
setcpm(70/4)
$: n("<[1,3,5,7] [4,6,8,10] [0,2,4,6]>").scale("C4:major").sound("piano")._pianoroll()
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDcwLzQpCiQ6IG4oIjxbMSwzLDUsN10gWzQsNiw4LDEwXSBbMCwyLDQsNl0%2BIikuc2NhbGUoIkM0Om1ham9yIikuc291bmQoInBpYW5vIikuX3BpYW5vcm9sbCgp)

```js
setcpm(70/4)
$: chord("<Dm7 G7 C^7>").voicing().sound("piano")._pianoroll()
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDcwLzQpCiQ6IGNob3JkKCI8RG03IEc3IENeNz4iKS52b2ljaW5nKCkuc291bmQoInBpYW5vIikuX3BpYW5vcm9sbCgp)

Version 1 is **root position** — correct notes, but the blocks leap around like a beginner's left
hand. Version 2 is **voiced** — same harmonies, notes chosen so each voice moves as little as
possible. On the roll: blocks vs almost-flat lines. That "almost-flat" is called **voice
leading**, it's why progressions sound *smooth*, and your ear already prefers it. (Check the F at
the top of Dm7 — it simply *stays* for G7. Session 3.3 makes that the whole lesson.)

### 3.2.3 Register — `.anchor()`

`.anchor()` sets the ceiling the voicing builds down from:

```js
setcpm(70/4)
$: chord("<Dm7 G7 C^7>").anchor("c6").voicing().sound("piano")
$: "<Dm7 G7 C^7>".rootNotes(2).note().sound("sawtooth").lpf(500).gain(.4)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDcwLzQpCiQ6IGNob3JkKCI8RG03IEc3IENeNz4iKS5hbmNob3IoImM2Iikudm9pY2luZygpLnNvdW5kKCJwaWFubyIpCiQ6ICI8RG03IEc3IENeNz4iLnJvb3ROb3RlcygyKS5ub3RlKCkuc291bmQoInNhd3Rvb3RoIikubHBmKDUwMCkuZ2FpbiguNCk%3D)

Try `"a3"` instead: same progression, murky cellar. Comping lives around `c5`–`c6`; leave the
basement for the bass (that second line is a Session 3.4 preview).

### Challenges 3.2

1. Write the **minor** ii-V-i in concert D minor with symbols: `Em7b5 A7 Dm7` — the book's ø
   making its first real appearance. Listen to how much darker it is than Dm7-G7-C^7.
2. Sharpen it: swap `A7` → `A7b9` — the *Spanish* b9 from your latin syllabus. One character,
   instant tango.
3. Patterned anchors: what does `.anchor("<c6 c4>")` do to a two-chord loop? Describe the effect
   in band terms.

<details><summary>Solution for 1–2</summary>

```js
setcpm(70/4)
$: chord("<Em7b5 A7b9 Dm7 Dm7>").voicing().sound("piano")._pianoroll()
$: "<Em7b5 A7b9 Dm7 Dm7>".rootNotes(2).note().sound("sawtooth").lpf(500).gain(.4)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDcwLzQpCiQ6IGNob3JkKCI8RW03YjUgQTdiOSBEbTcgRG03PiIpLnZvaWNpbmcoKS5zb3VuZCgicGlhbm8iKS5fcGlhbm9yb2xsKCkKJDogIjxFbTdiNSBBN2I5IERtNyBEbTc%2BIi5yb290Tm90ZXMoMikubm90ZSgpLnNvdW5kKCJzYXd0b290aCIpLmxwZig1MDApLmdhaW4oLjQp)

This four-bar loop is the harmonic heart of half the tango repertoire — remember how it sounds.

</details>

### 🎷 Horn time 3.2

Loop the plain ii-V-I (`Dm7 G7 C^7`). That's **written Em7-A7-D^7 on tenor, Bm7-E7-A^7 on alto**.
Play *only the 3rd* of each chord, whole notes (tenor: G-C#-F#; alto: D-G#-C#). The 3rds alone
outline the harmony — you can hear the progression from three notes. Then only the roots. Then
alternate root-3rd per bar.

---

## Session 3.3 — Arpeggios & guide tones

### 3.3.1 `.arp()` — chords, one note at a time

`.arp()` unrolls a voicing by index (0 = lowest note):

```js
setcpm(90/4)
$: chord("<Dm7 G7>").voicing().arp("0 1 2 3 4 3 2 1").sound("piano")
$: sound("bd ~ ~ bd ~ ~ bd ~").bank("RolandTR808").gain(.5)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCiQ6IGNob3JkKCI8RG03IEc3PiIpLnZvaWNpbmcoKS5hcnAoIjAgMSAyIDMgNCAzIDIgMSIpLnNvdW5kKCJwaWFubyIpCiQ6IHNvdW5kKCJiZCB%2BIH4gYmQgfiB%2BIGJkIH4iKS5iYW5rKCJSb2xhbmRUUjgwOCIpLmdhaW4oLjUp)

Up-and-down arpeggios that re-voice themselves every chord change — the pattern indexes *whatever
notes the voicing chose*. Try `"0 2 1 3"` (broken) or `"0 [2,4] 1 [2,4]"` (bass-and-chop — a
montuno seed for Module 5).

### 3.3.2 Skeleton and filler

Chord tones are the skeleton; the other scale degrees are connective tissue. Hear the difference —
bar 1 is only chord tones, bar 2 the full scale:

```js
setcpm(80/4)
$: n("<[0 2 4 6] [0 1 2 3 4 5 6 7]>").scale("D4:dorian").sound("piano")
$: chord("Dm7").voicing().struct("x ~ ~ x ~ ~ x ~").sound("piano").gain(.5)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDgwLzQpCiQ6IG4oIjxbMCAyIDQgNl0gWzAgMSAyIDMgNCA1IDYgN10%2BIikuc2NhbGUoIkQ0OmRvcmlhbiIpLnNvdW5kKCJwaWFubyIpCiQ6IGNob3JkKCJEbTciKS52b2ljaW5nKCkuc3RydWN0KCJ4IH4gfiB4IH4gfiB4IH4iKS5zb3VuZCgicGlhbm8iKS5nYWluKC41KQ%3D%3D)

Notice bar 1 *is* Dm7 — dorian's degrees `0 2 4 6` are exactly the chord tones (D F A C), which is
3.1's recipe read backwards. Bar 1 can land anywhere, anytime. Bar 2's odd-numbered degrees are
passing tones: beautiful in motion, wobbly if you sit on them. Improv rule of thumb: **long notes
on the skeleton, short notes in between**.

### 3.3.3 Guide tones — the two-note secret

The root and 5th are generic (every chord has them). The **3rd and 7th** carry the quality — they
are the *guide tones*, and they voice-lead all by themselves:

```js
setcpm(60/4)
$: note("<[f4,c5] [f4,b4]>").sound("piano")._pianoroll()
$: "<Dm7 G7>".rootNotes(2).note().sound("sawtooth").lpf(500).gain(.4)
$: sound("bd ~ sd ~").bank("RolandTR808").gain(.4)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDYwLzQpCiQ6IG5vdGUoIjxbZjQsYzVdIFtmNCxiNF0%2BIikuc291bmQoInBpYW5vIikuX3BpYW5vcm9sbCgpCiQ6ICI8RG03IEc3PiIucm9vdE5vdGVzKDIpLm5vdGUoKS5zb3VuZCgic2F3dG9vdGgiKS5scGYoNTAwKS5nYWluKC40KQokOiBzb3VuZCgiYmQgfiBzZCB%2BIikuYmFuaygiUm9sYW5kVFI4MDgiKS5nYWluKC40KQ%3D%3D)

Dm7's guide tones: F (3rd) and C (7th). G7's: B (3rd) and F (7th). Watch the roll: **F stays put**
(common tone), **C slides a half step to B**. Two notes, minimal motion, and the entire Dm7→G7
story is told. This is the most valuable improv concept in this module: land the guide tones and
the changes play themselves.

### Challenges 3.3

1. Extend the guide-tone line through the full ii-V-I: add C^7's pair (3rd = E, 7th = B). Which
   note moves this time, which stays?
2. Arp the five chord types from 3.1's challenge (`chord("<C^7 Cm7 C7 Cm7b5 Co7>")`) with the same
   `"0 1 2 3 4 3 2 1"` pattern. The °7 bar sounds like a diminished-scale run — why? (Its chord
   tones *are* every other note of the diminished scale.)
3. Write an 8th-note line over `<Dm7 G7>` that touches a guide tone on beats 1 and 3, passing
   tones elsewhere. (Use `n(...)` in D dorian / G mixolydian thinking, or `note(...)` directly.)

<details><summary>Solution for 1</summary>

```js
setcpm(60/4)
$: note("<[f4,c5] [f4,b4] [e4,b4] [e4,b4]>").sound("piano")._pianoroll()
$: "<Dm7 G7 C^7 C^7>".rootNotes(2).note().sound("sawtooth").lpf(500).gain(.4)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDYwLzQpCiQ6IG5vdGUoIjxbZjQsYzVdIFtmNCxiNF0gW2U0LGI0XSBbZTQsYjRdPiIpLnNvdW5kKCJwaWFubyIpLl9waWFub3JvbGwoKQokOiAiPERtNyBHNyBDXjcgQ143PiIucm9vdE5vdGVzKDIpLm5vdGUoKS5zb3VuZCgic2F3dG9vdGgiKS5scGYoNTAwKS5nYWluKC40KQ%3D%3D)

G7→C^7: B stays, F slides down to E. Full chain: each change moves exactly one of the two notes,
one half step. That's why ii-V-I feels *inevitable*.

</details>

### 🎷 Horn time 3.3

The guide-tone drill, on the horn — this is *the* session to spend extra days on. Loop 3.3.3's
track. **Tenor (Em7→A7): play G–D, then C#–G. Alto (Bm7→E7): D–A, then G#–D.** Half notes at
first, then in the tresillo rhythm, then decorate each guide tone with a neighbor note. When it
feels easy, extend to the ii-V-I chain from the challenge.

---

## Session 3.4 — Roots and bass

### 3.4.1 `rootNotes()` — the floor

`rootNotes(octave)` extracts roots from chord symbols. Give the same symbol string to two layers
and bass + comp stay in sync by construction:

```js
setcpm(90/4)
$: chord("<Dm7 G7 C^7 A7>").voicing().struct("~ x ~ x ~ x ~ x").sound("piano").gain(.6)
$: "<Dm7 G7 C^7 A7>".rootNotes(2).note().struct("x ~ ~ x ~ ~ x ~").sound("sawtooth").lpf(500)
$: sound("<[rim ~ ~ rim ~ ~ rim ~] [~ ~ rim ~ rim ~ ~ ~]>").bank("RolandTR808").gain(.8)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCiQ6IGNob3JkKCI8RG03IEc3IENeNyBBNz4iKS52b2ljaW5nKCkuc3RydWN0KCJ%2BIHggfiB4IH4geCB%2BIHgiKS5zb3VuZCgicGlhbm8iKS5nYWluKC42KQokOiAiPERtNyBHNyBDXjcgQTc%2BIi5yb290Tm90ZXMoMikubm90ZSgpLnN0cnVjdCgieCB%2BIH4geCB%2BIH4geCB%2BIikuc291bmQoInNhd3Rvb3RoIikubHBmKDUwMCkKJDogc291bmQoIjxbcmltIH4gfiByaW0gfiB%2BIHJpbSB%2BXSBbfiB%2BIHJpbSB%2BIHJpbSB%2BIH4gfl0%2BIikuYmFuaygiUm9sYW5kVFI4MDgiKS5nYWluKC44KQ%3D%3D)

Three layers, three rhythmic jobs: bass walks the **tresillo**, comp answers on the **offbeats**,
clave holds the key. This texture — roots low and rhythmic, voicings high and syncopated — is the
default shape of every latin rhythm section, and you just built it from two strings.

### 3.4.2 Root motion is a melody

Listen to the bass line alone through the full diatonic cycle — roots falling in 4ths:

```js
setcpm(90/4)
$: "<Dm7 G7 C^7 F^7 Bm7b5 E7 Am7 A7>".rootNotes(2).note().struct("x ~ ~ x ~ ~ x ~").sound("sawtooth").lpf(500)._pianoroll()
$: chord("<Dm7 G7 C^7 F^7 Bm7b5 E7 Am7 A7>").voicing().struct("~ x ~ x ~ x ~ x").sound("piano").gain(.5)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCiQ6ICI8RG03IEc3IENeNyBGXjcgQm03YjUgRTcgQW03IEE3PiIucm9vdE5vdGVzKDIpLm5vdGUoKS5zdHJ1Y3QoInggfiB%2BIHggfiB%2BIHggfiIpLnNvdW5kKCJzYXd0b290aCIpLmxwZig1MDApLl9waWFub3JvbGwoKQokOiBjaG9yZCgiPERtNyBHNyBDXjcgRl43IEJtN2I1IEU3IEFtNyBBNz4iKS52b2ljaW5nKCkuc3RydWN0KCJ%2BIHggfiB4IH4geCB%2BIHgiKS5zb3VuZCgicGlhbm8iKS5nYWluKC41KQ%3D%3D)

D→G→C→F→B→E→A: every move a falling 4th (the strongest root motion there is), visiting every
chord in the key, landing home on Am7 with `A7` to loop back around. Your Module 2 key-cycling
exercise (D→G→C dorian) was secretly practicing this. Root motion has its own contour — good bass
players *sing* it.

### Challenges 3.4

1. Rebuild 3.4.1 with a **habanera** bass (`x ~ ~ x x ~ x ~`) at 66 bpm and the `Em7b5 A7b9 Dm7`
   minor ii-V-i. Congratulations: that's a tango rhythm section.
2. Drop the bass an octave (`rootNotes(1)`) — why does it get *worse*? (Too low = mud; register
   is a musical choice, not a number.)
3. In the diatonic cycle, mute the comp layer. Can you still name each chord from the bass +
   memory of the qualities? (Δ-walk from 3.1.2 says: which roots carry m7, which Δ7, which 7?)

### 🎷 Horn time 3.4

Loop 3.4.2's cycle. First pass: play roots along with the bass (**tenor: E A D G C# F# B B / alto:
B E A D G# C# F# F#**, one per bar). Second pass: root on beat 1, then the chord's 3rd on beat 3
(Chord Reference table, tenor reads the E-A-D-G rows / alto the B-E-A-D rows). Third pass: connect
each root to the next with a two-note walk-up. You're a bass player now; it will change how you
solo.

---

## Session 3.5 — Chord-scale pairs

### 3.5.1 One chord, three colors

The mapping every improviser carries: each chord type owns a set of scales, mild to spicy. Hold a
Dm7 and rotate its scale wardrobe, two bars each:

```js
setcpm(90/4)
$: n("0 ~ 2 4 ~ 3 2 ~").scale("<D4:dorian D4:minor:pentatonic D4:minor:blues>/2").sound("piano")
$: chord("Dm7").voicing().struct("x ~ ~ x ~ ~ x ~").sound("piano").gain(.5)
$: "<Dm7>".rootNotes(2).note().sound("sawtooth").lpf(500).gain(.4)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCiQ6IG4oIjAgfiAyIDQgfiAzIDIgfiIpLnNjYWxlKCI8RDQ6ZG9yaWFuIEQ0Om1pbm9yOnBlbnRhdG9uaWMgRDQ6bWlub3I6Ymx1ZXM%2BLzIiKS5zb3VuZCgicGlhbm8iKQokOiBjaG9yZCgiRG03Iikudm9pY2luZygpLnN0cnVjdCgieCB%2BIH4geCB%2BIH4geCB%2BIikuc291bmQoInBpYW5vIikuZ2FpbiguNSkKJDogIjxEbTc%2BIi5yb290Tm90ZXMoMikubm90ZSgpLnNvdW5kKCJzYXd0b290aCIpLmxwZig1MDApLmdhaW4oLjQp)

Dorian: full, warm, every note welcome. Minor pentatonic: leaner, punchier — the safety net. Blues
scale: adds the b5 grit. Same chord, three attitudes — and all three live in your book under
Category 3 with `C–7` printed above them.

### 3.5.2 The lydian lift

For Δ chords the choice is 4 vs #4. The riff leans on degree index 3 — plain 4 in major, #4 in
lydian:

```js
setcpm(80/4)
$: n("4 3 2 3 4 ~ 3 ~").scale("<C4:major C4:lydian>").sound("piano")
$: chord("C^7").voicing().struct("x ~ ~ ~ x ~ ~ ~").sound("piano").gain(.5)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDgwLzQpCiQ6IG4oIjQgMyAyIDMgNCB%2BIDMgfiIpLnNjYWxlKCI8QzQ6bWFqb3IgQzQ6bHlkaWFuPiIpLnNvdW5kKCJwaWFubyIpCiQ6IGNob3JkKCJDXjciKS52b2ljaW5nKCkuc3RydWN0KCJ4IH4gfiB%2BIHggfiB%2BIH4iKS5zb3VuZCgicGlhbm8iKS5nYWluKC41KQ%3D%3D)

Major's 4 (an F over C^7) rubs against the chord's E — hear the cloudiness. Lydian's #4 (F#)
floats — no rub, pure shimmer. That's why the book lists Lydian right under the Δ chord, and why
your latin syllabus tags it "medium" color: prettier than plain major, not yet spicy.

**The working table** (from your syllabus's LEARNINGS, now with sounds attached):

| Chord | First call | Warmer / spicier |
|---|---|---|
| `^7` (Δ) | major | lydian |
| `7` | mixolydian | lydian dominant, bebop dominant |
| `7b9` | *spanish* (phrygian dominant) | diminished (H-W) — Module 4 |
| `m7` (–7) | dorian | minor pentatonic, blues |
| `m7b5` (ø) | locrian #2 | locrian |
| `o7` | diminished (W-H) | — |

### Challenges 3.5

1. Test the dominant row: riff over a `G7` comp with `G3:mixolydian` vs `G3:lydian:dominant`.
   Which degree changed, and toward what? (It's the same 4→#4 move as the lydian lift.)
2. Test the ø row: `Bm7b5` comp, riff in `B3:locrian` vs `B3:locrian:#2`. The #2 version sounds
   noticeably less claustrophobic — which degree got the breathing room?
3. Free choice: build any two-layer chord+scale pairing from the table that you *disagree* with,
   or love, and be ready to say why. (Taste is the curriculum here.)

### 🎷 Horn time 3.5

Loop 3.5.1 (Dm7, rotating scales — **tenor thinks E dorian family, alto B dorian family**). Solo
continuously through all six bars, *matching your scale to the loop's*: dorian bars use all seven
notes, pentatonic bars only the five, blues bars lean on the b5. The discipline of switching
palettes over one static chord is exactly what Module 4 asks over *changing* chords.

---

## 🏁 Module 3 Milestone — the two-chord vamp

Build, from scratch, a Dm7→G7 vamp (one bar each) with four layers:

1. **Clave** — 3-2 son on rim, 808
2. **Bass** — `rootNotes(2)` on the tresillo
3. **Comp** — voicings answering on offbeats (`.struct("~ x ~ x ~ x ~ x")` or your own)
4. **Guide tones** — the F,C → F,B pair, long notes, quiet, with `._pianoroll()`

Then the theory deliverable — a **degree map**, written down (three lines, plain text): over Dm7
in D dorian, which `n` degrees are chord tones? Over G7 in G mixolydian, which? Which two notes
are the guide tones and what does each do at the change? (You have all three answers in this
module; writing them cements them.)

<details><summary>My version — compare, don't copy</summary>

```js
setcpm(92/4)
$: sound("<[rim ~ ~ rim ~ ~ rim ~] [~ ~ rim ~ rim ~ ~ ~]>").bank("RolandTR808").gain(.9)
$: "<Dm7 G7>".rootNotes(2).note().struct("x ~ ~ x ~ ~ x ~").sound("sawtooth").lpf(500)
$: chord("<Dm7 G7>").voicing().struct("~ x ~ x ~ x ~ x").sound("piano").gain(.55)
$: note("<[f4,c5] [f4,b4]>").sound("piano").gain(.35)._pianoroll()
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkyLzQpCiQ6IHNvdW5kKCI8W3JpbSB%2BIH4gcmltIH4gfiByaW0gfl0gW34gfiByaW0gfiByaW0gfiB%2BIH5dPiIpLmJhbmsoIlJvbGFuZFRSODA4IikuZ2FpbiguOSkKJDogIjxEbTcgRzc%2BIi5yb290Tm90ZXMoMikubm90ZSgpLnN0cnVjdCgieCB%2BIH4geCB%2BIH4geCB%2BIikuc291bmQoInNhd3Rvb3RoIikubHBmKDUwMCkKJDogY2hvcmQoIjxEbTcgRzc%2BIikudm9pY2luZygpLnN0cnVjdCgifiB4IH4geCB%2BIHggfiB4Iikuc291bmQoInBpYW5vIikuZ2FpbiguNTUpCiQ6IG5vdGUoIjxbZjQsYzVdIFtmNCxiNF0%2BIikuc291bmQoInBpYW5vIikuZ2FpbiguMzUpLl9waWFub3JvbGwoKQ%3D%3D)

Degree map: Dm7/dorian chord tones `n` 0 2 4 6 (D F A C); G7/mixolydian chord tones `n` 0 2 4 6
(G B D F) — same indices, 3.1's recipe. Guide tones F+C → F+B: F holds, C resolves down a half
step into G7's 3rd.

</details>

**Milestone horn exercise:** the vamp is your practice track for the week. **Tenor: Em7→A7
(guide tones G,D→C#,G). Alto: Bm7→E7 (D,A→G#,D).** Ladder: (1) guide tones as whole notes,
(2) arpeggios 1-3-5-7 up each chord, (3) free solo in D dorian / G mixolydian — landing a guide
tone at every bar line. Record yourself once; you'll hear the changes in your line even with the
loop muted. That's the whole point of this module.

---

## New tools in this module

| Tool | Meaning | Example |
|---|---|---|
| `n("[0,2,4,6]")` | chord = stacked scale degrees | `.scale("C4:major")` → CΔ7 |
| `chord()` | name chords by symbol | `chord("<Dm7 G7 C^7>")` |
| `.voicing()` | symbols → smoothly-led notes | `chord("Dm7").voicing()` |
| symbol spellings | `^7`, `m7`/`-7`, `7`, `m7b5`, `o7`, `7sus` | wrong spelling = **silence** |
| `.anchor()` | register ceiling for voicings | `.anchor("c6")` |
| `.arp()` | unroll a voicing by index | `.arp("0 1 2 3 4 3 2 1")` |
| `.struct()` | stamp rhythm onto pitch material | `.struct("x ~ ~ x ~ ~ x ~")` |
| `rootNotes(oct)` | chord symbols → bass roots | `"<Dm7 G7>".rootNotes(2).note()` |

**Theory vocabulary:** chords as stacked scale degrees; the diatonic chord walk (ii = m7, V = 7);
the five chord types as one recipe on five scales; voicings & voice leading; guide tones (3rds &
7ths); root motion in falling 4ths; chord-scale pairing, mild → spicy.

→ **Next: Module 4 — Progressions** *(coming soon)*
