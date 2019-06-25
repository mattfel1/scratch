#include "structs.hpp"
#include <stdint.h>
#include <sys/time.h>
#include <iostream>
#include <fstream>
#include <string> 
#include <sstream> 
#include <stdarg.h>
#include <signal.h>
#include <sys/wait.h>
#include <pwd.h>
#include <map>
#include <math.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include "FringeContext.h"
#include "functions.hpp"
#include "ArgAPI.hpp"
#include "Fixed.hpp"
#include <vector>
using std::vector;

#ifndef ZYNQ
typedef __int128 int128_t;
#endif

void printHelp(); 

using namespace std;

void Application(int numThreads, vector<string> * args) {
  // Create an execution context.
  FringeContext *c1 = new FringeContext("./verilog/accel.bit.bin");
  c1->load();
  vector<string>* x31 = args;
  int32_t x32 = 0;
  //int32_t* x33 = new int32_t {0}; // Initialize cpp argout ???
  string x34;
  try {
    x34 = (*x31).at(0);
  }
  catch (std::out_of_range& e) {
    printHelp();
  }
  int32_t x35 = std::stol(x34);
  c1->setArg(X_arg, x35, false);
  x32 = x35;
  // Register ArgIns and ArgIOs in case some are unused
  c1->setNumArgIns(1 + 0 + 0);
  c1->setNumArgIOs(0);
  c1->setNumArgOuts(1);
  c1->setNumArgOutInstrs(2);
  c1->setNumEarlyExits(0);
  c1->flushCache(1024);
  time_t tstart = time(0);
  c1->run();
  time_t tend = time(0);
  double elapsed = difftime(tend, tstart);
  std::cout << "Kernel done, test run time = " << elapsed << " ms" << std::endl;
  c1->flushCache(1024);
  std::ofstream instrumentation ("./instrumentation.txt");
  // Need to instrument List((x9,1))
  std::cout << "ArgIns:" << x32 << ", ArgIOs:" <<  " "  << std::endl;
  if (instrumentation.is_open()) {
    instrumentation << "ArgIns:" << x32 << ", ArgIOs:" <<  " "  << std::endl;
  }
   // immediate parent hashmap now Map(1 -> x9), current node x9 is at depth 1
  long x9_cycles = c1->getArg(X9_cycles_arg, false);
  long x9_iters = c1->getArg(X9_iters_arg, false);
  long x9_iters_per_parent = x9_iters / std::max((long)1,x9_iters);
  long x9_avg = x9_cycles / std::max((long)1,x9_iters);
  std::cout << "  x9 - " << x9_avg << " (" << x9_cycles << " / " << x9_iters << ") ";
  std::cout << "[" << x9_iters_per_parent << " iters/parent execution]";
  if (instrumentation.is_open()) {
    instrumentation << "  x9 - " << x9_avg << " (" << x9_cycles << " / " << x9_iters << ") ";
    instrumentation << "[" << x9_iters_per_parent << " iters/parent execution]";
  }
  std::cout << std::endl;
  if (instrumentation.is_open()) {
    instrumentation << std::endl;
  }
  instrumentation.close();
  int64_t x40_tmp = c1->getArg(Y_arg, false);
  bool x40_sgned = true & ((x40_tmp & ((int64_t)1 << 31)) > 0); // Determine sign
  if (x40_sgned) x40_tmp = x40_tmp | ~(((int64_t)1 << 32)-1); // Sign-extend if necessary
  int32_t x40 = (int32_t) x40_tmp / ((int64_t)1 << 0);
  int32_t x41 = x35 + 4;
  string x42 = std::to_string(x41);
  string x43 = (string("expected: ") + x42);
  string x44 = (x43 + string("\n"));
  std::cout << x44;
  string x46 = std::to_string(x40);
  string x47 = (string("result: ") + x46);
  string x48 = (x47 + string("\n"));
  std::cout << x48;
  bool x50 = x41 == x40;
  string x51 = x50 ? string("true") : string("false");
  string x52 = (string("PASS: ") + x51);
  string x53 = (x52 + string(" (InOutArg)"));
  string x54 = (x53 + string("\n"));
  std::cout << x54;
  string x56 = ("\n=================\n" + (string("ArgInOut.scala:30:11: Assertion failure") + "\n=================\n"));
  if (true) { ASSERT(x50, x56.c_str()); }
  delete c1;
}

void printHelp() {
  fprintf(stderr, "Help for app: ArgInOut\n");
  fprintf(stderr, "  -- Args:    <0: N>\n");
  fprintf(stderr, "    -- Example: bash run.sh 7\n");
  exit(1);
}

int main(int argc, char *argv[]) {
  vector<string> *args = new vector<string>(argc-1);
  for (int i=1; i<argc; i++) {
    (*args)[i-1] = std::string(argv[i]);
    if (std::string(argv[i]) == "--help" | std::string(argv[i]) == "-h") {printHelp();}
  }
  int numThreads = 1;
  char *env_threads = getenv("DELITE_NUM_THREADS");
  if (env_threads != NULL) { numThreads = atoi(env_threads); } else {
    fprintf(stderr, "[WARNING]: DELITE_NUM_THREADS undefined, defaulting to 1\n");
  }
  fprintf(stderr, "Executing with %d thread(s)\n", numThreads);
  Application(numThreads, args);
  return 0;
}
