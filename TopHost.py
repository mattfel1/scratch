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
  x254 = self._reqFrame(16, True)
  set this IN_ptr
  c1->setArg(IN_ptr, x254, false);
  print("Allocate mem of size 16 at %p\n" % x254_ptr);
  * x271 = new (16);
  for b18 in range(0,16):
    x271[b18] = b18
  
  done = accel.Done.get()
  ctr = 0
  accel.Enable.set(1)
  while (done == 0):
    done = accel.Done.get()
    time.sleep(0.01)
    ctr = ctr + 1
    if (ctr % 500 == 0): print("  Polled flag %d times..." % ctr)
  
  print("Finished executing TopHost.py!")
  x344 = accel.X255_arg.get()
  time.sleep(0.001)
  x345 = str(x344)
  x346 = (str("got ") + (x345 + (str(", wanted ") + (str("-1") + str("")))));
  x347 = (x346 + str("\n"));
  print(x347)
  x349 = x344 == -1;
  x350 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x349), "%s" % x350
  x351 = accel.X256_arg.get()
  time.sleep(0.001)
  x352 = str(x351)
  x353 = (str("got ") + (x352 + (str(", wanted ") + (str("0") + str("")))));
  x354 = (x353 + str("\n"));
  print(x354)
  x356 = x351 == 0;
  x357 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x356), "%s" % x357
  x358 = accel.X257_arg.get()
  time.sleep(0.001)
  x359 = str(x358)
  x360 = (str("got ") + (x359 + (str(", wanted ") + (str("1") + str("")))));
  x361 = (x360 + str("\n"));
  print(x361)
  x363 = x358 == 1;
  x364 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x363), "%s" % x364
  x365 = accel.X258_arg.get()
  time.sleep(0.001)
  x366 = str(x365)
  x367 = (str("got ") + (x366 + (str(", wanted ") + (str("2") + str("")))));
  x368 = (x367 + str("\n"));
  print(x368)
  x370 = x365 == 2;
  x371 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x370), "%s" % x371
  x372 = accel.X259_arg.get()
  time.sleep(0.001)
  x373 = str(x372)
  x374 = (str("got ") + (x373 + (str(", wanted ") + (str("3") + str("")))));
  x375 = (x374 + str("\n"));
  print(x375)
  x377 = x372 == 3;
  x378 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x377), "%s" % x378
  x379 = accel.X260_arg.get()
  time.sleep(0.001)
  x380 = str(x379)
  x381 = (str("got ") + (x380 + (str(", wanted ") + (str("4") + str("")))));
  x382 = (x381 + str("\n"));
  print(x382)
  x384 = x379 == 4;
  x385 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x384), "%s" % x385
  x386 = accel.X261_arg.get()
  time.sleep(0.001)
  x387 = str(x386)
  x388 = (str("got ") + (x387 + (str(", wanted ") + (str("5") + str("")))));
  x389 = (x388 + str("\n"));
  print(x389)
  x391 = x386 == 5;
  x392 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x391), "%s" % x392
  x393 = accel.X262_arg.get()
  time.sleep(0.001)
  x394 = str(x393)
  x395 = (str("got ") + (x394 + (str(", wanted ") + (str("6") + str("")))));
  x396 = (x395 + str("\n"));
  print(x396)
  x398 = x393 == 6;
  x399 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x398), "%s" % x399
  x400 = accel.X263_arg.get()
  time.sleep(0.001)
  x401 = str(x400)
  x402 = (str("got ") + (x401 + (str(", wanted ") + (str("7") + str("")))));
  x403 = (x402 + str("\n"));
  print(x403)
  x405 = x400 == 7;
  x406 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x405), "%s" % x406
  x407 = accel.X264_arg.get()
  time.sleep(0.001)
  x408 = str(x407)
  x409 = (str("got ") + (x408 + (str(", wanted ") + (str("8") + str("")))));
  x410 = (x409 + str("\n"));
  print(x410)
  x412 = x407 == 8;
  x413 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x412), "%s" % x413
  x414 = accel.X265_arg.get()
  time.sleep(0.001)
  x415 = str(x414)
  x416 = (str("got ") + (x415 + (str(", wanted ") + (str("9") + str("")))));
  x417 = (x416 + str("\n"));
  print(x417)
  x419 = x414 == 9;
  x420 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x419), "%s" % x420
  x421 = accel.X266_arg.get()
  time.sleep(0.001)
  x422 = str(x421)
  x423 = (str("got ") + (x422 + (str(", wanted ") + (str("10") + str("")))));
  x424 = (x423 + str("\n"));
  print(x424)
  x426 = x421 == 10;
  x427 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x426), "%s" % x427
  x428 = accel.X267_arg.get()
  time.sleep(0.001)
  x429 = str(x428)
  x430 = (str("got ") + (x429 + (str(", wanted ") + (str("11") + str("")))));
  x431 = (x430 + str("\n"));
  print(x431)
  x433 = x428 == 11;
  x434 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x433), "%s" % x434
  x435 = accel.X268_arg.get()
  time.sleep(0.001)
  x436 = str(x435)
  x437 = (str("got ") + (x436 + (str(", wanted ") + (str("12") + str("")))));
  x438 = (x437 + str("\n"));
  print(x438)
  x440 = x435 == 12;
  x441 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x440), "%s" % x441
  x442 = accel.X269_arg.get()
  time.sleep(0.001)
  x443 = str(x442)
  x444 = (str("got ") + (x443 + (str(", wanted ") + (str("13") + str("")))));
  x445 = (x444 + str("\n"));
  print(x445)
  x447 = x442 == 13;
  x448 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x447), "%s" % x448
  x449 = accel.X270_arg.get()
  time.sleep(0.001)
  x450 = str(x449)
  x451 = (str("got ") + (x450 + (str(", wanted ") + (str("14") + str("")))));
  x452 = (x451 + str("\n"));
  print(x452)
  x454 = x449 == 14;
  x455 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x454), "%s" % x455

