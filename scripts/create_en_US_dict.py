#!/usr/bin/python

# USAGE:
#  PYTHONPATH="../.." python create_en_US_dict.py

import json, logging, os, re, subprocess, sys
from signal import signal, SIGPIPE, SIG_DFL
from eng_to_ipa import transcribe, tokenize

signal(SIGPIPE, SIG_DFL)

logging.basicConfig(format='%(message)s', level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger(__name__)

CMU_DICT      = 'CMU_dict.json'
#CMU_DICT      = 'en_US.json'
SYMBOLS_FILE = "cmu.symbols.txt"

def main(argv):
  us_dict = {}
  output_file = None
  
  p_out = subprocess.check_output( ['awk', '-f', '../../scripts/normalize_json.awk', CMU_DICT] )
  
  cmu_dict = json.loads( p_out )
  
  #words = "teacher".split()
  #print( words )
  #cmu = transcribe.get_cmu(words, db_type='sql')
  #print( cmu )
  #ipa = transcribe.cmu_to_ipa( cmu, stress_marking='both' )
  #print( ipa[0][0] )
  ##print( transcribe.cmu_to_ipa( ["a1 r d v aa2 r k"], stress_marking=True ) )
  #sys.exit(2)
  
  tokenize.configure( os.path.join(os.path.abspath(os.path.dirname(__file__)),
                         'CMU_source_files',SYMBOLS_FILE) )
  
  for key in cmu_dict:
    #if debug2: print( open_dict[key][0] )
    #print ( tokenize( open_dict[key][0] ) )
    #mylist.print()
    if( len( cmu_dict[key]) > 1 ):
      log.debug( "MULTI: {0}".format( key ) )
    for idx in range( len( cmu_dict[key] ) ):
      cmu = [[cmu_dict[key][idx]]]
      log.debug( "Input: {0}: {1}".format( key, cmu ) )
      ipa = transcribe.cmu_to_ipa( cmu, stress_marking='both' )
      log.debug( "Output: {0}".format( ipa ) )
      cmu_dict[key][idx] = tokenize.tokenize( ipa[0][0] )
      
  j = json.dumps( cmu_dict, check_circular=True, indent=None, separators=[',', ': '], sort_keys=True, ensure_ascii=False )
  j = re.sub(r"{", "{\n", j)
  j = re.sub(r"],", "],\n", j)
  j = re.sub(r"]}", "]\n}", j)
  print( j )
  
if( __name__ == "__main__"):
  main(sys.argv[1:])