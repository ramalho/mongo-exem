import sys
import json

OL_AUTHORS = 'ol_dump_authors_20120404.txt'

autores_set = set()

with open(sys.argv[1]) as entrada:
    for num_reg, lin in enumerate(entrada, 1):
        lin = lin.strip()
        if lin:
            autores_set.add(lin)

with open(OL_AUTHORS) as entrada:
    for num_reg, lin in enumerate(entrada, 1):
        tipo, id_ol, versao, data, reg = lin.split('\t')
        if id_ol in autores_set:
            print lin.rstrip()
            autores_set.remove(id_ol)
        if not autores_set:
            break
