\version "2.24.4"

\header {
  title = "Latin Jazz & Tango"
  subtitle = "Riffs, Licks & Melodic Patterns"
  subsubtitle = "For Alto & Tenor Saxophone — Transpose to all 12 keys"
  tagline = "Companion to the Latin Jazz & Tango Improvisation Syllabus"
}

\paper {
  #(set-paper-size "letter")
  top-margin = 12\mm
  bottom-margin = 12\mm
  left-margin = 14\mm
  right-margin = 14\mm
  indent = 0\mm
  system-system-spacing.basic-distance = #14
  markup-system-spacing.basic-distance = #10
  score-markup-spacing.basic-distance = #12
}

% ════════════════════════════════════════════════════════
% 1. LATIN JAZZ RIFFS — Over Minor Vamps (D Dorian)
% ════════════════════════════════════════════════════════

\markup \column {
  \vspace #0.5
  \override #'(font-size . 5) \bold "1. Latin Jazz Riffs — Minor Vamps"
  \vspace #0.2
  \italic "D Dorian (concert F for alto, C for tenor). Play over Dm7 montuno groove with clave."
  \vspace #0.5
}

\markup \bold "1a. Pentatonic Call"
\relative c' {
  \time 4/4
  \tempo "Latin groove" 4 = 110
  d8 f g a c d4.
  \bar "|."
}

\markup \bold "1b. Falling Answer"
\relative c'' {
  \time 4/4
  c8 a g f d2
  \bar "|."
}

\markup \bold "1c. The Montuno Riff"
\relative c' {
  \time 4/4
  d8 f a4 c8 a f4
  \bar "|."
}

\markup \bold "1d. Root-5th Anchor (marcato)"
\relative c' {
  \time 4/4
  d4-^ r a'-^ r | d-^ r a d,
  \bar "|."
}

\markup \bold "1e. Dorian Signature (1-2-b3-5-4-2-1)"
\relative c' {
  \time 4/4
  d8 e f a g e d4
  \bar "|."
}

\markup \bold "1f. Blue Note Dip (with b5 passing tone)"
\relative c' {
  \time 4/4
  d8 f g gis a c d4
  \bar "|."
}

\markup \bold "1g. Clave Melody (notes on clave hits only)"
\relative c' {
  \time 4/4
  d4. f4. a4 | r4 r8 g4. d4
  \bar "|."
}

\markup \bold "1h. Syncopated 3rds (upbeat pairs)"
\relative c' {
  \time 4/4
  r8 d f r r e g r | r f a r r g bes r
  \bar "|."
}


% ════════════════════════════════════════════════════════
% 2. ii-V-i LICKS (Dm7 — G7b9 — Cm)
% ════════════════════════════════════════════════════════

\markup \column {
  \vspace #1
  \override #'(font-size . 5) \bold "2. ii-V-i Licks"
  \vspace #0.2
  \italic "Dm7 — G7b9 — Cm. The core Latin jazz progression. Transpose to all 12 minor keys."
  \vspace #0.5
}

\markup \bold "2a. Smooth Dorian-Spanish"
\relative c' {
  \time 4/4
  \tempo "Medium Latin" 4 = 100
  d8^\markup{\small "Dm7"} e f g
  aes^\markup{\small "G7b9"} b d f |
  ees4^\markup{\small "Cm"} d c2
  \bar "|."
}

\markup \bold "2b. Bebop Connector"
\relative c'' {
  \time 4/4
  a8^\markup{\small "Dm7"} g f e
  f^\markup{\small "G7b9"} aes b d |
  ees4^\markup{\small "Cm"} c2.
  \bar "|."
}

\markup \bold "2c. Enclosure Lick"
\relative c' {
  \time 4/4
  e8^\markup{\small "Dm7"} d f e
  aes^\markup{\small "G7b9"} g b aes |
  g8^\markup{\small "Cm"} ees d c4. r4
  \bar "|."
}

\markup \bold "2d. Arpeggio + Scale Fill"
\relative c' {
  \time 4/4
  d8^\markup{\small "Dm7"} f a c
  b^\markup{\small "G7b9"} d f aes, |
  g8^\markup{\small "Cm"} ees d c4. r4
  \bar "|."
}

\markup \bold "2e. Altered Tension (max tension on V)"
\relative c' {
  \time 4/4
  d8^\markup{\small "Dm7"} f g a
  aes^\markup{\small "G7alt"} bes des e |
  ees4^\markup{\small "Cm"} d c2
  \bar "|."
}

\markup \bold "2f. Pentatonic Shift (Dm pent → Db pent → Cm)"
\relative c' {
  \time 4/4
  d8^\markup{\small "Dm7"} f g a c
  des^\markup{\small "G7 (Db pent)"} aes ges |
  c,2^\markup{\small "Cm"} ees4 g
  \bar "|."
}

\markup \bold "2g. Chromatic Approach (half steps into resolution)"
\relative c'' {
  \time 4/4
  a8^\markup{\small "Dm7"} g f e
  ees^\markup{\small "G7b9"} d des c |
  b c4.^\markup{\small "Cm"} r2
  \bar "|."
}

\markup \bold "2h. Spanish Signature (full Spanish run on V)"
\relative c' {
  \time 4/4
  d8^\markup{\small "Dm7"} e f g
  g^\markup{\small "G7b9 Spanish"} aes b c |
  d ees f ees
  d4^\markup{\small "Cm"} c |
  c1
  \bar "|."
}


% ════════════════════════════════════════════════════════
% 3. DOMINANT FLAVOR COMPARISON (all over G7)
% ════════════════════════════════════════════════════════

\markup \column {
  \vspace #1
  \override #'(font-size . 5) \bold "3. Dominant 7th — 8 Flavors of G7"
  \vspace #0.2
  \italic "Same chord, 8 different scale colors. Play each, hear the difference."
  \vspace #0.5
}

\markup \bold "3a. Mixolydian (vanilla)"
\relative c' {
  \time 4/4
  g'8 a b d c b a g
  \bar "|."
}

\markup \bold "3b. Spanish / Jewish (salsa fire)"
\relative c' {
  \time 4/4
  g'8 aes b c d ees f g
  \bar "|."
}

\markup \bold "3c. Bebop Dominant (smooth 8th notes)"
\relative c' {
  \time 4/4
  g'8 a b c d e f fis
  \bar "|."
}

\markup \bold "3d. Diminished H-W (angular, symmetric)"
\relative c' {
  \time 4/4
  g'8 aes ais b cis d e f
  \bar "|."
}

\markup \bold "3e. Altered (maximum heat)"
\relative c' {
  \time 4/4
  g'8 aes bes b des ees f4
  \bar "|."
}

\markup \bold "3f. Whole Tone (floating, dreamy)"
\relative c' {
  \time 4/4
  g'8 a b cis dis f4.
  \bar "|."
}

\markup \bold "3g. Blues (earthy, soulful)"
\relative c' {
  \time 4/4
  g'8 bes c cis d4 f8 d
  \bar "|."
}

\markup \bold "3h. Lydian Dominant (bright, non-resolving)"
\relative c' {
  \time 4/4
  g'8 a b cis d e f4
  \bar "|."
}


% ════════════════════════════════════════════════════════
% 4. PENTATONIC TRICKS (D minor pentatonic)
% ════════════════════════════════════════════════════════

\markup \column {
  \vspace #1
  \override #'(font-size . 5) \bold "4. Pentatonic Tricks"
  \vspace #0.2
  \italic "D minor pentatonic (D F G A C). Simple but powerful patterns."
  \vspace #0.5
}

\markup \bold "4a. Ascending 4ths"
\relative c' {
  \time 4/4
  d8 g f a g c a d
  \bar "|."
}

\markup \bold "4b. Falling 3rds"
\relative c'' {
  \time 4/4
  a8 f g d f c d4
  \bar "|."
}

\markup \bold "4c. 3-Note Cells (shifting up)"
\relative c' {
  \time 4/4
  d8 f g f g a g a | c a c d4. r4
  \bar "|."
}

\markup \bold "4d. Call & Response (leave space!)"
\relative c' {
  \time 4/4
  d8 f g a4. r4 | c8 a g f4. r4
  \bar "|."
}

\markup \bold "4e. Octave Displacement (dramatic jumps)"
\relative c {
  \time 4/4
  d8 f' g, a' c, d'4 r8
  \bar "|."
}

\markup \bold "4f. Clave Pentatonic"
\relative c' {
  \time 4/4
  d4. f4. g4 | r4 r8 a4. c4
  \bar "|."
}

\markup \bold "4g. Ab min pent over G7 (b9, 3, b5, b13, b7 of G7)"
\relative c'' {
  \time 4/4
  aes8^\markup{\small "Ab min pent over G7"} ces des ees ges aes
  g4^\markup{\small "resolve"}
  \bar "|."
}

% ════════════════════════════════════════════════════════
% 5. TANGO MELODIC PATTERNS (A harmonic minor)
% ════════════════════════════════════════════════════════

\markup \column {
  \vspace #1
  \override #'(font-size . 5) \bold "5. Tango Melodic Patterns"
  \vspace #0.2
  \italic "A harmonic minor (concert C for alto, G for tenor). Use 3-3-2 feel."
  \vspace #0.5
}

\markup \bold "5a. The Tango Sigh (upper neighbor, fall back)"
\relative c'' {
  \time 4/4
  \tempo "Tango" 4 = 90
  b8 c b4 a8 gis a4
  \bar "|."
}

\markup \bold "5b. Dramatic Leap + Stepwise Descent"
\relative c, {
  \time 4/4
  a'4 f'2. | e8 d c b a4 r4
  \bar "|."
}

\markup \bold "5c. Augmented 2nd Cry (F–G#–A = tango DNA)"
\relative c' {
  \time 4/4
  e4 f8 gis a2 | gis8 f e2.
  \bar "|."
}

\markup \bold "5d. Chromatic Approach (from half step below each note)"
\relative c {
  \time 4/4
  gis8 a bis c dis e | f gis a2
  \bar "|."
}

\markup \bold "5e. Phrygian Cadence Lick (bII → V → i)"
\relative c'' {
  \time 4/4
  bes8^\markup{\small "bII"} a gis a4.
  f8^\markup{\small "V"} e | dis e2.^\markup{\small "i"}
  \bar "|."
}

\markup \bold "5f. Bandoneon Imitation (descending arpeggio, staccato)"
\relative c''' {
  \time 4/4
  a8-. e-. c-. a-. e-. c-. a4-.
  \bar "|."
}

\markup \bold "5g. 3-3-2 Harmonic Minor Grouping"
\relative c'' {
  \time 4/4
  a8[ b c] d[ e f] gis4 a
  \bar "|."
}

\markup \bold "5h. Double Neighbor (surround from above & below)"
\relative c' {
  \time 4/4
  gis8 bes a4 dis,8 f e4
  \bar "|."
}

\markup \bold "5i. Piazzolla Sequence (rising 3rds through harm. minor)"
\relative c {
  \time 4/4
  a8 c e b d f | c e gis a4.
  \bar "|."
}

\markup \bold "5j. Tango Ending (turn on 5th, descend to tonic)"
\relative c' {
  \time 4/4
  e8 dis e4 f8 e d c | b a4. r2
  \bar "|."
}


% ════════════════════════════════════════════════════════
% 6. RHYTHMIC PATTERNS (applied to D Dorian)
% ════════════════════════════════════════════════════════

\markup \column {
  \vspace #1
  \override #'(font-size . 5) \bold "6. Rhythmic Patterns"
  \vspace #0.2
  \italic "Applied to D Dorian. Use these rhythms with ANY scale."
  \vspace #0.5
}

\markup \bold "6a. Son Clave 3-2"
\relative c' {
  \time 4/4
  d4. f4. a4 | r4 r8 g4. d4
  \bar "|."
}

\markup \bold "6b. Anticipated Downbeat (push the 'one')"
\relative c' {
  \time 4/4
  r4 r8 d8 f4 r | r4 r8 a g4 r
  \bar "|."
}

\markup \bold "6c. Tresillo (3+3+2)"
\relative c' {
  \time 4/4
  d4. f4. a4 | c4. a4. g4
  \bar "|."
}

\markup \bold "6d. Habanera (dotted quarter + eighth)"
\relative c' {
  \time 4/4
  d4. f8 g4 a | d,4. f8 g4 a
  \bar "|."
}

\markup \bold "6e. Cinquillo"
\relative c' {
  \time 4/4
  d4 f8 g4 a8 c4
  \bar "|."
}

\markup \bold "6f. Off-Beat Accents (all upbeats)"
\relative c' {
  \time 4/4
  r8 d-> r f-> r g-> r a->
  \bar "|."
}

\markup \bold "6g. 3-over-4 Polyrhythm (dotted quarters)"
\relative c' {
  \time 4/4
  d4. g4. c4~ | c4 a4. f4.
  \bar "|."
}

\markup \bold "6h. Cascara-Inspired"
\relative c' {
  \time 4/4
  d8 r f r g a r c | r a r g f r d r
  \bar "|."
}


% ════════════════════════════════════════════════════════
% 7. ii-V-i LICK #1 TRANSPOSED TO 4 COMMON KEYS
% ════════════════════════════════════════════════════════

\markup \column {
  \vspace #1
  \override #'(font-size . 5) \bold "7. Lick Transposition — Smooth Dorian-Spanish in 4 Keys"
  \vspace #0.2
  \italic "The same lick (2a) moved to the 4 most common Latin jazz key centers."
  \vspace #0.5
}

\markup \bold "C minor: Dm7 — G7b9 — Cm"
\relative c' {
  \time 4/4
  d8^\markup{\small "Dm7"} e f g
  aes^\markup{\small "G7b9"} b d f |
  ees4^\markup{\small "Cm"} d c2
  \bar "|."
}

\markup \bold "F minor: Gm7 — C7b9 — Fm"
\relative c' {
  \time 4/4
  g'8^\markup{\small "Gm7"} a bes c
  des^\markup{\small "C7b9"} e g bes |
  aes4^\markup{\small "Fm"} g f2
  \bar "|."
}

\markup \bold "G minor: Am7 — D7b9 — Gm"
\relative c'' {
  \time 4/4
  a8^\markup{\small "Am7"} b c d
  ees^\markup{\small "D7b9"} fis a c |
  bes4^\markup{\small "Gm"} a g2
  \bar "|."
}

\markup \bold "D minor: Em7 — A7b9 — Dm"
\relative c' {
  \time 4/4
  e8^\markup{\small "Em7"} fis g a
  bes^\markup{\small "A7b9"} cis e g |
  f4^\markup{\small "Dm"} e d2
  \bar "|."
}
