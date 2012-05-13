#!/coding: utf-8

from mongo_util import conectar
from bson.code import Code

db = conectar('openlibrary')

MAP = Code('''function () {
    for (field_name in this) emit(field_name, 1)
}''')

REDUCE = Code('''function (key, values) { 
    var total = 0;
    values.forEach(function(n) { total += n; });
    return total;
}''')

def count_fields(collection):
    return db[collection].map_reduce(MAP, REDUCE, "field_occur").find()
    
def report(results):
    docs = [(int(d['value']), d['_id']) for d in results]
    for line in sorted(docs, key=lambda i: (-i[0], i[1])):
        print '{0:6} {1}'.format(*line)

for col in 'authors works editions'.split():
    print '-' * 40, col
    report(count_fields(col))
