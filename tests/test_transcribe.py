# -*- coding: utf-8 -*-

# USAGE:
# PYTHONPATH=".." python test_transcribe.py 

from eng_to_ipa import transcribe
import transcribe_fixtures
import copy, sys

words = {
    'teacher':'', 'aardvark':'',
    'pangram': "The beige hue on the waters of the loch impressed all, including the French queen, before she heard that symphony again, just as young Arthur wanted.",
    'again':'', 'the':'', 'loch':'',
    'with':'', 'uk':'', 'gb':'', 'sewer':'', 'years':'', 'robotica':'', 'be':'', 'will':'', 'to':'', 'for':'', 'can':'', 'visually':'', 'tv':'',
    'and':'', 'aba':'', 'abalone':'', 'assistants':''
}
for key in words:
    if key == 'pangram':
        words[key] = [transcribe.preserve_punc(w.lower())[0] for w in words[key].split()]
        words[key] = [w[1] for w in words[key]]
        continue
    #print ('key: ' + key)
    #print ('oldval: ' + words[key])
    words[key] = key.split()


cmu = {
    'teacher'   : [['t iy1 ch er0']],
    'aardvark'  : [['aa1 r d v aa2 r k']]
}

ipa = {
    'again': [['əˑˈgˑeˑn', 'əˑˈgˑe\u200dɪˑn']],
    'the'  : [['ðˑə', 'ðˑiː']]
}


ipa4_CMU = [[
        ipa['again'][0][0].replace('ˑ', '').replace('‍','').replace('en','ɛn'),
        ipa['again'][0][1].replace('ˑ', '').replace('‍','')
    ]]


ipa5_CMU = [[
        ipa['the'][0][0],
        ipa['the'][0][1].replace('ː','')
    ]]


class TestConversion_default(transcribe_fixtures.BaseConversion):
    @classmethod
    def setUpClass(self):
        self.ipa = copy.deepcopy( ipa )
        self.ipa['teacher'] = [['ˈtˑiˑʧˑəˑr']]
        self.ipa['aardvark'] = [['ˈɑrdˌvɑrk']]
        self.ipa['pangram'] = [['ðə', 'ði'], ['beɪʒ'], ['hju'], ['ɑn', 'ɔn'], ['ðə', 'ði'], ['ˈwɔtərz'], ['əv'], ['ðə', 'ði'], ['lɑk'], ['ˌɪmˈprɛst'], ['ɔl'],
            ['ˌɪnˈkludɪŋ'], ['ðə', 'ði'], ['frɛnʧ'], ['kwin'], ['bɪˈfɔr', 'ˌbiˈfɔr'], ['ʃi'], ['hərd'], ['ðæt', 'ðət'], ['ˈsɪmfəni'], ['əˈgɛn', 'əˈgeɪn'],
            ['ʤəst', 'ʤɪst'], ['æz', 'ɛz'], ['jəŋ'], ['ˈɑrθər'], ['ˈwɔntɪd']]
        self.ipa['again'] = ipa4_CMU
        self.ipa['the'] = ipa5_CMU
        self.ipa['loch'] = [['lɑk']]
        self.ipa['with'] = [['w ih1 dh', 'w ih1 th', 'w ih0 th', 'w ih0 dh']]
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
        self.ipa['tv'] = 'ˌtɛləˈvɪʒən'
        self.ipa['and'] = 'ænd'
        self.ipa['aba'] = 'ˌeɪˌbiˈeɪ'
        self.ipa['abalone'] = 'ˌæbəˈloʊni'
        self.ipa['assistants'] = 'əˈsɪstənts'

        self.cmu = copy.deepcopy( cmu )
        self.cmu['pangram'] = [['dh ah0', 'dh ah1', 'dh iy0'], ['b ey1 zh'], ['hh y uw1'], ['aa1 n', 'ao1 n'], ['dh ah0', 'dh ah1', 'dh iy0'],
            ['w ao1 t er0 z'], ['ah1 v', 'ah0 v'], ['dh ah0', 'dh ah1', 'dh iy0'], ['l aa1 k'], ['ih2 m p r eh1 s t'], ['ao1 l'],
            ['ih2 n k l uw1 d ih0 ng'], ['dh ah0', 'dh ah1', 'dh iy0'], ['f r eh1 n ch'], ['k w iy1 n'], ['b ih0 f ao1 r', 'b iy2 f ao1 r'],
            ['sh iy1'], ['hh er1 d'], ['dh ae1 t', 'dh ah0 t'], ['s ih1 m f ah0 n iy0'], ['ah0 g eh1 n', 'ah0 g ey1 n'], ['jh ah1 s t', 'jh ih0 s t'],
            ['ae1 z', 'eh1 z'], ['y ah1 ng'], ['aa1 r th er0'], ['w ao1 n t ih0 d']]
        self.cmu['again'] = [['ah0 g eh1 n', 'ah0 g ey1 n']]
        self.cmu['the']   = [['dh ah0', 'dh ah1', 'dh iy0']]
        self.cmu['loch']  = [['l aa1 k']]


        self.cmu1_none = self.cmu1_spaces = self.cmu['teacher']
        self.ipa1_spaces = tk( self.ipa['teacher'], ' ')
        self.ipa1_none = tk( self.ipa['teacher'], '')
        
        self.cmu3_none = self.cmu3_spaces = self.cmu['pangram']
        self.ipa3_spaces = tk( self.ipa['pangram'], ' ')
        self.ipa3_none = tk( self.ipa['pangram'], '')
        
        self.cmu5_none = self.cmu5_spaces = self.cmu['the']
        self.ipa5_spaces = tk( self.ipa['the'], ' ')
        self.ipa5_none = tk( self.ipa['the'], '')
        
        self.ipa7c = 'wɪθ'
        
        self.words = words

        self.lang = None
    
class TestConversion_CMU(transcribe_fixtures.BaseConversion):
    @classmethod
    def setUpClass(self):
        self.ipa = copy.deepcopy( ipa )
        self.ipa['teacher'] = [['ˈtiʧər']]
        self.ipa['aardvark'] = [['ˈɑrdˌvɑrk']]
        self.ipa['pangram'] = [['ðə','ði'], ['beɪʒ'], ['hju'], ['ɑn', 'ɔn'], ['ðə','ði'], ['ˈwɔtərz'], ['əv'], ['ðə','ði'], ['lɑk'], ['ˌɪmˈprɛst'], ['ɔl'],
            ['ˌɪnˈkludɪŋ'], ['ðə','ði'], ['frɛnʧ'], ['kwin'], ['bɪˈfɔr', 'ˌbiˈfɔr'], ['ʃi'], ['hərd'], ['ðæt', 'ðət'], ['ˈsɪmfəni'], ['əˈgɛn', 'əˈgeɪn'],
            ['ʤəst', 'ʤɪst'], ['æz', 'ɛz'], ['jəŋ'], ['ˈɑrθər'], ['ˈwɔntɪd']]
        self.ipa['again'] = ipa4_CMU
        self.ipa['the']   = ipa5_CMU
        self.ipa['loch'] = [['lɑk']]
        self.ipa['with'] = [['w ih1 dh', 'w ih1 th', 'w ih0 th', 'w ih0 dh']]
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
        self.ipa['tv'] = 'ˌtɛləˈvɪʒən'
        self.ipa['and'] = 'ænd'
        self.ipa['aba'] = 'ˌeɪˌbiˈeɪ'
        self.ipa['abalone'] = 'ˌæbəˈloʊni'
        self.ipa['assistants'] = 'əˈsɪstənts'
        
        self.cmu = copy.deepcopy( cmu )
        self.cmu['pangram'] = [['dh ah0', 'dh ah1', 'dh iy0'], ['b ey1 zh'], ['hh y uw1'], ['aa1 n', 'ao1 n'], ['dh ah0', 'dh ah1', 'dh iy0'],
            ['w ao1 t er0 z'], ['ah1 v', 'ah0 v'], ['dh ah0', 'dh ah1', 'dh iy0'], ['l aa1 k'], ['ih2 m p r eh1 s t'], ['ao1 l'],
            ['ih2 n k l uw1 d ih0 ng'], ['dh ah0', 'dh ah1', 'dh iy0'], ['f r eh1 n ch'], ['k w iy1 n'], ['b ih0 f ao1 r', 'b iy2 f ao1 r'],
            ['sh iy1'], ['hh er1 d'], ['dh ae1 t', 'dh ah0 t'], ['s ih1 m f ah0 n iy0'], ['ah0 g eh1 n', 'ah0 g ey1 n'], ['jh ah1 s t', 'jh ih0 s t'],
            ['ae1 z', 'eh1 z'], ['y ah1 ng'], ['aa1 r th er0'], ['w ao1 n t ih0 d']]
        self.cmu['again'] = [['ah0 g eh1 n', 'ah0 g ey1 n']]
        self.cmu['the']   = [['dh ah0', 'dh ah1', 'dh iy0']]
        self.cmu['loch']  = [['l aa1 k']]
        
        self.cmu1_none = self.cmu1_spaces = self.cmu['teacher']
        self.ipa1_spaces = tk( self.ipa['teacher'], ' ')
        self.ipa1_none = tk( self.ipa['teacher'], '')
        
        self.cmu3_none = self.cmu3_spaces = self.cmu['pangram']
        self.ipa3_spaces = tk( self.ipa['pangram'], ' ')
        self.ipa3_none = tk( self.ipa['pangram'], '')
        
        self.cmu5_none = self.cmu5_spaces = self.cmu['the']
        self.ipa5_none = self.ipa5_spaces = self.ipa['the']
        self.ipa5_spaces = tk( self.ipa['the'], ' ')
        self.ipa5_none = tk( self.ipa['the'], '')
        
        self.ipa7c = 'wɪθ'
        
        self.words = words

        self.lang = 'CMU'
    
class TestConversion_en_GB(transcribe_fixtures.BaseConversion):
    @classmethod
    def setUpClass(self):
        self.maxDiff = None
        
        self.ipa = copy.deepcopy( ipa )
        self.ipa['teacher'] = [['tˑˈiːˑt\u200dʃˑə']]
        self.ipa['aardvark'] = [['ˈɑːdvɑːk']]
        self.ipa['pangram'] = [['ðˑə', 'ðˑiː', 'ðˑˈiː'], ['bˑˈe‍ɪˑʒ'], ['hˑjˑˈuː'], ['ˈɒˑn'], ['ðˑə', 'ðˑiː', 'ðˑˈiː'], ['wˑˈɔːˑtˑəˑz'], ['ˈɒˑv', 'əˑv'],
            ['ðˑə', 'ðˑiː', 'ðˑˈiː'], ['lˑˈɒˑx'], ['ɪˑmˑpˑrˑˈeˑsˑt'], ['ˈɔːˑl'], ['ɪˑnˑkˑlˑˈuːˑdˑɪˑŋ'], ['ðˑə', 'ðˑiː', 'ðˑˈiː'], ['fˑrˑˈeˑnˑt\u200dʃ'],
            ['kˑwˑˈiːˑn'], ['bˑɪˑfˑˈɔː'], ['ʃˑˈiː'], ['hˑˈɜːˑd'], ['ðˑˈæˑt', 'ðˑəˑt'], ['sˑˈɪˑmˑfˑəˑnˑˌiː', 'sˑˈɪˑmˑfˑəˑnˑiː'],
            ['ʌˑgˑˈeˑn', 'əˑgˑˈeˑn', 'əˑgˑˈe‍ɪˑn'], ['d\u200dʒˑˈʌˑsˑt', 'd\u200dʒˑəˑsˑt'], ['ˈæˑz', 'əˑz'],['jˑˈʌˑŋ'], ['ˈɑːˑθˑə'], ['wˑˈɒˑnˑtˑɪˑd']]
        self.ipa['again'] = [['ʌˑgˑˈeˑn', 'əˑgˑˈeˑn', 'əˑgˑˈe\u200dɪˑn']]
        self.ipa['the']   = [['ðˑə', 'ðˑiː', 'ðˑˈiː']]
        self.ipa['loch'] = [['lˈɒx']]
        self.ipa['with'] = [['w ˈɪ ð', 'w ɪ ð']]
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
        self.ipa['visually'] = 'vˈɪʒəˈliː'
        self.ipa['tv'] = 'ˈtiːˈviː'
        self.ipa['and'] = 'ˈænd'
        self.ipa['aba'] = 'æbˈæ'
        self.ipa['abalone'] = 'æbˈælə‍ʊn'
        self.ipa['assistants'] = 'əsˈɪstənts'
        
        self.cmu = copy.deepcopy( cmu )
        self.cmu['teacher']  = self.ipa['teacher']
        self.cmu['aardvark'] = self.ipa['aardvark']
        self.cmu['pangram']  = self.ipa['pangram']
        self.cmu['again']    = self.ipa['again']
        self.cmu['the']      = self.ipa['the']
        self.cmu['loch']     = self.ipa['loch']
        
        self.ipa1_spaces = self.cmu1_spaces = tk( self.ipa['teacher'], ' ')
        self.ipa1_none = self.cmu1_none = tk( self.ipa['teacher'], '')
        
        self.ipa3_spaces = self.cmu3_spaces = tk( self.ipa['pangram'], ' ')
        self.ipa3_none = self.cmu3_none = tk( self.ipa['pangram'], '')
        
        self.ipa5_spaces = self.cmu5_spaces = tk( self.ipa['the'], ' ')
        self.ipa5_none = self.cmu5_none = tk( self.ipa['the'], '')
        
        self.ipa7c = 'wɪð'
        
        self.words = words

        self.lang = 'en-GB'

class TestConversion_en_US(transcribe_fixtures.BaseConversion):
    @classmethod
    def setUpClass(self):
        self.maxDiff = None
        
        self.ipa = copy.deepcopy( ipa )
        self.ipa['teacher'] = [['ˈtˑiːˑt‍ʃˑəˑr']]
        self.ipa['aardvark'] = [['ˈɒrdˌvɒrk']]
        self.ipa['pangram'] = [['ðˑə', 'ðˑiː'], ['bˑe‍ɪˑʒ'], ['hˑjˑuː'], ['ɒˑn', 'ɔːˑn'], ['ðˑə', 'ðˑiː'], ['ˈwˑɔːˑtˑəˑrˑz'], ['əˑv'], ['ðˑə', 'ðˑiː'],
            ['lˑɒˑk'], ['ˌɪ mˑˈpˑrˑeˑsˑt'], ['ɔːˑl'], ['ˌɪˑnˑˈkˑlˑuːˑdˑɪˑŋ'], ['ðˑə', 'ðˑiː'], ['fˑrˑeˑnˑt‍ʃ'], ['kˑwˑiːˑn'], ['bˑɪˑˈfˑɔːˑr', 'ˌbˑiːˑˈfˑɔːˑr'], ['ʃˑiː'], ['hˑəˑrˑd'],
            ['ðˑæˑt', 'ðˑəˑt'], ['ˈsˑɪˑmˑfˑəˑnˑiː'], ['əˑˈgˑeˑn', 'əˑˈgˑe‍ɪˑn'], ['d‍ʒˑəˑsˑt', 'd‍ʒˑɪˑsˑt'], ['æˑz', 'eˑz'], ['jˑəˑŋ'], ['ˈɒˑrˑθˑəˑr'], ['ˈwˑɔːˑnˑtˑɪˑd']]
        # the
        # again
        self.ipa['loch'] = [['lɒk']]
        self.ipa['with'] = [['w ɪ ð', 'w ɪ θ']]
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
        self.ipa['tv'] = 'ˌteləˈvɪʒən'
        self.ipa['and'] = 'ænd'
        self.ipa['aba'] = 'ˌe‍ɪˌbiːˈe‍ɪ'
        self.ipa['abalone'] = 'ˌæbəˈlə‍ʊniː'
        self.ipa['assistants'] = 'əˈsɪstənts'
        
        self.cmu = copy.deepcopy( cmu )
        self.cmu['teacher']  = self.ipa['teacher']
        self.cmu['aardvark'] = self.ipa['aardvark']
        self.cmu['pangram']  = self.ipa['pangram']
        self.cmu['again']    = self.ipa['again']
        self.cmu['the']      = self.ipa['the']
        self.cmu['loch']     = self.ipa['loch']
        
        self.ipa1_spaces = self.cmu1_spaces = tk( self.ipa['teacher'], ' ')
        self.ipa1_none = self.cmu1_none = tk( self.ipa['teacher'], '')
        
        self.ipa3_spaces = self.cmu3_spaces = tk( self.ipa['pangram'], ' ')
        self.ipa3_none = self.cmu3_none = tk( self.ipa['pangram'], '')
        
        self.ipa5_spaces = self.cmu5_spaces = tk( self.ipa['the'], ' ')
        self.ipa5_none = self.cmu5_none = tk( self.ipa['the'], '')
        
        self.ipa7c = 'wɪθ'
        
        self.words = words

        self.lang = 'en-US'

def tk(arr, replace):
    newArr = copy.deepcopy(arr)
    for i in range( len( newArr)):
        for j in range( len( newArr[i])):
            newArr[i][j] = newArr[i][j].replace('ˑ', replace)
    return newArr

#if __name__ == "__main__":
#    unittest.main()
