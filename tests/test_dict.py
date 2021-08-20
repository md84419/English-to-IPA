# -*- coding: utf-8 -*-

# USAGE:
# PYTHONPATH=".." python test_dict.py 

from os import chdir, getcwd
import pathlib
from typing import Dict
from eng_to_ipa import transcribe
import json, re, sys, unittest
from os.path import join, abspath, dirname
import sqlite3

class BaseConversion(object):
    
    def test_UK_dict(self):
        dct = self.dct
        with open(join(abspath(dirname(__file__)),
                          "../eng_to_ipa/resources/" + dct + ".json"),
                     encoding="UTF-8") as json_file:
            thisdict = json.load(json_file)

        known = self.known
        
        found = {}
        for key, vlist in thisdict.items():
            for value in vlist:
                for symbol in re.split(' |ˈ|ˌ', value.replace('ˑ', ' ')):
                    if symbol != '' and symbol not in found and symbol not in known:
                        #value = value.replace('\u200d','')
                        found.update( {symbol:key+" /"+value+"/"} )
                        
        for key, symbol in found.items():
            print( key+": "+symbol )
            #pass
        self.assertEqual( {}, found, "unexpected symbol(s) in {} dictionary".format( self.dct ) )

class TestFrench_English_Same():

    def test_CocaCola_is_Same(self):
        chdir(pathlib.Path(__file__).parent.absolute().parent.absolute())
        dict_Path = '.\\eng_to_ipa\\resources'
        frenchDict = 'fr_Open_Dict.json'
        englishDict = 'Open-Dict.json'
        chdir('.\\eng_to_ipa\\resources')
        with open('fr_Open_Dict.json', 'r',encoding='UTF-8') as fp:
            jsonText = json.load(fp)
            jsonText = dict(jsonText)
            frenchColaIPA = jsonText['coca-cola']

        with open('open_Dict.json', 'r',encoding='UTF-8') as fp:
            jsonText = json.load(fp)
            jsonText = dict(jsonText)
            englsihColaIPA = jsonText['coca-cola']

        self.assertEqual(frenchColaIPA,englsihColaIPA)


class TestConversion_UK(BaseConversion,TestFrench_English_Same,unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dct = 'en_GB'
        self.known = ['p', 't', 'k', 'b', 'd', 'f', 'v', 's', 'z', 'm', 'n', 'r', 'l', 'w', 'h',
                      'x', 'g', 't‍ʃ', 'θ', 'ʃ', 'ŋ', 'd‍ʒ', 'ð', 'ʒ', 'j',
                      'ɪ', 'e', 'æ', 'ʊ', 'ʌ', 'ɒ', 'ə',
                      'ɑː', 'iː', 'uː', 'ɜː', 'ɔː',
                      'e‍ɪ', 'a‍ɪ', 'ɔ‍ɪ', 'ɪ‍ə', 'e‍ə', 'ə‍ʊ', 'a‍ʊ', 'ʊ‍ə']




# class TestConversion_US(BaseConversion,unittest.TestCase):
#     @classmethod
#     def setUpClass(self):
#         self.dct = 'en_US'
#         self.known = ['p', 't', 'k', 'b', 'd', 'f', 'v', 's', 'z', 'm', 'n', 'r', 'l', 'w', 'h',
#                       'x', 'g', 't‍ʃ', 'θ', 'ʃ', 'ŋ', 'd‍ʒ', 'ð', 'ʒ', 'j',
#                       'ɪ', 'e', 'æ', 'ʊ', 'ʌ', 'ɒ', 'ə',
#                       'ɑː', 'iː', 'uː', 'ɜː', 'ɔː',
#                       'e‍ɪ', 'a‍ɪ', 'ɔ‍ɪ', 'ɪ‍ə', 'e‍ə', 'ə‍ʊ', 'a‍ʊ', 'ʊ‍ə',
#                       'a‍ɪ‍ə', 'a‍ʊ‍ə', 'e‍ɪ‍ə', 'e‍ə‍ʊ', 'ɔ‍ɪ‍ə', 'ɪ‍ə‍ʊ', 'ə‍ʊ‍ə']
#                       #'e‍ɪ‍ə‍ʊ', 'ɔ‍ɪ‍ə‍ʊ']

# class TestCreateOpendictSymbols(unittest.TestCase):
#   def test_create_opendict_symbols(self):
#         dct = 'Britfone_dict'
#         with open(join(abspath(dirname(__file__)),
#                           "../eng_to_ipa/resources/" + dct + ".json"),
#                      encoding="UTF-8") as json_file:
#             self.dct = json.load(json_file)
        
#         found = {}
#         for key, vlist in self.dct.items():
#             for value in vlist:
#                 for symbol in re.split(' ', value):
#                     if symbol != '' and symbol not in found:
#                         #value = value.replace('\u200d','')
#                         found.update( {symbol:""} )
                        
#         for key in sorted(found.keys()):
#             print( key )

if __name__ == "__main__":
    unittest.main()