from dbf_rw import dbfreader
from pprint import pprint
from bz2 import BZ2File

arq_dbf = BZ2File('BR_Localidades_2010_v1.dbf.bz2')
localidades = dbfreader(arq_dbf)

nomes = []
tipos = []
try:
    for i, loc in enumerate(localidades):
        if i == 0:
            nomes = loc
        elif i == 1:
            tipos = loc
        else:
            if any(campo is None for campo in loc):
                pprint(zip(nomes, loc))

except ValueError:
    print i
    raise
