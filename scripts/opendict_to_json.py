#!/usr/bin/python

# USAGE:
#  python opendict_to_json.py en_UK.txt > ../open_dict.json

import sys, getopt, subprocess, json, io
from signal import signal, SIGPIPE, SIG_DFL
from eng_to_ipa import tokenize

signal(SIGPIPE, SIG_DFL)

debug  = False
debug2 = False

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
  
  #try:
  #  dict_file = args[0]
  #except IndexError:
  #  print( "{0}: syntax: [-d|-D] en_UK.txt".format( sys.argv[0]) )
  #  sys.exit(2)

  p_out = subprocess.check_output( ['awk', '-f', 'txt_to_json.awk', input_file] )
  
  open_dict = json.loads( p_out )
  for key in open_dict:
    #if debug2: print( open_dict[key][0] )
    #print ( tokenize( open_dict[key][0] ) )
    #mylist.print()
    if( len( open_dict[key]) > 1 ):
      print( key )
    for idx in range( len( open_dict[key] ) ):
      open_dict[key][idx] = tokenize( open_dict[key][idx] )
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

    
      
if( __name__ == "__main__"):
  main(sys.argv[1:])
