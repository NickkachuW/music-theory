\version "2.24.4"

\header {
  title = "Riffs & Licks in All 12 Keys"
  subtitle = "5 Essential Latin Jazz & Tango Patterns — Transposed for Practice"
  subsubtitle = "For Alto & Tenor Saxophone"
  tagline = "Companion to the Latin Jazz & Tango Improvisation Syllabus"
}

\paper {
  #(set-paper-size "letter")
  top-margin = 10\mm
  bottom-margin = 10\mm
  left-margin = 12\mm
  right-margin = 12\mm
  indent = 0\mm
  system-system-spacing.basic-distance = #11
  markup-system-spacing.basic-distance = #8
  score-markup-spacing.basic-distance = #8
}

% ════════════════════════════════════════════════════════════
% LICK 1: DORIAN PENTATONIC CALL
% Original: D F G A C D (ascending minor pentatonic burst)
% ════════════════════════════════════════════════════════════

\markup \column {
  \vspace #0.3
  \override #'(font-size . 5) \bold "Lick 1: Pentatonic Call"
  \vspace #0.2
  \italic "Ascending minor pentatonic burst — use over any minor 7th vamp"
  \vspace #0.3
}

\markup \bold "C minor"
\relative c' { \time 4/4 c8 ees f g bes c4. \bar "|." }
\markup \bold "Db minor"
\relative c' { \time 4/4 des8 fes ges aes ces des4. \bar "|." }
\markup \bold "D minor"
\relative c' { \time 4/4 d8 f g a c d4. \bar "|." }
\markup \bold "Eb minor"
\relative c' { \time 4/4 ees8 ges aes bes des ees4. \bar "|." }
\markup \bold "E minor"
\relative c' { \time 4/4 e8 g a b d e4. \bar "|." }
\markup \bold "F minor"
\relative c' { \time 4/4 f8 aes bes c ees f4. \bar "|." }
\markup \bold "F# minor"
\relative c' { \time 4/4 fis8 a b cis e fis4. \bar "|." }
\markup \bold "G minor"
\relative c' { \time 4/4 g8 bes c d f g4. \bar "|." }
\markup \bold "Ab minor"
\relative c'' { \time 4/4 aes,8 ces des ees ges aes4. \bar "|." }
\markup \bold "A minor"
\relative c' { \time 4/4 a8 c d e g a4. \bar "|." }
\markup \bold "Bb minor"
\relative c' { \time 4/4 bes8 des ees f aes bes4. \bar "|." }
\markup \bold "B minor"
\relative c' { \time 4/4 b8 d e fis a b4. \bar "|." }


% ════════════════════════════════════════════════════════════
% LICK 2: SMOOTH DORIAN-SPANISH ii-V-i
% Original in Cm: D E F G | Ab B D F | Eb D C
% ════════════════════════════════════════════════════════════

\markup \column {
  \vspace #0.8
  \override #'(font-size . 5) \bold "Lick 2: Smooth Dorian-Spanish ii-V-i"
  \vspace #0.2
  \italic "The essential Latin jazz ii-V-i lick. Dorian on ii, Spanish/Jewish on V, resolve to i."
  \vspace #0.3
}

\markup \bold "C minor: Dm7 — G7b9 — Cm"
\relative c' {
  \time 4/4
  d8^\markup{\small "ii"} e f g
  aes^\markup{\small "V7b9"} b d f |
  ees4^\markup{\small "i"} d c2
  \bar "|."
}
\markup \bold "Db minor: Ebm7 — Ab7b9 — Dbm"
\relative c' {
  \time 4/4
  ees8 f ges aes
  beses ces ees ges |
  fes4 ees des2
  \bar "|."
}
\markup \bold "D minor: Em7 — A7b9 — Dm"
\relative c' {
  \time 4/4
  e8 fis g a
  bes cis e g |
  f4 e d2
  \bar "|."
}
\markup \bold "Eb minor: Fm7 — Bb7b9 — Ebm"
\relative c' {
  \time 4/4
  f8 g aes bes
  ces d f aes |
  ges4 f ees2
  \bar "|."
}
\markup \bold "E minor: F#m7 — B7b9 — Em"
\relative c' {
  \time 4/4
  fis8 gis a b
  c dis fis a |
  g4 fis e2
  \bar "|."
}
\markup \bold "F minor: Gm7 — C7b9 — Fm"
\relative c' {
  \time 4/4
  g'8 a bes c
  des e g bes |
  aes4 g f2
  \bar "|."
}
\markup \bold "F# minor: G#m7 — C#7b9 — F#m"
\relative c'' {
  \time 4/4
  gis8 ais b cis
  d eis gis b |
  a4 gis fis2
  \bar "|."
}
\markup \bold "G minor: Am7 — D7b9 — Gm"
\relative c'' {
  \time 4/4
  a8 b c d
  ees fis a c |
  bes4 a g2
  \bar "|."
}
\markup \bold "Ab minor: Bbm7 — Eb7b9 — Abm"
\relative c'' {
  \time 4/4
  bes8 c des ees
  fes g bes des |
  ces4 bes aes2
  \bar "|."
}
\markup \bold "A minor: Bm7 — E7b9 — Am"
\relative c'' {
  \time 4/4
  b8 cis d e
  f gis b d |
  c4 b a2
  \bar "|."
}
\markup \bold "Bb minor: Cm7 — F7b9 — Bbm"
\relative c'' {
  \time 4/4
  c8 d ees f
  ges a c ees |
  des4 c bes2
  \bar "|."
}
\markup \bold "B minor: C#m7 — F#7b9 — Bm"
\relative c'' {
  \time 4/4
  cis8 dis e fis
  g ais cis e |
  d4 cis b2
  \bar "|."
}


% ════════════════════════════════════════════════════════════
% LICK 3: SPANISH SIGNATURE (full Spanish/Jewish run on V7)
% Original over G7b9: G Ab B C D Eb F -> resolve to Eb D C
% ════════════════════════════════════════════════════════════

\markup \column {
  \vspace #0.8
  \override #'(font-size . 5) \bold "Lick 3: Spanish Signature Run"
  \vspace #0.2
  \italic "Full ascending Spanish/Jewish scale on V7b9, resolving to i. THE Latin dominant sound."
  \vspace #0.3
}

\markup \bold "V = G7b9 → Cm"
\relative c' {
  \time 4/4
  g'8^\markup{\small "G7b9"} aes b c d ees f ees |
  d4^\markup{\small "Cm"} c2.
  \bar "|."
}
\markup \bold "V = Ab7b9 → Dbm"
\relative c'' {
  \time 4/4
  aes8 beses c des ees fes ges fes |
  ees4 des2.
  \bar "|."
}
\markup \bold "V = A7b9 → Dm"
\relative c'' {
  \time 4/4
  a8 bes cis d e f g f |
  e4 d2.
  \bar "|."
}
\markup \bold "V = Bb7b9 → Ebm"
\relative c'' {
  \time 4/4
  bes8 ces d ees f ges aes ges |
  f4 ees2.
  \bar "|."
}
\markup \bold "V = B7b9 → Em"
\relative c'' {
  \time 4/4
  b8 c dis e fis g a g |
  fis4 e2.
  \bar "|."
}
\markup \bold "V = C7b9 → Fm"
\relative c'' {
  \time 4/4
  c8 des e f g aes bes aes |
  g4 f2.
  \bar "|."
}
\markup \bold "V = C#7b9 → F#m"
\relative c'' {
  \time 4/4
  cis8 d eis fis gis a b a |
  gis4 fis2.
  \bar "|."
}
\markup \bold "V = D7b9 → Gm"
\relative c'' {
  \time 4/4
  d8 ees fis g a bes c bes |
  a4 g2.
  \bar "|."
}
\markup \bold "V = Eb7b9 → Abm"
\relative c'' {
  \time 4/4
  ees8 fes g aes bes ces des ces |
  bes4 aes2.
  \bar "|."
}
\markup \bold "V = E7b9 → Am"
\relative c'' {
  \time 4/4
  e8 f gis a b c d c |
  b4 a2.
  \bar "|."
}
\markup \bold "V = F7b9 → Bbm"
\relative c'' {
  \time 4/4
  f8 ges a bes c des ees des |
  c4 bes2.
  \bar "|."
}
\markup \bold "V = F#7b9 → Bm"
\relative c'' {
  \time 4/4
  fis8 g ais b cis d e d |
  cis4 b2.
  \bar "|."
}


% ════════════════════════════════════════════════════════════
% LICK 4: TANGO AUGMENTED 2nd CRY
% Pattern: 5 — b6 — maj7 — 1 — maj7 — b6 — 5  (harmonic minor)
% Mirror-symmetric phrase centered on the root, with the
% augmented-2nd interval (b6 → maj7) showcased on both sides.
% ════════════════════════════════════════════════════════════

\markup \column {
  \vspace #0.8
  \override #'(font-size . 5) \bold "Lick 4: Tango Augmented 2nd Cry"
  \vspace #0.2
  \italic "Scale degrees 5–b6–7–1–7–b6–5 of harmonic minor. The aug-2nd interval (b6→7) is the tango DNA."
  \vspace #0.3
}

\markup \bold "A minor — E F G# A G# F E"
\relative c' { \time 4/4 e4 f8 gis a2 | gis8 f e2. \bar "|." }
\markup \bold "Bb minor — F Gb A Bb A Gb F"
\relative c' { \time 4/4 f4 ges8 a bes2 | a8 ges f2. \bar "|." }
\markup \bold "B minor — F# G A# B A# G F#"
\relative c' { \time 4/4 fis4 g8 ais b2 | ais8 g fis2. \bar "|." }
\markup \bold "C minor — G Ab B C B Ab G"
\relative c' { \time 4/4 g'4 aes8 b c2 | b8 aes g2. \bar "|." }
\markup \bold "C# minor — G# A B# C# B# A G#"
\relative c' { \time 4/4 gis'4 a8 bis cis2 | bis8 a gis2. \bar "|." }
\markup \bold "D minor — A Bb C# D C# Bb A"
\relative c'' { \time 4/4 a4 bes8 cis d2 | cis8 bes a2. \bar "|." }
\markup \bold "Eb minor — Bb Cb D Eb D Cb Bb"
\relative c'' { \time 4/4 bes4 ces8 d ees2 | d8 ces bes2. \bar "|." }
\markup \bold "E minor — B C D# E D# C B"
\relative c'' { \time 4/4 b4 c8 dis e2 | dis8 c b2. \bar "|." }
\markup \bold "F minor — C Db E F E Db C"
\relative c'' { \time 4/4 c4 des8 e f2 | e8 des c2. \bar "|." }
\markup \bold "F# minor — C# D E# F# E# D C#"
\relative c'' { \time 4/4 cis4 d8 eis fis2 | eis8 d cis2. \bar "|." }
\markup \bold "G minor — D Eb F# G F# Eb D"
\relative c'' { \time 4/4 d4 ees8 fis g2 | fis8 ees d2. \bar "|." }
\markup \bold "Ab minor — Eb Fb G Ab G Fb Eb"
\relative c'' { \time 4/4 ees4 fes8 g aes2 | g8 fes ees2. \bar "|." }


% ════════════════════════════════════════════════════════════
% LICK 5: CHROMATIC APPROACH INTO RESOLUTION
% Original over G7->Cm: A G F E | Eb D Db C B | C
% ════════════════════════════════════════════════════════════

\markup \column {
  \vspace #0.8
  \override #'(font-size . 5) \bold "Lick 5: Chromatic Approach into Resolution"
  \vspace #0.2
  \italic "Descend from ii through V with chromatic half steps landing on the tonic. Works over any ii-V-i."
  \vspace #0.3
}

\markup \bold "→ C (Dm7 — G7 — C)"
\relative c'' {
  \time 4/4
  a8^\markup{\small "ii"} g f e
  ees^\markup{\small "V"} d des c | b c4.^\markup{\small "i"} r2
  \bar "|."
}
\markup \bold "→ Db"
\relative c'' {
  \time 4/4
  bes8 aes ges f
  fes ees d des | c des4. r2
  \bar "|."
}
\markup \bold "→ D"
\relative c'' {
  \time 4/4
  b8 a g fis
  f e ees d | cis d4. r2
  \bar "|."
}
\markup \bold "→ Eb"
\relative c'' {
  \time 4/4
  c8 bes aes g
  ges f fes ees | d ees4. r2
  \bar "|."
}
\markup \bold "→ E"
\relative c'' {
  \time 4/4
  cis8 b a gis
  g fis f e | dis e4. r2
  \bar "|."
}
\markup \bold "→ F"
\relative c'' {
  \time 4/4
  d8 c bes a
  aes g ges f | e f4. r2
  \bar "|."
}
\markup \bold "→ F#"
\relative c'' {
  \time 4/4
  dis8 cis b ais
  a gis g fis | eis fis4. r2
  \bar "|."
}
\markup \bold "→ G"
\relative c'' {
  \time 4/4
  e8 d c b
  bes a aes g | fis g4. r2
  \bar "|."
}
\markup \bold "→ Ab"
\relative c'' {
  \time 4/4
  f8 ees des c
  ces bes a aes | g aes4. r2
  \bar "|."
}
\markup \bold "→ A"
\relative c'' {
  \time 4/4
  fis8 e d cis
  c b bes a | gis a4. r2
  \bar "|."
}
\markup \bold "→ Bb"
\relative c'' {
  \time 4/4
  g'8 f ees d
  des c ces bes | a bes4. r2
  \bar "|."
}
\markup \bold "→ B"
\relative c'' {
  \time 4/4
  gis8 fis e dis
  d cis c b | ais b4. r2
  \bar "|."
}
