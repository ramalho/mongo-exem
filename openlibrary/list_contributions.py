#!/coding: utf-8

from mongo_util import conectar
from bson.code import Code
from pprint import pprint

db = conectar('openlibrary')

for res in db.editions.find({'contributions':{'$exists':1}}, {'contributions':1}):
    pprint(res)
    


    
    
    
