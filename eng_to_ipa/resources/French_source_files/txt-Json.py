import csv
import json
import os
import pathlib
import time
import re

def fix_britfone(source):
  """Add the IPA nobreak characters to the diphthongs, as these aren't present in the source file"""
  destination = source
  for key1 in destination:
    for key2 in range( len( destination[key1] )):
      # Map phonetic to phonemic
      destination[key1][key2] = destination[key1][key2].replace("ˈɐ", "ˈʌ")
      destination[key1][key2] = destination[key1][key2].replace("ˌɐ", "ˌʌ")
      destination[key1][key2] = destination[key1][key2].replace("ɐ", "ʌ")
      destination[key1][key2] = destination[key1][key2].replace("ɹ", "r")
      destination[key1][key2] = destination[key1][key2].replace("ɹ", "r")

      # Undo Upton's scheme (Oxford dictionary)
      # See section 7 of https://www.phon.ucl.ac.uk/home/wells/ipa-english-uni.htm
      # See also https://teflpedia.com/IPA_phoneme_/e%C9%99/ and related pages for the other symbols
      destination[key1][key2] = destination[key1][key2].replace("ˈɛ", "ˈe")
      destination[key1][key2] = destination[key1][key2].replace("ˌɛ", "ˌe")
      destination[key1][key2] = destination[key1][key2].replace("ɛr", "e‍ə")
      destination[key1][key2] = destination[key1][key2].replace("ɛː", "e‍ə")
      destination[key1][key2] = destination[key1][key2].replace("ɛ", "e")

      #mark the diphthongs with the non-breaking space character
      destination[key1][key2] = destination[key1][key2].replace("aɪ", "a‍ɪ")
      destination[key1][key2] = destination[key1][key2].replace("aʊ", "a‍ʊ")
      destination[key1][key2] = destination[key1][key2].replace("dʒ", "d‍ʒ")
      destination[key1][key2] = destination[key1][key2].replace("eə", "e‍ə")
      destination[key1][key2] = destination[key1][key2].replace("eɪ", "e‍ɪ")
      destination[key1][key2] = destination[key1][key2].replace("iə", "i‍ə")
      destination[key1][key2] = destination[key1][key2].replace("tʃ", "t‍ʃ")
      destination[key1][key2] = destination[key1][key2].replace("ɔɪ", "ɔ‍ɪ")
      destination[key1][key2] = destination[key1][key2].replace("əl", "ə‍l")
      destination[key1][key2] = destination[key1][key2].replace("əʊ", "ə‍ʊ")
      destination[key1][key2] = destination[key1][key2].replace("ɛə", "ɛ‍ə")
      destination[key1][key2] = destination[key1][key2].replace("ɪə", "ɪ‍ə")
      destination[key1][key2] = destination[key1][key2].replace("ʊə", "ʊ‍ə")

      # Use the standard (quantitative-qualitative) IPA notation scheme for vowels
      # See section 5 of https://www.phon.ucl.ac.uk/home/wells/ipa-english-uni.htm
      destination[key1][key2] = re.sub("ɑ(?!‍)", "ɑː", destination[key1][key2])
      destination[key1][key2] = destination[key1][key2].replace("ɒː", "ɒ")
      destination[key1][key2] = re.sub("i(?!‍)", "iː", destination[key1][key2])
      destination[key1][key2] = re.sub("ɔ(?!‍)", "ɔː", destination[key1][key2])
      destination[key1][key2] = re.sub("u(?!‍)", "uː", destination[key1][key2])
      destination[key1][key2] = destination[key1][key2].replace("ːː", "ː")

      # Change quadphthongs into 2x UK diphthongs
      #destination[key1][key2] = destination[key1][key2].replace("e‍ɪ‍ə‍ʊ", "e‍ɪ ə‍ʊ")
      #destination[key1][key2] = destination[key1][key2].replace("ɔ‍ɪ‍ə‍ʊ", "ɔ‍ɪ ə‍ʊ")
  return destination

os.chdir(pathlib.Path(__file__).parent.absolute())
txtFilePath = 'FR-IPA_Dictionary.txt'
jsonFilePath = 'FR-IPA_Dictionary.json'

f = open(txtFilePath, "r",encoding='UTF-8')
textDict = {}
text = f.read()
textLineList = text.split('\n')
for i in range(len(textLineList)):
    textLineDictStyleList = textLineList[i].split(',')
    textDict[textLineDictStyleList[0]] = [(textLineDictStyleList[1])]

textDict = fix_britfone(textDict)

with open(jsonFilePath, 'w',encoding='UTF-8') as fp:
    j = json.dump(textDict, fp,check_circular=True, indent=None, sort_keys=True, separators=[',\n', ':'], ensure_ascii=False )
    j = re.sub("{", "{\n", j)
    j = re.sub("],", "],\n", j)
    j = re.sub("]}", "]\n}", j)