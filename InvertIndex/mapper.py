#!/usr/bin/env python3
import sys 

for line in sys.stdin:
    line = line.strip()
    doc, content = line.split('->', 1)
    doc = doc.strip().lower()
    content = content.strip().lower()

    for word in content.split():
        print('{}\t{}'.format(word, doc))