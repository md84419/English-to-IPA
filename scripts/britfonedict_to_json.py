#!/usr/bin/python

# USAGE:
#  PYTHONPATH=".." python opendict_to_json.py ../eng_to_ipa/resources/Opendict_source_files/en_UK.txt > ../eng_to_ipa/resources/Open_dict.json

import csv, getopt, json, io, os, re, sys, subprocess
from signal import signal, SIGPIPE, SIG_DFL

signal(SIGPIPE, SIG_DFL)


def main(argv):
  input_file = None
  output_file = None
  
  try:
    opts, args = getopt.getopt(argv, "o:")
  except getopt.GetoptError:
    print( "{0}: syntax: [-o output.json] input.csv".format( sys.argv[0]) )
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-o':
      output_file = arg

  try:
    input_file = args[0]
  except:
    print( "{0}: syntax: [-o output.json] input.csv".format( sys.argv[0]) )
    sys.exit(2)

  britfone_dict = {}
  with open('../eng_to_ipa/resources/Britfone_source_files/britfone.main.3.0.1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for rows in reader:
      k = rows[0]
      v = rows[1].strip()
      
      # fix 3.0.1 source
      if k == 'AYE(1)': k = 'AYE'
      if k == 'YOB(1)': k = 'YOB'
      if k == 'PROJECTS(2)': k = 'PROJECTS(1)'
      if k == 'PROJECTS(3)': k = 'PROJECTS(2)'
      
      k = k.lower()
      v = v.lower().replace(' ', 'ˑ')
      
      britfone_dict.update( {k: [v]} )

  britfone_dict = fix_britfone( britfone_dict )
  britfone_dict = fix_britfone_words( britfone_dict )

  if( output_file != None ):
    try:
      with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                         '..','eng_to_ipa','resources',output_file), 'wb') as o_fp:
        json.dump( britfone_dict, o_fp, check_circular=True, indent=None, sort_keys=True, separators=[',\n', ':'], ensure_ascii=False )
      sys.exit(0)
    except TypeError:
      pass
  j = json.dumps( britfone_dict, check_circular=True, indent=None, separators=[',', ': '], sort_keys=True, ensure_ascii=False )
  j = re.sub("{", "{\n", j)
  j = re.sub("],", "],\n", j)
  j = re.sub("]}", "]\n}", j)
  print( j )
  sys.exit(0)

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

# fix whole words
def fix_britfone_words( dct ):
  # change
  dct.update({"loch": ["lˑˈɒˑx"]})
  dct.update({"sewer": ["sˑˈʊ‍ə"]})
  # remove
  dct.pop('croissant', None)
  dct.pop('with(2)', None)
  dct.pop('with(4)', None)
  dct.pop('years(2)', None)
  # add
  dct.update({"and(0)": ["nˑd"]})
  dct.update({"uk": ["jˑuːˑkˑe‍ɪ"]})
  dct.update({"gb": ["d‍ʒˑiːˑbˑiː"]})
  dct.update({"years'": ["jˑˈɪ‍əˑz"]})
  dct.update({"years-old": ["jˑˈɪ‍əˑzˑɔːˑlˑd"]})
  dct.update({'light-years': ["ˈlˑa‍ɪˑˌtˑjˑˈɪ‍əˑz"]})
  dct.update({'new-years': ["nˑjˑˈuːˑjˑˈɪ‍əˑz"]})
  dct.update({'thousand-years-long': ["ˈθˑa‍ʊˑzˑəˑnˑˌdˑjˑˈɪ‍əˑzˑˈlˑɔːˑŋ"]})
  dct.update({'robotica': ["rˑˈə‍ʊˑbˑˈɒˑtˑɪˑkˑʌ"]})
  return dct

if( __name__ == "__main__"):
  main(sys.argv[1:])
