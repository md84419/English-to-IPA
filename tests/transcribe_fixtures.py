# -*- coding: utf-8 -*-

# USAGE:
# PYTHONPATH=".." python test_transcribe.py 

from eng_to_ipa import transcribe
import unittest

class BaseConversion(unittest.TestCase):
    """Simple unit testing for the transcribe function(s)."""

    def test_get_cmu_teacher(self):
        transcribe.set_language( self.lang )
        res1 = transcribe.get_entries(self.words['teacher'], db_type='sql', language=self.lang, token_marking='spaces')
        res2 = transcribe.get_entries(self.words['teacher'], db_type='json', language=self.lang, token_marking='spaces')
        self.assertEqual(res1, self.cmu1_spaces)
        self.assertEqual(res2, self.cmu1_spaces)
        self.assertEqual(res1, res2)

    def test_cmu_to_ipa_teacher(self):
        transcribe.set_language( self.lang )
        res1 = transcribe.cmu_to_ipa( self.cmu['teacher'], stress_marking='both')
        #self.assertEqual(res1, self.ipa['teacher'])

    def test_get_cmu_aardvark(self):
        res1 = transcribe.get_entries(self.words['aardvark'], db_type='sql', language=self.lang, token_marking='none')
        res2 = transcribe.get_entries(self.words['aardvark'], db_type='json', language=self.lang, token_marking='none')
        self.assertEqual(res1, self.cmu['aardvark'])
        self.assertEqual(res2, self.cmu['aardvark'])
        self.assertEqual(res1, res2)

    def test_cmu_to_ipa_aardvark(self):
        transcribe.set_language( self.lang )
        res1 = transcribe.cmu_to_ipa( self.cmu['aardvark'], stress_marking='both')
        self.assertEqual(res1, self.ipa['aardvark'])

    def test_get_cmu_again(self):
        res1 = transcribe.get_entries(self.words['again'], db_type='sql', language=self.lang, token_marking='symbols')
        res2 = transcribe.get_entries(self.words['again'], db_type='json', language=self.lang, token_marking='symbols')
        self.assertEqual(res1, self.cmu['again'])
        self.assertEqual(res2, self.cmu['again'])
        self.assertEqual(res1, res2)

    def test_cmu_to_ipa_again(self):
        transcribe.set_language( self.lang )
        res1 = transcribe.cmu_to_ipa( self.cmu['again'], stress_marking='both', sorted_list=False)
        self.assertEqual(res1, self.ipa['again'])

    def test_get_cmu_the(self):
        res1 = transcribe.get_entries(self.words['the'], db_type='sql', language=self.lang, token_marking='spaces')
        res2 = transcribe.get_entries(self.words['the'], db_type='json', language=self.lang, token_marking='spaces')
        res3 = transcribe.get_entries(self.words['the'], db_type='sql', language=self.lang, token_marking='none')
        res4 = transcribe.get_entries(self.words['the'], db_type='json', language=self.lang, token_marking='none')
        res5 = transcribe.get_entries(self.words['the'], db_type='sql', language=self.lang, token_marking='symbols')
        res6 = transcribe.get_entries(self.words['the'], db_type='json', language=self.lang, token_marking='symbols')
        self.assertEqual(res1, self.cmu5_spaces)
        self.assertEqual(res2, self.cmu5_spaces)
        self.assertEqual(res3, self.cmu5_none)
        self.assertEqual(res4, self.cmu5_none)
        self.assertEqual(res5, self.cmu['the'])
        self.assertEqual(res6, self.cmu['the'])
        self.assertEqual(res1, res2)
        self.assertEqual(res3, res4)
        self.assertEqual(res5, res6)

    def test_cmu_to_ipa_the(self):
        transcribe.set_language( self.lang )
        res1 = transcribe.cmu_to_ipa( self.cmu5_none, stress_marking='both', sorted_list=False, token_marking='none')
        self.assertEqual(res1, self.ipa5_none)

    def test_get_cmu_loch(self):
        res1 = transcribe.get_entries(self.words['loch'], db_type='sql', language=self.lang, token_marking='none')
        res2 = transcribe.get_entries(self.words['loch'], db_type='json', language=self.lang, token_marking='none')
        self.assertEqual(res1, self.cmu['loch'])
        self.assertEqual(res2, self.cmu['loch'])
        self.assertEqual(res1, res2)

    def test_cmu_to_ipa_loch(self):
        transcribe.set_language( self.lang )
        res1 = transcribe.cmu_to_ipa( self.cmu['loch'], stress_marking='both')
        self.assertEqual(res1, self.ipa['loch'])

    def test_get_cmu_panagram(self):
        res1 = transcribe.get_entries(self.words['pangram'], db_type='sql', language=self.lang, token_marking='spaces')
        res2 = transcribe.get_entries(self.words['pangram'], db_type='json', language=self.lang, token_marking='spaces')
        self.assertEqual(res1, self.cmu3_spaces)
        self.assertEqual(res2, self.cmu3_spaces)
        self.assertEqual(res1, res2)
    
    def test_cmu_to_ipa_panagram(self):
        transcribe.set_language( self.lang )
        res1 = transcribe.cmu_to_ipa( self.cmu3_spaces, stress_marking='both', sorted_list=False, token_marking='spaces')
        res2 = transcribe.cmu_to_ipa( self.cmu3_none, stress_marking='both', sorted_list=False, token_marking='none')
        res3 = transcribe.cmu_to_ipa( self.cmu['pangram'], stress_marking='both', sorted_list=False, token_marking='symbols')
        self.assertEqual(res1, self.ipa3_spaces)
        self.assertEqual(res2, self.ipa3_none)
        self.assertEqual(res3, self.ipa['pangram'])
  
    def test_get_ipa_with(self):
        transcribe.set_language(self.lang)
        res1 = transcribe.get_entries(self.words['with'], db_type='sql', language=self.lang, token_marking='spaces')
        res2 = transcribe.get_entries(self.words['with'], db_type='json', language=self.lang, token_marking='spaces')
        self.assertEqual( res1, self.ipa['with'] )
        self.assertEqual( res2, self.ipa['with'] )
        self.assertEqual(res1, res2 )   
        res1 = transcribe.convert( self.words['with'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['with'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa7c )
        self.assertEqual( res2, self.ipa7c )
        self.assertEqual(res1, res2 )
    
    def test_get_ipa_gb(self):
        transcribe.set_language(self.lang)
        res1 = transcribe.convert( self.words['uk'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['uk'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa['uk'] )
        self.assertEqual( res2, self.ipa['uk'] )
        self.assertEqual(res1, res2 )
 
    def test_get_ipa_uk(self):
        transcribe.set_language(self.lang)
        res1 = transcribe.convert( self.words['gb'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['gb'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa['gb'] )
        self.assertEqual( res2, self.ipa['gb'] )
        self.assertEqual(res1, res2 )

    def test_get_ipa_sewer(self):
        res1 = transcribe.convert( self.words['sewer'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['sewer'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa['sewer'] )
        self.assertEqual( res2, self.ipa['sewer'] )
        self.assertEqual(res1, res2 )
    
    def test_get_ipa_years(self):
        transcribe.set_language(self.lang)
        res1 = transcribe.convert( self.words['years'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['years'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa['years'] )
        self.assertEqual( res2, self.ipa['years'] )
        self.assertEqual(res1, res2 )

    def test_get_ipa_robotica(self):
        transcribe.set_language(self.lang)
        res1 = transcribe.convert( self.words['robotica'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['robotica'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa['robotica'] )
        self.assertEqual( res2, self.ipa['robotica'] )
        self.assertEqual(res1, res2 )

    def test_get_ipa_be(self):
        transcribe.set_language(self.lang)
        res1 = transcribe.convert( self.words['be'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['be'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa['be'] )
        self.assertEqual( res2, self.ipa['be'] )
        self.assertEqual(res1, res2 )

    def test_get_ipa_will(self):
        transcribe.set_language(self.lang)
        res1 = transcribe.convert( self.words['will'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['will'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa['will'] )
        self.assertEqual( res2, self.ipa['will'] )
        self.assertEqual(res1, res2 )

    def test_get_ipa_to(self):
        transcribe.set_language(self.lang)
        res1 = transcribe.convert( self.words['to'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['to'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa['to'] )
        self.assertEqual( res2, self.ipa['to'] )
        self.assertEqual(res1, res2 )
    
    def test_get_ipa_for(self):
        transcribe.set_language(self.lang)
        res1 = transcribe.convert( self.words['for'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['for'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa['for'] )
        self.assertEqual( res2, self.ipa['for'] )
        self.assertEqual(res1, res2 )

    def test_get_ipa_can(self):
        transcribe.set_language(self.lang)
        res1 = transcribe.convert( self.words['can'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['can'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa['can'] )
        self.assertEqual( res2, self.ipa['can'] )
        self.assertEqual(res1, res2 )

    def test_get_ipa_visually(self):
        transcribe.set_language(self.lang)
        res1 = transcribe.convert( self.words['visually'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['visually'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa['visually'] )
        self.assertEqual( res2, self.ipa['visually'] )
        self.assertEqual(res1, res2 )

    def test_get_ipa_tv(self):
        transcribe.set_language(self.lang)
        res1 = transcribe.convert( self.words['tv'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['tv'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa['tv'] )
        self.assertEqual( res2, self.ipa['tv'] )
        self.assertEqual(res1, res2 )

    def test_get_ipa_and(self):
        transcribe.set_language(self.lang)
        res1 = transcribe.convert( self.words['and'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['and'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa['and'] )
        self.assertEqual( res2, self.ipa['and'] )
        self.assertEqual(res1, res2 )

    def test_get_ipa_aba(self):
        transcribe.set_language(self.lang)
        res1 = transcribe.convert( self.words['aba'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['aba'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa['aba'] )
        self.assertEqual( res2, self.ipa['aba'] )
        self.assertEqual(res1, res2 )

    def test_get_ipa_abalone(self):
        transcribe.set_language(self.lang)
        res1 = transcribe.convert( self.words['abalone'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['abalone'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa['abalone'] )
        self.assertEqual( res2, self.ipa['abalone'] )
        self.assertEqual(res1, res2 )

    def test_get_ipa_assistants(self):
        transcribe.set_language(self.lang)
        res1 = transcribe.convert( self.words['assistants'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['assistants'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa['assistants'] )
        self.assertEqual( res2, self.ipa['assistants'] )
        self.assertEqual(res1, res2 )

    def test_get_ipa_of(self):
        transcribe.set_language(self.lang)
        res1 = transcribe.convert( self.words['of'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['of'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa['of'] )
        self.assertEqual( res2, self.ipa['of'] )
        self.assertEqual(res1, res2 )

    def test_get_ipa_was(self):
        transcribe.set_language(self.lang)
        res1 = transcribe.convert( self.words['was'], language=self.lang, mode='sql', sorted_list=False )
        res2 = transcribe.convert( self.words['was'], language=self.lang, mode='json', sorted_list=False )
        self.assertEqual( res1, self.ipa['was'] )
        self.assertEqual( res2, self.ipa['was'] )
        self.assertEqual(res1, res2 )

    ### Matt's french testing
    def test_Chic_IPA_FR_Equal_EN(self):
        

if __name__ == "__main__":
    unittest.main()
