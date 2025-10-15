#!/usr/bin/venv python3
import sys, math

local_min = math.inf
local_max = -math.inf

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    values = line.split("\t") 
    user = values[0]
    income = values[1]
    try:
        val = float(income)
    except:
        continue

    if val < local_min: local_min = val
    if val > local_max: local_max = val
    print("{}\t{}".format(user, income))

if local_min < math.inf:
    print(f"0000_min\t{local_min}")
if local_max > -math.inf:
    print(f"0000_max\t{local_max}")
