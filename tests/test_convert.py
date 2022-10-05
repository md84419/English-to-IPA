# -*- coding: utf-8 -*-

# USAGE:
# PYTHONPATH=".." python test_transcribe.py 

from eng_to_ipa import stress, transcribe
import unittest

class TestConversion(unittest.TestCase):
    """Simple unit testing for the convert function."""
    @classmethod
    def setUpClass(self):
        self.lang = 'en-GB'

    def test_short_sentance_second_word_consonant(self):
        test_string = "The beige hue"
        expected = "ðˈiː bˈe\u200dɪʒ hjˈuː"

        transcribe.set_language(self.lang)
        res1 = transcribe.convert( test_string, language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( test_string, language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, expected )
        self.assertEqual( res2, expected )
        self.assertEqual(res1, res2 )

    def test_short_sentance_second_word_consonant_usual(self):
        test_string = "The usual"
        expected = "ðˈiː jˈuːʒʊ\u200dəl"

        transcribe.set_language(self.lang)
        res1 = transcribe.convert( test_string, language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( test_string, language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, expected )
        self.assertEqual( res2, expected )
        self.assertEqual(res1, res2 )

    def test_short_sentance_second_word_vowel_end(self):
        test_string = "The end"
        expected = "ðˈiː ˈend"

        transcribe.set_language(self.lang)
        res1 = transcribe.convert( test_string, language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( test_string, language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, expected )
        self.assertEqual( res2, expected )
        self.assertEqual(res1, res2 )

if __name__ == "__main__":
    unittest.main()
