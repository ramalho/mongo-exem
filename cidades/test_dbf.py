from dbf_rw import dbfreader
from pprint import pprint
from bz2 import BZ2File

arq_dbf = BZ2File('BR_Localidades_2010_v1.dbf.bz2')
localidades = dbfreader(arq_dbf)

nomes = []
tipos = []

localidades = list(localidades)

print 'Primeira localidade:'

for i, loc in enumerate(localidades):
    if i == 0:
        nomes = loc
    elif i == 1:
        tipos = loc
    else:
        pprint(zip(nomes, loc))
        break

print
print 'Total:', len(localidades)-2, 'localidades'
print 'Tipos dos campos:', [t[0] for t in tipos]
