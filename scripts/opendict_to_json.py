#!/usr/bin/python

# USAGE:
#  PYTHONPATH=".." python opendict_to_json.py ../eng_to_ipa/resources/Opendict_source_files/en_UK.txt > ../eng_to_ipa/resources/Open_dict.json

import getopt, json, io, os, re, sys, subprocess
try:
  from signal import signal, SIGPIPE, SIG_DFL
  signal(SIGPIPE, SIG_DFL)
except ImportError:
  # we're running on Windows oS
  pass
from eng_to_ipa import tokenize

debug  = False
debug2 = False

SYMBOLS_FILE1 = "opendict.symbols.txt"

tokenize.configure( os.path.join(os.path.abspath(os.path.dirname(__file__)),
                         '..','eng_to_ipa','resources','Opendict_source_files',SYMBOLS_FILE1) )

def main(argv):
  global debug, debug2
  input_file = None
  output_file = None
  
  try:
    opts, args = getopt.getopt(argv, "dDo:")
  except getopt.GetoptError:
    print( "{0}: syntax: [-d|-D] [-o output.json] input.txt".format( sys.argv[0]) )
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-d':
      debug2 = True
      if debug2: print( "debug level 1" )
    elif opt == '-D':
      debug = True
      debug2 = True
      if debug2: print( "debug level 2" )
    elif opt == '-o':
      output_file = arg
      if debug2: print( "output_file is {0}".format( output_file ) )
      
      
  try:
    input_file = args[0]
  except:
    print( "{0}: syntax: [-d|-D] [-o output.json] input.txt".format( sys.argv[0]) )
    sys.exit(2)
  

  p_out = subprocess.check_output( ['awk', '-f', 'txt_to_json.awk', input_file] )

  open_dict = json.loads( p_out )
  fix_opendict_words( open_dict )

  for key in open_dict:
    #if debug2: print( open_dict[key][0] )
    for idx in range( len( open_dict[key] ) ):
      open_dict[key][idx] = fix_opendict( open_dict[key][idx] )
      open_dict[key][idx] = tokenize.tokenize( open_dict[key][idx], 'ˑ', 'symbols' )
    #if debug2: print( "{0} {1}".format( key, open_dict[key][0] ) )
  
  if( output_file != None ):
    try:
      with open(output_file, 'wb') as o_fp:
        json.dump( open_dict, o_fp, check_circular=True, indent=None, sort_keys=True, separators=[',\n', ':'], ensure_ascii=False )
      sys.exit(0)
    except TypeError:
      pass
  j = json.dumps( open_dict, check_circular=True, indent=None, sort_keys=True, separators=[',\n', ':'], ensure_ascii=False )
  print( j )
  sys.exit(0)

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

# fix whole words
def fix_opendict_words( dct ):
  dct.update({"ablation": ["ʌblˈe‍ɪʃən","ʌblˈe‍ɪʃn"]})
  #dct.update({"abdominal": ["æbdˈɒmənəl"]})
  dct.update({"llanos": ["lænˈə‍ʊz"]})
  dct.update({"denouement": ["de‍ɪnˈuːmɔː"]})
  dct.update({"argyll": ["ˈɑːga‍ɪl"]})
  dct.update({"croissant": ["kwæsɒŋ","kwæsɒn"]})
  dct.update({"croissants": ["kwæsɒŋs","kwæsɒns"]})
  dct.update({"bach": ["bˈɒx"]})
  dct.update({"visually": ["vˈɪʒəˈliː"]})
  dct.update({"aba":["æbˈæ"]})
  dct.update({"abalone":["æbˈælə\u200dʊn"]})

if( __name__ == "__main__"):
  main(sys.argv[1:])
