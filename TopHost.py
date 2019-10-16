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
  x61 = base.frameIn
  done = accel.Done.get()
  ctr = 0
  accel.Enable.set(1)
  while (done == 0):
    done = accel.Done.get()
    time.sleep(0.01)
    ctr = ctr + 1
    if (ctr % 75 == 0): print("  Polled flag %d times..." % ctr)
  
  print("Finished executing TopHost.py for FrameStoreTest!") 
  x92 = np.zeros(8, dtype='uint32')
  # x93 in get x61 to x92
  x94 = np.array([50462976,117835012,185207048,252579084,319951120,387323156,454695192,522067228], dtype='uint64')
  x95 = (str("Wanted:") + str("\n"));
  print(x95)
  x97 = len(x94)
  for b26 in range(0,x97,1):
    x98 = x94[b26]
    x99 = str(x98)
    x100 = (x99 + str(" "));
    print(x100)
  
  print(str("\n"))
  x104 = (str("Got:") + str("\n"));
  print(x104)
  x106 = len(x92)
  for b36 in range(0,x106,1):
    x107 = x92[b36]
    x108 = str(x107)
    x109 = (x108 + str(" "));
    print(x109)
  
  print(str("\n"))
  x113 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:43:11: Assertion failure") + "\n=================\n"));
  if (True): assert(false), "%s" % x113

