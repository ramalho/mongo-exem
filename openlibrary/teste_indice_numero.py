#!/coding: utf-8

'''
Este exemplo deveria ser feito via agregação; da forma como está, serve 
para ilustrar o efeito de indexar.
'''

from mongo_util import conectar
from pprint import pprint
db = conectar('openlibrary')

def contar_revisoes():
    rev = 1
    while True:
        r = db.editions.find({'revision': rev})
        qt = r.count()
        if qt == 0:
            break
        #print rev, qt
        rev += 1


import time

pprint(db.editions.index_information())

NOME_INDICE = u'revision'

if NOME_INDICE in db.editions.index_information():
    db.editions.drop_index(NOME_INDICE)
t0 = time.time()
contar_revisoes()
print time.time() - t0, 'transcorrido'
print 'indexando...'
print db.editions.ensure_index('revision', name=NOME_INDICE)
print 'indexou.'
t0 = time.time()
contar_revisoes()
print time.time() - t0, 'transcorrido'



