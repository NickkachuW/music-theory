# Module 2 — Scale Lab: Degrees You Can Hear

Module 1 gave you time; this module gives you pitch. The core tool is a two-step recipe —
`n("0 2 4").scale("C4:dorian")` — numbers become scale degrees, degrees become notes. From here on
you'll *think in degrees* the way the Scale & Chord Reference is organized, and the scales you've
been reading on staves become things you build, mutate, and hear.

**Reference book tie-in:** every scale in this module lives in your
[Scale & Chord Reference](../Scale_and_Chord_Reference_Saxophones.pdf) — Category 1 (Major) and
Category 3 (Minor). Each horn exercise names the scale and *written* key to look up.

> **Concert pitch reminder.** Strudel sounds concert pitch. Your written note is a major 2nd up on
> tenor, a major 6th up on alto. Every horn exercise spells this out, but the rule for checking
> yourself: **concert C = tenor D = alto A**.

> **Degree numbering.** Strudel counts scale degrees **from 0**: `0` is the root, `2` is the third,
> `7` is the octave. The book (and every musician) counts from 1. So *book degree = strudel number
> + 1*. It feels wrong for a day and then becomes automatic — when this workbook says "the 6th",
> the code says `5`.

> **Seeing pitch.** Two visual tools join Module 1's punchcard, both chainable onto any line and
> both sound-neutral. `._pianoroll()` draws a scrolling piano roll under the line — pitch as
> height, so interval sizes become *distances you can see*. `._scope()` draws a live oscilloscope
> of the actual waveform — you'll use it to watch a filter reshape a sawtooth in 2.1.3. (The
> versions without the underscore, like `.pianoroll()`, paint the whole page background instead —
> try it once, it's fun.)

---

## Session 2.1 — Numbers into notes

### 2.1.1 Two ways to say the same thing

```js
setcpm(90/4)
note("c4 e4 g4 c5").sound("piano")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCm5vdGUoImM0IGU0IGc0IGM1Iikuc291bmQoInBpYW5vIik%3D)

`note()` speaks in note names — fine, but it's spelling, not thinking. Now the same sound as
*degrees of C major*:

```js
setcpm(90/4)
n("0 2 4 7").scale("C4:major").sound("piano")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCm4oIjAgMiA0IDciKS5zY2FsZSgiQzQ6bWFqb3IiKS5zb3VuZCgicGlhbm8iKQ%3D%3D)

Root, third, fifth, octave — a major arpeggio *as an idea*. Change `C4` to `Eb4`: same idea, new
key, zero respelling. That's the whole superpower, and it's exactly how the reference book is
organized — one shape, twelve keys.

### 2.1.2 The major scale, and where the half steps hide

```js
setcpm(90/4)
n("0 1 2 3 4 5 6 7").scale("C4:major").sound("piano")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCm4oIjAgMSAyIDMgNCA1IDYgNyIpLnNjYWxlKCJDNDptYWpvciIpLnNvdW5kKCJwaWFubyIp)

(There's a shorthand: `n("0 .. 7")` — same thing.) The book gives major as `W W H W W W H` — five
whole steps, two half steps. But *where* are the half steps? This snippet plays one pair of
neighboring degrees per bar (that's all the `<[ ] [ ] [ ]>` is doing — three bars, two half notes
each) so you can compare the step sizes directly:

```js
setcpm(60/4)
n("<[2 3] [6 7] [0 1]>").scale("C4:major").sound("piano")._pianoroll()
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDYwLzQpCm4oIjxbMiAzXSBbNiA3XSBbMCAxXT4iKS5zY2FsZSgiQzQ6bWFqb3IiKS5zb3VuZCgicGlhbm8iKS5fcGlhbm9yb2xsKCk%3D)

- Bar 1: `n` 2→3 = **E→F** — a half step. Small, leaning, almost touching.
- Bar 2: `n` 6→7 = **B→C** — the other half step.
- Bar 3: `n` 0→1 = **C→D** — a whole step, for comparison. Hear how much roomier it is.

The piano roll makes this literal: the half-step pairs sit one pixel-row apart, the whole-step
pair visibly further. Interval size = vertical distance, from now on.

Those two half-step locations are the major scale's fingerprint — every other neighbor pair is a
whole step (try a few: edit the brackets). When Session 2.3 swaps scales, what actually changes is
where the half steps sit.

### 2.1.3 The drone — your new practice partner

A root that never moves makes every degree's *tension* audible. One event per cycle = a bar-long
sustained note:

```js
setcpm(90/4)
$: n("0 1 2 3 4 5 6 7").scale("C4:major").sound("piano")
$: note("c2").sound("sawtooth").lpf("<400 800 2000>").gain(.35)._scope()
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCiQ6IG4oIjAgMSAyIDMgNCA1IDYgNyIpLnNjYWxlKCJDNDptYWpvciIpLnNvdW5kKCJwaWFubyIpCiQ6IG5vdGUoImMyIikuc291bmQoInNhd3Rvb3RoIikubHBmKCI8NDAwIDgwMCAyMDAwPiIpLmdhaW4oLjM1KS5fc2NvcGUoKQ%3D%3D)

`lpf()` is a low-pass filter, and the `._scope()` shows you exactly what it does. A raw sawtooth
wave is a jagged ramp — that jaggedness *is* its buzzy brightness (sharp corners = strong high
harmonics). The pattern `"<400 800 2000>"` sweeps the filter cutoff one value per bar: at 400 the
corners are sanded off and the wave is nearly a smooth hump (mellow, drone-friendly); by 2000 the
ramp shape comes back and so does the buzz. Shape = tone. Watch a few bars, then park it on
`lpf(400)` for practicing.

Now to the ear-training part: listen to how degree `6` (the 7th) *leans* toward the octave while
`4` (the fifth) sits perfectly still against the drone. Tension and resolution against a drone is
the fastest ear-training there is.

### Challenges 2.1

1. Play the scale descending. Two ways — find both (one types numbers, one doesn't).
2. Build the 1-3-5-8 arpeggio up *and* back down in one bar of eighth notes.
3. Against the drone, play each degree one per bar (`n("<0 1 2 3 4 5 6 7>")`) and rank them from
   "at rest" to "restless". (Classic answer: 1 5 3 6 2 4 7 — but trust your ears over the classic.)

<details><summary>Solutions</summary>

```js
setcpm(90/4)
n("0 1 2 3 4 5 6 7").scale("C4:major").rev().sound("piano")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCm4oIjAgMSAyIDMgNCA1IDYgNyIpLnNjYWxlKCJDNDptYWpvciIpLnJldigpLnNvdW5kKCJwaWFubyIp)

— or type `n("7 6 5 4 3 2 1 0")`. `.rev()` reverses the cycle.

```js
setcpm(90/4)
n("0 2 4 7 4 2 0 ~").scale("C4:major").sound("piano")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCm4oIjAgMiA0IDcgNCAyIDAgfiIpLnNjYWxlKCJDNDptYWpvciIpLnNvdW5kKCJwaWFubyIp)

(Ending on a rest instead of repeating the low root keeps it breathing — your call.)

</details>

### 🎷 Horn time 2.1

Loop the scale + drone at 60 bpm, one degree per bar (`n("<0 1 2 3 4 5 6 7>")`). Echo each note on
your horn: **concert C major = written D major on tenor, written A major on alto** (book: Category
1, Major, in that key). Then the ranking exercise from challenge 3 — but *on the horn*, listening
for which of your notes want to move.

---

## Session 2.2 — Pentatonics & first melodies

### 2.2.1 Five notes, zero clashes

```js
setcpm(90/4)
$: n("0 1 2 3 4 5").scale("C4:major:pentatonic").sound("piano")
$: note("c2").sound("sawtooth").lpf(400).gain(.35)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCiQ6IG4oIjAgMSAyIDMgNCA1Iikuc2NhbGUoIkM0Om1ham9yOnBlbnRhdG9uaWMiKS5zb3VuZCgicGlhbm8iKQokOiBub3RlKCJjMiIpLnNvdW5kKCJzYXd0b290aCIpLmxwZig0MDApLmdhaW4oLjM1KQ%3D%3D)

Major pentatonic: book degrees 1 2 3 5 6 — the major scale with 4 and 7 removed. And 4 and 7 were
exactly the two half-step makers from Session 2.1. No half steps anywhere = no note ever sounds
wrong = why pentatonics are every improviser's safety net. In degree-speak: index `5` is already
the octave here — five notes per octave changes the wrap point.

The minor pentatonic (book: Category 3) is the same trick on minor — 1 b3 4 5 b7:

```js
setcpm(90/4)
$: n("0 1 2 3 4 5").scale("A3:minor:pentatonic").sound("piano")
$: note("a1").sound("sawtooth").lpf(400).gain(.35)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCiQ6IG4oIjAgMSAyIDMgNCA1Iikuc2NhbGUoIkEzOm1pbm9yOnBlbnRhdG9uaWMiKS5zb3VuZCgicGlhbm8iKQokOiBub3RlKCJhMSIpLnNvdW5kKCJzYXd0b290aCIpLmxwZig0MDApLmdhaW4oLjM1KQ%3D%3D)

(Note the scale name syntax: multi-word names join with colons — `minor:pentatonic`,
`harmonic:minor`.)

### 2.2.2 Below the root: negative degrees

Melodies don't start politely on the root and climb. Negative numbers wrap *down* the scale:

```js
setcpm(90/4)
$: n("-2 -1 0 2 1 0 ~ ~").scale("A3:minor:pentatonic").sound("piano")
$: note("a1").sound("sawtooth").lpf(400).gain(.35)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCiQ6IG4oIi0yIC0xIDAgMiAxIDAgfiB%2BIikuc2NhbGUoIkEzOm1pbm9yOnBlbnRhdG9uaWMiKS5zb3VuZCgicGlhbm8iKQokOiBub3RlKCJhMSIpLnNvdW5kKCJzYXd0b290aCIpLmxwZig0MDApLmdhaW4oLjM1KQ%3D%3D)

`-1` is one scale step below the root, `-2` two steps. Approaching the root from below is the
oldest phrase-shape in the book.

### 2.2.3 Module 1 + Module 2 = music

Put degrees on the tresillo:

```js
setcpm(90/4)
$: n("0 ~ ~ 2 ~ ~ 4 ~").scale("A3:minor:pentatonic").sound("piano")
$: sound("bd@3 bd@3 bd@2").bank("RolandTR808").gain(.7)
$: sound("hh*8").gain(.3)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCiQ6IG4oIjAgfiB%2BIDIgfiB%2BIDQgfiIpLnNjYWxlKCJBMzptaW5vcjpwZW50YXRvbmljIikuc291bmQoInBpYW5vIikKJDogc291bmQoImJkQDMgYmRAMyBiZEAyIikuYmFuaygiUm9sYW5kVFI4MDgiKS5nYWluKC43KQokOiBzb3VuZCgiaGgqOCIpLmdhaW4oLjMp)

Same rhythm you built in Session 1.2 — now it has a melody. This is the template for everything
that follows: rhythm layer + degree layer + (soon) harmony layer.

### Challenges 2.2

1. Write a two-bar question/answer using `< >`: bar 1 ends *away* from the root (restless), bar 2
   ends *on* it (resolved).
2. Take your Module 1 milestone groove and replace the cowbell layer with a pentatonic melody on
   the cinquillo rhythm — `n("0 ~ 2 4 ~ 3 2 ~")` territory, your choice of degrees.
3. Rebuild the tresillo melody using only negative degrees and `0`. Where does it feel like it
   resolves now?

<details><summary>Solution sketch for 1</summary>

```js
setcpm(90/4)
$: n("<[0 2 3 4] [3 2 -1 0]>").scale("A3:minor:pentatonic").sound("piano")
$: note("a1").sound("sawtooth").lpf(400).gain(.35)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCiQ6IG4oIjxbMCAyIDMgNF0gWzMgMiAtMSAwXT4iKS5zY2FsZSgiQTM6bWlub3I6cGVudGF0b25pYyIpLnNvdW5kKCJwaWFubyIpCiQ6IG5vdGUoImExIikuc291bmQoInNhd3Rvb3RoIikubHBmKDQwMCkuZ2FpbiguMzUp)

Bar 1 parks on `4` (the restless b7); bar 2 walks home through `-1`. Any answer that lands on `0`
and *feels* landed is correct.

</details>

### 🎷 Horn time 2.2

Loop the tresillo melody (2.2.3). **Concert A minor pentatonic = written B minor pent on tenor,
written F# minor pent on alto.** Trade bars with the loop: it plays a bar, you answer with your own
pentatonic bar on the horn. Stay on the tresillo rhythm at first, then free the rhythm while
keeping the five notes.

---

## Session 2.3 — The minor family: one riff, three colors

### 2.3.1 The A/B/C test

This session is the heart of the module. One riff that leans on the 6th and 7th — the degrees where
the minor scales disagree — cycled through three scales, one bar each:

```js
setcpm(80/4)
$: n("0 2 4 5 6 5 4 2").scale("<D4:dorian D4:aeolian D4:harmonic:minor>").sound("piano")._pianoroll()
$: note("d2").sound("sawtooth").lpf(400).gain(.35)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDgwLzQpCiQ6IG4oIjAgMiA0IDUgNiA1IDQgMiIpLnNjYWxlKCI8RDQ6ZG9yaWFuIEQ0OmFlb2xpYW4gRDQ6aGFybW9uaWM6bWlub3I%2BIikuc291bmQoInBpYW5vIikuX3BpYW5vcm9sbCgpCiQ6IG5vdGUoImQyIikuc291bmQoInNhd3Rvb3RoIikubHBmKDQwMCkuZ2FpbiguMzUp)

**Identical code, three musics.** What changed, bar by bar:

| Scale | 6th (`n` 5) | 7th (`n` 6) | Character | Book (Cat. 3) |
|---|---|---|---|---|
| Dorian | natural 6 | b7 | bright minor — the latin workhorse | Minor (Dorian) |
| Aeolian | b6 | b7 | plain, darker — "sad" default | Pure/Natural Minor |
| Harmonic minor | b6 | **natural 7** | dramatic, Old-World — tango's home | Harmonic Minor |

Listen for bar 1's `5` sounding *sweet*, bar 2's `5` sagging darker, and bar 3's `6` yanking hard
up toward the root. On the piano roll the riff redraws itself each bar with the same *shape* but
different heights at positions 4 and 6 — the two notes sliding down or up a row are precisely the
6th and 7th from the table.

### 2.3.2 The augmented 2nd

Harmonic minor's b6 → natural 7 gap is *three* half steps — the augmented 2nd, the interval your
LEARNINGS notes call the defining tango sound. Isolate it:

```js
setcpm(60/4)
$: n("5 6 7 ~").scale("A3:harmonic:minor").sound("piano")._pianoroll()
$: note("a1").sound("sawtooth").lpf(400).gain(.35)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDYwLzQpCiQ6IG4oIjUgNiA3IH4iKS5zY2FsZSgiQTM6aGFybW9uaWM6bWlub3IiKS5zb3VuZCgicGlhbm8iKS5fcGlhbm9yb2xsKCkKJDogbm90ZSgiYTEiKS5zb3VuZCgic2F3dG9vdGgiKS5scGYoNDAwKS5nYWluKC4zNSk%3D)

In A harmonic minor that's **F → G# → A**: the exotic leap, then the half-step snap home. The
piano roll shows it as a big jump followed by a tiny one — three rows up, then one. No other
common scale contains this. Once you can hear it, you'll notice it in every tango ever written.

### Challenges 2.3

1. Ear test: change the scale list to an order you *don't* write down (shuffle the three names,
   evaluate, look away for a minute). Playing back — name each bar's scale by ear.
2. Add `D4:melodic:minor` as a fourth bar. Which existing bar does it most resemble, and which
   single degree gives it away? (Answer in solution.)
3. Write a riff using **only** degrees `4 5 6 7` — the maximum-contrast zone — and cycle the three
   scales. It should sound like three different songs.

<details><summary>Solutions / answers</summary>

2: Melodic minor = harmonic minor with the 6th raised back to natural — so it resembles the
harmonic minor bar but without the augmented-2nd exotic gap; `n` 5 is the giveaway degree. It's
"minor below, major above": dark 3rd, smooth sweet top half.

```js
setcpm(80/4)
$: n("4 5 6 7 6 5 4 ~").scale("<D4:dorian D4:aeolian D4:harmonic:minor>").sound("piano")
$: note("d2").sound("sawtooth").lpf(400).gain(.35)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDgwLzQpCiQ6IG4oIjQgNSA2IDcgNiA1IDQgfiIpLnNjYWxlKCI8RDQ6ZG9yaWFuIEQ0OmFlb2xpYW4gRDQ6aGFybW9uaWM6bWlub3I%2BIikuc291bmQoInBpYW5vIikKJDogbm90ZSgiZDIiKS5zb3VuZCgic2F3dG9vdGgiKS5scGYoNDAwKS5nYWluKC4zNSk%3D)

</details>

### 🎷 Horn time 2.3

Loop 2.3.1's riff+drone but slow the scale change to taste. **Concert D minor = written E on
tenor, written B on alto** — find Dorian, Natural Minor, and Harmonic Minor in those keys in the
book (Category 3). Play the riff along with each bar, matching the loop's 6th and 7th. The goal
isn't speed — it's that your fingers learn *which degree changed* between scales.

---

## Session 2.4 — The tango scale

### 2.4.1 First tango texture

Habanera bass from Session 1.3 + harmonic minor line on top. This is the sound Modules 4–6 build
into full arrangements:

```js
setcpm(66/4)
$: n("<[0 ~ 2 4] [5 6 7 6] [4 ~ 2 1] [0 ~ ~ ~]>").scale("A3:harmonic:minor").sound("piano")
$: sound("bd@3 bd@1 bd@2 bd@2").bank("RolandTR808").gain(.8)
$: note("<a1 a1 e1 a1>").sound("sawtooth").lpf(400).gain(.35)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDY2LzQpCiQ6IG4oIjxbMCB%2BIDIgNF0gWzUgNiA3IDZdIFs0IH4gMiAxXSBbMCB%2BIH4gfl0%2BIikuc2NhbGUoIkEzOmhhcm1vbmljOm1pbm9yIikuc291bmQoInBpYW5vIikKJDogc291bmQoImJkQDMgYmRAMSBiZEAyIGJkQDIiKS5iYW5rKCJSb2xhbmRUUjgwOCIpLmdhaW4oLjgpCiQ6IG5vdGUoIjxhMSBhMSBlMSBhMT4iKS5zb3VuZCgic2F3dG9vdGgiKS5scGYoNDAwKS5nYWluKC4zNSk%3D)

Four-bar phrase: rise, the augmented-2nd bar, descent, rest. The bass drone dips to the fifth (E)
in bar 3 — a preview of harmony doing its own moving (Module 3's whole subject).

### 2.4.2 Melodic minor — the smooth cousin

Your reference book prints melodic minor with two forms: raised 6+7 going up, natural minor coming
down (the only scale in the book with different ascending/descending spellings). Jazz and modern
tango players mostly use the ascending form in both directions. Compare directly:

```js
setcpm(66/4)
$: n("0 1 2 3 4 5 6 7").scale("<A3:harmonic:minor A3:melodic:minor>").sound("piano")
$: note("a1").sound("sawtooth").lpf(400).gain(.35)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDY2LzQpCiQ6IG4oIjAgMSAyIDMgNCA1IDYgNyIpLnNjYWxlKCI8QTM6aGFybW9uaWM6bWlub3IgQTM6bWVsb2RpYzptaW5vcj4iKS5zb3VuZCgicGlhbm8iKQokOiBub3RlKCJhMSIpLnNvdW5kKCJzYXd0b290aCIpLmxwZig0MDApLmdhaW4oLjM1KQ%3D%3D)

Harmonic minor: passionate, angular (the aug 2nd). Melodic minor: the same drama *sanded smooth* —
your LEARNINGS file tags it "modern tango tonic (sophisticated)". Piazzolla lives in both.

### Challenges 2.4

1. Transpose the whole tango texture (2.4.1) to **D minor** — the most common tango/latin key.
   Count how many characters you changed. (This is the payoff of degree-thinking.)
2. Make the melody sincopa: shift it so bar 1 starts on the and-of-1 instead of the downbeat
   (a well-placed `~` or `[~ x]` does it).
3. Swap `harmonic:minor` → `melodic:minor` in the texture. Describe the mood change in one word.

<details><summary>Solution for 1</summary>

```js
setcpm(66/4)
$: n("<[0 ~ 2 4] [5 6 7 6] [4 ~ 2 1] [0 ~ ~ ~]>").scale("D3:harmonic:minor").sound("piano")
$: sound("bd@3 bd@1 bd@2 bd@2").bank("RolandTR808").gain(.8)
$: note("<d2 d2 a1 d2>").sound("sawtooth").lpf(400).gain(.35)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDY2LzQpCiQ6IG4oIjxbMCB%2BIDIgNF0gWzUgNiA3IDZdIFs0IH4gMiAxXSBbMCB%2BIH4gfl0%2BIikuc2NhbGUoIkQzOmhhcm1vbmljOm1pbm9yIikuc291bmQoInBpYW5vIikKJDogc291bmQoImJkQDMgYmRAMSBiZEAyIGJkQDIiKS5iYW5rKCJSb2xhbmRUUjgwOCIpLmdhaW4oLjgpCiQ6IG5vdGUoIjxkMiBkMiBhMSBkMj4iKS5zb3VuZCgic2F3dG9vdGgiKS5scGYoNDAwKS5nYWluKC4zNSk%3D)

Two spots: the scale root, and the bass notes (root and fifth). The melody — untouched. Twelve
keys, one riff.

</details>

### 🎷 Horn time 2.4

The 2.4.1 loop is your first real backing track. **Concert A harmonic minor = written B harmonic
minor on tenor, written F# harmonic minor on alto.** First pass: play the four-bar melody with the
loop. Second pass: keep the loop's bars 1–3 and improvise your own bar 4. Third pass: improvise all
four bars using degrees 0–7, making sure to *land* the augmented 2nd (your written 6th→7th) at
least once per pass — that's the tango move.

---

## Session 2.5 — Modes as rotations

### 2.5.1 The drone proof

Modes confuse people on paper and are obvious in the ear. Same seven notes, same melody line —
only the **drone** moves:

```js
setcpm(80/4)
$: n("0 1 2 3 4 5 6 7").scale("C4:major").sound("piano")._pianoroll()
$: note("<c2 d2 e2>").sound("sawtooth").lpf(400).gain(.4)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDgwLzQpCiQ6IG4oIjAgMSAyIDMgNCA1IDYgNyIpLnNjYWxlKCJDNDptYWpvciIpLnNvdW5kKCJwaWFubyIpLl9waWFub3JvbGwoKQokOiBub3RlKCI8YzIgZDIgZTI%2BIikuc291bmQoInNhd3Rvb3RoIikubHBmKDQwMCkuZ2FpbiguNCk%3D)

Bar 1 is C major (ionian). Bar 2: *nothing about the melody changed*, but home is now D — you're
hearing **D dorian**. Bar 3: home is E — **E phrygian**, instantly darker. The piano roll is the
receipt: an identical picture every single bar, while the mood transforms underneath it. A mode
isn't a new set of notes; it's a new center of gravity. The drone *is* the mode.

### 2.5.2 The same thing, named

`D4:dorian` spells out what the moving drone implied — and now degree numbers are *relative to the
new home*:

```js
setcpm(80/4)
$: n("0 2 4 5 6 5 4 2").scale("<D4:dorian E4:phrygian F4:lydian G4:mixolydian>").sound("piano")
$: note("<d2 e2 f2 g2>").sound("sawtooth").lpf(400).gain(.35)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDgwLzQpCiQ6IG4oIjAgMiA0IDUgNiA1IDQgMiIpLnNjYWxlKCI8RDQ6ZG9yaWFuIEU0OnBocnlnaWFuIEY0Omx5ZGlhbiBHNDptaXhvbHlkaWFuPiIpLnNvdW5kKCJwaWFubyIpCiQ6IG5vdGUoIjxkMiBlMiBmMiBnMj4iKS5zb3VuZCgic2F3dG9vdGgiKS5scGYoNDAwKS5nYWluKC4zNSk%3D)

All four bars use only white-key notes — the same seven pitches — yet: dorian (bright minor, you
know it from 2.3), phrygian (that b2 shadow right above the root — the latin *tinge*, and the seed
of Module 4's phrygian dominant), lydian (the #4 glow — floaty, film-score major), mixolydian
(major with a b7 — the dominant sound, the key to Module 3's `7` chords).

### Challenges 2.5

1. Major vs mixolydian differ by one degree. Which `n` number exposes it? Write a two-bar A/B that
   proves it.
2. Make lydian glow: a riff that leans on `n` 3 (the #4) against an F drone, alternating
   `F4:lydian` and `F4:major`. The lydian bars should shimmer; the major bars should sound plain.
3. The 2.5.1 drone trick with minor: melody in `A3:aeolian`, drone walking `<a1 d2 e2>`. What are
   the three modes you're hearing? (Modes of minor work the same way.)

<details><summary>Answers</summary>

1: `n` 6 — the 7th (B natural in C major, Bb in C mixolydian). E.g.
`n("4 5 6 7")` over `"<C4:major C4:mixolydian>"` with a C drone.

3: A aeolian, D dorian, E phrygian — the same rotation game inside the minor family.

</details>

### 🎷 Horn time 2.5

The drone proof, live: loop **only the drone** `note("<c2 d2 e2 d2>").sound("sawtooth").lpf(400)`
(one bar each). On the horn, play your **written D major scale (tenor) / A major scale (alto)** —
concert C major — continuously in eighth notes, up and down, while the drone moves underneath you.
Feel your unchanged notes turn ionian → dorian → phrygian → dorian. This one exercise is worth the
whole session.

---

## Session 2.6 — Scale patterns: the technique lab

*The patterns you drill from technique books — thirds, cells, sequences — generated instead of
read. This session's tools power the Module 6 scale-drill machine.*

### 2.6.1 Parallel thirds — `.add()` with a stack

`.add()` shifts degrees *before* the scale maps them — so adding 2 adds a diatonic third, never a
wrong note. And adding a stack `n("0,2")` plays original + third together:

```js
setcpm(80/4)
$: n("0 1 2 3 4 5 6 7").add(n("0,2")).scale("C4:major").sound("piano")
$: note("c2").sound("sawtooth").lpf(400).gain(.3)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDgwLzQpCiQ6IG4oIjAgMSAyIDMgNCA1IDYgNyIpLmFkZChuKCIwLDIiKSkuc2NhbGUoIkM0Om1ham9yIikuc291bmQoInBpYW5vIikKJDogbm90ZSgiYzIiKS5zb3VuZCgic2F3dG9vdGgiKS5scGYoNDAwKS5nYWluKC4zKQ%3D%3D)

> **The `.add(n(...))` gotcha.** Whatever you add must be wrapped in `n()`, matching the pattern
> you're adding to. A bare `.add(2)` does **nothing** — silently, no error. Strudel patterns carry
> *labeled* values (`n`, `note`, `gain`, ...), and a naked `2` doesn't say which label it belongs
> to, so the addition is skipped. If an `.add()` ever seems to have no effect, this is why. The
> same rule applies elsewhere: `note("c2").add(note(12))`, `.add(gain(.2))`.

Diatonic harmony for one comma. Try `n("0,4")` (fifths — instantly medieval) and `n("0,2,4")`
(full triads — a Module 3 spoiler).

### 2.6.2 The canon trick — `.off()`

`.off(t, f)` layers a time-shifted, transformed copy. Offset by an eighth, up a third:

```js
setcpm(80/4)
$: n("0 2 1 3 2 4 3 5").off(1/8, x=>x.add(n(2))).scale("C4:major").sound("piano").gain(.7)
$: note("c2").sound("sawtooth").lpf(400).gain(.3)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDgwLzQpCiQ6IG4oIjAgMiAxIDMgMiA0IDMgNSIpLm9mZigxLzgsIHg9PnguYWRkKG4oMikpKS5zY2FsZSgiQzQ6bWFqb3IiKS5zb3VuZCgicGlhbm8iKS5nYWluKC43KQokOiBub3RlKCJjMiIpLnNvdW5kKCJzYXd0b290aCIpLmxwZig0MDApLmdhaW4oLjMp)

The line chases itself in thirds — instant two-part counterpoint. (`.superimpose(x=>x.add(n(2)))`
is the same idea with no time shift — parallel motion instead of a chase.)

### 2.6.3 The climbing cell — your technique book, generated

The classic **1-2-3-5 cell** (degrees `0 1 2 4`), walked up the scale one step per bar:

```js
setcpm(100/4)
$: n("0 1 2 4").add(n("<0 1 2 3 4 5 6 7>")).scale("D4:dorian").sound("piano")._pianoroll()
$: note("d2").sound("sawtooth").lpf(400).gain(.3)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDEwMC80KQokOiBuKCIwIDEgMiA0IikuYWRkKG4oIjwwIDEgMiAzIDQgNSA2IDc%2BIikpLnNjYWxlKCJENDpkb3JpYW4iKS5zb3VuZCgicGlhbm8iKS5fcGlhbm9yb2xsKCkKJDogbm90ZSgiZDIiKS5zb3VuZCgic2F3dG9vdGgiKS5scGYoNDAwKS5nYWluKC4zKQ%3D%3D)

`.add(n("<...>"))` bumps the whole cell by one scale degree each cycle — eight bars later you've
sequenced the cell through the entire scale, diatonically correct at every step. The piano roll
draws it as a staircase: the same four-note shape stamped one row higher each bar. This exact
exercise fills pages of jazz technique books. You just wrote it in one line, in any scale, in any
key.

### 2.6.4 Key cycling

The scale itself can be a sequence — three latin priority keys, descending in the circle:

```js
setcpm(100/4)
$: n("0 1 2 4 2 1 0 ~").scale("<D4:dorian G4:dorian C4:dorian>").sound("piano")
$: note("<d2 g2 c2>").sound("sawtooth").lpf(400).gain(.3)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDEwMC80KQokOiBuKCIwIDEgMiA0IDIgMSAwIH4iKS5zY2FsZSgiPEQ0OmRvcmlhbiBHNDpkb3JpYW4gQzQ6ZG9yaWFuPiIpLnNvdW5kKCJwaWFubyIpCiQ6IG5vdGUoIjxkMiBnMiBjMj4iKS5zb3VuZCgic2F3dG9vdGgiKS5scGYoNDAwKS5nYWluKC4zKQ%3D%3D)

D → G → C is root motion in fourths — the strongest progression in music and the engine of Module
4's ii-V-i. Your fingers are already practicing it.

### Challenges 2.6

1. Sequence the cell in *descending* thirds: cell `0 1 2 4`, added offsets walking down
   (`<7 6 5 ...>` or `.rev()` — compare both).
2. Build the "1235" drill in harmonic minor and find the bar where the augmented 2nd lands inside
   the cell. It'll sound suddenly Middle-Eastern — which offset bar is it?
3. Combine everything: climbing cell + `.off(1/8, x=>x.add(n(2)))` canon + drone. Two-part
   counterpoint etude, zero notes written by hand.

<details><summary>Solution for 3 (and answer for 2)</summary>

2: Two bars, actually — offsets `4` and `5`. At offset 4 the cell is degrees `4 5 6 8` and at
offset 5 it's `5 6 7 9`; both contain the b6→7 step, so the exotic color arrives twice in a row.

```js
setcpm(100/4)
$: n("0 1 2 4").add(n("<0 1 2 3 4 5 6 7>")).off(1/8, x=>x.add(n(2))).scale("D4:harmonic:minor").sound("piano").gain(.7)
$: note("d2").sound("sawtooth").lpf(400).gain(.3)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDEwMC80KQokOiBuKCIwIDEgMiA0IikuYWRkKG4oIjwwIDEgMiAzIDQgNSA2IDc%2BIikpLm9mZigxLzgsIHg9PnguYWRkKG4oMikpKS5zY2FsZSgiRDQ6aGFybW9uaWM6bWlub3IiKS5zb3VuZCgicGlhbm8iKS5nYWluKC43KQokOiBub3RlKCJkMiIpLnNvdW5kKCJzYXd0b290aCIpLmxwZig0MDApLmdhaW4oLjMp)

</details>

### 🎷 Horn time 2.6

Whatever Strudel generates, you can read from the book and play. Loop the climbing cell in
**concert D dorian** at 60 bpm — on your horn that's the **written E dorian (tenor) / B dorian
(alto)** scale, cell 1-2-3-5 from each degree. Strudel plays a bar, you play the *next* bar's cell
before the loop gets there. You're not echoing anymore — you're predicting, which means you're
thinking in the scale, not about it.

---

## 🏁 Module 2 Milestone — one cell, three scales, three keys

Build a single practice file, from scratch:

1. The `0 1 2 4` cell climbing through a full octave of offsets (2.6.3)
2. Scale switching **every 8 bars** through: dorian → harmonic minor → minor pentatonic
   (mini-notation: `< >` accepts `/8` to stretch each entry to 8 cycles)
3. Key set: D, then G, then C (edit by hand between runs, or nest `< >` if you're feeling brave)
4. Drone following the root; tresillo kick underneath

Then — the actual milestone — **write three sentences**, one per scale, describing what the scale
color does to the same cell. ("Dorian makes it sound like...") If you can say it, you can hear it;
if you can hear it, you'll find it on the horn.

<details><summary>My version — compare, don't copy</summary>

```js
setcpm(100/4)
$: n("0 1 2 4").add(n("<0 1 2 3 4 5 6 7>"))
   .scale("<D4:dorian D4:harmonic:minor D4:minor:pentatonic>/8")
   .sound("piano")._pianoroll()
$: note("d2").sound("sawtooth").lpf(400).gain(.3)
$: sound("bd@3 bd@3 bd@2").bank("RolandTR808").gain(.5)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDEwMC80KQokOiBuKCIwIDEgMiA0IikuYWRkKG4oIjwwIDEgMiAzIDQgNSA2IDc%2BIikpCiAgIC5zY2FsZSgiPEQ0OmRvcmlhbiBENDpoYXJtb25pYzptaW5vciBENDptaW5vcjpwZW50YXRvbmljPi84IikKICAgLnNvdW5kKCJwaWFubyIpLl9waWFub3JvbGwoKQokOiBub3RlKCJkMiIpLnNvdW5kKCJzYXd0b290aCIpLmxwZig0MDApLmdhaW4oLjMpCiQ6IHNvdW5kKCJiZEAzIGJkQDMgYmRAMiIpLmJhbmsoIlJvbGFuZFRSODA4IikuZ2FpbiguNSk%3D)

For mine: dorian turns the cell into a warm montuno fragment; harmonic minor makes bars 5–6
suddenly Andalusian as the aug 2nd enters the cell; pentatonic swallows the passing tones and
turns it into a riff.

</details>

**Milestone horn exercise:** play along with the full 24-bar cycle in concert D — written E
(tenor) / B (alto) — reading each scale from the book as it arrives. Then close the book and do it
again.

---

## New tools in this module

| Tool | Meaning | Example |
|---|---|---|
| `n()` + `.scale()` | numbers → scale degrees → notes | `n("0 2 4").scale("C4:dorian")` |
| scale names | root+octave, colons join words | `"A3:harmonic:minor"`, `"C4:minor:pentatonic"` |
| `0 .. 7` | degree range shorthand | `n("0 .. 7")` |
| negative `n` | wrap below the root | `n("-2 -1 0")` |
| `note()` | literal note names (for drones) | `note("c2")` |
| `.sound()` / `.lpf()` | timbre; filter for drones | `.sound("sawtooth").lpf(400)` |
| `.rev()` | reverse the cycle | `.rev()` |
| `.add(n(...))` | shift degrees — addend must be `n()`-wrapped! | `.add(n("<0 1 2>"))`, `.add(n("0,2"))` |
| `.off(t, f)` | delayed transformed copy | `.off(1/8, x=>x.add(n(2)))` |
| `.superimpose(f)` | parallel transformed copy | `.superimpose(x=>x.add(n(2)))` |
| `<a b>/n` | stretch alternation to n cycles each | `"<X Y>/8"` |
| patterned scales | scale changes are patterns too | `.scale("<D4:dorian G4:dorian>")` |
| `._pianoroll()` | piano roll under the line (visual only) | `.sound("piano")._pianoroll()` |
| `._scope()` | live oscilloscope of the waveform | `.sound("sawtooth")._scope()` |

**Theory vocabulary:** degrees as numbers (0-indexed); W-W-H-W-W-W-H and where half steps live;
pentatonics as "the scale minus its half steps"; the minor family's 6th/7th fingerprint; the
augmented 2nd; modes as rotations (the drone proof); diatonic sequencing (cells, thirds).

→ **Next: Module 3 — Chord Lab** *(coming soon)*
