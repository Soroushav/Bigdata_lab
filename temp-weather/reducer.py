#!/usr/bin/env python3
import sys

current_year = None
current_year_acc = 0
current_year_records = 0

for line in sys.stdin:
    line.strip()
    year, temp = line.split("\t", 1)
    if current_year != year:
        if current_year:
            print("{}\t{}".format(current_year, round(float(current_year_acc/current_year_records), 2)))
        current_year = year
        current_year_acc = 0
        current_year_records = 0
    current_year_acc += float(temp)
    current_year_records += 1
