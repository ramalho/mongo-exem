import sys
import json

OL_WORKS = 'ol_dump_works_20120404.txt'

works_set = set()

with open(sys.argv[1]) as entrada:
    for num_reg, lin in enumerate(entrada, 1):
        lin = lin.strip()
        if lin:
            works_set.add(lin)

with open(OL_WORKS) as entrada:
    for num_reg, lin in enumerate(entrada, 1):
        tipo, id_ol, versao, data, reg = lin.split('\t')
        if id_ol in works_set:
            print lin.rstrip()
            works_set.remove(id_ol)
        if not works_set:
            break
