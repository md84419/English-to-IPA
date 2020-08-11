# -*- coding: utf-8 -*-

# USAGE:
# PYTHONPATH=".." python test_tokenize.py 

from eng_to_ipa import tokenize
import copy, os, unittest

SYMBOLS_FILE1 = "cmu.symbols.txt"

tokenize.configure( os.path.join(os.path.abspath(os.path.dirname(__file__)),
                         '..','eng_to_ipa','resources','CMU_source_files',SYMBOLS_FILE1) )
                         
                         

ipa1 = [['ˈtiʧər']]
tok1 = [["ˈt i ʧ ə r"]]

ipa2 = [['ˈɑrdˌvɑrk']]
tok2 = [["ˈɑr d ˌv ɑr k"]]

ipa3 = [['ði', 'ðə'], ['beɪʒ'], ['hju'], ['ɑn', 'ɔn'], ['ði', 'ðə'], ['ˈwɔtərz'], ['əv'], ['ði', 'ðə'], ['lɑk'], ['ˌɪmˈprɛst'], ['ɔl'],
    ['ˌɪnˈkludɪŋ'], ['ði', 'ðə'], ['frɛnʧ'], ['kwin'], ['bɪˈfɔr', 'ˌbiˈfɔr'], ['ʃi'], ['hərd'], ['ðæt', 'ðət'], ['ˈsɪmfəni'], ['əˈgeɪn', 'əˈgɛn'],
    ['ʤəst', 'ʤɪst'], ['æz', 'ɛz'], ['jəŋ'], ['ˈɑrθər'], ['ˈwɔntɪd']]
tok3 = [['ð i', 'ð ə'], ['b eɪ ʒ'], ['h j u'], ['ɑ n', 'ɔ n'], ['ð i', 'ð ə'], ['ˈw ɔ t ə r z'], ['ə v'], ['ð i', 'ð ə'], ['l ɑ k'], ['ˌɪ m ˈp r ɛ s t'],
    ['ɔ l'], ['ˌɪ n ˈk l u d ɪ ŋ'], ['ð i', 'ð ə'], ['f r ɛ n ʧ'], ['k w i n'], ['b ɪ ˈf ɔr', 'ˌb i ˈf ɔr'], ['ʃ i'], ['h ə r d'], ['ð æ t', 'ð ə t'],
    ['ˈs ɪ m f ə n i'], ['ə ˈg eɪ n', 'ə ˈg ɛ n'], ['ʤ ə s t', 'ʤ ɪ s t'], ['æ z', 'ɛ z'], ['j ə ŋ'], ['ˈɑr θ ə r'], ['ˈw ɔ n t ɪ d']]



class TestConversion(unittest.TestCase):
    """Simple unit testing for the transcribe function(s)."""

    def test_tokenize_teacher(self):
        res1 = copy.deepcopy( ipa1 )
        for word in range(len(ipa1)):
            for idx in range(len(ipa1[word])):
                res1[word][idx] = ( tokenize.tokenize(ipa1[word][idx]))
        self.assertEqual(res1, tok1)

    def test_tokenize_aardvark(self):
        res2 = copy.deepcopy( ipa2 )
        for word in range(len(ipa2)):
            for idx in range(len(ipa2[word])):
                res2[word][idx] = ( tokenize.tokenize(ipa2[word][idx]))
        self.assertEqual(res2, tok2)

    def test_tokenize_panagram(self):
        res3 = copy.deepcopy( ipa3 )
        for word in range(len(ipa3)):
            for idx in range(len(ipa3[word])):
                res3[word][idx] = (tokenize.tokenize(ipa3[word][idx]))
        self.assertEqual(res3, tok3)

if __name__ == "__main__":
    unittest.main()
