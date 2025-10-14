#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    year, temp = line.split("\t", 1)

    print("{}\t{}".format(year, temp))
