#!/usr/bin/env python3
import setupLibPaths

import sys
import argparse
import rogue
import rogue.hardware.axi
import rogue.interfaces.stream
import rogue.interfaces.memory

import pyrogue as pr
import pyrogue.gui
import pyrogue.utilities.prbs
import pyrogue.interfaces.simulation

import axipcie  as pcie
# import rogue.axi as axi

import time
import math
import random
import struct
import numpy as np

def execute(base, cliargs):
  accel = base.Fpga.SpatialBox
  accel.Reset.set(1)
  accel.Enable.set(0)
  time.sleep(0.01)
  accel.Reset.set(0)
  print("Starting TopHost.py...")
  x77 = base.frameIn
  done = accel.Done.get()
  ctr = 0
  accel.Enable.set(1)
  while (done == 0):
    done = accel.Done.get()
    time.sleep(0.01)
    ctr = ctr + 1
    if (ctr % 75 == 0): print("  Polled flag %d times..." % ctr)
  
  print("Finished executing TopHost.py for FrameStoreTest!") 
  x108 = np.zeros(8, dtype='uint64')
  # x109 in get x77 to x108
  x110 = np.array([50462976,117835012,185207048,252579084,319951120,387323156,454695192,522067228], dtype='uint64')
  x111 = (str("Wanted:") + str("\n"));
  print(x111)
  x113 = len(x110)
  for b27 in range(0,x113,1):
    x114 = x110[b27]
    x115 = str(x114)
    x116 = (x115 + str(" "));
    print(x116)
  
  print(str("\n"))
  x120 = (str("Got:") + str("\n"));
  print(x120)
  x122 = len(x108)
  for b37 in range(0,x122,1):
    x123 = x108[b37]
    x124 = str(x123)
    x125 = (x124 + str(" "));
    print(x125)
  
  print(str("\n"))
  x132 = np.zeros(len(x108), dtype=bool)
  for b44 in range(len(x108)):
    x129 = x108[b44]
    x130 = x110[b44]
    x131 = x129 == x130;
    x132[b44] = x131
  
  x134 = np.zeros(len(x132),dtype='bool')
  for b49 in range(0,len(x132)):
    x133 = x132[b49]
    x134[b49] = x133
  
  x137 = 0
  if (len(x134) > 0): # Hack to handle reductions on things of length 0
    x137 = x134[0]
  else:
    x137 = 0
  
  for b52 in range(1,len(x134)):
    b53 = x134[b52]
    b54 = x137;
    x136 = b53 & b54;
    x137 = x136;
  
  x138 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:43:11: Assertion failure") + "\n=================\n"));
  if (True): assert(x137), "%s" % x138

