#!/usr/bin/env python3

tempfile = 'avg_temp_temp.csv'
writefile = 'avg_temp.csv'

wfh = open(writefile, 'w')

for line in open(tempfile):
	flow, fhigh, city, clow, chigh = line.split('\t')
	writeline = ':'.join([city, flow, fhigh, clow, chigh])

	wfh.write(writeline)

wfh.close()
