#! /usr/bin/env python
import re
import sys

def decimalat(DegreeString):
	#Converts a string for latitude or longitude into a float
	SearchString = '(\d+) ([\d\.]+) (\w)'
	Result = re.search( SearchString, DegreeString )
		
	Degree = float( Result.group( 1 ))
	Minute = float( Result.group( 2 ))
	Compass = Result.group( 3 )
	DecimalDegree = Degree + Minute /60
		
	if Compass in 'SW':
		DecimalDegree = - DecimalDegree

	return DecimalDegree

assert( decimalat ('24 14.04 N') == 24.234)
assert( decimalat ('24 14.04 S') == -24.234)
assert( decimalat ('24 14.04 W') == -24.234)

arguments = sys.argv
print (arguments)

InFileName = sys.argv [1]

InFile = open ( InFileName, 'r' )

LineNumbre = 0

for Line in InFile:
	Line = Line.strip()

	if LineNumbre > 0:
		ElementList = Line.split( '\t' )
		print('Depth: {} Lat: {} Lon {}'.format (ElementList [4], ElementList [2], ElementList [3]))
		
		latitude = decimalat (ElementList[2])
		print ( latitude )

		longitude = decimalat (ElementList[3])
		print (longitude)

	LineNumbre = LineNumbre + 1

InFile.close()