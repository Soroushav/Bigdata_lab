#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    values = line.split("\t")
    user, income = values[1], values[3]
    print("{}\t{}".format(user, income))
    