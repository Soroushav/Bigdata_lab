#!/user/bin/venv python3
import sys
global_min = None
global_max = None
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    if line.split("\t")[0].startswith('0000'):
        if line.split("\t")[0].split("_")[1] == "max":
            global_max = float(line.split("\t")[1])
        if line.split("\t")[0].split("_")[1] == "min":
            global_min = float(line.split("\t")[1])
    else:
        user, income = line.split("\t")
        normalized_income = (float(income) - global_min) / (global_max - global_min)
        print("{}\t{}".format(user, round(normalized_income, 2)))
     