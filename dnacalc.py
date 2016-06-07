#! /usr/bin/env python

# comments

# DNASeq = raw_input ("Enter a DNA sequence: ")

DNASeq = 'AATCGCGATTATCGCATCGATCG'
DNASeq = DNASeq.upper()

print( 'Sequence ' + DNASeq )

SeqLength = float( len( DNASeq ))
print ( 'Length is ' + str( SeqLength ) )

TotalWeak  = 0
TotalStrong = 0

Bases = "CGTA"
for Base in Bases:
	Count = DNASeq.count(Base)
	Frequency = DNASeq.count(Base) / SeqLength
	print ('{}: {}'.format(Base, Frequency))
	if Base in 'GC':
			TotalStrong = TotalStrong + Count
	elif Base in 'TA':
			TotalWeak = TotalWeak + Count

print (TotalWeak, TotalStrong)


#Counts = dict()
#for Base in Bases:
#	COunt = DNASeq.count(Base)
#	Counts[Base] = Count

#print (Counts)


#for Base in DNASeq: 
	

if SeqLength <= 14:
	MeltTemp = (4 * TotalStrong) + (2 * TotalWeak)
	print("Using short formula.")
else: 
	MeltTemp = 64.9 + 41 * (TotalStrong - 16.4) / SeqLength
	print("Using long formula.")
	
print ( 'Melting temperature: {}'.format(MeltTemp))

print ('Done')

#NumberA = DNASeq.count('A')
#NumberT = DNASeq.count('T')
#NumberC = DNASeq.count('C')
#NumberG = DNASeq.count('G')

#print 'A: {:.2f}'.format (NumberA / SeqLength)
#print 'T: {:.2f}'.format (NumberT / SeqLength)
#print 'C: {:.2f}'.format (NumberC / SeqLength)
#print 'G: {:.2f}'.format (NumberG / SeqLength)


