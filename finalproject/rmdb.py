#! /usr/bin/env python

InFileName = 'seqid.fa'

InFile = open ( InFileName, 'r' )

LineNumbre = 0

lines_seen = set() # holds lines already seen
for line in InFile:
	LineNumbre = LineNumbre + 1
	if LineNumbre > 1:
		if line not in lines_seen: # not a duplicate
   			print(line)
   			lines_seen.add(line)

InFile.close()