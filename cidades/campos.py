#!/coding: utf-8

from bson.code import Code

from pymongo import Connection

HOST = 'localhost'
PORT = 27017

db = Connection(HOST, PORT).ibge

MAP = Code('''function () {
    for (field_name in this) emit(field_name, 1);
}''')

REDUCE = Code('''function (key, values) { 
    var total = 0;
    values.forEach(function(n) { total += n; });
    return total;
}''')

def report(results):
    docs = [(int(d['value']), d['_id']) for d in results]
    for line in sorted(docs, key=lambda i: (-i[0], i[1])):
        print '{0:6} {1}'.format(*line)

res = db.localidades.map_reduce(MAP, REDUCE, "field_occur").find()
    
report(res)
