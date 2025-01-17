# -*- coding: utf-8 -*-
import ast, copy, logging, os, re, sys
from os.path import join, abspath, dirname
from num2words import num2words
import eng_to_ipa.stress as stress
from collections import defaultdict, OrderedDict

logging.basicConfig(format='%(message)s', level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger(__name__)

class ModeType(object):

    def __init__(self, mode):
        self.name = mode
        if mode.lower() == "sql":
            import sqlite3
            conn = sqlite3.connect(join(abspath(dirname(__file__)),
                                        "./resources/" + lang.dict + ".db"))
            self.mode = conn.cursor()
        elif mode.lower() == "json":
            import json
            with open(join(abspath(dirname(__file__)),
                                  "../eng_to_ipa/resources/" + lang.dict + ".json"),
                             encoding="UTF-8") as json_file:
              self.mode = json.load(json_file)

    def __str__(self):
        return self.name


class Language(object):

    def __init__(self, lang='cmu'):
        if lang:
            self.lang = lang = lang.lower()
        else:
            self.lang = lang = 'cmu'
        self.dict = ''
        if lang == "cmu":
            self.lang = 'en-US'
            self.dict = 'CMU_dict'
        elif lang == "en-us":
            self.lang = 'en-US'
            self.dict = 'en_US'
        elif lang == "en-gb":
            self.lang = 'en-GB'
            self.dict = 'en_GB'
        else:
            log.error("Language '{0}' not recognised.".format( lang ))
            sys.exit(2)

    def __str__(self):
        return self.lang

        
lang = Language()


def set_language(language='cmu'):
    global lang
    if( language ):
        lang = Language(language)
    
def preprocess(words):
    """Returns a string of words stripped of punctuation"""
    punct_str = '!"#$%&\'()*+,-./:;<=>/?@[\\]^_`{|}~«» …'
    return ' '.join([w.strip(punct_str).lower() for w in words.split()])


def preserve_punc(words):
    """converts words to IPA and finds punctuation before and after the word."""
    words_preserved = []
    for w in words.split():
        punct_list = ["", preprocess(w), ""]
        before = re.search(r"^([^A-Za-z0-9]+)[A-Za-z]", w)
        after = re.search(r"[A-Za-z]([^A-Za-z0-9]+)$", w)
        if before:
            punct_list[0] = str(before.group(1))
        if after:
            punct_list[2] = str(after.group(1))
        words_preserved.append(punct_list)
    return words_preserved


def apply_punct(triple, as_str=False):
    """places surrounding punctuation back on center on a list of preserve_punc triples"""
    if type(triple[0]) == list:
        for i, t in enumerate(triple):
            triple[i] = str(''.join(triple[i]))
        if as_str:
            return ' '.join(triple)
        return triple
    if as_str:
        return str(''.join(t for t in triple))
    return [''.join(t for t in triple)]


def _punct_replace_word(original, transcription):
    """Get the IPA transcription of word with the original punctuation marks"""
    for i, trans_list in enumerate(transcription):
        for j, item in enumerate(trans_list):
            triple = [original[i][0]] + [item] + [original[i][2]]
            transcription[i][j] = apply_punct(triple, as_str=True)
    return transcription


def fetch_words(words_in, db_type="sql", token_marking="none"):
    """fetches a list of words from the database"""
    # token_marking = 'none' is the default...
    replace = ''
    if token_marking == 'none':
        replace = ''
    if token_marking == 'spaces':
        replace = ' '
    asset = ModeType(mode=db_type).mode
    if db_type.lower() == "sql":
        quest = "?, " * len(words_in)
        asset.execute("SELECT word, phonemes FROM dictionary "
                      "WHERE word IN ({0})".format(quest[:-2]), words_in)
        result = asset.fetchall()
        d = defaultdict(list)
        for k, v in result:
            if( lang.dict == 'CMU_dict'):
                d[k].append(v)
            else:
                v = ast.literal_eval(v)
                for val in v:
                    # if token_marking == 'symbols', leave the 'ˑ' characters in the results
                    if token_marking == 'none' or token_marking == 'spaces':
                        val = val.replace('ˑ', replace)
                    d[k].append(val)
        return list(d.items())
    if db_type.lower() == "json":
        words = []
        for k, v in asset.items():
            if k in words_in:
                # if token_marking == 'symbols', leave the 'ˑ' characters in the results
                if token_marking == 'none' or token_marking == 'spaces':
                    for idx in range( len(v) ):
                        v[idx] = v[idx].replace('ˑ', replace)
                words.append((k, v))
        return words

def get_cmu(tokens_in, db_type="sql"):
    return get_entries(tokens_in, db_type, language='cmu')

def get_entries(tokens_in, db_type="sql", language='cmu', token_marking='none'):
    """query the SQL database for the words and return the phonemes in the order of user_in"""
    result = fetch_words(tokens_in, db_type, token_marking)
    ordered = []
    space = ''

    if language == 'cmu':
        space = ' '

    for word in tokens_in:
        this_word = [[i[1] for i in result if i[0] == word]][0]
        if this_word:
            ordered.append(this_word[0])
        else:
            # word not found in dict
            # is it all numbers?
            if( language != 'cmu' and re.match( r"\d", word) ):
                tmpresult = re.sub(r"(?<![\-\d])(0+\d+)", lambda x: _phone( x.group(1)), word )
                tmpresult = re.sub(r"([\-\.])(0+\d+)", lambda x: x.group(1) + _phone( x.group(2)), tmpresult )
                tmpresult = re.sub(r"(?<![\-\d])(\d+)", lambda x: num2words( int(x.group(1))), tmpresult )
                tmpresult = re.sub(r"([\-\.])(\d+)", lambda x: x.group(1) + num2words( int(x.group(2))), tmpresult )
                tmpresult = get_entries( tmpresult.split(' '), db_type=db_type, language=language )
                if( language == 'cmu' ):
                    # @TODO: @FIXME
                    print('lang is cmu')
                    ordered.append(['1'])
                else:
                    for word in tmpresult:
                        ordered.append( word )
            # is it a letter followed by numbers?
            elif( re.match( r"([a-z]+)(\d+)\Z", word) ):
                # try the letters and numbers seperately
                x = re.match(r"([a-z]+)(\d+)\Z", word)
                tmpresult = get_entries( [x.group(1), x.group(2)] , db_type=db_type, language=language )
                if not tmpresult[0][0].startswith('__IGNORE__') and not tmpresult[1][0].startswith('__IGNORE__'):
                    this_word = []
                    for this_word1 in tmpresult[0]:
                        for this_word2 in tmpresult[1]:
                            this_word.append(this_word1 + space + this_word2)
                    ordered.append(this_word)
                else:
                    ordered.append(["__IGNORE__" + word])
            elif( word.find('-') != -1 ):
                # we couldn't transliterate a hyphenated word - try word parts
                tmpresult = get_entries( word.split('-'), db_type=db_type, language=language )
                if not tmpresult[0][0].startswith('__IGNORE__') and not tmpresult[1][0].startswith('__IGNORE__'):
                    this_word = []
                    for this_word1 in tmpresult[0]:
                        for this_word2 in tmpresult[1]:
                            this_word.append(this_word1 + space + this_word2)
                    ordered.append(this_word)
                else:
                    ordered.append(["__IGNORE__" + word])
            else:
                ordered.append(["__IGNORE__" + word])
    return ordered

def _phone(number):
    numbers = ['zero', 'one', 'two', 'three', 'four',
               'five', 'six', 'seven', 'eight', 'nine']
    return ' '.join(numbers[c] for c in map(int, number))

def cmu_to_ipa(dict_list, mark=True, stress_marking='all', sorted_list=True, token_marking='none'):
    """converts the CMU word lists into IPA transcriptions"""
    return dict_to_ipa(dict_list, mark, stress_marking, sorted_list, token_marking)

def dict_to_ipa(dict_list, mark=True, stress_marking='all', sorted_list=True, token_marking='none'):
    """converts the dictionary entries into eng-to-ipa format IPA transcriptions"""
    symbols = {"a": "ə", "ey": "eɪ", "aa": "ɑ", "ae": "æ", "ah": "ə", "ao": "ɔ",
               "aw": "aʊ", "ay": "aɪ", "ch": "ʧ", "dh": "ð", "eh": "ɛ", "er": "ər",
               "hh": "h", "ih": "ɪ", "jh": "ʤ", "ng": "ŋ",  "ow": "oʊ", "oy": "ɔɪ",
               "sh": "ʃ", "th": "θ", "uh": "ʊ", "uw": "u", "zh": "ʒ", "iy": "i", "y": "j"}
    final_list = []  # the final list of IPA tokens to be returned
    if stress_marking:
        stress_marking = stress_marking.lower()
    for word_list in dict_list:
        ipa_word_list = []  # the word list for each word
        for word in word_list:
            if lang.dict == 'CMU_dict' and stress_marking and stress_marking != 'none':
                word = stress.find_stress(word, type=stress_marking)
            else:
                if( not stress_marking or stress_marking != 'both' ):
                    word = stress.keep_stress(word, type=stress_marking)
                if re.sub(r"\d*", "", word.replace("__IGNORE__", "")) == "":
                    pass  # do not delete token if it's all numbers
                else:
                    word = re.sub("[0-9]", "", word)
            ipa_form = ''
            if word.startswith("__IGNORE__"):
                ipa_form = word.replace("__IGNORE__", "")
                # mark words we couldn't transliterate with an asterisk:
                if mark:
                    if not re.sub(r"\d*", "", ipa_form) == "":
                        ipa_form += "*"
            else:
                if lang.dict == 'CMU_dict':
                    for piece in word.split(" "):
                        marked = False
                        unmarked = piece
                        if piece[0] in ["ˈ", "ˌ"]:
                            marked = True
                            mark = piece[0]
                            unmarked = piece[1:]
                        if unmarked in symbols:
                            if marked:
                                ipa_form += mark + symbols[unmarked]
                            else:
                                ipa_form += symbols[unmarked]
                        else:
                            ipa_form += piece
                else:
                    ipa_form += word
            if lang.dict == 'CMU_dict':
                swap_list = [["ˈər", "əˈr"], ["ˈie", "iˈe"]]
                for sym in swap_list:
                    if not ipa_form.startswith(sym[0]):
                        ipa_form = ipa_form.replace(sym[0], sym[1])
            ipa_word_list.append(ipa_form)
        if sorted_list:
            final_list.append(sorted(list(OrderedDict.fromkeys(ipa_word_list))))
        else:
            final_list.append(list(OrderedDict.fromkeys(ipa_word_list)))
    return final_list


def get_top(ipa_list):
    """Returns only the one result for a query. If multiple entries for words are found, only the last is used."""
    return ' '.join([word_list[-1] for word_list in ipa_list])


def get_all(ipa_list):
    """utilizes an algorithm to discover and return all possible combinations of IPA transcriptions"""
    final_size = 1
    for word_list in ipa_list:
        final_size *= len(word_list)
    list_all = ["" for s in range(final_size)]
    for i in range(len(ipa_list)):
        if i == 0:
            swtich_rate = final_size / len(ipa_list[i])
        else:
            swtich_rate /= len(ipa_list[i])
        k = 0
        for j in range(final_size):
            if (j+1) % int(swtich_rate) == 0:
                k += 1
            if k == len(ipa_list[i]):
                k = 0
            list_all[j] = list_all[j] + ipa_list[i][k] + " "
    return sorted([sent[:-1] for sent in list_all])


def ipa_list(words_in, keep_punct=True, stress_marks='both', db_type="sql", language='cmu', sorted_list=True, token_marking='none'):
    """Returns a list of all the discovered IPA transcriptions for each word."""
    global lang
    lang = Language(language)
    words = [preserve_punc(w.lower())[0] for w in words_in.split()] \
        if type(words_in) == str else [preserve_punc(w.lower())[0] for w in words_in]
    dct = get_entries([w[1] for w in words], db_type=db_type, language=language, token_marking=token_marking)
    ipa = dict_to_ipa(dct, stress_marking=stress_marks, sorted_list=sorted_list)
    if language == 'cmu' and keep_punct:
        ipa = _punct_replace_word(words, ipa)
    return ipa


def isin_cmu(word, db_type="sql"):
    """checks if a word is in the CMU dictionary. Doesn't strip punctuation.
    If given more than one word, returns True only if all words are present."""
    return(isin_dict(word,db_type,'cmu'))
    
def isin_dict(word, db_type="sql", language='cmu'):
    """checks if a word is in the dictionary. Doesn't strip punctuation.
    If given more than one word, returns True only if all words are present."""
    if type(word) == str:
        word = [preprocess(w) for w in word.split()]
    results = fetch_words(word, db_type)
    as_set = list(set(t[0] for t in results))
    return len(as_set) == len(set(word))


def contains(ipa, db_type="sql"):
    """Get any words that contain the IPA string. Returns the word and the IPA as a list."""
    asset = ModeType(mode=db_type).mode
    if db_type.lower() == "sql":
        asset.execute("SELECT word, ipa FROM eng_ipa WHERE "
                      "REPLACE(REPLACE(ipa, 'ˌ', ''), 'ˈ', '') "
                      "LIKE \"%{}%\"".format(str(ipa)))
        return [list(res) for res in asset.fetchall()]


def convert(text, retrieve_all=False, keep_punct=True, stress_marks='both', mode="sql", language='cmu', sorted_list=True, token_marking='none'):
    """takes either a string or list of English words and converts them to IPA"""
    ipa = ipa_list(words_in=text, keep_punct=keep_punct,
                   stress_marks=stress_marks, db_type=mode, language=language, sorted_list=sorted_list, token_marking=token_marking)
    return get_all(ipa) if retrieve_all else get_top(ipa)


def jonvert(text, retrieve_all=False, keep_punct=True, stress_marks='both', language='cmu', sorted_list=True, token_marking='none'):
    """Forces use of JSON database for fetching phoneme data."""
    return convert(text, retrieve_all, keep_punct, stress_marks, mode="json", language=language, sorted_list=sorted_list, token_marking=token_marking)
