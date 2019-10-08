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
  x478 = self._reqFrame(32, True)
  set this IN_ptr
  c1->setArg(IN_ptr, x478, false);
  print("Allocate mem of size 32 at %p\n" % x478_ptr);
  x511 = [None for _ in range(32)]
  for b34 in range(0,32):
    x511[b34] = b34
  
  done = accel.Done.get()
  ctr = 0
  accel.Enable.set(1)
  while (done == 0):
    done = accel.Done.get()
    time.sleep(0.01)
    ctr = ctr + 1
    if (ctr % 75 == 0): print("  Polled flag %d times..." % ctr)
  
  print("Finished executing TopHost.py for LoadOnlyTest!
  x632 = accel.X479_arg.get()
  time.sleep(0.001)
  x633 = str(x632)
  x634 = (str("got ") + (x633 + (str(", wanted ") + (str("-1") + str("")))));
  x635 = (x634 + str("\n"));
  print(x635)
  x637 = x632 == -1;
  x638 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x637), "%s" % x638
  x639 = accel.X480_arg.get()
  time.sleep(0.001)
  x640 = str(x639)
  x641 = (str("got ") + (x640 + (str(", wanted ") + (str("0") + str("")))));
  x642 = (x641 + str("\n"));
  print(x642)
  x644 = x639 == 0;
  x645 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x644), "%s" % x645
  x646 = accel.X481_arg.get()
  time.sleep(0.001)
  x647 = str(x646)
  x648 = (str("got ") + (x647 + (str(", wanted ") + (str("1") + str("")))));
  x649 = (x648 + str("\n"));
  print(x649)
  x651 = x646 == 1;
  x652 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x651), "%s" % x652
  x653 = accel.X482_arg.get()
  time.sleep(0.001)
  x654 = str(x653)
  x655 = (str("got ") + (x654 + (str(", wanted ") + (str("2") + str("")))));
  x656 = (x655 + str("\n"));
  print(x656)
  x658 = x653 == 2;
  x659 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x658), "%s" % x659
  x660 = accel.X483_arg.get()
  time.sleep(0.001)
  x661 = str(x660)
  x662 = (str("got ") + (x661 + (str(", wanted ") + (str("3") + str("")))));
  x663 = (x662 + str("\n"));
  print(x663)
  x665 = x660 == 3;
  x666 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x665), "%s" % x666
  x667 = accel.X484_arg.get()
  time.sleep(0.001)
  x668 = str(x667)
  x669 = (str("got ") + (x668 + (str(", wanted ") + (str("4") + str("")))));
  x670 = (x669 + str("\n"));
  print(x670)
  x672 = x667 == 4;
  x673 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x672), "%s" % x673
  x674 = accel.X485_arg.get()
  time.sleep(0.001)
  x675 = str(x674)
  x676 = (str("got ") + (x675 + (str(", wanted ") + (str("5") + str("")))));
  x677 = (x676 + str("\n"));
  print(x677)
  x679 = x674 == 5;
  x680 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x679), "%s" % x680
  x681 = accel.X486_arg.get()
  time.sleep(0.001)
  x682 = str(x681)
  x683 = (str("got ") + (x682 + (str(", wanted ") + (str("6") + str("")))));
  x684 = (x683 + str("\n"));
  print(x684)
  x686 = x681 == 6;
  x687 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x686), "%s" % x687
  x688 = accel.X487_arg.get()
  time.sleep(0.001)
  x689 = str(x688)
  x690 = (str("got ") + (x689 + (str(", wanted ") + (str("7") + str("")))));
  x691 = (x690 + str("\n"));
  print(x691)
  x693 = x688 == 7;
  x694 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x693), "%s" % x694
  x695 = accel.X488_arg.get()
  time.sleep(0.001)
  x696 = str(x695)
  x697 = (str("got ") + (x696 + (str(", wanted ") + (str("8") + str("")))));
  x698 = (x697 + str("\n"));
  print(x698)
  x700 = x695 == 8;
  x701 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x700), "%s" % x701
  x702 = accel.X489_arg.get()
  time.sleep(0.001)
  x703 = str(x702)
  x704 = (str("got ") + (x703 + (str(", wanted ") + (str("9") + str("")))));
  x705 = (x704 + str("\n"));
  print(x705)
  x707 = x702 == 9;
  x708 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x707), "%s" % x708
  x709 = accel.X490_arg.get()
  time.sleep(0.001)
  x710 = str(x709)
  x711 = (str("got ") + (x710 + (str(", wanted ") + (str("10") + str("")))));
  x712 = (x711 + str("\n"));
  print(x712)
  x714 = x709 == 10;
  x715 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x714), "%s" % x715
  x716 = accel.X491_arg.get()
  time.sleep(0.001)
  x717 = str(x716)
  x718 = (str("got ") + (x717 + (str(", wanted ") + (str("11") + str("")))));
  x719 = (x718 + str("\n"));
  print(x719)
  x721 = x716 == 11;
  x722 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x721), "%s" % x722
  x723 = accel.X492_arg.get()
  time.sleep(0.001)
  x724 = str(x723)
  x725 = (str("got ") + (x724 + (str(", wanted ") + (str("12") + str("")))));
  x726 = (x725 + str("\n"));
  print(x726)
  x728 = x723 == 12;
  x729 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x728), "%s" % x729
  x730 = accel.X493_arg.get()
  time.sleep(0.001)
  x731 = str(x730)
  x732 = (str("got ") + (x731 + (str(", wanted ") + (str("13") + str("")))));
  x733 = (x732 + str("\n"));
  print(x733)
  x735 = x730 == 13;
  x736 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x735), "%s" % x736
  x737 = accel.X494_arg.get()
  time.sleep(0.001)
  x738 = str(x737)
  x739 = (str("got ") + (x738 + (str(", wanted ") + (str("14") + str("")))));
  x740 = (x739 + str("\n"));
  print(x740)
  x742 = x737 == 14;
  x743 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x742), "%s" % x743
  x744 = accel.X495_arg.get()
  time.sleep(0.001)
  x745 = str(x744)
  x746 = (str("got ") + (x745 + (str(", wanted ") + (str("15") + str("")))));
  x747 = (x746 + str("\n"));
  print(x747)
  x749 = x744 == 15;
  x750 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x749), "%s" % x750
  x751 = accel.X496_arg.get()
  time.sleep(0.001)
  x752 = str(x751)
  x753 = (str("got ") + (x752 + (str(", wanted ") + (str("16") + str("")))));
  x754 = (x753 + str("\n"));
  print(x754)
  x756 = x751 == 16;
  x757 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x756), "%s" % x757
  x758 = accel.X497_arg.get()
  time.sleep(0.001)
  x759 = str(x758)
  x760 = (str("got ") + (x759 + (str(", wanted ") + (str("17") + str("")))));
  x761 = (x760 + str("\n"));
  print(x761)
  x763 = x758 == 17;
  x764 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x763), "%s" % x764
  x765 = accel.X498_arg.get()
  time.sleep(0.001)
  x766 = str(x765)
  x767 = (str("got ") + (x766 + (str(", wanted ") + (str("18") + str("")))));
  x768 = (x767 + str("\n"));
  print(x768)
  x770 = x765 == 18;
  x771 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x770), "%s" % x771
  x772 = accel.X499_arg.get()
  time.sleep(0.001)
  x773 = str(x772)
  x774 = (str("got ") + (x773 + (str(", wanted ") + (str("19") + str("")))));
  x775 = (x774 + str("\n"));
  print(x775)
  x777 = x772 == 19;
  x778 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x777), "%s" % x778
  x779 = accel.X500_arg.get()
  time.sleep(0.001)
  x780 = str(x779)
  x781 = (str("got ") + (x780 + (str(", wanted ") + (str("20") + str("")))));
  x782 = (x781 + str("\n"));
  print(x782)
  x784 = x779 == 20;
  x785 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x784), "%s" % x785
  x786 = accel.X501_arg.get()
  time.sleep(0.001)
  x787 = str(x786)
  x788 = (str("got ") + (x787 + (str(", wanted ") + (str("21") + str("")))));
  x789 = (x788 + str("\n"));
  print(x789)
  x791 = x786 == 21;
  x792 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x791), "%s" % x792
  x793 = accel.X502_arg.get()
  time.sleep(0.001)
  x794 = str(x793)
  x795 = (str("got ") + (x794 + (str(", wanted ") + (str("22") + str("")))));
  x796 = (x795 + str("\n"));
  print(x796)
  x798 = x793 == 22;
  x799 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x798), "%s" % x799
  x800 = accel.X503_arg.get()
  time.sleep(0.001)
  x801 = str(x800)
  x802 = (str("got ") + (x801 + (str(", wanted ") + (str("23") + str("")))));
  x803 = (x802 + str("\n"));
  print(x803)
  x805 = x800 == 23;
  x806 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x805), "%s" % x806
  x807 = accel.X504_arg.get()
  time.sleep(0.001)
  x808 = str(x807)
  x809 = (str("got ") + (x808 + (str(", wanted ") + (str("24") + str("")))));
  x810 = (x809 + str("\n"));
  print(x810)
  x812 = x807 == 24;
  x813 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x812), "%s" % x813
  x814 = accel.X505_arg.get()
  time.sleep(0.001)
  x815 = str(x814)
  x816 = (str("got ") + (x815 + (str(", wanted ") + (str("25") + str("")))));
  x817 = (x816 + str("\n"));
  print(x817)
  x819 = x814 == 25;
  x820 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x819), "%s" % x820
  x821 = accel.X506_arg.get()
  time.sleep(0.001)
  x822 = str(x821)
  x823 = (str("got ") + (x822 + (str(", wanted ") + (str("26") + str("")))));
  x824 = (x823 + str("\n"));
  print(x824)
  x826 = x821 == 26;
  x827 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x826), "%s" % x827
  x828 = accel.X507_arg.get()
  time.sleep(0.001)
  x829 = str(x828)
  x830 = (str("got ") + (x829 + (str(", wanted ") + (str("27") + str("")))));
  x831 = (x830 + str("\n"));
  print(x831)
  x833 = x828 == 27;
  x834 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x833), "%s" % x834
  x835 = accel.X508_arg.get()
  time.sleep(0.001)
  x836 = str(x835)
  x837 = (str("got ") + (x836 + (str(", wanted ") + (str("28") + str("")))));
  x838 = (x837 + str("\n"));
  print(x838)
  x840 = x835 == 28;
  x841 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x840), "%s" % x841
  x842 = accel.X509_arg.get()
  time.sleep(0.001)
  x843 = str(x842)
  x844 = (str("got ") + (x843 + (str(", wanted ") + (str("29") + str("")))));
  x845 = (x844 + str("\n"));
  print(x845)
  x847 = x842 == 29;
  x848 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x847), "%s" % x848
  x849 = accel.X510_arg.get()
  time.sleep(0.001)
  x850 = str(x849)
  x851 = (str("got ") + (x850 + (str(", wanted ") + (str("30") + str("")))));
  x852 = (x851 + str("\n"));
  print(x852)
  x854 = x849 == 30;
  x855 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:22:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x854), "%s" % x855

