'''
Gerar tabela ReStructuredText a partir do CSV
'''

import csv


leitor = csv.reader(open('descritivo_campos_localidades_2010.csv'))
largs = {}
lido = list(leitor)

for i, lin in enumerate(lido):
    if i == 0:
        continue
    for c, campo in enumerate(lin):
        largs[c] = max(largs.get(c,0), len(campo.strip()))

for i in sorted(largs):
    print '='*largs[i],
print

for i, lin in enumerate(lido):
    for c, campo in enumerate(lin):
        print campo.ljust(largs[c]),
    print

for i in sorted(largs):
    print '='*largs[i],
print
