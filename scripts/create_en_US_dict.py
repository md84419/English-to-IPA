#!/usr/bin/python

# USAGE:
#  PYTHONPATH=".." python create_en_US_dict.py > ../eng_to_ipa/resources/en_US.json

import json, logging, os, re, subprocess, sys
from signal import signal, SIGPIPE, SIG_DFL
from eng_to_ipa import transcribe, tokenize

signal(SIGPIPE, SIG_DFL)

logging.basicConfig(format='%(message)s', level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger(__name__)

CMU_DICT      = 'CMU_dict.json'
SYMBOLS_FILE = "cmu.symbols.txt"

def main(argv):
  us_dict = {}
  output_file = None
  
  p_out = subprocess.check_output( ['awk', '-f', 'normalize_json.awk',
                          os.path.join(os.path.abspath(os.path.dirname(__file__)),'..','eng_to_ipa','resources',CMU_DICT ) ] )
  
  cmu_dict = json.loads( p_out )
  
  tokenize.configure( os.path.join(os.path.abspath(os.path.dirname(__file__)),
                         '..','eng_to_ipa','resources','CMU_source_files',SYMBOLS_FILE) )
  
  for key in cmu_dict:
    if( len( cmu_dict[key]) > 1 ):
      log.debug( "MULTI: {0}".format( key ) )
    log.debug( "Input: {0}: {1}".format( key, cmu_dict[key] ) )
    ipa = transcribe.cmu_to_ipa( [cmu_dict[key]], stress_marking='both', sorted_list=False )
    log.debug( "Output: {0}".format( ipa ) )
    cmu_dict[key] = []
    for idx in range( len( ipa[0] ) ):
      # fix CMU dictionary
      ipa[0][idx] = fix_cmu( ipa[0][idx] )

      cmu_dict[key].append( tokenize.tokenize( ipa[0][idx], 'ˑ', 'symbols' ) )

  fix_US_words( cmu_dict )

  j = json.dumps( cmu_dict, check_circular=True, indent=None, separators=[',', ': '], sort_keys=True, ensure_ascii=False )
  j = re.sub(r"{", "{\n", j)
  j = re.sub(r"],", "],\n", j)
  j = re.sub(r"]}", "]\n}", j)
  print( j )

def fix_cmu(source):
  destination = source

  # Use the correct symbol for primary stress marking
  destination.replace( "'", "ˈ")

  # Replace obsolete IPA ligatures with their modern digraph alternatives
  destination = destination.replace("ʤ", "d‍ʒ")
  destination = destination.replace("ʧ", "t‍ʃ")
  destination = destination.replace("ɹ", "r")
  destination = destination.replace("o", "ə")

  # Undo Upton's scheme (Oxford dictionary)
  # See section 7 of https://www.phon.ucl.ac.uk/home/wells/ipa-english-uni.htm
  # See also https://teflpedia.com/IPA_phoneme_/e%C9%99/ and related pages for the other symbols
  destination = destination.replace("ɛr", "e‍ə")
  destination = destination.replace("ɛː", "e‍ə")
  destination = destination.replace("ɛ", "e")
  # Note: we may need similar rules for a -> ae, əː -> ɜː, ʌɪ -> aɪ

  #mark the diphthongs with the non-breaking space character
  destination = destination.replace("aɪ", "a‍ɪ")
  destination = destination.replace("aʊ", "a‍ʊ")
  destination = destination.replace("dʒ", "d‍ʒ")
  destination = destination.replace("eə", "e‍ə")
  destination = destination.replace("eɪ", "e‍ɪ")
  destination = destination.replace("iə", "i‍ə")
  destination = destination.replace("tʃ", "t‍ʃ")
  destination = destination.replace("ɔɪ", "ɔ‍ɪ")
  #destination = destination.replace("əl", "ə‍l")
  destination = destination.replace("əʊ", "ə‍ʊ")
  destination = destination.replace("ɛə", "ɛ‍ə")
  destination = destination.replace("ɪə", "ɪ‍ə")
  destination = destination.replace("ʊə", "ʊ‍ə")

  # Use the standard (quantitative-qualitative) IPA notation scheme for vowels
  # See section 5 of https://www.phon.ucl.ac.uk/home/wells/ipa-english-uni.htm
  #destination = destination.replace("ɒː", "ɒ")
  destination = re.sub("ɑ(?!‍)", "ɒ", destination)
  destination = re.sub("i(?!‍)", "iː", destination)
  destination = re.sub("ɔ(?!‍)", "ɔː", destination)
  destination = re.sub("u(?!‍)", "uː", destination)
  destination = destination.replace("ːː", "ː")

  # undo unusual triphtongs
  destination = destination.replace("ə‍ʊ‍ə", "ə‍ʊ ə")

  return destination

# fix whole words
def fix_US_words( dct ):
  dct.update({'robotica': ["rˑˈə‍ʊˑbˑˈɒˑtˑɪˑkˑʌ"]})

if( __name__ == "__main__"):
  main(sys.argv[1:])
