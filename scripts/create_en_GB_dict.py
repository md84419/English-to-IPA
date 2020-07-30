#!/usr/bin/python

# Creates en_GB.json from the Open, Britfone and CMU dictionaries

# USAGE:
#  PYTHONPATH=".." python create_en_GB_dict.py > ../eng_to_ipa/resources/en_GB.json

import copy, json, logging, os, re, sys
from signal import signal, SIGPIPE, SIG_DFL

signal(SIGPIPE, SIG_DFL)

OPEN_DICT     = 'Open_dict.json'
BRITFONE_DICT = 'Britfone_dict.json'
CMU_DICT      = 'en_US.json'
EN_GB_DICT    = 'en_GB.json'

debug = False
debug2 = False

logging.basicConfig(format='%(message)s', level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger(__name__)

def main(argv):
  gb_dict = {}
  output_file = None
  britfone_count =0
  opendict_count = 0
  both_count = 0
  cmu_count = 0
  
  with open( os.path.join(os.path.abspath(os.path.dirname(__file__)),
                         '..','eng_to_ipa','resources',OPEN_DICT), 'r') as o_fh:
    open_dict = json.load( o_fh )
  with open( os.path.join(os.path.abspath(os.path.dirname(__file__)),
                         '..','eng_to_ipa','resources',BRITFONE_DICT), 'r') as b_fh:
    britfone_dict = json.load( b_fh )
  with open( os.path.join(os.path.abspath(os.path.dirname(__file__)),
                         '..','eng_to_ipa','resources',CMU_DICT), 'r') as c_fh:
    cmu_dict = json.load( c_fh )

  # convert britfone_dict to value list
  keys = list(britfone_dict)
  for key in keys:
    idx = key.find( '(' )
    if( idx > -1 ):
      log.debug( "Found '(' in {0}".format( key ) )
      tmpkey = key[0:idx]
      log.debug( "tmpkey is {0}".format( tmpkey ) )
      if ( tmpkey not in britfone_dict ):
        britfone_dict[tmpkey] = []
      for idx in range( len( britfone_dict[key] ) ):
        if( britfone_dict[key][idx] not in britfone_dict[tmpkey] ):
          britfone_dict[tmpkey].append( britfone_dict[key][idx] )
      britfone_dict.pop(key, None)
      log.debug( "New value is {0}: {1}".format( tmpkey, britfone_dict[tmpkey] ) )
  
  gb_dict = copy.deepcopy( open_dict )
  opendict_count = len( gb_dict )
  for key in britfone_dict:
    if( key not in gb_dict ):
      gb_dict[key] = []
      britfone_count +=1
    else:
      both_count +=1
      opendict_count -=1
    for idx in range( len( britfone_dict[key] ) ):
      if( britfone_dict[key][idx] not in gb_dict[key] ):
        gb_dict[key].append( britfone_dict[key][idx] )
        log.debug( "Added open_dict '{0}' to en_GB".format( key ) )
  
  for key in cmu_dict:
#    if( key in britfone_dict ):
#      gb_dict[key] = []
#      for idx in range( len( britfone_dict[key] ) ):
#        gb_dict[key].append( britfone_dict[key][idx] )
#        log.debug( "Added britfone '{0}' to en_GB".format( key ) )
#    else:
#      log.debug( "'{0}' not found in britfone dict".format( key ) )
#    if( key in open_dict ):
#      if ( key not in gb_dict ):
#        gb_dict[key] = []
#      for idx in range( len( open_dict[key] ) ):
#        if( open_dict[key][idx] not in gb_dict[key] ):
#          gb_dict[key].append( open_dict[key][idx] )
#          log.debug( "Added open_dict '{0}' to en_GB".format( key ) )
    if( key not in open_dict ):
      log.debug( "'{0}' not found in Open dict".format( key ) )
    if( key not in gb_dict ):
      log.debug( "'{0}' not found in en_GB: adding CMU".format( key ) )
      gb_dict[key] = []
      gb_dict[key].append( cmu_dict[key][0] )
      cmu_count += 1
    log.debug( "{0}: {1}".format( key, gb_dict[key] ) )

  if( output_file != None ):
    try:
      with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                         '..','eng_to_ipa','resources',output_file), 'wb') as o_fp:
        json.dump( open_dict, o_fp, check_circular=True, indent=None, sort_keys=True, separators=[',\n', ':'], ensure_ascii=False )
      sys.exit(0)
    except TypeError:
      pass
  j = json.dumps( gb_dict, check_circular=True, indent=None, separators=[',', ': '], sort_keys=True, ensure_ascii=False )
  j = re.sub("{", "{\n", j)
  j = re.sub("],", "],\n", j)
  j = re.sub("]}", "]\n}", j)
  print( j )
  log.info( "Entries Britfone keys: {0}".format( britfone_count ) )
  log.info( "Entries Opendict keys: {0}".format( opendict_count ) )
  log.info( "Entries using both keys: {0}".format( both_count ) )
  log.info( "Entries using en_US keys: {0}".format( cmu_count ) )
  log.info( "Total Entries in en_GB dictionary: {0}".format( len( gb_dict ) ) )
  sys.exit(0)

if( __name__ == "__main__"):
  main(sys.argv[1:])

