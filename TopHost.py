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

def execute(accel, cliargs):
  accel.Reset.set(1)
  accel.Enabled.set(0)
  time.sleep(0.01)
  accel.Reset.set(0)
  print("Starting TopHost.py...")
  x37 = cliargs;
  x38 = 0;
  x40 = x37[0]
  x41 = int(x40)
  accel.x38.set(x41)
  time.sleep(0.001)
  done = accel.Done.get()
  ctr = 0
  while (done == 0):
    done = accel.Done.get()
    time.sleep(0.01)
    ctr = ctr + 1
    if (ctr % 10000 == 0) print("  Polled flag %d times..." % str(ctr))
  
  x58 = accel.x39.get()
  time.sleep(0.001)
  x59 = x41 + 383;
  x60 = str(x59)
  x61 = (str("expected: ") + x60);
  x62 = (x61 + str("\n"));
  print(x62)
  x64 = str(x58)
  x65 = (str("result: ") + x64);
  x66 = (x65 + str("\n"));
  print(x66)
  x68 = x59 == x58;
  x69 = ("\n=================\n" + (str("SRAM1D.scala:35:11: Assertion failure") + "\n=================\n"));
  if (true): assert(x68), "%s" % x69
print("Finished executing TopHost.py!")
