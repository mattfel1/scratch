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
import surf.axi as axi

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
  x44 = cliargs;
  x45 = 0;
  x47 = x44[0]
  x48 = int(x47)
  accel.X_arg.set(x48)
  print("Wrote %d to x45!" % x48)
  time.sleep(0.001)
  done = accel.Done.get()
  ctr = 0
  accel.Enable.set(1)
  while (done == 0):
    done = accel.Done.get()
    time.sleep(0.01)
    ctr = ctr + 1
    if (ctr % 500 == 0): print("  Polled flag %d times..." % ctr)
  
  print("Finished executing TopHost.py!")
  x71 = accel.Y_arg.get()
  time.sleep(0.001)
  x72 = x48 + 8191;
  x73 = str(x72)
  x74 = (str("expected: ") + x73);
  x75 = (x74 + str("\n"));
  print(x75)
  x77 = str(x71)
  x78 = (str("result: ") + x77);
  x79 = (x78 + str("\n"));
  print(x79)
  x81 = x72 == x71;
  x82 = ("\n=================\n" + (str("SRAM2D.scala:28:11: Assertion failure") + "\n=================\n"));
  if (true): assert(x81), "%s" % x82

