#! /usr/bin/env python

# comments

DNASeq = 'ATGAAC'
print( 'Sequence ' + DNASeq )

SeqLength = float( len( DNASeq ))
print ( 'Length is ' + str( SeqLength ) )

NumberA = DNASeq.count('A')
NumberT = DNASeq.count('T')
NumberC = DNASeq.count('C')
NumberG = DNASeq.count('G')
print ( 'A: ' + str( NumberA / SeqLength))
