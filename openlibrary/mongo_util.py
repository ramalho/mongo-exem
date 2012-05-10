# coding: utf-8

import sys

from pymongo import Connection
from pymongo.errors import ConnectionFailure

def conectar(database, host="localhost", port=27017):
    try:
        cnx = Connection(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Erro ao conectar com MongoDB: %s" % e)
        sys.exit(1)
    # obter referencia ao database solicitado
    db_handle = cnx[database]

    # note que o objeto database tem uma referencia à conexão de sua origem
    assert db_handle.connection == cnx
    return db_handle
