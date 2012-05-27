#!/coding: utf-8

from pprint import pprint
import json

from pymongo import Connection
from bson.code import Code

HOST = 'localhost'
PORT = 27017

UFS = {
    'Acre': 'AC',   
    'Alagoas': 'AL',
    'Amapá': 'AP',
    'Amazonas': 'AM',
    'Bahia': 'BA',
    'Ceará': 'CE',
    'Distrito Federal': 'DF',
    'Espírito Santo': 'ES',
    'Goiás': 'GO',
    'Maranhão': 'MA',
    'Mato Grosso': 'MT',
    'Mato Grosso do Sul': 'MS',
    'Minas Gerais': 'MG',
    'Paraná': 'PR',
    'Paraíba': 'PB',
    'Pará': 'PA',
    'Pernambuco': 'PE',
    'Piauí': 'PI',
    'Rio de Janeiro': 'RJ',
    'Rio Grande do Norte': 'RN',
    'Rio Grande do Sul': 'RS',
    'Rondônia': 'RO',
    'Roraima': 'RR',
    'Santa Catarina': 'SC',
    'Sergipe': 'SE',
    'São Paulo': 'SP',
    'Tocantins': 'TO'
}

UFS_UPPER = dict([(k.upper(), v) for k, v in UFS.items()])

db = Connection(HOST, PORT).ibge

print 'MongoDB', db.connection.server_info()['version']

MAP = '''function () {
    var ufs = %s;
    emit(this.cd_geocodm.slice(0,2)+"-"+(ufs[this.nm_uf]||this.nm_uf), 1);
}''' % json.dumps(UFS_UPPER)

REDUCE = Code('''function (key, values) { 
    var total = 0;
    values.forEach(function(n) { total += n; });
    return total;
}''')

res = db.localidades.map_reduce(MAP, REDUCE, 'uf_muni_count').find()
    
def report(results):
    docs = [(int(d['value']), d['_id']) for d in results]
    for line in sorted(docs, key=lambda i: (-i[0], i[1])):
        print u'{0:6} {1}'.format(*line)

report(res)
