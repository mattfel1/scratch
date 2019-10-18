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
  x415 = base.frameIn
  x416 = np.array([50462976,117835012,185207048,252579084,319951120,387323156,454695192,522067228], dtype='uint64')
  base.frameIn.sendFrame(x416)
  done = accel.Done.get()
  ctr = 0
  accel.Enable.set(1)
  while (done == 0):
    done = accel.Done.get()
    time.sleep(0.01)
    ctr = ctr + 1
    if (ctr % 75 == 0): print("  Polled flag %d times..." % ctr)
  
  print("Finished executing TopHost.py for FrameLoadTest!") 
  x553 = accel.X418_arg.get()
  time.sleep(0.001)
  x554 = str(x553)
  x555 = (str("got ") + (x554 + (str(", wanted ") + (str("0") + str("")))));
  x556 = (x555 + str("\n"));
  print(x556)
  x558 = x553 == 0;
  x559 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x558), "%s" % x559
  x560 = accel.X419_arg.get()
  time.sleep(0.001)
  x561 = str(x560)
  x562 = (str("got ") + (x561 + (str(", wanted ") + (str("1") + str("")))));
  x563 = (x562 + str("\n"));
  print(x563)
  x565 = x560 == 1;
  x566 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x565), "%s" % x566
  x567 = accel.X420_arg.get()
  time.sleep(0.001)
  x568 = str(x567)
  x569 = (str("got ") + (x568 + (str(", wanted ") + (str("2") + str("")))));
  x570 = (x569 + str("\n"));
  print(x570)
  x572 = x567 == 2;
  x573 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x572), "%s" % x573
  x574 = accel.X421_arg.get()
  time.sleep(0.001)
  x575 = str(x574)
  x576 = (str("got ") + (x575 + (str(", wanted ") + (str("3") + str("")))));
  x577 = (x576 + str("\n"));
  print(x577)
  x579 = x574 == 3;
  x580 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x579), "%s" % x580
  x581 = accel.X422_arg.get()
  time.sleep(0.001)
  x582 = str(x581)
  x583 = (str("got ") + (x582 + (str(", wanted ") + (str("4") + str("")))));
  x584 = (x583 + str("\n"));
  print(x584)
  x586 = x581 == 4;
  x587 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x586), "%s" % x587
  x588 = accel.X423_arg.get()
  time.sleep(0.001)
  x589 = str(x588)
  x590 = (str("got ") + (x589 + (str(", wanted ") + (str("5") + str("")))));
  x591 = (x590 + str("\n"));
  print(x591)
  x593 = x588 == 5;
  x594 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x593), "%s" % x594
  x595 = accel.X424_arg.get()
  time.sleep(0.001)
  x596 = str(x595)
  x597 = (str("got ") + (x596 + (str(", wanted ") + (str("6") + str("")))));
  x598 = (x597 + str("\n"));
  print(x598)
  x600 = x595 == 6;
  x601 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x600), "%s" % x601
  x602 = accel.X425_arg.get()
  time.sleep(0.001)
  x603 = str(x602)
  x604 = (str("got ") + (x603 + (str(", wanted ") + (str("7") + str("")))));
  x605 = (x604 + str("\n"));
  print(x605)
  x607 = x602 == 7;
  x608 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x607), "%s" % x608
  x609 = accel.X426_arg.get()
  time.sleep(0.001)
  x610 = str(x609)
  x611 = (str("got ") + (x610 + (str(", wanted ") + (str("8") + str("")))));
  x612 = (x611 + str("\n"));
  print(x612)
  x614 = x609 == 8;
  x615 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x614), "%s" % x615
  x616 = accel.X427_arg.get()
  time.sleep(0.001)
  x617 = str(x616)
  x618 = (str("got ") + (x617 + (str(", wanted ") + (str("9") + str("")))));
  x619 = (x618 + str("\n"));
  print(x619)
  x621 = x616 == 9;
  x622 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x621), "%s" % x622
  x623 = accel.X428_arg.get()
  time.sleep(0.001)
  x624 = str(x623)
  x625 = (str("got ") + (x624 + (str(", wanted ") + (str("10") + str("")))));
  x626 = (x625 + str("\n"));
  print(x626)
  x628 = x623 == 10;
  x629 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x628), "%s" % x629
  x630 = accel.X429_arg.get()
  time.sleep(0.001)
  x631 = str(x630)
  x632 = (str("got ") + (x631 + (str(", wanted ") + (str("11") + str("")))));
  x633 = (x632 + str("\n"));
  print(x633)
  x635 = x630 == 11;
  x636 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x635), "%s" % x636
  x637 = accel.X430_arg.get()
  time.sleep(0.001)
  x638 = str(x637)
  x639 = (str("got ") + (x638 + (str(", wanted ") + (str("12") + str("")))));
  x640 = (x639 + str("\n"));
  print(x640)
  x642 = x637 == 12;
  x643 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x642), "%s" % x643
  x644 = accel.X431_arg.get()
  time.sleep(0.001)
  x645 = str(x644)
  x646 = (str("got ") + (x645 + (str(", wanted ") + (str("13") + str("")))));
  x647 = (x646 + str("\n"));
  print(x647)
  x649 = x644 == 13;
  x650 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x649), "%s" % x650
  x651 = accel.X432_arg.get()
  time.sleep(0.001)
  x652 = str(x651)
  x653 = (str("got ") + (x652 + (str(", wanted ") + (str("14") + str("")))));
  x654 = (x653 + str("\n"));
  print(x654)
  x656 = x651 == 14;
  x657 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x656), "%s" % x657
  x658 = accel.X433_arg.get()
  time.sleep(0.001)
  x659 = str(x658)
  x660 = (str("got ") + (x659 + (str(", wanted ") + (str("15") + str("")))));
  x661 = (x660 + str("\n"));
  print(x661)
  x663 = x658 == 15;
  x664 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x663), "%s" % x664
  x665 = accel.X434_arg.get()
  time.sleep(0.001)
  x666 = str(x665)
  x667 = (str("got ") + (x666 + (str(", wanted ") + (str("16") + str("")))));
  x668 = (x667 + str("\n"));
  print(x668)
  x670 = x665 == 16;
  x671 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x670), "%s" % x671
  x672 = accel.X435_arg.get()
  time.sleep(0.001)
  x673 = str(x672)
  x674 = (str("got ") + (x673 + (str(", wanted ") + (str("17") + str("")))));
  x675 = (x674 + str("\n"));
  print(x675)
  x677 = x672 == 17;
  x678 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x677), "%s" % x678
  x679 = accel.X436_arg.get()
  time.sleep(0.001)
  x680 = str(x679)
  x681 = (str("got ") + (x680 + (str(", wanted ") + (str("18") + str("")))));
  x682 = (x681 + str("\n"));
  print(x682)
  x684 = x679 == 18;
  x685 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x684), "%s" % x685
  x686 = accel.X437_arg.get()
  time.sleep(0.001)
  x687 = str(x686)
  x688 = (str("got ") + (x687 + (str(", wanted ") + (str("19") + str("")))));
  x689 = (x688 + str("\n"));
  print(x689)
  x691 = x686 == 19;
  x692 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x691), "%s" % x692
  x693 = accel.X438_arg.get()
  time.sleep(0.001)
  x694 = str(x693)
  x695 = (str("got ") + (x694 + (str(", wanted ") + (str("20") + str("")))));
  x696 = (x695 + str("\n"));
  print(x696)
  x698 = x693 == 20;
  x699 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x698), "%s" % x699
  x700 = accel.X439_arg.get()
  time.sleep(0.001)
  x701 = str(x700)
  x702 = (str("got ") + (x701 + (str(", wanted ") + (str("21") + str("")))));
  x703 = (x702 + str("\n"));
  print(x703)
  x705 = x700 == 21;
  x706 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x705), "%s" % x706
  x707 = accel.X440_arg.get()
  time.sleep(0.001)
  x708 = str(x707)
  x709 = (str("got ") + (x708 + (str(", wanted ") + (str("22") + str("")))));
  x710 = (x709 + str("\n"));
  print(x710)
  x712 = x707 == 22;
  x713 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x712), "%s" % x713
  x714 = accel.X441_arg.get()
  time.sleep(0.001)
  x715 = str(x714)
  x716 = (str("got ") + (x715 + (str(", wanted ") + (str("23") + str("")))));
  x717 = (x716 + str("\n"));
  print(x717)
  x719 = x714 == 23;
  x720 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x719), "%s" % x720
  x721 = accel.X442_arg.get()
  time.sleep(0.001)
  x722 = str(x721)
  x723 = (str("got ") + (x722 + (str(", wanted ") + (str("24") + str("")))));
  x724 = (x723 + str("\n"));
  print(x724)
  x726 = x721 == 24;
  x727 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x726), "%s" % x727
  x728 = accel.X443_arg.get()
  time.sleep(0.001)
  x729 = str(x728)
  x730 = (str("got ") + (x729 + (str(", wanted ") + (str("25") + str("")))));
  x731 = (x730 + str("\n"));
  print(x731)
  x733 = x728 == 25;
  x734 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x733), "%s" % x734
  x735 = accel.X444_arg.get()
  time.sleep(0.001)
  x736 = str(x735)
  x737 = (str("got ") + (x736 + (str(", wanted ") + (str("26") + str("")))));
  x738 = (x737 + str("\n"));
  print(x738)
  x740 = x735 == 26;
  x741 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x740), "%s" % x741
  x742 = accel.X445_arg.get()
  time.sleep(0.001)
  x743 = str(x742)
  x744 = (str("got ") + (x743 + (str(", wanted ") + (str("27") + str("")))));
  x745 = (x744 + str("\n"));
  print(x745)
  x747 = x742 == 27;
  x748 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x747), "%s" % x748
  x749 = accel.X446_arg.get()
  time.sleep(0.001)
  x750 = str(x749)
  x751 = (str("got ") + (x750 + (str(", wanted ") + (str("28") + str("")))));
  x752 = (x751 + str("\n"));
  print(x752)
  x754 = x749 == 28;
  x755 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x754), "%s" % x755
  x756 = accel.X447_arg.get()
  time.sleep(0.001)
  x757 = str(x756)
  x758 = (str("got ") + (x757 + (str(", wanted ") + (str("29") + str("")))));
  x759 = (x758 + str("\n"));
  print(x759)
  x761 = x756 == 29;
  x762 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x761), "%s" % x762
  x763 = accel.X448_arg.get()
  time.sleep(0.001)
  x764 = str(x763)
  x765 = (str("got ") + (x764 + (str(", wanted ") + (str("30") + str("")))));
  x766 = (x765 + str("\n"));
  print(x766)
  x768 = x763 == 30;
  x769 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x768), "%s" % x769
  x770 = accel.X449_arg.get()
  time.sleep(0.001)
  x771 = str(x770)
  x772 = (str("got ") + (x771 + (str(", wanted ") + (str("31") + str("")))));
  x773 = (x772 + str("\n"));
  print(x773)
  x775 = x770 == 31;
  x776 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (True): assert(x775), "%s" % x776

