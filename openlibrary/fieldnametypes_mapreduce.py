#!/coding: utf-8

from mongo_util import conectar
from bson.code import Code

db = conectar('openlibrary')

TYPE_CODES = {'object':1, 'array':2, 'string':4, 'number': 8}

MAP = Code('''function () {
    var type_codes = %r;
    var type = '';
    for (field_name in this) {
        type = typeof this[field_name];
        if (type === 'object') {
            type = this[field_name] instanceof Array ? 'array' : 'object';
        }
        emit(field_name+':'+type, 1)
    }
}''' % TYPE_CODES)

REDUCE = Code('''function (key, values) { 
    var total = 0;
    values.forEach(function(n) { total += n; });
    return total;
}''')

def count_fields(collection):
    return db[collection].map_reduce(MAP, REDUCE, "field_types").find()
    
def report(results):
    docs = [(d['_id'], int(d['value']), ) for d in results]
    prev_name = None
    for field_tag, count in sorted(docs):
        field_name, type = field_tag.split(':')
        if field_name == prev_name:
            field_name = '_'*len(prev_name)
        else:
            prev_name = field_name
        print '{0:6} {1} : {2}'.format(count, field_name, type)

for col in 'authors works editions'.split():
    print '-' * 40, col
    report(count_fields(col))
