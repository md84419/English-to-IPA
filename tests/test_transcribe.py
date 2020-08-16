# -*- coding: utf-8 -*-

# USAGE:
# PYTHONPATH=".." python test_transcribe.py 

from eng_to_ipa import transcribe
import transcribe_fixtures
import sys

words1 = "teacher".split()
words2 = "aardvark".split()

words3 = "The beige hue on the waters of the loch impressed all, including the French queen, before she heard that symphony again, just as young Arthur wanted"
words3 = [transcribe.preserve_punc(w.lower())[0] for w in words3.split()]
words3 = [w[1] for w in words3]

class TestConversion_default(transcribe_fixtures.BaseConversion):
    @classmethod
    def setUpClass(self):
        self.words1 = words1
        self.cmu1 = [['t iy1 ch er0']]
        self.ipa1 = [['ˈtiʧər']]
        
        self.words2 = words2
        self.cmu2 = [['aa1 r d v aa2 r k']]
        self.ipa2 = [['ˈɑrdˌvɑrk']]
        
        self.words3 = words3

        self.cmu3 = [['dh ah0', 'dh ah1', 'dh iy0'], ['b ey1 zh'], ['hh y uw1'], ['aa1 n', 'ao1 n'], ['dh ah0', 'dh ah1', 'dh iy0'],
            ['w ao1 t er0 z'], ['ah1 v', 'ah0 v'], ['dh ah0', 'dh ah1', 'dh iy0'], ['l aa1 k'], ['ih2 m p r eh1 s t'], ['ao1 l'],
            ['ih2 n k l uw1 d ih0 ng'], ['dh ah0', 'dh ah1', 'dh iy0'], ['f r eh1 n ch'], ['k w iy1 n'], ['b ih0 f ao1 r', 'b iy2 f ao1 r'],
            ['sh iy1'], ['hh er1 d'], ['dh ae1 t', 'dh ah0 t'], ['s ih1 m f ah0 n iy0'], ['ah0 g eh1 n', 'ah0 g ey1 n'], ['jh ah1 s t', 'jh ih0 s t'],
            ['ae1 z', 'eh1 z'], ['y ah1 ng'], ['aa1 r th er0'], ['w ao1 n t ih0 d']]
        self.ipa3 = [['ði', 'ðə'], ['beɪʒ'], ['hju'], ['ɑn', 'ɔn'], ['ði', 'ðə'], ['ˈwɔtərz'], ['əv'], ['ði', 'ðə'], ['lɑk'], ['ˌɪmˈprɛst'], ['ɔl'],
            ['ˌɪnˈkludɪŋ'], ['ði', 'ðə'], ['frɛnʧ'], ['kwin'], ['bɪˈfɔr', 'ˌbiˈfɔr'], ['ʃi'], ['hərd'], ['ðæt', 'ðət'], ['ˈsɪmfəni'], ['əˈgeɪn', 'əˈgɛn'],
            ['ʤəst', 'ʤɪst'], ['æz', 'ɛz'], ['jəŋ'], ['ˈɑrθər'], ['ˈwɔntɪd']]
        
        self.lang = None
    
class TestConversion_CMU(transcribe_fixtures.BaseConversion):
    @classmethod
    def setUpClass(self):
        
        self.words1 = words1
        self.cmu1 = [['t iy1 ch er0']]
        self.ipa1 = [['ˈtiʧər']]
        
        self.words2 = words2
        self.cmu2 = [['aa1 r d v aa2 r k']]
        self.ipa2 = [['ˈɑrdˌvɑrk']]

        self.words3 = words3

        self.cmu3 = [['dh ah0', 'dh ah1', 'dh iy0'], ['b ey1 zh'], ['hh y uw1'], ['aa1 n', 'ao1 n'], ['dh ah0', 'dh ah1', 'dh iy0'],
            ['w ao1 t er0 z'], ['ah1 v', 'ah0 v'], ['dh ah0', 'dh ah1', 'dh iy0'], ['l aa1 k'], ['ih2 m p r eh1 s t'], ['ao1 l'],
            ['ih2 n k l uw1 d ih0 ng'], ['dh ah0', 'dh ah1', 'dh iy0'], ['f r eh1 n ch'], ['k w iy1 n'], ['b ih0 f ao1 r', 'b iy2 f ao1 r'],
            ['sh iy1'], ['hh er1 d'], ['dh ae1 t', 'dh ah0 t'], ['s ih1 m f ah0 n iy0'], ['ah0 g eh1 n', 'ah0 g ey1 n'], ['jh ah1 s t', 'jh ih0 s t'],
            ['ae1 z', 'eh1 z'], ['y ah1 ng'], ['aa1 r th er0'], ['w ao1 n t ih0 d']]
        self.ipa3 = [['ði', 'ðə'], ['beɪʒ'], ['hju'], ['ɑn', 'ɔn'], ['ði', 'ðə'], ['ˈwɔtərz'], ['əv'], ['ði', 'ðə'], ['lɑk'], ['ˌɪmˈprɛst'], ['ɔl'],
            ['ˌɪnˈkludɪŋ'], ['ði', 'ðə'], ['frɛnʧ'], ['kwin'], ['bɪˈfɔr', 'ˌbiˈfɔr'], ['ʃi'], ['hərd'], ['ðæt', 'ðət'], ['ˈsɪmfəni'], ['əˈgeɪn', 'əˈgɛn'],
            ['ʤəst', 'ʤɪst'], ['æz', 'ɛz'], ['jəŋ'], ['ˈɑrθər'], ['ˈwɔntɪd']]
            
        self.lang = 'CMU'
    
class TestConversion_en_GB(transcribe_fixtures.BaseConversion):
    @classmethod
    def setUpClass(self):
        self.maxDiff = None
        
        self.words1 = words1
        self.cmu1 = self.ipa1 = [['t ˈiː t\u200dʃ ɐ', 't ˈiː t\u200dʃ ə']]

        self.words2 = words2
        self.cmu2 = self.ipa2 = [['ˈɑː d v ɑː k']]
        
        self.words3 = words3

        self.cmu3 = self.ipa3 = [['ð ə', 'ð iː', 'ð ˈiː'], ['b ˈe‍ɪ ʒ'], ['h j ˈuː'], ['ˈɒ n'], ['ð ə', 'ð iː', 'ð ˈiː'], ['w ˈɔː t ə z'], ['ˈɒ v', 'ə v'],
            ['ð ə', 'ð iː', 'ð ˈiː'], ['l ˈɒ k'], ['ɪ m p r ˈe s t'], ['ˈɔː l'], ['ɪ n k l ˈuː d ɪ ŋ'], ['ð ə', 'ð iː', 'ð ˈiː'], ['f r ˈe n t\u200dʃ'],
            ['k w ˈiː n'], ['b ɪ f ˈɔː'], ['ʃ ˈiː'], ['h ˈɜː d'], ['ð ˈæ t', 'ð ə t'], ['s ˈɪ m f ə n ˌ i', 's ˈɪ m f ə n iː'],
            ['ɐ ɡ ˈe n', 'ə g ˈe n', 'ə g ˈe‍ɪ n'], ['d\u200dʒ ˈʌ s t', 'd\u200dʒ ə s t', 'd\u200dʒ ˈɐ s t'], ['ˈæ z', 'ə z'],['j ˈʌ ŋ', 'j ˈɐ ŋ'], ['ˈɑː θ ə'], ['w ˈɒ n t ɪ d']]
            
        self.lang = 'en_GB'

class TestConversion_en_US(transcribe_fixtures.BaseConversion):
    @classmethod
    def setUpClass(self):
        self.maxDiff = None
        
        self.words1 = words1
        self.cmu1 = self.ipa1 = [['ˈt iː t‍ʃ ə r']]
        
        self.words2 = words2
        self.cmu2 = self.ipa2 = [['ˈɒ r d ˌv ɒ r k']]
        
        self.words3 = words3

        self.cmu3 = self.ipa3 = [['ð ə', 'ð iː'], ['b e‍ɪ ʒ'], ['h j uː'], ['ɒ n', 'ɔː n'], ['ð ə', 'ð iː'], ['ˈw ɔː t ə r z'], ['ə v'], ['ð ə', 'ð iː'],
            ['l ɒ k'], ['ˌɪ m ˈp r e s t'], ['ɔː l'], ['ˌɪ n ˈk l uː d ɪ ŋ'], ['ð ə', 'ð iː'], ['f r e n t‍ʃ'], ['k w iː n'], ['b ɪ ˈf ɔː r', 'ˌb iː ˈf ɔː r'], ['ʃ iː'], ['h ə r d'],
            ['ð æ t', 'ð ə t'], ['ˈs ɪ m f ə n iː'], ['ə ˈg e n', 'ə ˈg e‍ɪ n'], ['d‍ʒ ə s t', 'd‍ʒ ɪ s t'], ['æ z', 'e z'], ['j ə ŋ'], ['ˈɒ r θ ə r'], ['ˈw ɔː n t ɪ d']]
            
        self.lang = 'en_US'
        
#if __name__ == "__main__":
#    unittest.main()
