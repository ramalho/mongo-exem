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
        emit(field_name, type_codes[type])
    }
}''' % TYPE_CODES)

REDUCE = Code('''function (key, values) { 
    var types = 0;
    values.forEach(function(type_code) { types |= type_code; });
    return types;
}''')

def count_fields(collection):
    return db[collection].map_reduce(MAP, REDUCE, "field_types").find()
    
def report(results):
    code_types = sorted( ((v, k) for k, v in TYPE_CODES.items() ))
    docs = [(int(d['value']), d['_id']) for d in results]
    for type_code, field_name in docs:
        types = [type_name for code, type_name in code_types if code & type_code]
        print '{0:20} {1} {2}'.format(field_name, type_code, ', '.join(types))

for col in 'authors works editions'.split():
    print '-' * 40, col
    report(count_fields(col))
