# -*- coding: utf-8 -*-

# USAGE:
# PYTHONPATH=".." python test_stress.py 

from eng_to_ipa import stress, transcribe
import unittest


class TestConversion(unittest.TestCase):
    """Simple unit testing for the stress functions."""
    @classmethod
    def setUpClass(self):
        self.lang = None

    def test_stress_type(self):
        self.assertEqual(stress.stress_type("primary"), {"1": "ˈ"})
        self.assertEqual(stress.stress_type("secondary"), {"2": "ˌ"})
        self.assertEqual(stress.stress_type("all"), {"1": "ˈ", "2": "ˌ"})
        self.assertEqual(stress.stress_type("both"), {"1": "ˈ", "2": "ˌ"})
        self.assertEqual(stress.stress_type("tertiary"), {"1": "ˈ", "2": "ˌ"})

    def test_find_stress(self):
        test_string = "reflect respect recline reduce obsessively demonstrate baseball cloud brother cobblestone " +\
            "complete conspire estuary"
        raw_cmu = transcribe.get_cmu(test_string.split(" "))
        result = []
        for word_list in raw_cmu:
            for word in word_list:
                stressed = stress.find_stress(word)
                result.append(stressed)
        self.assertEqual(result, ['r ah ˈf l eh k t', 'r ih ˈf l eh k t', 'r ih ˈs p eh k t', 'r iy ˈs p eh k t',
                                  'r ih ˈk l ay n', 'r ih ˈd uw s', 'aa b ˈs eh s ih v l iy',
                                  'ˈd eh m ah n ˌs t r ey t', 'ˈb ey s ˈb ao l', 'k l aw d', 'ˈb r ah dh er',
                                  'ˈk aa b ah l ˌs t ow n', 'k ah m ˈp l iy t', 'k ah n ˈs p ay er',
                                  'ˈeh s ch uw ˌeh r iy'])

        # test the retrieval of only primary stress
        self.assertEqual(stress.find_stress("d eh1 m ah0 n s t r ey2 t", type="primary"), 'ˈd eh m ah n s t r ey t')
        # test the retrieval of only secondary stress
        self.assertEqual(stress.find_stress("d eh1 m ah0 n s t r ey2 t", type="secondary"), 'd eh m ah n ˌs t r ey t')
        # test the retrieval of both stress
        self.assertEqual(stress.find_stress("dh ah0", type="both"), 'dh ah')
        #self.assertEqual(stress.find_stress("dh ah1", type="both"), 'dh ˈah')  # CMU dict provides stress for single-syllable words, eng-to-ipa currently disregards
        self.assertEqual(stress.find_stress("dh iy0", type="both"), 'dh iy')


class TestStress2(unittest.TestCase):
    """Simple unit testing for the stress functions."""
    @classmethod
    def setUpClass(self):
        self.lang = 'en-GB'

    def test_find_stress(self):
        test_string = "reflect respect recline reduce obsessively demonstrate baseball cloud brother cobblestone " +\
            "complete conspire estuary"
        dct = transcribe.get_entries(test_string.split(" "), language=self.lang)
        ipa = transcribe.dict_to_ipa( dct, stress_marking='both')
        self.assertEqual(ipa, [['rəˈflɛkt', 'rɪˈflɛkt'],
                               ['riˈspɛkt', 'rɪˈspɛkt'],
                               ['rɪˈklaɪn'],
                               ['rɪˈdus'],
                               ['ɑbˈsɛsɪvli'],
                               ['ˈdɛmənˌstreɪt'],
                               ['ˈbeɪsˈbɔl'],
                               ['klaʊd'],
                               ['ˈbrəðər'],
                               ['ˈkɑbəlˌstoʊn'],
                               ['kəmˈplit'],
                               ['kənˈspaɪər'],
                               ['ˈɛsʧuˌɛri']])

        # test the retrieval of only primary stress
        self.assertEqual(stress.keep_stress("s ˈɪ m f ə n ˌiː", type="primary"), 's ˈɪ m f ə n iː')
        # test the retrieval of only secondary stress
        self.assertEqual(stress.keep_stress("s ˈɪ m f ə n ˌiː", type="secondary"), 's ɪ m f ə n ˌiː')
        # test the retrieval of both stress
        self.assertEqual(stress.keep_stress("s ˈɪ m f ə n ˌiː", type="both"), 's ˈɪ m f ə n ˌiː')
        #self.assertEqual(stress.find_stress("dh ah1", type="both"), 'dh ˈah')  # CMU dict provides stress for single-syllable words, eng-to-ipa currently disregards
        self.assertEqual(stress.keep_stress("s ˈɪ m f ə n ˌiː", type="none"), 's ɪ m f ə n iː')


if __name__ == "__main__":
    unittest.main()
