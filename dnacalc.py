#! /usr/bin/env python

# comments

# DNASeq = raw_input ("Enter a DNA sequence: ")

DNASeq = 'AATCGCGATTATCGCATCGATCG'
DNASeq = DNASeq.upper()

print( 'Sequence ' + DNASeq )

SeqLength = float( len( DNASeq ))
print ( 'Length is ' + str( SeqLength ) )

NumberA = DNASeq.count('A')
NumberT = DNASeq.count('T')
NumberC = DNASeq.count('C')
NumberG = DNASeq.count('G')

print 'A: {:.2f}'.format (NumberA / SeqLength)
print 'T: {:.2f}'.format (NumberT / SeqLength)
print 'C: {:.2f}'.format (NumberC / SeqLength)
print 'G: {:.2f}'.format (NumberG / SeqLength)

TotalStrong = NumberG + NumberC
TotalWeak = NumberA + NumberT

if SeqLength <= 14:
	MeltTemp = (4 * TotalStrong) + (2 * TotalWeak)
	print("Using short formula.")
else: 
	MeltTemp = 64.9 + 41 * (TotalStrong - 16.4) / SeqLength
	print("Using long formula.")
	
print ( 'Melting temperature: {}'.format(MeltTemp))

print ('Done')
