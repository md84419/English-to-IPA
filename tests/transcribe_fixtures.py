# -*- coding: utf-8 -*-

# USAGE:
# PYTHONPATH=".." python test_transcribe.py 

from eng_to_ipa import transcribe
import unittest

class BaseConversion(unittest.TestCase):
    """Simple unit testing for the transcribe function(s)."""

    def test_get_cmu_teacher(self):
        transcribe.set_language( self.lang )
        res1 = transcribe.get_entries(self.words1, db_type='sql', language=self.lang, token_marking='spaces')
        res2 = transcribe.get_entries(self.words1, db_type='json', language=self.lang, token_marking='spaces')
        self.assertEqual(res1, self.cmu1_spaces)
        self.assertEqual(res2, self.cmu1_spaces)
        self.assertEqual(res1, res2)

    def test_cmu_to_ipa_teacher(self):
        transcribe.set_language( self.lang )
        res1 = transcribe.cmu_to_ipa( self.cmu1, stress_marking='both')
        #self.assertEqual(res1, self.ipa1)

    def test_get_cmu_aardvark(self):
        res1 = transcribe.get_entries(self.words2, db_type='sql', language=self.lang, token_marking='none')
        res2 = transcribe.get_entries(self.words2, db_type='json', language=self.lang, token_marking='none')
        self.assertEqual(res1, self.cmu2)
        self.assertEqual(res2, self.cmu2)
        self.assertEqual(res1, res2)

    def test_cmu_to_ipa_aardvark(self):
        transcribe.set_language( self.lang )
        res1 = transcribe.cmu_to_ipa( self.cmu2, stress_marking='both')
        self.assertEqual(res1, self.ipa2)

    def test_get_cmu_again(self):
        res1 = transcribe.get_entries(self.words4, db_type='sql', language=self.lang, token_marking='symbols')
        res2 = transcribe.get_entries(self.words4, db_type='json', language=self.lang, token_marking='symbols')
        self.assertEqual(res1, self.cmu4)
        self.assertEqual(res2, self.cmu4)
        self.assertEqual(res1, res2)

    def test_cmu_to_ipa_again(self):
        transcribe.set_language( self.lang )
        res1 = transcribe.cmu_to_ipa( self.cmu4, stress_marking='both', sorted_list=False)
        self.assertEqual(res1, self.ipa4)

    def test_get_cmu_the(self):
        res1 = transcribe.get_entries(self.words5, db_type='sql', language=self.lang, token_marking='spaces')
        res2 = transcribe.get_entries(self.words5, db_type='json', language=self.lang, token_marking='spaces')
        res3 = transcribe.get_entries(self.words5, db_type='sql', language=self.lang, token_marking='none')
        res4 = transcribe.get_entries(self.words5, db_type='json', language=self.lang, token_marking='none')
        res5 = transcribe.get_entries(self.words5, db_type='sql', language=self.lang, token_marking='symbols')
        res6 = transcribe.get_entries(self.words5, db_type='json', language=self.lang, token_marking='symbols')
        self.assertEqual(res1, self.cmu5_spaces)
        self.assertEqual(res2, self.cmu5_spaces)
        self.assertEqual(res3, self.cmu5_none)
        self.assertEqual(res4, self.cmu5_none)
        self.assertEqual(res5, self.cmu5)
        self.assertEqual(res6, self.cmu5)
        self.assertEqual(res1, res2)
        self.assertEqual(res3, res4)
        self.assertEqual(res5, res6)

    def test_cmu_to_ipa_the(self):
        transcribe.set_language( self.lang )
        res1 = transcribe.cmu_to_ipa( self.cmu5_none, stress_marking='both', sorted_list=False, token_marking='none')
        self.assertEqual(res1, self.ipa5_none)

    def test_get_cmu_loch(self):
        res1 = transcribe.get_entries(self.words6, db_type='sql', language=self.lang, token_marking='none')
        res2 = transcribe.get_entries(self.words6, db_type='json', language=self.lang, token_marking='none')
        self.assertEqual(res1, self.cmu6)
        self.assertEqual(res2, self.cmu6)
        self.assertEqual(res1, res2)

    def test_cmu_to_ipa_loch(self):
        transcribe.set_language( self.lang )
        res1 = transcribe.cmu_to_ipa( self.cmu6, stress_marking='both')
        self.assertEqual(res1, self.ipa6)

    def test_get_cmu_panagram(self):
        res1 = transcribe.get_entries(self.words3, db_type='sql', language=self.lang, token_marking='spaces')
        res2 = transcribe.get_entries(self.words3, db_type='json', language=self.lang, token_marking='spaces')
        self.assertEqual(res1, self.cmu3_spaces)
        self.assertEqual(res2, self.cmu3_spaces)
        self.assertEqual(res1, res2)

    def test_cmu_to_ipa_panagram(self):
        transcribe.set_language( self.lang )
        res1 = transcribe.cmu_to_ipa( self.cmu3_spaces, stress_marking='both', sorted_list=False, token_marking='spaces')
        res2 = transcribe.cmu_to_ipa( self.cmu3_none, stress_marking='both', sorted_list=False, token_marking='none')
        res3 = transcribe.cmu_to_ipa( self.cmu3, stress_marking='both', sorted_list=False, token_marking='symbols')
        self.assertEqual(res1, self.ipa3_spaces)
        self.assertEqual(res2, self.ipa3_none)
        self.assertEqual(res3, self.ipa3)
        
if __name__ == "__main__":
    unittest.main()
