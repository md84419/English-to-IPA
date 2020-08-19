#!/usr/bin/python

# USAGE:
#  PYTHONPATH=".." python opendict_to_json.py ../eng_to_ipa/resources/Opendict_source_files/en_UK.txt > ../eng_to_ipa/resources/Open_dict.json

import getopt, json, io, os, sys, subprocess
from signal import signal, SIGPIPE, SIG_DFL
from eng_to_ipa import tokenize

signal(SIGPIPE, SIG_DFL)

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
  for key in open_dict:
    #if debug2: print( open_dict[key][0] )
    #print ( tokenize( open_dict[key][0] ) )
    #mylist.print()
    if( len( open_dict[key]) > 1 ):
      print( key )
    for idx in range( len( open_dict[key] ) ):
      open_dict[key][idx] = fix_opendict( open_dict[key][idx] )
      open_dict[key][idx] = tokenize.tokenize( open_dict[key][idx] )
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
  # Replace obsolete IPA symbols with their modern alternatives
  destination = destination.replace("ɹ", "r")
  destination = destination.replace("ˈɛ", "ˈe")
  destination = destination.replace("ˌɛ", "ˌe")
  destination = destination.replace("ɛr", "eə")
  destination = destination.replace("ˈɛː", "ˈeə")
  destination = destination.replace("ˌɛː", "ˌeə")
  destination = destination.replace("ɛː", "eə")
  destination = destination.replace("ɛ", "e")

  # Map phonetic to phonemic
  destination = destination.replace("ˈɐ", "ˈʌ")
  destination = destination.replace("ˌɐ", "ˌʌ")
  destination = destination.replace("ɐ", "ʌ")
  return destination
      
if( __name__ == "__main__"):
  main(sys.argv[1:])
