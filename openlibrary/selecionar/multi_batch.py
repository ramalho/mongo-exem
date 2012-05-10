
SIZE = 3

outfile_number = 1
with open('multi_batch.py') as infile:
    while True:
        outfile_name = '%03d.dat' % outfile_number
        with open(outfile_name, 'wt') as outfile:
            count = 0
            for count, lin in enumerate(infile, 1):
                outfile.write(lin)
                if count == SIZE:
                    break
        if count == 0:
            break
        outfile_number += 1
        
        
