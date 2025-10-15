#!/usr/bin/env python3
import sys

current_user = None

for line in sys.stdin:
    line = line.strip()
    values = line.split("\t")
    user = line.split("\t")[0]
    if user == current_user:
        continue
    current_user = user
    if len(values) != 1:
        income = line.split("\t")[1]
        print("{}\t{}".format(user, income))