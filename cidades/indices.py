#!/coding: utf-8

from pprint import pprint

from pymongo import Connection
from bson.code import Code

HOST = 'localhost'
PORT = 27017

db = Connection(HOST, PORT).ibge

print 'MongoDB', db.connection.server_info()['version']

reg = db.localidades.find_one()

for campo_cod in (k for k in reg.keys() if k.startswith('cd_')):
    db.localidades.ensure_index(campo_cod)

db.localidades.ensure_index('nm_uf')

munis = db.localidades.distinct('cd_geocodm')
print len(munis), 'códigos de município'

niveis = db.localidades.distinct('cd_nivel')
print ', '.join(niveis)

ufs = db.localidades.distinct('nm_uf')
for uf in ufs:
    print uf
