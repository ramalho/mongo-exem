#!/usr/bin/env python

'''
Open Library dumps: tab separated files with the following columns:

type - type of record (/type/edition, /type/work etc.)
key - unique key of the record. (/books/OL1M etc.)
revision - revision number of the record
last_modified - last modified timestamp
JSON - the complete record in JSON format
'''

import sys
import json

LIN_PER_FILE = 100000

def writer(file_name_pattern, file_number):
    with open(file_name_pattern % file_number, 'wt') as outfile:
        while True:
            lin = yield
            outfile.write()
        

if len(sys.argv) != 2:
    print 'usage: %s <ol_dump_file>' % sys.argv[0]
infile_name = sys.argv[1]
outfile_name = infile_name.replace('.txt', '_%03d.mongoimport')
outfile_name = outfile_name.replace('_dump', '')
outfile_number = 1
with open(infile_name) as infile:
    for count, lin in enumerate(infile, 1):
        if count % LIN_PER_FILE == 1:
            
