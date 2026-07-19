# Module 4 — Progressions: ii-V-i and the Tango Cadences

This is the module the first three were building. You have rhythm (M1), scale colors (M2), and the
chord/bass/comp machinery (M3) — now the chords start *moving*, and the two motions that power all
of latin jazz and tango are the **minor ii-V-i** and the **half-step cadences** (bII and bVI).
Milestone: a full 16-bar tango you can solo over.

**Reference tie-ins:** the ii-V-i and cadence patterns from your
[Latin Jazz & Tango Syllabus](../latin-jazz-syllabus/Latin_Jazz_Tango_Syllabus.pdf); scale colors
from Categories 2 (Dominant), 3 (Minor), and 4 (Half-Diminished) of the
[Scale & Chord Reference](../Scale_and_Chord_Reference_Saxophones.pdf).

> **The one technique this module drills:** give every layer the *same-length* `< >` list. If the
> chords, the bass symbols, and the melody's scales are all 4-entry lists, they change together,
> bar by bar, forever locked. Write the progression once, then re-spell it per layer.

---

## Session 4.1 — The minor ii-V-i: the sound of coming home

### 4.1.1 The progression

Concert D minor — the most common latin key. One bar of iiø, one of V7b9, two bars home:

```js
setcpm(80/4)
$: chord("<Em7b5 A7b9 Dm Dm>").voicing().struct("~ x ~ x ~ x ~ ~").sound("piano").gain(.55)
$: "<Em7b5 A7b9 Dm Dm>".rootNotes(2).note().struct("x ~ ~ x x ~ x ~").sound("sawtooth").lpf(500)
$: sound("bd@3 bd@1 bd@2 bd@2").bank("RolandTR808").gain(.7)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDgwLzQpCiQ6IGNob3JkKCI8RW03YjUgQTdiOSBEbSBEbT4iKS52b2ljaW5nKCkuc3RydWN0KCJ%2BIHggfiB4IH4geCB%2BIH4iKS5zb3VuZCgicGlhbm8iKS5nYWluKC41NSkKJDogIjxFbTdiNSBBN2I5IERtIERtPiIucm9vdE5vdGVzKDIpLm5vdGUoKS5zdHJ1Y3QoInggfiB%2BIHggeCB%2BIHggfiIpLnNvdW5kKCJzYXd0b290aCIpLmxwZig1MDApCiQ6IHNvdW5kKCJiZEAzIGJkQDEgYmRAMiBiZEAyIikuYmFuaygiUm9sYW5kVFI4MDgiKS5nYWluKC43KQ%3D%3D)

Three functions, three feelings: **iiø** leans (that ø instability), **V7b9** *demands* (the b9 is
the Spanish tension you met in 3.2's challenge), **i** arrives. The bass is on the habanera —
this progression with this rhythm is already tango. Sit inside it for a while; every session in
this module is a variation of this homecoming.

### 4.1.2 The scale-per-chord melody

Now the module's core technique — a melody whose scale changes with the chord, using a locked
4-entry list. From your syllabus's mapping: locrian #2 over ø, **spanish** over 7b9, harmonic
minor over i:

```js
setcpm(80/4)
$: n("0 2 4 6 4 2 0 ~")
   .scale("<E4:locrian:#2 A3:spanish D4:harmonic:minor D4:harmonic:minor>")
   .sound("piano")._pianoroll()
$: chord("<Em7b5 A7b9 Dm Dm>").voicing().struct("~ x ~ x ~ x ~ ~").sound("piano").gain(.5)
$: "<Em7b5 A7b9 Dm Dm>".rootNotes(2).note().struct("x ~ ~ x x ~ x ~").sound("sawtooth").lpf(500)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDgwLzQpCiQ6IG4oIjAgMiA0IDYgNCAyIDAgfiIpCiAgIC5zY2FsZSgiPEU0OmxvY3JpYW46IzIgQTM6c3BhbmlzaCBENDpoYXJtb25pYzptaW5vciBENDpoYXJtb25pYzptaW5vcj4iKQogICAuc291bmQoInBpYW5vIikuX3BpYW5vcm9sbCgpCiQ6IGNob3JkKCI8RW03YjUgQTdiOSBEbSBEbT4iKS52b2ljaW5nKCkuc3RydWN0KCJ%2BIHggfiB4IH4geCB%2BIH4iKS5zb3VuZCgicGlhbm8iKS5nYWluKC41KQokOiAiPEVtN2I1IEE3YjkgRG0gRG0%2BIi5yb290Tm90ZXMoMikubm90ZSgpLnN0cnVjdCgieCB%2BIH4geCB4IH4geCB%2BIikuc291bmQoInNhd3Rvb3RoIikubHBmKDUwMCk%3D)

One degree pattern, three scales, zero wrong notes — the pattern *rides* the harmony.

And here's the beautiful secret, which is Module 2.5's modes-as-rotations paying off: **A spanish
and D harmonic minor are the same seven notes.** Spanish (phrygian dominant) is the 5th mode of
harmonic minor — A Bb C# D E F G *is* D E F G A Bb C# started from A. The V chord's exotic scale
and the home scale are one collection with two centers of gravity. That's why the resolution
sounds inevitable: the notes never changed, only home did.

### Challenges 4.1

1. Swap the i-bars' scale to `D4:melodic:minor`, then `D4:dorian` (with chord `Dm7` instead of
   `Dm`). Three flavors of "home": dramatic / smooth / vamp-ready. Which is *your* tango?
2. Make the melody sincopa: rests on beats 1 and 3, notes between.
3. Two-chords-per-bar compression: `"<[Em7b5 A7b9] Dm>"` — the whole ii-V in one bar. (Remember
   to compress *every* layer's list the same way.)

### 🎷 Horn time 4.1

Loop 4.1.1 (no Strudel melody). **Tenor: F#m7b5–B7b9–Em (E minor). Alto: C#m7b5–F#7b9–Bm
(B minor).** Ladder: (1) roots only; (2) guide tones — over the ø play its 3rd+7th, over V7b9 the
3rd+b9 (the spicy pair), over i land the 5th or root; (3) the written scales — tenor: F# locrian
#2 → B spanish → E harmonic minor; alto: C# locrian #2 → F# spanish → B harmonic minor. Your book
has each under Categories 4, 2, and 3.

---

## Session 4.2 — The five priority keys

### 4.2.1 Two keys, one loop

Your syllabus names the latin priority minor keys: **D, G, C, F, A minor**. The move between keys
is itself practice material — here's Dm then Gm, eight locked bars:

```js
setcpm(84/4)
$: chord("<Em7b5 A7b9 Dm Dm Am7b5 D7b9 Gm Gm>").voicing().struct("~ x ~ x ~ x ~ ~").sound("piano").gain(.55)
$: "<Em7b5 A7b9 Dm Dm Am7b5 D7b9 Gm Gm>".rootNotes(2).note().struct("x ~ ~ x ~ ~ x ~").sound("sawtooth").lpf(500)
$: sound("<[rim ~ ~ rim ~ ~ rim ~] [~ ~ rim ~ rim ~ ~ ~]>").bank("RolandTR808").gain(.8)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDg0LzQpCiQ6IGNob3JkKCI8RW03YjUgQTdiOSBEbSBEbSBBbTdiNSBEN2I5IEdtIEdtPiIpLnZvaWNpbmcoKS5zdHJ1Y3QoIn4geCB%2BIHggfiB4IH4gfiIpLnNvdW5kKCJwaWFubyIpLmdhaW4oLjU1KQokOiAiPEVtN2I1IEE3YjkgRG0gRG0gQW03YjUgRDdiOSBHbSBHbT4iLnJvb3ROb3RlcygyKS5ub3RlKCkuc3RydWN0KCJ4IH4gfiB4IH4gfiB4IH4iKS5zb3VuZCgic2F3dG9vdGgiKS5scGYoNTAwKQokOiBzb3VuZCgiPFtyaW0gfiB%2BIHJpbSB%2BIH4gcmltIH5dIFt%2BIH4gcmltIH4gcmltIH4gfiB%2BXT4iKS5iYW5rKCJSb2xhbmRUUjgwOCIpLmdhaW4oLjgp)

Notice Dm's home becomes the *approach* to Gm (D is the 5th of G) — the keys chain in falling
4ths, Module 3.4's strongest root motion, now at the level of whole keys.

### 4.2.2 The full set

The five progressions — spell them yourself before peeking (that spelling *is* the theory):

| Concert key | iiø | V7b9 | i | Tenor home | Alto home |
|---|---|---|---|---|---|
| D minor | Em7b5 | A7b9 | Dm | E minor | B minor |
| G minor | Am7b5 | D7b9 | Gm | A minor | E minor |
| C minor | Dm7b5 | G7b9 | Cm | D minor | A minor |
| F minor | Gm7b5 | C7b9 | Fm | G minor | D minor |
| A minor | Bm7b5 | E7b9 | Am | B minor | F# minor |

The pattern: ii sits on the scale's 2nd degree, V on its 5th — you can *derive* any key's ii-V-i
from the scale itself (3.1's diatonic walk, minor edition).

### Challenges 4.2

1. Extend 4.2.1 to a 20-bar loop visiting all five keys (order them in falling 4ths: D→G→C→F...
   then A is the odd one out — where does it splice in least jarringly?).
2. Halve the harmonic rhythm (`[iiø V]` in one bar, i in the next) for one key — the "quick"
   ii-V. Big-band tango energy.
3. Ear quiz: play your 20-bar loop days later; name the key of each phrase *before* the i lands.

### 🎷 Horn time 4.2

This is the week-long exercise: 4.2.1's two-key loop, then add a key per day. Guide tones only at
first — by day three your fingers know that iiø's 3rd *is* the key's 4th, and V's b9 *is* the
key's b6. (Check those claims on paper — they're true, and they're why the changes feel like one
gesture.) The written keys are in the table; the book rows follow them.

---

## Session 4.3 — The Phrygian cadence: tango's signature

### 4.3.1 bII → V7b9 → i

A chord built a half step *above* home, melting downward. Concert D minor: **Eb^7 → A7b9 → Dm**:

```js
setcpm(66/4)
$: chord("<Eb^7 A7b9 Dm Dm>").voicing().sound("piano")._pianoroll()
$: "<Eb^7 A7b9 Dm Dm>".rootNotes(2).note().struct("x ~ ~ x x ~ x ~").sound("sawtooth").lpf(500)
$: sound("bd@3 bd@1 bd@2 bd@2").bank("RolandTR808").gain(.7)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDY2LzQpCiQ6IGNob3JkKCI8RWJeNyBBN2I5IERtIERtPiIpLnZvaWNpbmcoKS5zb3VuZCgicGlhbm8iKS5fcGlhbm9yb2xsKCkKJDogIjxFYl43IEE3YjkgRG0gRG0%2BIi5yb290Tm90ZXMoMikubm90ZSgpLnN0cnVjdCgieCB%2BIH4geCB4IH4geCB%2BIikuc291bmQoInNhd3Rvb3RoIikubHBmKDUwMCkKJDogc291bmQoImJkQDMgYmRAMSBiZEAyIGJkQDIiKS5iYW5rKCJSb2xhbmRUUjgwOCIpLmdhaW4oLjcp)

Watch the piano roll: the Eb chord's notes are all a breath above Dm's — the resolution is a
*collapse by half steps*, and that chromatic sigh is the most tango sound there is. Your syllabus
calls this the signature resolution; you'll find it in Piazzolla constantly (file that away for
Module 6's Libertango).

### 4.3.2 Why lydian over the bII

The syllabus prescribes **Eb lydian** over that Eb^7. Here's the why, and it's satisfying: Eb
lydian's #4 is **A natural** — the one alteration that makes the bII chord's scale share its most
important note with the home key's V. Eb *major* would carry Ab and fight everything:

```js
setcpm(66/4)
$: n("0 2 4 3 4 ~ 2 0")
   .scale("<Eb4:lydian A3:spanish D4:harmonic:minor D4:harmonic:minor>")
   .sound("piano")
$: chord("<Eb^7 A7b9 Dm Dm>").voicing().struct("x ~ ~ x ~ ~ x ~").sound("piano").gain(.5)
$: "<Eb^7 A7b9 Dm Dm>".rootNotes(2).note().struct("x ~ ~ x x ~ x ~").sound("sawtooth").lpf(500)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDY2LzQpCiQ6IG4oIjAgMiA0IDMgNCB%2BIDIgMCIpCiAgIC5zY2FsZSgiPEViNDpseWRpYW4gQTM6c3BhbmlzaCBENDpoYXJtb25pYzptaW5vciBENDpoYXJtb25pYzptaW5vcj4iKQogICAuc291bmQoInBpYW5vIikKJDogY2hvcmQoIjxFYl43IEE3YjkgRG0gRG0%2BIikudm9pY2luZygpLnN0cnVjdCgieCB%2BIH4geCB%2BIH4geCB%2BIikuc291bmQoInBpYW5vIikuZ2FpbiguNSkKJDogIjxFYl43IEE3YjkgRG0gRG0%2BIi5yb290Tm90ZXMoMikubm90ZSgpLnN0cnVjdCgieCB%2BIH4geCB4IH4geCB%2BIikuc291bmQoInNhd3Rvb3RoIikubHBmKDUwMCk%3D)

Degree `3` in bar 1 *is* that A natural — the melody touches the pivot as the harmony turns.

### Challenges 4.3

1. Break the theory: change bar 1's scale to `Eb4:major` and lean on degree 3 (now Ab). Hear the
   fight, then put lydian back. (Breaking it once is worth ten explanations.)
2. Compress: `"<[Eb^7 A7b9] Dm>"` — the cadence in half the time, twice the drama.
3. Chain 4.1 and 4.3: `iiø → V → i` then `bII → V → i`, eight bars. Two roads to the same home.

### 🎷 Horn time 4.3

Loop 4.3.1. **Tenor: F^7→B7b9→Em; alto: C^7→F#7b9→Bm.** First: roots (hear your own half-step
fall bII→...→i via V). Then 3rds. Then the lydian exercise: on the bII bar, find and *hold* the
written #4 (tenor: B natural over F^7; alto: F# over C^7) — feel it agree with the V chord that
follows. That note is the cadence's hinge.

---

## Session 4.4 — bVI → V → i, and the minor vamp

### 4.4.1 The other half-step cadence

Tango's second classic approach: **bVI^7 → V7b9 → i** — in D minor, **Bb^7 → A7b9 → Dm**. Compare
both cadences back to back, four bars each:

```js
setcpm(66/4)
$: chord("<Eb^7 A7b9 Dm Dm Bb^7 A7b9 Dm Dm>").voicing().sound("piano")._pianoroll()
$: "<Eb^7 A7b9 Dm Dm Bb^7 A7b9 Dm Dm>".rootNotes(2).note().struct("x ~ ~ x x ~ x ~").sound("sawtooth").lpf(500)
$: sound("bd@3 bd@1 bd@2 bd@2").bank("RolandTR808").gain(.7)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDY2LzQpCiQ6IGNob3JkKCI8RWJeNyBBN2I5IERtIERtIEJiXjcgQTdiOSBEbSBEbT4iKS52b2ljaW5nKCkuc291bmQoInBpYW5vIikuX3BpYW5vcm9sbCgpCiQ6ICI8RWJeNyBBN2I5IERtIERtIEJiXjcgQTdiOSBEbSBEbT4iLnJvb3ROb3RlcygyKS5ub3RlKCkuc3RydWN0KCJ4IH4gfiB4IHggfiB4IH4iKS5zb3VuZCgic2F3dG9vdGgiKS5scGYoNTAwKQokOiBzb3VuZCgiYmRAMyBiZEAxIGJkQDIgYmRAMiIpLmJhbmsoIlJvbGFuZFRSODA4IikuZ2FpbiguNyk%3D)

Different geometry: the bII collapses onto home from *above*; the bVI walks its **bass** down by
half step (Bb → A) while sharing most of its notes with D minor (Bb^7 is just the b6 and friends).
bII = exotic arrival; bVI = inevitable descent. Tango uses both, often in the same tune.

### 4.4.2 The i–iv vamp

Between cadences, latin tunes *live* on vamps. i–iv in D minor, dorian on both, two bars each —
plus the arp figure from 3.3 as a montuno seed:

```js
setcpm(96/4)
$: chord("<Dm7 Dm7 Gm7 Gm7>").voicing().arp("0 [2,4] 1 [2,4] 0 [2,4] 1 [2,4]").sound("piano").gain(.6)
$: "<Dm7 Dm7 Gm7 Gm7>".rootNotes(2).note().struct("x ~ ~ x ~ ~ x ~").sound("sawtooth").lpf(500)
$: sound("<[rim ~ ~ rim ~ ~ rim ~] [~ ~ rim ~ rim ~ ~ ~]>").bank("RolandTR808").gain(.8)
$: sound("hh*8").gain("1 .4 .6 .4 .8 .4 .6 .4")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDk2LzQpCiQ6IGNob3JkKCI8RG03IERtNyBHbTcgR203PiIpLnZvaWNpbmcoKS5hcnAoIjAgWzIsNF0gMSBbMiw0XSAwIFsyLDRdIDEgWzIsNF0iKS5zb3VuZCgicGlhbm8iKS5nYWluKC42KQokOiAiPERtNyBEbTcgR203IEdtNz4iLnJvb3ROb3RlcygyKS5ub3RlKCkuc3RydWN0KCJ4IH4gfiB4IH4gfiB4IH4iKS5zb3VuZCgic2F3dG9vdGgiKS5scGYoNTAwKQokOiBzb3VuZCgiPFtyaW0gfiB%2BIHJpbSB%2BIH4gcmltIH5dIFt%2BIH4gcmltIH4gcmltIH4gfiB%2BXT4iKS5iYW5rKCJSb2xhbmRUUjgwOCIpLmdhaW4oLjgpCiQ6IHNvdW5kKCJoaCo4IikuZ2FpbigiMSAuNCAuNiAuNCAuOCAuNCAuNiAuNCIp)

That broken bass-and-chop arp against the clave is the skeleton of a montuno — Module 5 grows it
into the real thing. Melodically the vamp is home turf for everything in Module 2: dorian, minor
pentatonic, blues, all in D (both chords live in one scale family — which one? Answer: D dorian =
G mixolydian's family... work it out).

### Challenges 4.4

1. Build the vamp in G minor and A minor (priority keys — you'll want these ready for Module 5).
2. Write an 8-bar form: 4 vamp bars, then `bVI → V7b9 → i → i`. Vamp-then-cadence is the shape of
   a hundred salsa tunes.
3. In 4.4.1, mute everything but bass. The two cadences reduce to *two bass gestures* — sing them.

### 🎷 Horn time 4.4

The vamp (4.4.2) is your improv playground this week. **Tenor: Em7–Am7 (E dorian). Alto: Bm7–Em7
(B dorian).** Rules of engagement, one pass each: (1) chord tones only, long notes; (2) add
passing tones, but land chord tones on bar lines; (3) blues scale over everything, attitude over
accuracy; (4) two-bar phrases that *breathe* — play bars 1–2, rest bars 3–4. Rule 4 is the hardest
and the most latin.

---

## Session 4.5 — Dominant colors: the tension ladder

One chord — A7, the V of D minor — held as a vamp while the melody climbs your book's Category 2
ladder, two bars per rung:

```js
setcpm(84/4)
$: n("0 1 2 3 4 3 2 1")
   .scale("<A3:mixolydian A3:spanish A3:whole:tone A3:altered>/2")
   .sound("piano")._pianoroll()
$: chord("A7").voicing().struct("x ~ ~ x ~ ~ x ~").sound("piano").gain(.5)
$: note("a1").sound("sawtooth").lpf(450).gain(.4)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDg0LzQpCiQ6IG4oIjAgMSAyIDMgNCAzIDIgMSIpCiAgIC5zY2FsZSgiPEEzOm1peG9seWRpYW4gQTM6c3BhbmlzaCBBMzp3aG9sZTp0b25lIEEzOmFsdGVyZWQ%2BLzIiKQogICAuc291bmQoInBpYW5vIikuX3BpYW5vcm9sbCgpCiQ6IGNob3JkKCJBNyIpLnZvaWNpbmcoKS5zdHJ1Y3QoInggfiB%2BIHggfiB%2BIHggfiIpLnNvdW5kKCJwaWFubyIpLmdhaW4oLjUpCiQ6IG5vdGUoImExIikuc291bmQoInNhd3Rvb3RoIikubHBmKDQ1MCkuZ2FpbiguNCk%3D)

| Rung | Scale | Alterations | Character | Book (Cat. 2) |
|---|---|---|---|---|
| 1 | mixolydian | none | plain, honest | Dominant 7th |
| 2 | spanish | b9, b13 | traditional latin heat | Spanish / Jewish |
| 3 | whole tone | #4, #5 | floating, unresolved | Whole Tone |
| 4 | altered | b9, #9, #4, b13 | modern, maximum burn | Diminished Whole Tone |

Same chord underneath every rung — all the tension is in the *line*. (The book's "Diminished
begin with H" rung exists too: `A3:dominant:diminished`, the b9-with-natural-13 color between
spanish and altered. Add it as rung 2.5 if you're curious.)

### Challenges 4.5

1. Resolution test: extend each rung to resolve — 2 bars of the color, 1 bar of `Dm`, 1 bar rest
   (all layers to 4-entry lists ×4 rungs = 16 bars). Which rung *pulls* hardest into Dm?
2. Reorder the ladder by ear with your eyes closed a day later — can you rank the four by tension
   without the code?
3. The `altered` scale is melodic minor in disguise (built on its 7th degree — A altered = Bb
   melodic minor). Verify: play `A3:altered` against `Bb3:melodic:minor` in alternating bars.
   Modes-as-rotations, one last time.

### 🎷 Horn time 4.5

The A7 vamp loop, ladder on the horn. **Tenor: B7 vamp — B mixolydian → B spanish → B whole tone
→ B altered. Alto: F#7 — same ladder on F#.** All four rows are in your book under the dominant
category in those keys. Two bars each, continuous, then freely mix rungs — reaching for *more*
tension right before you resolve is 90% of sounding like you know something the rhythm section
doesn't.

---

## Session 4.6 — The pentatonic trick

Your LEARNINGS file's party trick, now audible. Over **G7**, play **Ab minor pentatonic** — the
minor pentatonic *a half step above the dominant's root*:

```js
setcpm(80/4)
$: n("0 2 1 3 2 4 3 ~")
   .scale("<Ab3:minor:pentatonic Ab3:minor:pentatonic C4:major:pentatonic C4:major:pentatonic>")
   .sound("piano")._pianoroll()
$: chord("<G7 G7 C^7 C^7>").voicing().struct("x ~ ~ x ~ ~ x ~").sound("piano").gain(.5)
$: "<G7 G7 C^7 C^7>".rootNotes(2).note().sound("sawtooth").lpf(500).gain(.4)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDgwLzQpCiQ6IG4oIjAgMiAxIDMgMiA0IDMgfiIpCiAgIC5zY2FsZSgiPEFiMzptaW5vcjpwZW50YXRvbmljIEFiMzptaW5vcjpwZW50YXRvbmljIEM0Om1ham9yOnBlbnRhdG9uaWMgQzQ6bWFqb3I6cGVudGF0b25pYz4iKQogICAuc291bmQoInBpYW5vIikuX3BpYW5vcm9sbCgpCiQ6IGNob3JkKCI8RzcgRzcgQ143IENeNz4iKS52b2ljaW5nKCkuc3RydWN0KCJ4IH4gfiB4IH4gfiB4IH4iKS5zb3VuZCgicGlhbm8iKS5nYWluKC41KQokOiAiPEc3IEc3IENeNyBDXjc%2BIi5yb290Tm90ZXMoMikubm90ZSgpLnNvdW5kKCJzYXd0b290aCIpLmxwZig1MDApLmdhaW4oLjQp)

Two bars *outside*, two bars *home* — maximum contrast. Why five "wrong" notes all work:

| Ab min pent note | Against G7 | Color |
|---|---|---|
| Ab | b9 | the Spanish note |
| Cb (B) | 3 | chord tone! the anchor |
| Db | b5/#4 | lydian-dominant bite |
| Eb | b13/#5 | whole-tone float |
| Gb (F#... enharm. F) | ~b7 | the dominant's core |

Every note is an altered-dominant color, and one (the 3rd) is a plain chord tone holding the
whole thing to the ground. You get the entire 4.5 ladder's spice from *one pentatonic you already
know* — which is why this is the highest-value cheap trick in jazz education.

**The rule: over any V7, minor pentatonic up a half step.** Then resolve *inside* (here: C major
pentatonic — note how bar 3 feels like sunrise).

### Challenges 4.6

1. Apply it to the module's home key: over `A7b9 → Dm`, that's **Bb minor pentatonic** → D minor
   pentatonic. Rebuild 4.1.1 with this melody scheme.
2. Which of the five Ab-pent notes sounds *most* outside to you? Look it up in the table — you've
   just learned your own tension tolerance.
3. Alternate bars: mixolydian bar / half-step-up-pent bar over a static G7. In-out-in-out is a
   whole improv style (file under "Michael Brecker").

### 🎷 Horn time 4.6

Loop 4.6's track. **Tenor: over written A7, play Bb minor pentatonic → resolve with D major
pentatonic. Alto: over E7, F minor pentatonic → A major pentatonic.** You already have all these
pentatonics under your fingers from Module 2 — this session is purely a *permission slip*: play
the "wrong" pentatonic on purpose, land the resolution, grin.

---

## 🏁 Module 4 Milestone — the 16-bar tango

Build the full form in concert D minor, every layer a locked 16-entry list. The architecture:

| Bars | Chords | The move | Solo scales |
|---|---|---|---|
| 1–4 | `Dm · [Em7b5 A7b9] · Dm · Dm` | home + quick ii-V | D harmonic minor (spanish over the V) |
| 5–8 | `Gm7 · C7 · F^7 · Bb^7` | escape to the relative major, falling 4ths | all one family — F major / D natural minor |
| 9–12 | `Eb^7 · Eb^7 · [Em7b5 A7b9] · Dm` | **the Phrygian cadence**, stretched | Eb lydian → locrian #2 / spanish → harm. minor |
| 13–16 | `Bb^7 · A7b9 · Dm · [Dm A7b9]` | bVI → V → i, turnaround | Bb lydian → spanish → harm. minor |

Requirements: habanera bass (`rootNotes`), comping voicings (marcato on 13–16 — heavy, even),
a drum layer that *thins out* in bars 5–8 (the major-key window should feel like air), and
`._pianoroll()` on the harmony while you build. Then transpose the entire form to **A minor** by
re-spelling the lists (challenge: it's 16 chords, but only ~7 distinct spellings).

<details><summary>My version — compare, don't copy</summary>

```js
setcpm(63/4)
$: chord("<Dm [Em7b5 A7b9] Dm Dm Gm7 C7 F^7 Bb^7 Eb^7 Eb^7 [Em7b5 A7b9] Dm Bb^7 A7b9 Dm [Dm A7b9]>")
   .voicing().struct("~ x ~ x ~ x ~ ~").sound("piano").gain(.55)._pianoroll()
$: "<Dm [Em7b5 A7b9] Dm Dm Gm7 C7 F^7 Bb^7 Eb^7 Eb^7 [Em7b5 A7b9] Dm Bb^7 A7b9 Dm [Dm A7b9]>"
   .rootNotes(2).note().struct("x ~ ~ x x ~ x ~").sound("sawtooth").lpf(500)
$: sound("bd@3 bd@1 bd@2 bd@2, hh*8").gain("<.8 .8 .8 .8 .5 .5 .5 .5 .8 .8 .8 .8 .9 .9 .9 .9>")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDYzLzQpCiQ6IGNob3JkKCI8RG0gW0VtN2I1IEE3YjldIERtIERtIEdtNyBDNyBGXjcgQmJeNyBFYl43IEViXjcgW0VtN2I1IEE3YjldIERtIEJiXjcgQTdiOSBEbSBbRG0gQTdiOV0%2BIikKICAgLnZvaWNpbmcoKS5zdHJ1Y3QoIn4geCB%2BIHggfiB4IH4gfiIpLnNvdW5kKCJwaWFubyIpLmdhaW4oLjU1KS5fcGlhbm9yb2xsKCkKJDogIjxEbSBbRW03YjUgQTdiOV0gRG0gRG0gR203IEM3IEZeNyBCYl43IEViXjcgRWJeNyBbRW03YjUgQTdiOV0gRG0gQmJeNyBBN2I5IERtIFtEbSBBN2I5XT4iCiAgIC5yb290Tm90ZXMoMikubm90ZSgpLnN0cnVjdCgieCB%2BIH4geCB4IH4geCB%2BIikuc291bmQoInNhd3Rvb3RoIikubHBmKDUwMCkKJDogc291bmQoImJkQDMgYmRAMSBiZEAyIGJkQDIsIGhoKjgiKS5nYWluKCI8LjggLjggLjggLjggLjUgLjUgLjUgLjUgLjggLjggLjggLjggLjkgLjkgLjkgLjk%2BIik%3D)

(The gain list is doing the bars-5–8 thinning; a cleaner way with `.arrange()` arrives in
Module 5. If a bar sounds wrong while you build — check your three lists are still exactly 16
entries. Locked lengths are the whole game.)

</details>

**Milestone horn exercise:** this is your tune for the next two weeks. **Tenor: E minor form
(Em, F#ø-B7b9, Am7-D7-G^7-C^7, F^7...). Alto: B minor form.** Learn it in three passes: (1) roots
with the bass, whole form; (2) guide tones, whole form; (3) solo — using the table's scale plan,
with one non-negotiable: *land the half-step resolutions* (bars 9→12's Eb→D world, and 14→15's
A7b9→Dm). Record pass 3. When your line makes the form audible without the backing track, Module
5 will make the backing track worthy of the line.

---

## New tools in this module

| Tool / idea | Meaning | Example |
|---|---|---|
| locked `< >` lists | all layers change together | 4-entry chords + 4-entry scales |
| `[X Y]` inside `< >` | two chords in one bar | `"<[Em7b5 A7b9] Dm>"` |
| minor ii-V-i | iiø → V7b9 → i | `Em7b5 A7b9 Dm` |
| spanish = 5th mode of harm. minor | V-scale *is* the i-scale, recentered | `A3:spanish` ≡ `D:harmonic:minor` |
| Phrygian cadence | bII^7 → V7b9 → i, lydian on the bII | `Eb^7 A7b9 Dm` |
| bVI cadence | bVI^7 → V7b9 → i, bass falls by half step | `Bb^7 A7b9 Dm` |
| tension ladder | mixolydian → spanish → whole tone → altered | `.scale("<...>/2")` |
| pentatonic trick | over V7: minor pent a half step up | Ab min pent over G7 |

**Theory vocabulary:** harmonic function (lean / demand / arrive); priority keys and falling-4th
key chains; half-step cadences from above (bII) and in the bass (bVI); harmonic rhythm (quick
ii-Vs); tension as a ladder; superimposition.

→ **Next: Module 5 — Groove Engineering** *(coming soon)*
