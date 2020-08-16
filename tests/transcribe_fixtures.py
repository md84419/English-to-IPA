# -*- coding: utf-8 -*-

# USAGE:
# PYTHONPATH=".." python test_transcribe.py 

from eng_to_ipa import transcribe
import unittest

class BaseConversion(unittest.TestCase):
    """Simple unit testing for the transcribe function(s)."""

    def test_get_cmu_teacher(self):
        res1 = transcribe.get_entries(self.words1, db_type='sql', language=self.lang)
        res2 = transcribe.get_entries(self.words1, db_type='json', language=self.lang)
        self.assertEqual(res1, self.cmu1)
        self.assertEqual(res2, self.cmu1)
        self.assertEqual(res1, res2)

    def test_cmu_to_ipa_teacher(self):
        transcribe.set_language( self.lang )
        res1 = transcribe.cmu_to_ipa( self.cmu1, stress_marking='both')
        self.assertEqual(res1, self.ipa1)

    def test_get_cmu_aardvark(self):
        res1 = transcribe.get_entries(self.words2, db_type='sql', language=self.lang)
        res2 = transcribe.get_entries(self.words2, db_type='json', language=self.lang)
        self.assertEqual(res1, self.cmu2)
        self.assertEqual(res2, self.cmu2)
        self.assertEqual(res1, res2)

    def test_cmu_to_ipa_aardvark(self):
        transcribe.set_language( self.lang )
        res1 = transcribe.cmu_to_ipa( self.cmu2, stress_marking='both')
        self.assertEqual(res1, self.ipa2)

    def test_get_cmu_panagram(self):
        res1 = transcribe.get_entries(self.words3, db_type='sql', language=self.lang)
        res2 = transcribe.get_entries(self.words3, db_type='json', language=self.lang)
        self.assertEqual(res1, self.cmu3)
        self.assertEqual(res2, self.cmu3)
        self.assertEqual(res1, res2)

    def test_cmu_to_ipa_panagram(self):
        transcribe.set_language( self.lang )
        res1 = transcribe.cmu_to_ipa( self.cmu3, stress_marking='both', sorted_list=False)
        self.assertEqual(res1, self.ipa3)
        
if __name__ == "__main__":
    unittest.main()
