import csv
import json
import os
import pathlib
import time
import re
import os
import pathlib
from os import chdir
import tokenize
import platform


#This scripts run on linux (Ubuntu) not in a virtual environment 
#All the imports are the latest version of each

def findOS():
  global path_seperator
  if platform.system() == 'Windows': #Windows (for me to develope the program)
      path_seperator = '\\'
  elif platform.system() == 'Darwin': #MAC OS (for my end user to run the program)
      path_seperator = '/'
  elif platform.system() == 'Linux':
      path_seperator = '/'

def fix_opendict(source):
  destination = source
  # Map phonetic to phonemic; Anglicise IPA for foreign words (croissant, denouement, frisson, etc)
  destination = destination.replace("ɐ", "ʌ")
  destination = destination.replace("ɡ", "g")
  destination = destination.replace("ɔ̃", "ɔ")
  destination = destination.replace("ɑ̃", "ɒn")
  destination = destination.replace("ɹ", "r")
  destination = destination.replace("ˈɛ", "ˈe")
  destination = destination.replace("ˌɛ", "ˌe")
  destination = destination.replace("ɛr", "eə")
  destination = destination.replace("ˈɛː", "ˈeə")
  destination = destination.replace("ˌɛː", "ˌeə")
  destination = destination.replace("ɛː", "eə")
  destination = destination.replace("ɛ", "e")

  #mark the diphthongs with the non-breaking space character
  destination = destination.replace("aɪ", "a‍ɪ") # 39
  destination = destination.replace("aʊ", "a‍ʊ") # 45
  destination = destination.replace("eə", "e‍ə") # 42
  destination = destination.replace("eɪ", "e‍ɪ") # 38
  destination = destination.replace("ɔɪ", "ɔ‍ɪ") # 40
  destination = destination.replace("əʊ", "ə‍ʊ") # 45
  destination = destination.replace("ɛə", "ɛ‍ə") # 42
  destination = destination.replace("ɪə", "ɪ‍ə") # 41
  destination = destination.replace("ʊə", "ʊ‍ə") # 43
  
  # mark the affricates with the non-breaking space character
  destination = destination.replace("dʒ", "d‍ʒ")
  destination = destination.replace("tʃ", "t‍ʃ")
  
  # mark US English diphthong /ie/ - we'll undo this again in create_en_GB_dict
  destination = destination.replace("iə", "i‍ə")
  
  # unmark US English /əl/
  destination = destination.replace("ə‍l", "əl")

  # Use the standard (quantitative-qualitative) IPA notation scheme for vowels
  # See section 5 of https://www.phon.ucl.ac.uk/home/wells/ipa-english-uni.htm
  destination = re.sub("ɑ(?!‍)", "ɑː", destination)
  destination = destination.replace("ɒː", "ɒ")
  destination = re.sub("i(?!‍)", "iː", destination)
  destination = re.sub("ɔ(?!‍)", "ɔː", destination)
  destination = re.sub("u(?!‍)", "uː", destination)
  destination = destination.replace("ːː", "ː")

  # Replace US diphthongs with UK diphthongs in UK dictionary
  destination = destination.replace("ɔ‍ɪ‍ə‍ʊ", "ɔ‍ɪə‍ʊ")
  destination = destination.replace("ɔ‍ɪ‍ə‍ʊ", "ɔ‍ɪə‍ʊ")
  destination = destination.replace("e‍ɪ‍ə‍ʊ", "e‍ɪə‍ʊ")
  destination = destination.replace("a‍ɪ‍ə‍ʊ", "a‍ɪə‍ʊ")

  #Split triphthongs into diphthong followed by schwa or ʊ
  #'a‍ɪ‍ə', 'a‍ʊ‍ə', 'e‍ɪ‍ə', 'e‍ə‍ʊ', 'ɔ‍ɪ‍ə', 'ɪ‍ə‍ʊ', 'ə‍ʊ‍ə'
  destination = destination.replace("a‍ɪ‍ə", "a‍ɪə")
  destination = destination.replace("a‍ʊ‍ə", "a‍ʊə")
  destination = destination.replace("e‍ɪ‍ə", "e‍ɪə")
  destination = destination.replace("e‍ə‍ʊ", "e‍əʊ")
  destination = destination.replace("ɔ‍ɪ‍ə", "ɔ‍ɪə")
  destination = destination.replace("ɪ‍ə‍ʊ", "ɪ‍əʊ")
  destination = destination.replace("ə‍ʊ‍ə", "ə‍ʊə")
  return destination


#start of running
findOS()

os.chdir(pathlib.Path(__file__).parent.absolute().parent.absolute())
txtFilePath = f'.{path_seperator}eng_to_ipa{path_seperator}resources{path_seperator}Opendict_source_files{path_seperator}French'
textFileName = 'fr_FR.txt'
jsonFilePath = f'.{path_seperator}eng_to_ipa{path_seperator}resources'
jsonFileName = 'fr_Open_Dict.json'

os.chdir(txtFilePath)
f = open(textFileName, "r",encoding='UTF-8')
textDict = {}
text = f.read()
textLineList = text.split('\n')
for i in range(len(textLineList)):
    textLineDictStyleList = textLineList[i].split(',')
    textDict[textLineDictStyleList[0]] = [(textLineDictStyleList[1])]

for key in textDict:
  print(textDict[key])
  for idx in range( len( textDict[key] ) ):
      textDict[key][idx] = fix_opendict( textDict[key][idx] )
      textDict[key][idx] = tokenize.tokenize( textDict[key][idx], 'ˑ', 'symbols' )
  print(textDict[key])

os.chdir(pathlib.Path(__file__).parent.absolute().parent.absolute())
if platform.system() == 'Linux':
  chdir('..')
  chdir('..')
  chdir('..')
os.chdir(jsonFilePath)
with open(jsonFileName, 'w',encoding='UTF-8') as fp:
    json.dump(textDict,fp,check_circular=True, indent=None, separators=[',\n', ': '], sort_keys=True, ensure_ascii=False)