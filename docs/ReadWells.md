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
One English lexical item should have:
- one ReadWells spelling,
- regardless of accent.

---

### Workflow ###

```
English word
    ↓ (requires lexical context)
Lexical item 
    ↓
Davian spelling (dialect neutral)
    ↓ (Accent mapping)
IPA
```

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
- ReadWells uses Wells' solution for vowels and extends the same philosophy to consonants.

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
- Every ordinary English word can be assigned a unique ReadWells spelling using the current 55-category inventory.

No obvious missing sound categories have been identified so far.

The remaining work is:
- Define all 55 glyphs.
- Create category-assignment rules.
- Build a canonical ReadWells dictionary.
- Define accent-specific IPA mappings from ReadWells categories to pronunciations.

---

| P | B | T | D | K | G | F | V | TH   | DH   | S | Z | SH   | ZH   | CH   | DZH   | M | N | NG | L | R | H | W | WH   | Y | LOCH | AX | EX | KIT | DRESS | TRAP | LOT | STRUT | FOOT | BATH | CLOTH | NURSE | FLEECE | FACE | PALM | THOUGHT | GOAT | GOOSE | PRICE | CHOICE | MOUTH | NEAR | SQUARE | START | NORTH | FORCE | CURE | happY | commA | lettER |
| - | - | - | - | - | - | - | - | ---- | ---- | - | - | ---- | ---- | ---- | ----- | - | - | -- | - | - | - | - | ---- | - | ---- | -- | -- | --- | ----- | ---- | --- | ----- | ---- | ---- | ----- | ----- | ------ | ---- | ---- | ------- | ---- | ----- | ----- | ------ | ----- | ---- | ------ | ----- | ----- | ----- | ---- | ----- | ----- | ------ |
| p | b | t | d | k | g | f | v | [th] | [dh] | s | z | ʃ    | ʒ    | tʃ   | dʒ    | m | n | ŋ  | l | r | h | w | ʍ    | - | ch   | -- | -- | ɪ   | e     | æ    | ɒ   | ʌ     | ---- | ---- | ----- | ɜ     | i      | eɪ   | ---- | ------- | əʊ   | ----- | ??--- | ɔɪ     | ??--- | ɪə-- | eə---- | ----- | ----- | ----- | ʊə-- | ----- | ----- | ------ |
|   |   |   |   |   |   |   |   |      |      |   |   | ş    | z̧    | ç    | dz̧    |   |   |    |   |   |   |   | [wh] |   |      |    |    |     |       |      |     |       |      |      |       |       |        |      |      |         |      |       |       |        |       |      |        |       |       |       |      |       |       |        |
|   |   |   |   |   |   |   |   |      |      |   |   | [sh] | [zh] | [ch] | [dzh] |   |   |    |   |   |   |   | [wh] |   |      |    |    |     |       |      |     |       |      |      |       |       |        |      |      |         |      |       |       |        |       |      |        |       |       |       |      |       |       |        |

<img width="2590" height="566" alt="image" src="https://github.com/user-attachments/assets/a64a7dd1-a696-400e-b075-86a4fb2148c4" />


There are **55 ReadWells lexical categories**:

* **28 consonant categories**
* **27 vowel categories**

for a total of **55 glyphs**.

---

## Exceptions & Problems ##

The following words do not map cleanly and are intentionally outside of the scope:
- Unstressed-only function words such as the, a, to, of, and. The Shavian rules are used.
- Interjections ich as h,, shh, psst, uh-oh
- Syllabic constant words/vowels such as rhtym, button, little
- Borrowings such as zeitgeist, hors d’oeuvre (especially if the borrowings are recent therefore unstable)
- Proper names such as Nguyen, Siobhán, Qatar (dependent on source language)
- Onomatopoeia such as brrr, meow, woof, tsk (often outside of normal English vowel categories)
- Acronyms and initialistms such as BBC, HTML, X-ray

### Not a problem ###
The following are handled gracefully:
- sure
- poor
- tourist
- pasta
- square-type subsets
- nurse-type subsets
- r-condition:
  - Mary
  - marry
  - merry
  - mirror
  - nearer
  - spirit
  - Sirius
  - very
  - carry
  - ...

### Problematic examples ###
There are a small number of words whuch change lexical sets depending on the accent:
- Tomato (the -ma- syllable belongs to PALM in received pronounciation but FACE in General American pronounciation.
- Vase (same as tomato)
- Garage (four pronunciations: G commA R PALM ZH [RP,GA], G TRAP R PALM ZH [RP], G commA R PALM J [GA], G commA R TRAP J[GA])
- Lieutenant (British-specific pronunciation: leftenant - deal with by exception?)
- Route (British-specific pronunciation - deal with by exception?)
- Either (FLEECE + DH + commA / PRICE + DH + commA pronunciation within accents)
- Neither (N + FLEECE + DH + commA / N + PRICE + DH + commA pronunciation within accents)
- Privacy (KIT-PRICE pronunciation within British accent (usually PRICE); KIT is rare within American)
- Dynasty (KIT-PRICE pronunciation within British accent, KIT is less common within American)
- Vitamin (almost universally KIT within British accemt, almost universally PRICE within American accent)
- Direct (usually commA within British accent (occassionally PRICE); usually commA within American accent, PRICE also exists)

These might be examples of where an unidentified additional Wellian set is required to disabmiguate. Wells lexical sets were designed to answer:
- "Given a word in a particular accent, what vowel category does it belong to?"
They were not designed to answer:
- "What is the unique accent-independent category for this word?"
For most words, the answer happens to be the same. For the above, it isn't.

Current proposal: Encode as exceptions in the translation layer.

---

## Stress ##

Two probable solutions
- encode the IPA stress markers at the spelling level. Problematic because the same spelling has different pronounciation in different accents
- encode the stress pattern per word per accent: RP: 1000; GA: 0100
- Morphological stress rules

| Ending  | Stress tendency           |
| ------- | ------------------------- |
| -ity    | stress antepenultimate    |
| -ation  | stress penultimate        |
| -ic     | stress preceding syllable |
| -graphy | stress antepenultimate    |
| -ee     | final stress              |

Still needs lexical exceptions.

### Stress rules ###

#### Level 00 ####
Where the verb form of an English word is pronounced differently to the noun form, a primary stress mark is optionally inserted immediately before the stressed syllable.
This stress mark is present in the ReadWells dictionary, it is not part of the stress rules below. This allows a reader to differentiate between the two different lexical
items out of context and know how to pronounce the word in their accent whilst allowing ReadWells to remain largely independent of pronounciation and part-of-speech and
solving the 'Heteronyms caused solely by stress' problem.
- nouns: first syllable: REcord, PREsent, CONtract, IMport
- verbs: second syllable: re'CORD, pre'SENT, con'TRACT, im'PORT
This is a finate list of a few thousand words and requires lexical knowledge.
These are mostly French/Latinate borrowings, not native Germanic vocabulary.

We also do this for a finite list of compound verbs (not all compound verbs - some have been normalised, e.g. weekend, breakfast:
- nouns: stress first element (not syllable): BLACKbird, GREENhouse, TOOTHbrush
- verbs: stress second element (not syllable): over'COME, under'STAND, out'RUN, outper'FORM, under'ESTimate

Also encoded here: French loan words have a stress marker on the final syllable (examples: caf'é, bal'let, buf'fet, de'bris, gar'age, va'let, cha'let, cli'ché, crois'sant, mon'tage). They are marked
with the ReadWells accent-dependent stress marker (ˌ).
Also encoded here: words that are stressed the same in every accent, where the stress is not on syllable 1, and would otherwise would end up in the level 0 exceptions list: (currently no examples)

#### Level 0 - Explicit stress marker
- If a ReadWells stress marker (ˈ) is present:
- primary stress falls on the following syllable
- if not the French loan words marker (see level 4), break here (don't apply any following rules, move on to the next word)
#### Level 1 - lexical exceptions ####
accent-specific: requires lexical storage: 
- class A - stress exceptions (words where the stress cannot be predicted and where the stress varies from accent to accent): controversy, laboratory, applicable, adult
- class B - pronounciation exceptions (stress varies from accent to accent): ally
For exceptions, the whole answer is provided so break here (don't apply any following rules, move on to the next word)
Check for correct handling in levels 2..7 before adding any word here.
Words falling into the exceptions list generally fall into one or more of the following categories:
- stress differs between dialects/accents (e.g. RP / GA)
- stress varies between educated speakers
- the variation is lexical ratehr than morphological
#### Level 2 - Default stress assignment ####
One-syllable words: stress the only syllable.
For the rest: assign primary stress to the first syllable of the lexical root.
#### Level 3 - Suffix rule ####
-ee - stress the suffix (pattern 001)
-eer - final stress
-ese - final stress
-ette - final stress
-oon - final stress
-ic - stress preceding syllable
-ical - stress preceding syllable
-ity - Stress antepenultimate (third from end).
-ion - stress preceding syllable
-ian - stress preceding syllable
-ial - stress preceding syllable
-ious - stress preceding syllable
-eous - stress preceding syllable
-ify - stress preceding syllable
-ography - Stress antepenultimate 
-graphy - Stress antepenultimate 
-ology - Stress antepenultimate 
-ion - stress preceding syllable
#### Level 4 - French loan rule ####
French loan words have a stress marker already present on the final syllable as per level 00 (examples: café, ballet, buffet, debris, garage, valet, chalet, cliché, croissant, montage).
Nativised French loans do not have a stress marker applied (these behave like ordinary English and follow the rules for level 3, levels 5+. Examples: courage, village, message, image, language).
- American-final vs British-earlier stress (American English preserves the French stress, British places the stress on the first syllable. Examples: GARage, BALlet, CAFé, DEbris). If RP,
hide or remove the stress marker on the final syllable (therefore the first syllable is implicitly stressed); otherwise promote it to the primary stress marker.
This is a finate list and requires lexical knowledge.


