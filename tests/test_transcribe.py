# -*- coding: utf-8 -*-

# USAGE:
# PYTHONPATH=".." python test_transcribe.py 

from eng_to_ipa import transcribe
import unittest

words1 = "teacher".split()
cmu1 = [['t iy1 ch er0']]
ipa1 = [['ˈtiʧər']]

words2 = "aardvark".split()
cmu2 = [['aa1 r d v aa2 r k']]
ipa2 = [['ˈɑrdˌvɑrk']]

words3 = "The beige hue on the waters of the loch impressed all including the French queen before she heard that symphony again just as young Arthur wanted".lower().split()
cmu3 = [['dh ah0', 'dh ah1', 'dh iy0'], ['b ey1 zh'], ['hh y uw1'], ['aa1 n', 'ao1 n'], ['dh ah0', 'dh ah1', 'dh iy0'],
    ['w ao1 t er0 z'], ['ah1 v', 'ah0 v'], ['dh ah0', 'dh ah1', 'dh iy0'], ['l aa1 k'], ['ih2 m p r eh1 s t'], ['ao1 l'],
    ['ih2 n k l uw1 d ih0 ng'], ['dh ah0', 'dh ah1', 'dh iy0'], ['f r eh1 n ch'], ['k w iy1 n'], ['b ih0 f ao1 r', 'b iy2 f ao1 r'],
    ['sh iy1'], ['hh er1 d'], ['dh ae1 t', 'dh ah0 t'], ['s ih1 m f ah0 n iy0'], ['ah0 g eh1 n', 'ah0 g ey1 n'], ['jh ah1 s t', 'jh ih0 s t'],
    ['ae1 z', 'eh1 z'], ['y ah1 ng'], ['aa1 r th er0'], ['w ao1 n t ih0 d']]
ipa3 = [['ði', 'ðə'], ['beɪʒ'], ['hju'], ['ɑn', 'ɔn'], ['ði', 'ðə'], ['ˈwɔtərz'], ['əv'], ['ði', 'ðə'], ['lɑk'], ['ˌɪmˈprɛst'], ['ɔl'],
    ['ˌɪnˈkludɪŋ'], ['ði', 'ðə'], ['frɛnʧ'], ['kwin'], ['bɪˈfɔr', 'ˌbiˈfɔr'], ['ʃi'], ['hərd'], ['ðæt', 'ðət'], ['ˈsɪmfəni'], ['əˈgeɪn', 'əˈgɛn'],
    ['ʤəst', 'ʤɪst'], ['æz', 'ɛz'], ['jəŋ'], ['ˈɑrθər'], ['ˈwɔntɪd']]

class TestConversion(unittest.TestCase):
    """Simple unit testing for the transcribe function(s)."""

    def test_get_cmu_teacher(self):
        res1 = transcribe.get_cmu(words1, db_type='sql')
        res2 = transcribe.get_cmu(words1, db_type='json')
        self.assertEqual(res1, cmu1)
        self.assertEqual(res2, cmu1)
        self.assertEqual(res1, res2)

    def test_cmu_to_ipa_teacher(self):
        res1 = transcribe.cmu_to_ipa( cmu1, stress_marking='both' )
        self.assertEqual(res1, ipa1)

    def test_get_cmu_aardvark(self):
        res1 = transcribe.get_cmu(words2, db_type='sql')
        res2 = transcribe.get_cmu(words2, db_type='json')
        self.assertEqual(res1, cmu2)
        self.assertEqual(res2, cmu2)
        self.assertEqual(res1, res2)

    def test_cmu_to_ipa_aardvark(self):
        res1 = transcribe.cmu_to_ipa( cmu2, stress_marking='both' )
        self.assertEqual(res1, ipa2)

    def test_get_cmu_panagram(self):
        res1 = transcribe.get_cmu(words3, db_type='sql')
        res2 = transcribe.get_cmu(words3, db_type='json')
        self.assertEqual(res1, cmu3)
        self.assertEqual(res2, cmu3)
        self.assertEqual(res1, res2)

    def test_cmu_to_ipa_panagram(self):
        res1 = transcribe.cmu_to_ipa( cmu3, stress_marking='both' )
        self.assertEqual(res1, ipa3)

if __name__ == "__main__":
    unittest.main()
