# Module 1 — First Loops: Rhythm Before Notes

No pitches in this module — every bit of attention goes to *time*. By the end you'll have coded a
four-layer latin percussion groove from scratch, and you'll know the mini-notation that everything
else in this workbook builds on.

**How to work:** open [strudel.cc](https://strudel.cc) in a browser tab. **Type every snippet
yourself** — the ▶ links are for checking your result against mine, not a substitute for typing.
- `Ctrl+Enter` — evaluate / update the pattern (do this after every change, the loop updates live)
- `Ctrl+.` — stop

> **When something errors:** Strudel shows the error inline. The two you'll hit most: a typo in a
> sound name (it tells you the name wasn't found — check spelling), and unbalanced brackets. The
> loop keeps playing the last working version while you fix it.

**Tempo convention for the whole workbook:** one cycle = one bar of 4/4. Strudel counts in
*cycles per minute*, so we write `setcpm(90/4)` for 90 bpm — 90 beats, 4 to a bar. Keep this line
at the top of everything you write.

---

## Session 1.1 — The REPL & mini-notation

### 1.1.1 First sound

Type this and hit `Ctrl+Enter`:

```js
setcpm(90/4)
sound("bd sd bd sd")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCnNvdW5kKCJiZCBzZCBiZCBzZCIp)

`bd` is a bass drum, `sd` a snare. The quoted string is **mini-notation**, and here is the single
most important idea in Strudel:

> **Mini-notation divides time.** The events in a sequence split the cycle *equally*. Four events =
> four quarter notes. Three events = triplets. You don't write durations; you write divisions.

This is the opposite of sheet music, where each note carries its own duration. Internalizing this
takes about ten minutes of playing — so play: change `90` to `140`, remove one `sd`, add another
`bd`. Notice how three events give you a bar of even triplets for free.

### 1.1.2 Rests: `~`

A `~` is silence, but it still occupies its slot in the division:

```js
setcpm(90/4)
sound("bd ~ sd ~")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCnNvdW5kKCJiZCB%2BIHNkIH4iKQ%3D%3D)

Kick on 1, snare on 3. Now the reveal — compare with `sound("bd sd")`. **They sound identical.**
Two events split the bar in half; four slots where 2 and 4 are silent produce the same two onsets.
Same music, different resolution. You choose the grid that makes the *rhythm you're thinking of*
easy to write.

### 1.1.3 Subdivision: `[ ]`

Square brackets group events into one slot — division *within* a division:

```js
setcpm(90/4)
sound("bd [hh hh] sd [hh hh]")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCnNvdW5kKCJiZCBbaGggaGhdIHNkIFtoaCBoaF0iKQ%3D%3D)

Four slots (quarter notes); slots 2 and 4 each hold two eighth notes. Brackets nest:
`[hh [hh hh]]` puts an eighth plus two sixteenths in one beat.

### 1.1.4 Repetition: `*`

`*n` squeezes n repeats into one slot. These two lines are the same:

```js
setcpm(90/4)
sound("hh hh hh hh hh hh hh hh")
```

```js
setcpm(90/4)
sound("hh*8")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCnNvdW5kKCJoaCo4Iik%3D)

Straight eighth-note hats. `bd*4` is four-on-the-floor. `[hh hh]*2` works too — `*` applies to
groups.

### Challenges 1.1

1. Write the *We Will Rock You* stomp-stomp-clap: kick, kick, clap, rest (sound: `cp`).
2. One bar: kick on every beat, but sixteenth-note hats **only on beat 4**.
3. Explain (out loud, to the room) why `"bd sd"` and `"bd ~ sd ~"` sound the same, then write a
   *third* string that also sounds the same.

<details><summary>Solutions</summary>

```js
setcpm(90/4)
sound("bd bd cp ~")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCnNvdW5kKCJiZCBiZCBjcCB%2BIik%3D)

```js
setcpm(90/4)
sound("bd bd bd [bd,hh*4]")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCnNvdW5kKCJiZCBiZCBiZCBbYmQsaGgqNF0iKQ%3D%3D)

(That comma is a sneak preview of Session 1.2 — it layers the kick and the hats *inside* beat 4.
If you solved it with two separate `$:` lines — `bd*4` plus `~ ~ ~ hh*4` — also correct.)

3: Both put onsets at 0 and ½ of the cycle; the grid resolution differs but the onsets don't.
A third spelling: `"bd ~ ~ ~ sd ~ ~ ~"` — or `"bd*1 sd*1"`.

</details>

### 🎷 Horn time 1.1

Loop `setcpm(60/4)` + `sound("bd hh hh hh")` as your metronome-with-a-downbeat. Long tones:
breathe during beat 4, land **exactly** on the `bd`. One note per bar, chromatic walk from low
written C upward. The point: your entrance is a rhythmic event — place it like you'd place a note
in mini-notation, slot 1 of 4.

---

## Session 1.2 — Tresillo & clave

### 1.2.1 Layers: `,` and `$:`

Two ways to stack patterns. A comma layers sequences *inside one string*:

```js
setcpm(90/4)
sound("bd*4, hh*8")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCnNvdW5kKCJiZCo0LCBoaCo4Iik%3D)

And `$:` lines run as separate simultaneous patterns — this is how we'll build multi-part grooves:

```js
setcpm(90/4)
$: sound("bd*4")
$: sound("hh*8").bank("RolandTR808")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCiQ6IHNvdW5kKCJiZCo0IikKJDogc291bmQoImhoKjgiKS5iYW5rKCJSb2xhbmRUUjgwOCIp)

Two useful extras: `.bank("RolandTR808")` (or `"RolandTR909"`) swaps the drum samples — same
pattern, different kit. And prefixing a line with an underscore (`_$:`) **mutes** it without
deleting it — you'll use that constantly when building layer by layer.

### 1.2.2 The tresillo — 3+3+2

The fundamental Afro-Cuban cell. On an eighth-note grid, hits on **1, the and-of-2, and 4**:

```js
setcpm(90/4)
$: sound("bd ~ ~ bd ~ ~ bd ~")
$: sound("hh*8").gain(.5)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCiQ6IHNvdW5kKCJiZCB%2BIH4gYmQgfiB%2BIGJkIH4iKQokOiBzb3VuZCgiaGgqOCIpLmdhaW4oLjUp)

Count it against the hats: **ONE**-and-two-**AND**-three-**FOUR**-and. Three, three, two.

Mini-notation has a more honest spelling of the same rhythm — `@` stretches an event's share of
the bar:

```js
setcpm(90/4)
sound("bd@3 bd@3 bd@2")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCnNvdW5kKCJiZEAzIGJkQDMgYmRAMiIp)

Three eighths + three eighths + two eighths. Identical sound; the code now *says* 3+3+2. Keep both
spellings — the grid version is easier to edit, the `@` version easier to read.

### 1.2.3 Son clave — the two-bar key

Clave is a **two-bar** pattern; our cycles are one bar, so we need `< >`, which alternates its
contents one per cycle. Son clave **3-2**:

```js
setcpm(90/4)
$: sound("<[rim ~ ~ rim ~ ~ rim ~] [~ ~ rim ~ rim ~ ~ ~]>").bank("RolandTR808")
$: sound("hh*8").gain(.4)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCiQ6IHNvdW5kKCI8W3JpbSB%2BIH4gcmltIH4gfiByaW0gfl0gW34gfiByaW0gfiByaW0gfiB%2BIH5dPiIpLmJhbmsoIlJvbGFuZFRSODA4IikKJDogc291bmQoImhoKjgiKS5nYWluKC40KQ%3D%3D)

Bar 1 (the **3-side**) is *exactly the tresillo* — that's not a coincidence, it's the genetic link.
Bar 2 (the **2-side**) answers on beats 2 and 3. Count until you can sing it:
`ONE-and-two-AND-three-FOUR-and | one-and-TWO-and-THREE-and-four-and`.

**2-3 clave** is the same pattern with the bars swapped — swap the two bracket groups. Everything
in latin music is phrased *relative to which side of the clave you're on*; feeling that difference
is the actual skill, and it starts here.

### Challenges 1.2

1. Write **2-3 son clave** (don't peek at 3-2 — reconstruct it).
2. **Rumba clave 3-2:** the 3-side's last hit moves from beat 4 to the *and* of 4. One character
   moves.
3. Stack 3-2 clave + tresillo kick + hats, then use `_$:` to mute the clave line and check the
   tresillo still feels right alone.

<details><summary>Solutions</summary>

```js
setcpm(90/4)
sound("<[~ ~ rim ~ rim ~ ~ ~] [rim ~ ~ rim ~ ~ rim ~]>").bank("RolandTR808")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCnNvdW5kKCI8W34gfiByaW0gfiByaW0gfiB%2BIH5dIFtyaW0gfiB%2BIHJpbSB%2BIH4gcmltIH5dPiIpLmJhbmsoIlJvbGFuZFRSODA4Iik%3D)

```js
setcpm(90/4)
sound("<[rim ~ ~ rim ~ ~ ~ rim] [~ ~ rim ~ rim ~ ~ ~]>").bank("RolandTR808")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCnNvdW5kKCI8W3JpbSB%2BIH4gcmltIH4gfiB%2BIHJpbV0gW34gfiByaW0gfiByaW0gfiB%2BIH5dPiIpLmJhbmsoIlJvbGFuZFRSODA4Iik%3D)

```js
setcpm(90/4)
$: sound("<[rim ~ ~ rim ~ ~ rim ~] [~ ~ rim ~ rim ~ ~ ~]>").bank("RolandTR808")
$: sound("bd@3 bd@3 bd@2").bank("RolandTR808")
$: sound("hh*8").gain(.4)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCiQ6IHNvdW5kKCI8W3JpbSB%2BIH4gcmltIH4gfiByaW0gfl0gW34gfiByaW0gfiByaW0gfiB%2BIH5dPiIpLmJhbmsoIlJvbGFuZFRSODA4IikKJDogc291bmQoImJkQDMgYmRAMyBiZEAyIikuYmFuaygiUm9sYW5kVFI4MDgiKQokOiBzb3VuZCgiaGgqOCIpLmdhaW4oLjQp)

</details>

### 🎷 Horn time 1.2

Loop the tresillo kick + hats (challenge 3, clave muted). Play the **clave rhythm on one note** —
concert Bb: that's written **C** on tenor, written **G** on alto. Two bars clave rhythm, two bars
rest, repeat. Then trade jobs: loop the clave, *play* the tresillo. When both feel easy, try
starting your phrase on the 2-side. This is the rhythmic vocabulary every montuno phrase in
Module 5 will assume.

---

## Session 1.3 — Habanera, accents & euclidean rhythms

### 1.3.1 The habanera — tango's heartbeat

Take the tresillo and add a hit on beat 3: **1, and-of-2, 3, 4**. That's the habanera:

```js
setcpm(80/4)
$: sound("bd ~ ~ bd bd ~ bd ~")
$: sound("hh*8").gain(.4)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDgwLzQpCiQ6IHNvdW5kKCJiZCB%2BIH4gYmQgYmQgfiBiZCB%2BIikKJDogc291bmQoImhoKjgiKS5nYWluKC40KQ%3D%3D)

Or in duration spelling: `"bd@3 bd@1 bd@2 bd@2"` — dotted-quarter, eighth, quarter, quarter. Slow
it down (`setcpm(66/4)`) and it's unmistakably tango. This rhythm carries the whole of Module 5's
tango work; the 3-3-2 grouping inside it is the same DNA as the tresillo.

### 1.3.2 Accents: `.gain()` with a pattern

`.gain()` accepts a *pattern* too, so accents are just another sequence, aligned slot-for-slot:

```js
setcpm(90/4)
sound("hh*8").gain("1 .4 .6 .4 .8 .4 .6 .4")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCnNvdW5kKCJoaCo4IikuZ2FpbigiMSAuNCAuNiAuNCAuOCAuNCAuNiAuNCIp)

Same onsets, completely different feel — the accent shape *is* the groove. Two tango feels, same
four quarter notes:

```js
setcpm(66/4)
sound("bd*4").gain(".9 .8 .9 .8")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDY2LzQpCnNvdW5kKCJiZCo0IikuZ2FpbigiLjkgLjggLjkgLjgiKQ%3D%3D)

That heavy, even tread is **marcato**. Now shift the weight onto the habanera onsets instead —
accents off the beat, pushing forward — and you're in **sincopa** territory:

```js
setcpm(66/4)
sound("bd*8").gain(".9 .2 .2 .7 .8 .2 .7 .2")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDY2LzQpCnNvdW5kKCJiZCo4IikuZ2FpbigiLjkgLjIgLjIgLjcgLjggLjIgLjcgLjIiKQ%3D%3D)

Marcato vs sincopa is *the* expressive axis in tango accompaniment. Notice you never changed
*what* plays — only how hard.

### 1.3.3 Euclidean rhythms: `(k,n)`

`sound("hh(3,8)")` means: distribute 3 hits as evenly as possible over 8 slots.

```js
setcpm(90/4)
$: sound("bd(3,8)")
$: sound("hh*8").gain(.4)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCiQ6IHNvdW5kKCJiZCgzLDgpIikKJDogc291bmQoImhoKjgiKS5nYWluKC40KQ%3D%3D)

Recognize it? **`(3,8)` is the tresillo.** The pattern you built by hand is what even-distribution
mathematics produces on its own — which is precisely why it shows up in music worldwide. And
`(5,8)`:

```js
setcpm(90/4)
$: sound("cb(5,8)").bank("RolandTR808").gain(.6)
$: sound("hh*8").gain(.4)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCiQ6IHNvdW5kKCJjYig1LDgpIikuYmFuaygiUm9sYW5kVFI4MDgiKS5nYWluKC42KQokOiBzb3VuZCgiaGgqOCIpLmdhaW4oLjQp)

That's the **cinquillo** — the tresillo's ornamented sibling, the lead rhythm of danzón and early
tango. Tresillo ⊂ habanera ⊂ cinquillo: one family, increasingly decorated, and mini-notation lets
you *see* the family resemblance.

### Challenges 1.3

1. Play tresillo `(3,8)` and cinquillo `(5,8)` simultaneously on different sounds. Which hits do
   they share? (Work it out by ear first, then on paper.)
2. Take the marcato bar and turn beat 4 into two eighth notes without losing the heavy feel.
3. Try `(3,8)`, `(5,8)`, `(7,16)`, `(5,16)` on `mt` (mid tom). Which one is the son clave 3-side?
   Which could pass as a bossa pattern?

<details><summary>Solutions</summary>

```js
setcpm(90/4)
$: sound("bd(3,8)")
$: sound("cb(5,8)").bank("RolandTR808").gain(.6)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDkwLzQpCiQ6IHNvdW5kKCJiZCgzLDgpIikKJDogc291bmQoImNiKDUsOCkiKS5iYW5rKCJSb2xhbmRUUjgwOCIpLmdhaW4oLjYp)

1: They share 1, the and-of-2, and beat 4 — the cinquillo adds beat 2 and the and-of-3. The
tresillo is *inside* the cinquillo.

```js
setcpm(66/4)
sound("bd bd bd [bd bd]").gain(".9 .8 .9 .8")
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDY2LzQpCnNvdW5kKCJiZCBiZCBiZCBbYmQgYmRdIikuZ2FpbigiLjkgLjggLjkgLjgiKQ%3D%3D)

3: `(3,8)` is the 3-side. `(5,16)` = `x..x..x..x..x...` — squint and it's cousin to the bossa
feel. `(7,16)` is a busy samba-ish carpet.

</details>

### 🎷 Horn time 1.3

Loop the habanera at 66 bpm. On one note (concert Bb again), play: bar 1 marcato quarters, bar 2
the habanera rhythm itself, bar 3 sincopa (avoid beat 1 entirely — start on the and-of-1), bar 4
rest. The rest bar matters: space is a rhythmic choice too.

---

## 🏁 Module 1 Milestone — the four-layer groove

Build this from scratch, layer by layer, using `_$:` to mute while you work. Requirements:

1. **Clave** — son 3-2, on `rim`, 808 kit
2. **Tresillo kick** — use the `@` spelling
3. **Eighth-note pulse** — hats with an accent shape (strong 1, lighter offbeats)
4. **Cinquillo color layer** — euclidean, quiet, on cowbell or tom

Then live-edit without stopping: flip the clave to 2-3 (does the groove change character?), mute
layers 2 and 4 to hear the skeleton, push the tempo from 90 to 110.

<details><summary>My version — compare, don't copy</summary>

```js
setcpm(96/4)
$: sound("<[rim ~ ~ rim ~ ~ rim ~] [~ ~ rim ~ rim ~ ~ ~]>").bank("RolandTR808").gain(.9)
$: sound("bd@3 bd@3 bd@2").bank("RolandTR808")
$: sound("hh*8").gain("1 .4 .6 .4 .8 .4 .6 .4")
$: sound("cb(5,8)").bank("RolandTR808").gain(.35)
```
[▶ Open in Strudel](https://strudel.cc/#c2V0Y3BtKDk2LzQpCiQ6IHNvdW5kKCI8W3JpbSB%2BIH4gcmltIH4gfiByaW0gfl0gW34gfiByaW0gfiByaW0gfiB%2BIH5dPiIpLmJhbmsoIlJvbGFuZFRSODA4IikuZ2FpbiguOSkKJDogc291bmQoImJkQDMgYmRAMyBiZEAyIikuYmFuaygiUm9sYW5kVFI4MDgiKQokOiBzb3VuZCgiaGgqOCIpLmdhaW4oIjEgLjQgLjYgLjQgLjggLjQgLjYgLjQiKQokOiBzb3VuZCgiY2IoNSw4KSIpLmJhbmsoIlJvbGFuZFRSODA4IikuZ2FpbiguMzUp)

</details>

**Milestone horn exercise:** loop your groove, two bars on / two bars off on one note. During the
"on" bars, phrase *with* the clave side you're on: busy on the 3-side, answering on the 2-side.
When that's comfortable, you're done with Module 1 — Module 2 gives you actual notes.

---

## Mini-notation learned in this module

| Syntax | Meaning | Example |
|---|---|---|
| `"a b c"` | sequence — events divide the cycle equally | `sound("bd sd")` |
| `~` | rest (occupies a slot) | `"bd ~ sd ~"` |
| `[ ]` | subdivide one slot | `"bd [hh hh]"` |
| `*n` | repeat n× inside one slot | `"hh*8"` |
| `@n` | stretch event to n shares | `"bd@3 bd@3 bd@2"` |
| `< >` | alternate per cycle (multi-bar patterns) | `"<[bar1] [bar2]>"` |
| `,` | layer inside one string | `"bd*4, hh*8"` |
| `(k,n)` | euclidean: k hits over n slots | `"bd(3,8)"` |
| `$:` / `_$:` | parallel pattern / muted pattern | `$: sound("bd*4")` |
| `.bank()` | choose drum machine | `.bank("RolandTR808")` |
| `.gain()` | volume — takes patterns → accents | `.gain("1 .5 .7 .5")` |
| `setcpm(bpm/4)` | tempo, one cycle = one 4/4 bar | `setcpm(90/4)` |

**Rhythm vocabulary:** tresillo (3+3+2) → habanera (+beat 3) → cinquillo (ornamented); son clave
3-2/2-3 (tresillo is its 3-side); rumba clave; marcato vs sincopa; euclidean rhythms as
even-distribution.

→ **Next: [Module 2 — Scale Lab](module-2-scale-lab.md)** *(coming soon)*
