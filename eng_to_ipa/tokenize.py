#!/usr/bin/python

# USAGE:
#   tokenize( "ˈɑːdvɑːk" )
#   @returns"ˈɑː d v ɑː k"

import logging, subprocess, json, os
from signal import signal, SIGPIPE, SIG_DFL

signal(SIGPIPE, SIG_DFL)

logging.basicConfig(format='%(message)s', level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger(__name__)

symbols_arr = {}


def configure( config_file ):
  global symbols_arr
  with open( config_file , "r") as symbols_fh:
    for line in symbols_fh:
      line = line.strip();
      l = len(line);
      if l not in symbols_arr:
        symbols_arr[l] = []
      symbols_arr[l].append(line)
  symbols_fh.close();
  


def tokenize( word ):
  mylist = doubly_linked_list();
  mylist.push( word )

  for key in sorted(symbols_arr.keys(), reverse=True):
    if key == 0:
      continue
    while( mylist.tokenize( symbols_arr[key] ) ):
      pass
  return mylist.get()


class Node:
  def __init__( self, data ):
    self.data = data
    self.processed = False
    self.next = None
    self.prev = None
    
class doubly_linked_list:
  def __init__( self ):
    self.head = None
    self.tail = None
    
  def unshift( self, NewVal ):
    NewNode = Node( NewVal )
    NewNode.next = self.head
    if self.head is not None:
      self.head.prev = NewNode
    self.head = NewNode
    if self.tail is None:
      self.tail = NewNode
    
  def push( self, NewVal ):
    NewNode = Node( NewVal )
    NewNode.prev = self.tail
    if self.tail is not None:
      self.tail.next = NewNode
    if self.head is None:
      self.head = NewNode
      self.tail = NewNode
  
  def insert( self, current_node, newVal, NewValBefore, NewValAfter ):
    if current_node is None:
      return
    current_node.data = newVal
    current_node.processed = True
    
    if( len(NewValBefore) > 0 ):
      log.debug( "New lhs: {0}".format( NewValBefore ) )
      NewNode = Node( NewValBefore )
      NewNode.next = current_node
      NewNode.prev = current_node.prev
      if( self.head == current_node ):
        self.head = NewNode
      if( current_node.prev is not None ):
        current_node.prev.next = NewNode
        current_node.prev = NewNode
      if NewNode.data in symbols_arr:
        log.debug( "LHS {0} found in symbols".format( NewNode.data ) )
        NewNode.processed = True
  
    log.debug( "New middle: {0}".format( newVal ) )

    if( len(NewValAfter) > 0 ):
      log.debug( "New rhs: {0}".format( NewValAfter ) )
      NewNode = Node( NewValAfter )
      NewNode.prev = current_node
      NewNode.next = current_node.next
      if( self.tail == current_node ):
        self.tail = NewNode
      if( current_node.next is not None ):
        current_node.next.prev = NewNode
      current_node.next = NewNode
      if NewNode.data in symbols_arr:
        log.debug( "RHS {0} found in symbols".format( NewNode.data ) )
        NewNode.processed = True
        
  def tokenize( self, symbols ):
    doneWork = False
    node = self.head
    if node is None:
      log.debug("head == None")
      return
    while( node is not None ):
      if node.processed == True:
        last = node
        node = node.next
        continue
      for symbol in symbols:
        if node.processed == True:
          last = node
          node = node.next
          break
        log.debug( "Before processing: {0} (with symbol: {1})".format( node.data, symbol ) )
        res = node.data.split( symbol, 1 )
        if( len(res) == 2 ):
          self.insert( node, symbol, res[0], res[1] )
          doneWork = True
          # start again at head
          last = node
          node = self.head
          break
      last = node
      node = node.next
    return doneWork

  def get(self):
    ret = ""
    node = self.head
    while( node is not None):
      ret += "{0}".format(node.data)
      last = node
      node = node.next
      if( (node is not None) and (len(node.data) > 0) ):
        ret += " "
    return ret
