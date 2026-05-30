# ReadWells #

ReadWells (also known colloquially as Davian) builds on ReadSpel by Ronald Kingsley Read (which itself builds on QuikScript and Shavian) as follows:
- Builds on the lexical sets work by John C. Wells (which itself was likley inspired in part by Shavian and Read's other works)
- Creates a lexical set for consonants, similar in concept to Well's work with vowels

---

## Core philosophy ##
ReadWells is a (dialect-neutral) diaphonemic lexical-category alphabet.

ReadWells is not
- IPA
- A phonetic alphabet
- A phonemic alphabet in the Shavian sense

A ReadWells glyph does not directly specify a pronunciation.

Instead it specifies:
- a stable English lexical category
- Each accent or dialect then maps that category to its own IPA realization
- This is analogous to how Wells lexical sets work

---

## Design goal ##
One English word should have:
- one ReadWells spelling,
- regardless of accent.

---

## Vowel system ##
ReadWells adopts the full 27 Wells lexical categories.

These are:
- KIT
- DRESS
- TRAP
- LOT
- STRUT
- FOOT
- BATH
- CLOTH
- NURSE
- FLEECE
- FACE
- PALM
- THOUGHT
- GOAT
- GOOSE
- PRICE
- CHOICE
- MOUTH
- NEAR
- SQUARE
- START
- NORTH
- FORCE
- CURE
- happY
- commA
- lettER

Each receives its own ReadWells vowel glyph.
Rule: Merged accents do not invaludate lexical distinctions.

---

## Consonant system ##

### Voiced/Unvoiced pairs ###
|  |  |  |  |  |  |  |  |  |  |  |
| ----------------- | - | - | - | - | -- | - | -- | -- | -- | -- |
| **Deep/Voiced**   | b | d | g | v | dh | z | zh | j  | w | ex |
| **Tall/Unvoiced** | p | t | k | f | th | s | sh | ch | wh | ax |
EX - exam, exact
AX - ax, box, fox

### Nasal family ###
| Category | m     | n     | ng    |
| -------- | ----- | ----- | ----- |
| Type     | Nasal | Nasal | Nasal |

### Liquid family ###
| Category | l      | r      |
| -------- | ----- | ----- |
| Type     | Liquid | Liquid |

### Glide family ###
Note that [w] and [wh] belong to both a voicing pair and to the glide family
| Category | w     | wh     | y     |
| -------- | ----- | ----- | ----- |
| Type     | Glide | Glide | Glide |

### Other ###
| Category | h         | lock      |
| -------- | --------- | --------- |
| Type     | Fricative | Fricative |
LOCH - loch, Bach

---

## Character set ##
- 28 vowel categories/glyphs
- 27 consonant cagegories/glyphs
- 55 ReadWells glyphs in total

---

## Treatment of accent variation ##
ReadWells spelling remains constant.
Accent determines IPA realisation
Examples:
### WH ###
| Accent   | IPA |
| -------- | --- |
| Scottish | /ʍ/ |
| RP       | /w/ |
| American | /w/ |

### GOAT ###
| Accent   | IPA  |
| -------- | ---- |
| RP       | /əʊ/ |
| American | /oʊ/ |
| Scottish | /o/  |

### T ###
| Accent   | IPA |
| -------- | --- |
| RP       | /t/ |
| American | [ɾ] |
| Cockney  | [ʔ] |

---

## What does NOT get new glyphs? ##
Pure accent realisations
Examples:
| IPA realization | Category |
| --------------- | -------- |
| [t]             |          |
| [ɾ]             | T        |
| [ʔ]             |          |
...remains one category.

Similarly:
| IPA realization | Category |
| --------------- | -------- |
| /w/             |          |
| /ʍ/             |          |
...remain distinct because of WH

---

## Morphology policy ##
Rule: Morphological relationships do not drive spelling.
Examples:
- sign / signal
- electric / electricity
need not share visible spelling features.

Rationale:
Modern tools already provide:
- etymology
- semantic relationships
- lexical networks
through resources such as WordNet.
Therefore spelling does not need to preserve morphology.

--- 

## Dictionary philiosophy ##
The main remaining challenge is assigning every English word to its ReadWells lexical categories.

Examples:
| Word  | Category  |
| ----- | --------- |
| poor  | CURE      |
| pore  | FORCE     |
| Mary  | FACE + R  |
| marry | TRAP + R  |
| merry | DRESS + R |
These are dictionary-classification questions, not glyph-design questions.

---

## Relationship to existing systems ##
### IPA ###
- ReadWells is not IPA.
- IPA describes pronunciation.
- ReadWells describes lexical categories.

### Shavian ###
- Shavian is largely phonemic.
- ReadWells is diaphonemic.

### Quikscript ###
- Quikscript approximates a reduced Wells-like system.
- ReadWells restores the distinctions that Read collapsed.

### Wells ###
- Davian uses Wells' solution for vowels and extends the same philosophy to consonants.

### Other notable works ###
The idea is similar to:
- Archiphonemes by Prague Linguistic Circle / Prague School (1920s-1930s)
- Trager–Smith Diasystem by George L. Trager and Henry Lee Smith Jr. (1950s)
- Diaphonemic Dictionaries e.g. A. C. Gimson circa 1950s (not fully IPA; represents categroies that readers map to their own accent)
- Unifon by John Malone
- Chinese Phonological systems such as Qieyun
- Proto-Germanic and Proto-Indo-European language reconstructions

---

## Current Working Hypothesis ##

The working assumption is:
- Every ordinary English word can be assigned a unique Davian spelling using the current 55-category inventory.

No obvious missing sound categories have been identified so far.

The remaining work is:
- Define all 55 glyphs.
- Create category-assignment rules.
- Build a canonical Davian dictionary.
- Define accent-specific IPA mappings from Davian categories to pronunciations.

---

| P | B | T | D | K | G | F | V | TH   | DH   | S | Z | SH   | ZH   | CH   | DZH   | M | N | NG | L | R | H | W | WH   | Y | LOCH | AX | EX | KIT | DRESS | TRAP | LOT | STRUT | FOOT | BATH | CLOTH | NURSE | FLEECE | FACE | PALM | THOUGHT | GOAT | GOOSE | PRICE | CHOICE | MOUTH | NEAR | SQUARE | START | NORTH | FORCE | CURE | happY | commA | lettER |
| - | - | - | - | - | - | - | - | ---- | ---- | - | - | ---- | ---- | ---- | ----- | - | - | -- | - | - | - | - | ---- | - | ---- | -- | -- | --- | ----- | ---- | --- | ----- | ---- | ---- | ----- | ----- | ------ | ---- | ---- | ------- | ---- | ----- | ----- | ------ | ----- | ---- | ------ | ----- | ----- | ----- | ---- | ----- | ----- | ------ |
| p | b | t | d | k | g | f | v | [th] | [dh] | s | z | ʃ    | ʒ    | tʃ   | dʒ    | m | n | ŋ  | l | r | h | w | ʍ    | - | ch   | -- | -- | ɪ   | e     | æ    | ɒ   | ʌ     | ---- | ---- | ----- | ɜ     | i      | eɪ   | ---- | ------- | əʊ   | ----- | ??--- | ɔɪ     | ??--- | ɪə-- | eə---- | ----- | ----- | ----- | ʊə-- | ----- | ----- | ------ |
|   |   |   |   |   |   |   |   |      |      |   |   | ş    | z̧    | ç    | dz̧    |   |   |    |   |   |   |   | [wh] |   |      |    |    |     |       |      |     |       |      |      |       |       |        |      |      |         |      |       |       |        |       |      |        |       |       |       |      |       |       |        |
|   |   |   |   |   |   |   |   |      |      |   |   | [sh] | [zh] | [ch] | [dzh] |   |   |    |   |   |   |   | [wh] |   |      |    |    |     |       |      |     |       |      |      |       |       |        |      |      |         |      |       |       |        |       |      |        |       |       |       |      |       |       |        |


There are **55 Davian lexical categories**:

* **28 consonant categories**
* **27 vowel categories**

for a total of **55 glyphs**.

