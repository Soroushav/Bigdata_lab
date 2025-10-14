#!/usr/bin/env python3
from operator import itemgetter
import sys 

current_word = None
current_word_docs = ""

for line in sys.stdin:
    line = line.strip()
    word, doc = line.split("\t")
    if word != current_word:
        if current_word:
            print('{} {}'.format(current_word, current_word_docs))
        current_word_docs = ""
        current_word = word
    if current_word_docs == "":
        current_word_docs += doc
    else:
        current_word_docs += "," + doc
if current_word == word:
    print('{} {}'.format(current_word, current_word_docs))