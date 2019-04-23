#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    #or word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
     #   print '%s\t%s' % (word, 1)
     #top ten words array for cooccurence
    top_ten_words =["new","us","e","la","home","a","one","et","news","pm"]
    for i in xrange(len(words)-1):
	if words[i] in top_ten_words:
				print "%s|%s \t %s" %(words[i],words[i+1],1)
				print "%s|%s \t %s" %(words[i],words[i-1],1)
