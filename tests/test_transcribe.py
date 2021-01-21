# -*- coding: utf-8 -*-

# USAGE:
# PYTHONPATH=".." python test_transcribe.py 

from eng_to_ipa import transcribe
import transcribe_fixtures
import copy, sys

words = {}

words1 = "teacher".split()
words2 = "aardvark".split()
words4 = "again".split()
words5 = "the".split()
words6 = "loch".split()
words['with']  = "with".split()
words['uk']    = "uk".split()
words['gb']    = "gb".split()
words['sewer'] = "sewer".split()
words['years'] = "years".split()
words['robotica'] = "robotica".split()
words['be'] = "be".split()
words['will'] = "will".split()
words['to'] = "to".split()
words['for'] = "for".split()
words['can'] = "can".split()
words['visually'] = "visually".split()

cmu1   = [['t iy1 ch er0']]
cmu2   = [['aa1 r d v aa2 r k']]

ipa4     = [['əˑˈgˑeˑn', 'əˑˈgˑe\u200dɪˑn']]
ipa4_CMU = [[
        ipa4[0][0].replace('ˑ', '').replace('‍','').replace('en','ɛn'),
        ipa4[0][1].replace('ˑ', '').replace('‍','')
    ]]

ipa5     = [['ðˑə', 'ðˑiː']]
ipa5_CMU = [[
        ipa5[0][0],
        ipa5[0][1].replace('ː','')
    ]]

words3 = "The beige hue on the waters of the loch impressed all, including the French queen, before she heard that symphony again, just as young Arthur wanted."
words3 = [transcribe.preserve_punc(w.lower())[0] for w in words3.split()]
words3 = [w[1] for w in words3]


class TestConversion_default(transcribe_fixtures.BaseConversion):
    @classmethod
    def setUpClass(self):
        self.words1 = words1
        self.cmu1_none = self.cmu1_spaces = self.cmu1 = cmu1
        self.ipa1 = [['ˈtˑiˑʧˑəˑr']]
        self.ipa1_spaces = tk( self.ipa1, ' ')
        self.ipa1_none = tk( self.ipa1, '')

        self.words2 = words2
        self.cmu2 = cmu2
        self.ipa2 = [['ˈɑrdˌvɑrk']]

        self.words4 = words4
        self.cmu4 = [['ah0 g eh1 n', 'ah0 g ey1 n']]
        self.ipa4 = ipa4_CMU

        self.words5 = words5
        self.cmu5_none = self.cmu5_spaces = self.cmu5 = [['dh ah0', 'dh ah1', 'dh iy0']]
        self.ipa5 = ipa5_CMU
        self.ipa5_spaces = tk( self.ipa5, ' ')
        self.ipa5_none = tk( self.ipa5, '')

        self.words6 = words6
        self.cmu6 = [['l aa1 k']]
        self.ipa6 = [['lɑk']]
        
        self.words = words
        self.ipa = {}
        
        self.ipa['with'] = [['w ih1 dh', 'w ih1 th', 'w ih0 th', 'w ih0 dh']]
        self.ipa7c = 'wɪθ'
        
        self.ipa['uk'] = 'uk*'
        self.ipa['gb'] = 'gb*'
        self.ipa['sewer'] = 'suər'
        self.ipa['years'] = 'jɪrz'
        self.ipa['robotica'] = 'robotica*'
        self.ipa['be'] = 'bi'
        self.ipa['will'] = 'wəl'
        self.ipa['to'] = 'tə'
        self.ipa['for'] = 'frər'
        self.ipa['can'] = 'kən'
        self.ipa['visually'] = 'ˈvɪʒwəli'
        
        self.words = words
        
        self.words3 = words3

        self.cmu3_none = self.cmu3_spaces = self.cmu3 = [['dh ah0', 'dh ah1', 'dh iy0'], ['b ey1 zh'], ['hh y uw1'], ['aa1 n', 'ao1 n'], ['dh ah0', 'dh ah1', 'dh iy0'],
            ['w ao1 t er0 z'], ['ah1 v', 'ah0 v'], ['dh ah0', 'dh ah1', 'dh iy0'], ['l aa1 k'], ['ih2 m p r eh1 s t'], ['ao1 l'],
            ['ih2 n k l uw1 d ih0 ng'], ['dh ah0', 'dh ah1', 'dh iy0'], ['f r eh1 n ch'], ['k w iy1 n'], ['b ih0 f ao1 r', 'b iy2 f ao1 r'],
            ['sh iy1'], ['hh er1 d'], ['dh ae1 t', 'dh ah0 t'], ['s ih1 m f ah0 n iy0'], ['ah0 g eh1 n', 'ah0 g ey1 n'], ['jh ah1 s t', 'jh ih0 s t'],
            ['ae1 z', 'eh1 z'], ['y ah1 ng'], ['aa1 r th er0'], ['w ao1 n t ih0 d']]
        self.ipa3 = [['ðə', 'ði'], ['beɪʒ'], ['hju'], ['ɑn', 'ɔn'], ['ðə', 'ði'], ['ˈwɔtərz'], ['əv'], ['ðə', 'ði'], ['lɑk'], ['ˌɪmˈprɛst'], ['ɔl'],
            ['ˌɪnˈkludɪŋ'], ['ðə', 'ði'], ['frɛnʧ'], ['kwin'], ['bɪˈfɔr', 'ˌbiˈfɔr'], ['ʃi'], ['hərd'], ['ðæt', 'ðət'], ['ˈsɪmfəni'], ['əˈgɛn', 'əˈgeɪn'],
            ['ʤəst', 'ʤɪst'], ['æz', 'ɛz'], ['jəŋ'], ['ˈɑrθər'], ['ˈwɔntɪd']]
        self.ipa3_spaces = tk( self.ipa3, ' ')
        self.ipa3_none = tk( self.ipa3, '')
        
        self.lang = None
    
class TestConversion_CMU(transcribe_fixtures.BaseConversion):
    @classmethod
    def setUpClass(self):
        
        self.words1 = words1
        self.cmu1_none = self.cmu1_spaces = self.cmu1 = cmu1
        self.ipa1 = [['ˈtiʧər']]
        self.ipa1_spaces = tk( self.ipa1, ' ')
        self.ipa1_none = tk( self.ipa1, '')
        
        self.words2 = words2
        self.cmu2 = cmu2
        self.ipa2 = [['ˈɑrdˌvɑrk']]

        self.words4 = words4
        self.cmu4 = [['ah0 g eh1 n', 'ah0 g ey1 n']]
        self.ipa4 = ipa4_CMU

        self.words5 = words5
        self.cmu5_none = self.cmu5_spaces = self.cmu5   = [['dh ah0', 'dh ah1', 'dh iy0']]
        self.ipa5_none = self.ipa5_spaces = self.ipa5   = ipa5_CMU
        self.ipa5_spaces = tk( self.ipa5, ' ')
        self.ipa5_none = tk( self.ipa5, '')

        self.words6 = words6
        self.cmu6 = [['l aa1 k']]
        self.ipa6 = [['lɑk']]
        
        self.words = words
        self.ipa = {}
        
        self.ipa['with'] = [['w ih1 dh', 'w ih1 th', 'w ih0 th', 'w ih0 dh']]
        self.ipa7c = 'wɪθ'
        
        self.ipa['uk'] = 'uk*'
        self.ipa['gb'] = 'gb*'
        self.ipa['sewer'] = 'suər'
        self.ipa['years'] = 'jɪrz'
        self.ipa['robotica'] = 'robotica*'
        self.ipa['be'] = 'bi'
        self.ipa['will'] = 'wəl'
        self.ipa['to'] = 'tə'
        self.ipa['for'] = 'frər'
        self.ipa['can'] = 'kən'
        self.ipa['visually'] = 'ˈvɪʒwəli'
        
        self.words3 = words3

        self.cmu3_none = self.cmu3_spaces = self.cmu3 = [['dh ah0', 'dh ah1', 'dh iy0'], ['b ey1 zh'], ['hh y uw1'], ['aa1 n', 'ao1 n'], ['dh ah0', 'dh ah1', 'dh iy0'],
            ['w ao1 t er0 z'], ['ah1 v', 'ah0 v'], ['dh ah0', 'dh ah1', 'dh iy0'], ['l aa1 k'], ['ih2 m p r eh1 s t'], ['ao1 l'],
            ['ih2 n k l uw1 d ih0 ng'], ['dh ah0', 'dh ah1', 'dh iy0'], ['f r eh1 n ch'], ['k w iy1 n'], ['b ih0 f ao1 r', 'b iy2 f ao1 r'],
            ['sh iy1'], ['hh er1 d'], ['dh ae1 t', 'dh ah0 t'], ['s ih1 m f ah0 n iy0'], ['ah0 g eh1 n', 'ah0 g ey1 n'], ['jh ah1 s t', 'jh ih0 s t'],
            ['ae1 z', 'eh1 z'], ['y ah1 ng'], ['aa1 r th er0'], ['w ao1 n t ih0 d']]
        self.ipa3 = [['ðə','ði'], ['beɪʒ'], ['hju'], ['ɑn', 'ɔn'], ['ðə','ði'], ['ˈwɔtərz'], ['əv'], ['ðə','ði'], ['lɑk'], ['ˌɪmˈprɛst'], ['ɔl'],
            ['ˌɪnˈkludɪŋ'], ['ðə','ði'], ['frɛnʧ'], ['kwin'], ['bɪˈfɔr', 'ˌbiˈfɔr'], ['ʃi'], ['hərd'], ['ðæt', 'ðət'], ['ˈsɪmfəni'], ['əˈgɛn', 'əˈgeɪn'],
            ['ʤəst', 'ʤɪst'], ['æz', 'ɛz'], ['jəŋ'], ['ˈɑrθər'], ['ˈwɔntɪd']]
        self.ipa3_spaces = tk( self.ipa3, ' ')
        self.ipa3_none = tk( self.ipa3, '')
            
        self.lang = 'CMU'
    
class TestConversion_en_GB(transcribe_fixtures.BaseConversion):
    @classmethod
    def setUpClass(self):
        self.maxDiff = None
        
        self.words1 = words1
        self.cmu1 = self.ipa1 = [['tˑˈiːˑt\u200dʃˑə']]
        self.ipa1_spaces = self.cmu1_spaces = tk( self.ipa1, ' ')
        self.ipa1_none = self.cmu1_none = tk( self.ipa1, '')

        self.words2 = words2
        self.cmu2 = self.ipa2 = [['ˈɑːdvɑːk']]

        self.words4 = words4
        self.cmu4 = self.ipa4 = [['ʌˑgˑˈeˑn', 'əˑgˑˈeˑn', 'əˑgˑˈe\u200dɪˑn']]

        self.words5 = words5
        self.cmu5   = self.ipa5   = [['ðˑə', 'ðˑiː', 'ðˑˈiː']]
        self.ipa5_spaces = self.cmu5_spaces = tk( self.ipa5, ' ')
        self.ipa5_none = self.cmu5_none = tk( self.ipa5, '')

        self.words6 = words6
        self.cmu6 = self.ipa6 = [['lˈɒx']]
        
        self.words = words
        self.ipa = {}
        
        self.ipa['with'] = [['w ˈɪ ð', 'w ɪ ð']]
        self.ipa7c = 'wɪð'
        
        self.ipa['uk'] = 'juːke‍ɪ'
        self.ipa['gb'] = 'd‍ʒiːbiː'
        self.ipa['sewer'] = 'sˈʊ‍ə'
        self.ipa['years'] = 'jˈɪ‍əz'
        self.ipa['robotica'] = "rˈə‍ʊbˈɒtɪkʌ"
        self.ipa['be'] = 'bˈiː'
        self.ipa['will'] = 'wˈɪl'
        self.ipa['to'] = 'tˈuː'
        self.ipa['for'] = 'fˈɔː'
        self.ipa['can'] = 'kˈæn'
        self.ipa['visually'] = 'vɪʒəliː'
        
        self.words3 = words3

        self.cmu3 = self.ipa3 = [['ðˑə', 'ðˑiː', 'ðˑˈiː'], ['bˑˈe‍ɪˑʒ'], ['hˑjˑˈuː'], ['ˈɒˑn'], ['ðˑə', 'ðˑiː', 'ðˑˈiː'], ['wˑˈɔːˑtˑəˑz'], ['ˈɒˑv', 'əˑv'],
            ['ðˑə', 'ðˑiː', 'ðˑˈiː'], ['lˑˈɒˑx'], ['ɪˑmˑpˑrˑˈeˑsˑt'], ['ˈɔːˑl'], ['ɪˑnˑkˑlˑˈuːˑdˑɪˑŋ'], ['ðˑə', 'ðˑiː', 'ðˑˈiː'], ['fˑrˑˈeˑnˑt\u200dʃ'],
            ['kˑwˑˈiːˑn'], ['bˑɪˑfˑˈɔː'], ['ʃˑˈiː'], ['hˑˈɜːˑd'], ['ðˑˈæˑt', 'ðˑəˑt'], ['sˑˈɪˑmˑfˑəˑnˑˌiː', 'sˑˈɪˑmˑfˑəˑnˑiː'],
            ['ʌˑgˑˈeˑn', 'əˑgˑˈeˑn', 'əˑgˑˈe‍ɪˑn'], ['d\u200dʒˑˈʌˑsˑt', 'd\u200dʒˑəˑsˑt'], ['ˈæˑz', 'əˑz'],['jˑˈʌˑŋ'], ['ˈɑːˑθˑə'], ['wˑˈɒˑnˑtˑɪˑd']]

        self.ipa3_spaces = self.cmu3_spaces = tk( self.ipa3, ' ')
        self.ipa3_none = self.cmu3_none = tk( self.ipa3, '')
            
        self.lang = 'en-GB'

class TestConversion_en_US(transcribe_fixtures.BaseConversion):
    @classmethod
    def setUpClass(self):
        self.maxDiff = None
        
        self.words1 = words1
        self.cmu1 = self.ipa1 = [['ˈtˑiːˑt‍ʃˑəˑr']]
        self.ipa1_spaces = self.cmu1_spaces = tk( self.ipa1, ' ')
        self.ipa1_none = self.cmu1_none = tk( self.ipa1, '')
        
        self.words2 = words2
        self.cmu2 = self.ipa2 = [['ˈɒrdˌvɒrk']]
        
        self.words4 = words4
        self.cmu4 = self.ipa4 = ipa4

        self.words5 = words5
        self.cmu5   = self.ipa5   = ipa5
        self.ipa5_spaces = self.cmu5_spaces = tk( self.ipa5, ' ')
        self.ipa5_none = self.cmu5_none = tk( self.ipa5, '')

        self.words6 = words6
        self.cmu6 = self.ipa6 = [['lɒk']]
        
        self.words = words
        self.ipa = {}
        
        self.ipa['with'] = [['w ɪ ð', 'w ɪ θ']]
        self.ipa7c = 'wɪθ'
        
        self.ipa['uk'] = 'uk*'
        self.ipa['gb'] = 'gb*'
        self.ipa['sewer'] = 'suːər'
        self.ipa['years'] = 'jɪrz'
        self.ipa['robotica'] = 'rˈə‍ʊbˈɒtɪkʌ'
        self.ipa['be'] = 'biː'
        self.ipa['will'] = 'wəl'
        self.ipa['to'] = 'tə'
        self.ipa['for'] = 'frər'
        self.ipa['can'] = 'kən'
        self.ipa['visually'] = 'ˈvɪʒwəliː'

        self.words3 = words3

        self.cmu3 = self.ipa3 = [['ðˑə', 'ðˑiː'], ['bˑe‍ɪˑʒ'], ['hˑjˑuː'], ['ɒˑn', 'ɔːˑn'], ['ðˑə', 'ðˑiː'], ['ˈwˑɔːˑtˑəˑrˑz'], ['əˑv'], ['ðˑə', 'ðˑiː'],
            ['lˑɒˑk'], ['ˌɪ mˑˈpˑrˑeˑsˑt'], ['ɔːˑl'], ['ˌɪˑnˑˈkˑlˑuːˑdˑɪˑŋ'], ['ðˑə', 'ðˑiː'], ['fˑrˑeˑnˑt‍ʃ'], ['kˑwˑiːˑn'], ['bˑɪˑˈfˑɔːˑr', 'ˌbˑiːˑˈfˑɔːˑr'], ['ʃˑiː'], ['hˑəˑrˑd'],
            ['ðˑæˑt', 'ðˑəˑt'], ['ˈsˑɪˑmˑfˑəˑnˑiː'], ['əˑˈgˑeˑn', 'əˑˈgˑe‍ɪˑn'], ['d‍ʒˑəˑsˑt', 'd‍ʒˑɪˑsˑt'], ['æˑz', 'eˑz'], ['jˑəˑŋ'], ['ˈɒˑrˑθˑəˑr'], ['ˈwˑɔːˑnˑtˑɪˑd']]

        self.ipa3_spaces = self.cmu3_spaces = tk( self.ipa3, ' ')
        self.ipa3_none = self.cmu3_none = tk( self.ipa3, '')

        self.lang = 'en-US'

def tk(arr, replace):
    newArr = copy.deepcopy(arr)
    for i in range( len( newArr)):
        for j in range( len( newArr[i])):
            newArr[i][j] = newArr[i][j].replace('ˑ', replace)
    return newArr

#if __name__ == "__main__":
#    unittest.main()
