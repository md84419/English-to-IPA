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

  britfone_dict = fix_britfone( britfone_dict )

  # create gb dict from Open_dict
  # add in Britfone_dict entries
  gb_dict = fix_gb( open_dict )
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

  # add in entries from the US dictionary if the word isn't in the GB dictioanry
  for key in cmu_dict:
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

def fix_britfone(source):
  """Add the IPA nobreak characters to the diphthongs, as these aren't present in the source file"""
  destination = source
  for key1 in destination:
    for key2 in range( len( destination[key1] )):
      # Replace obsolete IPA symbols with their modern alternatives
      destination[key1][key2] = destination[key1][key2].replace("ɹ", "r")

      # Undo Upton's scheme (Oxford dictionary)
      # See section 7 of https://www.phon.ucl.ac.uk/home/wells/ipa-english-uni.htm
      # See also https://teflpedia.com/IPA_phoneme_/e%C9%99/ and related pages for the other symbols
      destination[key1][key2] = destination[key1][key2].replace("ˈɛ", "ˈe")
      destination[key1][key2] = destination[key1][key2].replace("ˌɛ", "ˌe")
      destination[key1][key2] = destination[key1][key2].replace("ɛr", "e‍ə")
      destination[key1][key2] = destination[key1][key2].replace("ɛː", "e‍ə")
      destination[key1][key2] = destination[key1][key2].replace("ɛ", "e")

      # Use the standard (quantitative-qualitative) IPA notation scheme for vowels
      # See section 5 of https://www.phon.ucl.ac.uk/home/wells/ipa-english-uni.htm
      destination[key1][key2] = destination[key1][key2].replace("ɑ", "ɑː")
      destination[key1][key2] = destination[key1][key2].replace("ɒː", "ɒ")
      destination[key1][key2] = destination[key1][key2].replace("i", "iː")
      destination[key1][key2] = destination[key1][key2].replace("ɔ", "ɔː")
      destination[key1][key2] = destination[key1][key2].replace("u", "uː")
      destination[key1][key2] = destination[key1][key2].replace("ːː", "ː")

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
  return destination

def fix_gb(source):
  destination = copy.deepcopy( source )
  for key1 in destination:
    for key2 in range( len( destination[key1] )):
      # Replace obsolete IPA symbols with their modern alternatives
      destination[key1][key2] = destination[key1][key2].replace("ɹ", "r")

      # Undo Upton's scheme (Oxford dictionary)
      # See section 7 of https://www.phon.ucl.ac.uk/home/wells/ipa-english-uni.htm
      # See also https://teflpedia.com/IPA_phoneme_/e%C9%99/ and related pages for the other symbols
      destination[key1][key2] = destination[key1][key2].replace("ˈɛ", "ˈe")
      destination[key1][key2] = destination[key1][key2].replace("ˌɛ", "ˌe")
      destination[key1][key2] = destination[key1][key2].replace("ɛr", "e‍ə")
      destination[key1][key2] = destination[key1][key2].replace("ɛː", "e‍ə")
      destination[key1][key2] = destination[key1][key2].replace("ɛ", "e")
  return destination

if( __name__ == "__main__"):
  main(sys.argv[1:])

