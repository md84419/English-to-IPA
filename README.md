

### English to IPA (eng_to_ipa)


This Python program utilizes the Carnegie-Mellon University Pronouncing Dictionary to convert American English or the Britfone Pronouncing Dictionary to convert British English text into the [International Phonetic Alphabet](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet).

### Installation ### 

1. Download this directory locally 
2. Run `python -m pip install .` in the same directory as ` setup.py`.


### Running the tests ###
`PYTHONPATH="tests" python -m unittest 2>&1`


### Key functions ###


The `convert` function is used to take English text and convert it to IPA, like so:

```Python
>>> import eng_to_ipa as ipa
>>> ipa.convert("The quick brown fox jumped over the lazy dog.")
'ðə kwɪk braʊn fɑks ʤəmpt ˈoʊvər ðə ˈleɪzi dɔg.'
``` 

Note that words that cannot be found in the dictionary are simply reprinted with an asterisk.


#### Dictionaries

* The CMU dictionary has 124999 entries in it as of July 2020
* The Open Britfone dictionary has 65118 words from Open Dict and 16000 words from Britfone
  * The top 10,000 most frequent words according to BNC and Google Web Corpus
  * Proper nouns including all UK counties, London boroughs, major UK towns, European Capitals, US states, common irregular plurals and verbs
  * Distributed under a MIT license
  * Sources: https://github.com/JoseLlarena/Britfone and https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/en_UK.txt


#### Configuration



#### `convert` parameters

* **text** : *string* - The input string of English text to be converted to IPA notation.

* **keep_punct** : *boolean, optional (default=True)* - Determines whether or not the punctuation marks from the input string
should be retained or not.

* **retrieve_all** : *boolean, optional (default=False)* - Given that some words might have more than one transcription,
this parameter determines whether or not a list of all possible combinations of transcriptions should be returned (True)
 or just the string of one transcription (False).
 
* **stress_marks** : *string, optional (default='both')* - Determines whether or not the primary and secondary stress 
markings (ˈ, ˌ) should be retained. Understood arguments are:
   * "primary" - retains primary stress only 
   * "secondary" - retains secondary stress only
   * "both" - to keep both primary and secondary stress markers
   * "none" - preserve neither primary nor secondary stress
   
* **mode** : *string, optional (default='sql')* - Accepts "sql" or "json", depending on which version of the database you'd like to use.
 As another option for JSON users, simply use the function `jonvert` instead of `convert`. 

* **language** : *string, optional (default='cmu')* - The language tag in W3 / IETF BCP 47 format (ISO 639-1 lowercase 2- or 3- character
language code then optionally a hyphen '-' then ISO 3166-1 uppercase 2-character country code then optionally a hyphen '-' followed by
a 3-character region code) - example: en-GB, en-US (or in future, it, es-419, en-GB-WLS).  The special value 'cmu' is also supported for
legacy behaviour consistent with eng_to_ipa v0.2.x (the Carnegie Mellon University US-English dictionary).

Note: At the time of writing, eng_to_ipa supports three language tags: en-US, en-GB and cmu.  Future versions may support langauge tags
from BCP 47 which are compliant with that standard but are not in the above format (e.g. zh-Hans).  BCP 47 states that language
codes should be kept as short as possible - language code 'it' is prefered over 'it-IT' for example.
Contributions providing further language dictionaries are welcome.

* **token_marking** : *string, optional (default='none')* - What tokenization to apply to the IPA.  Currently not implemented for language='cmu'
where the tokenization is always 'none'.  In langauge modes other than 'cmu', the IPA no-space character is used between individual glyphs in
dipthongs and affricates that use two UTF characters to build an IPA symbol.
   * "none" - IPA symbols are not tokenized.  A regex expression can be used in calling code to split characters that don't have the IPA
 no-space character between them.
   * "spaces" - A space is inserted between each IPA symbol for ease of parsing.
   * "symbols" - The IPA triangular interpunct character ('ˑ', UTF-8 0xCB 0x91, UTF-16 0x02DC) is inserted between each IPA symbol for ease of parsing.

See:
* https://tools.ietf.org/html/bcp47
* https://www.w3.org/International/articles/language-tags/

* **sorted_list** : *bool, optional (default='True')* - Whether to return a sorted list or the list in the natural order of the source dictionary.  When sorted_list==False and retrieve_all==False, the 'best' match (the last transcription in the dictionary) will be returned.

#### `ipa_list`

The `ipa_list` function returns a list of each word as a list of all its possible transcriptions. It has all the same
optional `stress_marks` and `keep_punct` parameters as `convert`.
```Python
>>> ipa.ipa_list("The record was expensive.")
[['ði', 'ðə'], ['rəˈkɔrd', 'rɪˈkɔrd', 'ˈrɛkərd'], ['wɑz'], ['ɪkˈspɛnsɪv.']]
```
   
#### `isin_cmu`

The `isin_cmu` function takes a word (or list of words) and checks if it is in the CMU pronouncing dictionary (returns 
`True` or `False`). If a list of words is provided, then `True` will only be returned if *every* provided word is in the dictionary.

```Python
>>> ipa.isin_cmu("The dentist opened a new practice.")
True
>>> ipa.isin_cmu("emoji")
False
```
   
#### `get_rhymes`

The `get_rhymes` function returns a list of rhymes for a word or set of words. 
```Python
>>> ipa.get_rhymes("rhyming function")
[['climbing', 'diming', 'liming', 'priming', 'timing'], ['compunction', 'conjunction', 'dysfunction', 'injunction', 'junction', 'malfunction']]
```
*Use the `jhymes` function instead to force usage of the JSON database.*
   
#### `syllable_count`

The `syllable_count` function returns an integer, corresponding to the number of syllables in a word. Returns a list of 
syllable counts if more than one word is provided in the input string.

```Python
>>> ipa.syllable_count("computer programming")
[3, 3]
```

### Other Resources

For another Python package that offers support for rhyming and syllable counts (as well as other cool things), see [pronouncingpy](https://github.com/aparrish/pronouncingpy).
Further dictionaries: https://github.com/Kyubyong/pron_dictionaries
