import cowsay
import sys

if len(sys.argv) == 2:
  cowsay.cat("Hi "+ sys.argv[1])
