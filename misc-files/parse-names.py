#-*- coding: utf-8 -*-


import csv
import sys

f = open(sys.argv[1], 'rt')


for line in f:
    if 'boy' in line:
        print line.split(',')[1].replace("'",'').strip()
#try:
#    reader = csv.reader(f)
#    for row in reader:
#        print row
#finally:
#    f.close()
