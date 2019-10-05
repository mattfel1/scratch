import numpy as np
def execute():
   x38 = 0;
  //* x39 = new int32_t {0}; // Initialize cpp argout ???
  c1->setArg(X_arg, x41, false);
  x38 = x41;
  int64_t x58_tmp = c1->getArg(Y_arg, false);
  bool x58_sgned = true & ((x58_tmp & ((int64_t)1 << 31)) > 0); // Determine sign
  if (x58_sgned) x58_tmp = x58_tmp | ~(((int64_t)1 << 32)-1); // Sign-extend if necessary
   x58 = () x58_tmp / ((int64_t)1 << 0);
