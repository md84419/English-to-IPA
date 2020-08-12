# -*- coding: utf-8 -*-

# USAGE:
# PYTHONPATH=".." python test_tokenize.py 

from eng_to_ipa import tokenize
import copy, os, unittest

SYMBOLS_FILE = "cmu.symbols.txt"
SYMBOLS_FILE_LEGACY = "cmu.symbols.legacy.txt"

# Legacy
ipa1 = [['ˈtiʧər']]
tok1 = [["ˈt i ʧ ə r"]]

ipa2 = [['ˈɑrdˌvɑrk']]
tok2 = [["ˈɑ r d ˌv ɑ r k"]]

ipa3 = [['ði', 'ðə'], ['beɪʒ'], ['hju'], ['ɑn', 'ɔn'], ['ði', 'ðə'], ['ˈwɔtərz'], ['əv'], ['ði', 'ðə'], ['lɑk'], ['ˌɪmˈprɛst'], ['ɔl'],
    ['ˌɪnˈkludɪŋ'], ['ði', 'ðə'], ['frɛnʧ'], ['kwin'], ['bɪˈfɔr', 'ˌbiˈfɔr'], ['ʃi'], ['hərd'], ['ðæt', 'ðət'], ['ˈsɪmfəni'], ['əˈgeɪn', 'əˈgɛn'],
    ['ʤəst', 'ʤɪst'], ['æz', 'ɛz'], ['jəŋ'], ['ˈɑrθər'], ['ˈwɔntɪd']]
tok3 = [['ð i', 'ð ə'], ['b eɪ ʒ'], ['h j u'], ['ɑ n', 'ɔ n'], ['ð i', 'ð ə'], ['ˈw ɔ t ə r z'], ['ə v'], ['ð i', 'ð ə'], ['l ɑ k'], ['ˌɪ m ˈp r ɛ s t'],
    ['ɔ l'], ['ˌɪ n ˈk l u d ɪ ŋ'], ['ð i', 'ð ə'], ['f r ɛ n ʧ'], ['k w i n'], ['b ɪ ˈf ɔr', 'ˌb i ˈf ɔr'], ['ʃ i'], ['h ə r d'], ['ð æ t', 'ð ə t'],
    ['ˈs ɪ m f ə n i'], ['ə ˈg eɪ n', 'ə ˈg ɛ n'], ['ʤ ə s t', 'ʤ ɪ s t'], ['æ z', 'ɛ z'], ['j ə ŋ'], ['ˈɑ r θ ə r'], ['ˈw ɔ n t ɪ d']]

# Modern
ipa4 = [['ˈtiːt‍ʃər']]
tok4 = [["ˈt iː t‍ʃ ə r"]]

ipa5 = [['ˈɒrdˌvɒrk']]
tok5 = [["ˈɒ r d ˌv ɒ r k"]]

ipa6 = [['ðiː', 'ðə'], ['be‍ɪʒ'], ['hju'], ['ɑn', 'ɔːn'], ['ðiː', 'ðə'], ['ˈwɔtərz'], ['əv'], ['ðiː', 'ðə'], ['lɑk'], ['ˌɪmˈprest'], ['ɔːl'],
    ['ˌɪnˈkluːdɪŋ'], ['ðiː', 'ðə'], ['frent‍ʃ'], ['kwiːn'], ['bɪˈfɔːr', 'ˌbiːˈfɔːr'], ['ʃiː'], ['hərd'], ['ðæt', 'ðət'], ['ˈsɪmfəniː'], ['əˈge‍ɪn', 'əˈgen'],
    ['d‍ʒəst', 'd‍ʒɪst'], ['æz', 'ɛz'], ['jəŋ'], ['ˈɑrθər'], ['ˈwɔːntɪd']]
tok6 = [['ð iː', 'ð ə'], ['b e‍ɪ ʒ'], ['h j u'], ['ɑ n', 'ɔː n'], ['ð iː', 'ð ə'], ['ˈw ɔ t ə r z'], ['ə v'], ['ð iː', 'ð ə'], ['l ɑ k'], ['ˌɪ m ˈp r e s t'],
    ['ɔː l'], ['ˌɪ n ˈk l uː d ɪ ŋ'], ['ð iː', 'ð ə'], ['f r e n t‍ʃ'], ['k w iː n'], ['b ɪ ˈf ɔː r', 'ˌb iː ˈf ɔː r'], ['ʃ iː'], ['h ə r d'], ['ð æ t', 'ð ə t'],
    ['ˈs ɪ m f ə n iː'], ['ə ˈg e‍ɪ n', 'ə ˈg e n'], ['d‍ʒ ə s t', 'd‍ʒ ɪ s t'], ['æ z', 'ɛ z'], ['j ə ŋ'], ['ˈɑr θ ə r'], ['ˈw ɔː n t ɪ d']]


class BaseConversion(object):
    """Simple unit testing for the transcribe function(s)."""
    def test_tokenize_teacher(self):
        res1 = copy.deepcopy( self.ipa1 )
        for word in range(len(self.ipa1)):
            for idx in range(len(self.ipa1[word])):
                res1[word][idx] = ( tokenize.tokenize(self.ipa1[word][idx]))
        self.assertEqual(res1, self.tok1)

    def test_tokenize_aardvark(self):
        res2 = copy.deepcopy( self.ipa2 )
        for word in range(len(self.ipa2)):
            for idx in range(len(self.ipa2[word])):
                res2[word][idx] = ( tokenize.tokenize(self.ipa2[word][idx]))
        self.assertEqual(res2, self.tok2)

    def test_tokenize_panagram(self):
        res3 = copy.deepcopy( self.ipa3 )
        for word in range(len(self.ipa3)):
            for idx in range(len(self.ipa3[word])):
                res3[word][idx] = (tokenize.tokenize(self.ipa3[word][idx]))
        self.assertEqual(res3, self.tok3)


class TestConversionLegacy(BaseConversion, unittest.TestCase):
    """Simple unit testing for the transcribe function(s)."""

    @classmethod
    def setUpClass(self):
        tokenize.configure( os.path.join(os.path.abspath(os.path.dirname(__file__)),
                         '..','eng_to_ipa','resources','CMU_source_files',SYMBOLS_FILE_LEGACY) )
        self.ipa1 = ipa1
        self.ipa2 = ipa2
        self.ipa3 = ipa3
        self.tok1 = tok1
        self.tok2 = tok2
        self.tok3 = tok3

class TestConversion(BaseConversion, unittest.TestCase):
    """Simple unit testing for the transcribe function(s)."""

    @classmethod
    def setUpClass(self):
        tokenize.configure( os.path.join(os.path.abspath(os.path.dirname(__file__)),
                         '..','eng_to_ipa','resources','CMU_source_files',SYMBOLS_FILE) )
        self.ipa1 = ipa4
        self.ipa2 = ipa5
        self.ipa3 = ipa6
        self.tok1 = tok4
        self.tok2 = tok5
        self.tok3 = tok6


if __name__ == "__main__":
    unittest.main()
