#!/coding: utf-8

from mongo_util import conectar
from bson.code import Code
from pprint import pprint

db = conectar('openlibrary')

for res in db.editions.find({'authors':{'$exists':1}}, {'authors':1}):
    for author_fkey in res[u'authors']:
        author = db.authors.find_one({'_id':author_fkey[u'key']}, {'name':1})
        if author is None:
            print author['name']
    


    
    
    
