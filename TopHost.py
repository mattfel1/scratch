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
  # x417 = new frame of size 8, called IN_ptr
  x418 = [Const(34),Const(94),Const(154),Const(214),Const(274),Const(334),Const(394),Const(454)]
  # x419 in set x417 with x418
  done = accel.Done.get()
  ctr = 0
  accel.Enable.set(1)
  while (done == 0):
    done = accel.Done.get()
    time.sleep(0.01)
    ctr = ctr + 1
    if (ctr % 75 == 0): print("  Polled flag %d times..." % ctr)
  
  print("Finished executing TopHost.py for FrameLoadTest!") 
  x556 = accel.X420_arg.get()
  time.sleep(0.001)
  x557 = str(x556)
  x558 = (str("got ") + (x557 + (str(", wanted ") + (str("-1") + str("")))));
  x559 = (x558 + str("\n"));
  print(x559)
  x561 = x556 == 65535;
  x562 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x561), "%s" % x562
  x563 = accel.X421_arg.get()
  time.sleep(0.001)
  x564 = str(x563)
  x565 = (str("got ") + (x564 + (str(", wanted ") + (str("0") + str("")))));
  x566 = (x565 + str("\n"));
  print(x566)
  x568 = x563 == 0;
  x569 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x568), "%s" % x569
  x570 = accel.X422_arg.get()
  time.sleep(0.001)
  x571 = str(x570)
  x572 = (str("got ") + (x571 + (str(", wanted ") + (str("1") + str("")))));
  x573 = (x572 + str("\n"));
  print(x573)
  x575 = x570 == 1;
  x576 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x575), "%s" % x576
  x577 = accel.X423_arg.get()
  time.sleep(0.001)
  x578 = str(x577)
  x579 = (str("got ") + (x578 + (str(", wanted ") + (str("2") + str("")))));
  x580 = (x579 + str("\n"));
  print(x580)
  x582 = x577 == 2;
  x583 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x582), "%s" % x583
  x584 = accel.X424_arg.get()
  time.sleep(0.001)
  x585 = str(x584)
  x586 = (str("got ") + (x585 + (str(", wanted ") + (str("3") + str("")))));
  x587 = (x586 + str("\n"));
  print(x587)
  x589 = x584 == 3;
  x590 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x589), "%s" % x590
  x591 = accel.X425_arg.get()
  time.sleep(0.001)
  x592 = str(x591)
  x593 = (str("got ") + (x592 + (str(", wanted ") + (str("4") + str("")))));
  x594 = (x593 + str("\n"));
  print(x594)
  x596 = x591 == 4;
  x597 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x596), "%s" % x597
  x598 = accel.X426_arg.get()
  time.sleep(0.001)
  x599 = str(x598)
  x600 = (str("got ") + (x599 + (str(", wanted ") + (str("5") + str("")))));
  x601 = (x600 + str("\n"));
  print(x601)
  x603 = x598 == 5;
  x604 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x603), "%s" % x604
  x605 = accel.X427_arg.get()
  time.sleep(0.001)
  x606 = str(x605)
  x607 = (str("got ") + (x606 + (str(", wanted ") + (str("6") + str("")))));
  x608 = (x607 + str("\n"));
  print(x608)
  x610 = x605 == 6;
  x611 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x610), "%s" % x611
  x612 = accel.X428_arg.get()
  time.sleep(0.001)
  x613 = str(x612)
  x614 = (str("got ") + (x613 + (str(", wanted ") + (str("7") + str("")))));
  x615 = (x614 + str("\n"));
  print(x615)
  x617 = x612 == 7;
  x618 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x617), "%s" % x618
  x619 = accel.X429_arg.get()
  time.sleep(0.001)
  x620 = str(x619)
  x621 = (str("got ") + (x620 + (str(", wanted ") + (str("8") + str("")))));
  x622 = (x621 + str("\n"));
  print(x622)
  x624 = x619 == 8;
  x625 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x624), "%s" % x625
  x626 = accel.X430_arg.get()
  time.sleep(0.001)
  x627 = str(x626)
  x628 = (str("got ") + (x627 + (str(", wanted ") + (str("9") + str("")))));
  x629 = (x628 + str("\n"));
  print(x629)
  x631 = x626 == 9;
  x632 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x631), "%s" % x632
  x633 = accel.X431_arg.get()
  time.sleep(0.001)
  x634 = str(x633)
  x635 = (str("got ") + (x634 + (str(", wanted ") + (str("10") + str("")))));
  x636 = (x635 + str("\n"));
  print(x636)
  x638 = x633 == 10;
  x639 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x638), "%s" % x639
  x640 = accel.X432_arg.get()
  time.sleep(0.001)
  x641 = str(x640)
  x642 = (str("got ") + (x641 + (str(", wanted ") + (str("11") + str("")))));
  x643 = (x642 + str("\n"));
  print(x643)
  x645 = x640 == 11;
  x646 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x645), "%s" % x646
  x647 = accel.X433_arg.get()
  time.sleep(0.001)
  x648 = str(x647)
  x649 = (str("got ") + (x648 + (str(", wanted ") + (str("12") + str("")))));
  x650 = (x649 + str("\n"));
  print(x650)
  x652 = x647 == 12;
  x653 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x652), "%s" % x653
  x654 = accel.X434_arg.get()
  time.sleep(0.001)
  x655 = str(x654)
  x656 = (str("got ") + (x655 + (str(", wanted ") + (str("13") + str("")))));
  x657 = (x656 + str("\n"));
  print(x657)
  x659 = x654 == 13;
  x660 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x659), "%s" % x660
  x661 = accel.X435_arg.get()
  time.sleep(0.001)
  x662 = str(x661)
  x663 = (str("got ") + (x662 + (str(", wanted ") + (str("14") + str("")))));
  x664 = (x663 + str("\n"));
  print(x664)
  x666 = x661 == 14;
  x667 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x666), "%s" % x667
  x668 = accel.X436_arg.get()
  time.sleep(0.001)
  x669 = str(x668)
  x670 = (str("got ") + (x669 + (str(", wanted ") + (str("15") + str("")))));
  x671 = (x670 + str("\n"));
  print(x671)
  x673 = x668 == 15;
  x674 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x673), "%s" % x674
  x675 = accel.X437_arg.get()
  time.sleep(0.001)
  x676 = str(x675)
  x677 = (str("got ") + (x676 + (str(", wanted ") + (str("16") + str("")))));
  x678 = (x677 + str("\n"));
  print(x678)
  x680 = x675 == 16;
  x681 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x680), "%s" % x681
  x682 = accel.X438_arg.get()
  time.sleep(0.001)
  x683 = str(x682)
  x684 = (str("got ") + (x683 + (str(", wanted ") + (str("17") + str("")))));
  x685 = (x684 + str("\n"));
  print(x685)
  x687 = x682 == 17;
  x688 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x687), "%s" % x688
  x689 = accel.X439_arg.get()
  time.sleep(0.001)
  x690 = str(x689)
  x691 = (str("got ") + (x690 + (str(", wanted ") + (str("18") + str("")))));
  x692 = (x691 + str("\n"));
  print(x692)
  x694 = x689 == 18;
  x695 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x694), "%s" % x695
  x696 = accel.X440_arg.get()
  time.sleep(0.001)
  x697 = str(x696)
  x698 = (str("got ") + (x697 + (str(", wanted ") + (str("19") + str("")))));
  x699 = (x698 + str("\n"));
  print(x699)
  x701 = x696 == 19;
  x702 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x701), "%s" % x702
  x703 = accel.X441_arg.get()
  time.sleep(0.001)
  x704 = str(x703)
  x705 = (str("got ") + (x704 + (str(", wanted ") + (str("20") + str("")))));
  x706 = (x705 + str("\n"));
  print(x706)
  x708 = x703 == 20;
  x709 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x708), "%s" % x709
  x710 = accel.X442_arg.get()
  time.sleep(0.001)
  x711 = str(x710)
  x712 = (str("got ") + (x711 + (str(", wanted ") + (str("21") + str("")))));
  x713 = (x712 + str("\n"));
  print(x713)
  x715 = x710 == 21;
  x716 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x715), "%s" % x716
  x717 = accel.X443_arg.get()
  time.sleep(0.001)
  x718 = str(x717)
  x719 = (str("got ") + (x718 + (str(", wanted ") + (str("22") + str("")))));
  x720 = (x719 + str("\n"));
  print(x720)
  x722 = x717 == 22;
  x723 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x722), "%s" % x723
  x724 = accel.X444_arg.get()
  time.sleep(0.001)
  x725 = str(x724)
  x726 = (str("got ") + (x725 + (str(", wanted ") + (str("23") + str("")))));
  x727 = (x726 + str("\n"));
  print(x727)
  x729 = x724 == 23;
  x730 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x729), "%s" % x730
  x731 = accel.X445_arg.get()
  time.sleep(0.001)
  x732 = str(x731)
  x733 = (str("got ") + (x732 + (str(", wanted ") + (str("24") + str("")))));
  x734 = (x733 + str("\n"));
  print(x734)
  x736 = x731 == 24;
  x737 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x736), "%s" % x737
  x738 = accel.X446_arg.get()
  time.sleep(0.001)
  x739 = str(x738)
  x740 = (str("got ") + (x739 + (str(", wanted ") + (str("25") + str("")))));
  x741 = (x740 + str("\n"));
  print(x741)
  x743 = x738 == 25;
  x744 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x743), "%s" % x744
  x745 = accel.X447_arg.get()
  time.sleep(0.001)
  x746 = str(x745)
  x747 = (str("got ") + (x746 + (str(", wanted ") + (str("26") + str("")))));
  x748 = (x747 + str("\n"));
  print(x748)
  x750 = x745 == 26;
  x751 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x750), "%s" % x751
  x752 = accel.X448_arg.get()
  time.sleep(0.001)
  x753 = str(x752)
  x754 = (str("got ") + (x753 + (str(", wanted ") + (str("27") + str("")))));
  x755 = (x754 + str("\n"));
  print(x755)
  x757 = x752 == 27;
  x758 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x757), "%s" % x758
  x759 = accel.X449_arg.get()
  time.sleep(0.001)
  x760 = str(x759)
  x761 = (str("got ") + (x760 + (str(", wanted ") + (str("28") + str("")))));
  x762 = (x761 + str("\n"));
  print(x762)
  x764 = x759 == 28;
  x765 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x764), "%s" % x765
  x766 = accel.X450_arg.get()
  time.sleep(0.001)
  x767 = str(x766)
  x768 = (str("got ") + (x767 + (str(", wanted ") + (str("29") + str("")))));
  x769 = (x768 + str("\n"));
  print(x769)
  x771 = x766 == 29;
  x772 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x771), "%s" % x772
  x773 = accel.X451_arg.get()
  time.sleep(0.001)
  x774 = str(x773)
  x775 = (str("got ") + (x774 + (str(", wanted ") + (str("30") + str("")))));
  x776 = (x775 + str("\n"));
  print(x776)
  x778 = x773 == 30;
  x779 = ("\n=================\n" + (str("LoadStoreUnitTests.scala:25:13: Assertion failure") + "\n=================\n"));
  if (true): assert(x778), "%s" % x779

