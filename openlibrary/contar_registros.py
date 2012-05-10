#!/usr/bin/env python
# coding: utf-8

from mongo_util import conectar

def contar_registros():
    db = conectar('openlibrary')
    for nome in db.collection_names():
        if nome.startswith('system.'):
            continue
        colecao = getattr(db, nome)
        print '{1:10,} {0}'.format(nome, colecao.count())

if __name__=='__main__':
    contar_registros()
