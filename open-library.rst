==============================================
Operações básicas com os dados da Open Library
==============================================

-------------------------------
Iniciando e testando o MongoDB
-------------------------------

Se o MongoDB não está rodando como um serviço, execute em um shell::

  $ mongod

Para usar o console do MongoDB::

  $ mongo

Uma vez no console, exercitamos algumas operações básicas.

Criar um database ``contatos``::

  > use contatos
  switched to db contatos

Criar e salvar um registro::

  > m = {nome:'Maria', fone:'4321-1234'}
  { "nome" : "Maria", "fone" : "4321-1234" }
  > db.pessoas.save(m)

Contar e recuperar todos os registros::

  > db.pessoas.count()
  1
  > db.pessoas.find()
  { "_id" : ObjectId("4fab96419e937836fb32ddbb"), "nome" : "Maria", "fone" : "4321-1234" }

Criar outro registro::

  > a = {nome:'Ana', fone:'8765-5678'}
  { "nome" : "Ana", "fone" : "8765-5678" }
  > db.pessoas.save(a)
  > db.pessoas.count()
  2
  > db.pessoas.find()
  { "_id" : ObjectId("4fab96419e937836fb32ddbb"), "nome" : "Maria", "fone" : "4321-1234" }
  { "_id" : ObjectId("4fab96bf9e937836fb32ddbc"), "nome" : "Ana", "fone" : "8765-5678" }

Para recuperar uma pessoa pelo nome::

  > db.pessoas.find({nome:'Maria'})
  { "_id" : ObjectId("4fab96419e937836fb32ddbb"), "nome" : "Maria", "fone" : "4321-1234" }
 
----------------
Carga dos dados
----------------

Executar script ``make_import.py`` para gerar arquivos de importação para o MongoDB::

  $ ./make_import.py data/ol_dump_authors_20120404_BR.txt.gz
  $ ./make_import.py data/ol_dump_works_20120404_BR.txt.gz
  $ ./make_import.py data/ol_dump_editions_20120404_BR.txt.gz

Executar script ``import.sh``:

.. literalinclude:: openlibrary/import.sh
  
Entrar no console do MongoDB para verificar o que foi feito::

  $ mongo
  MongoDB shell version: 2.0.4
  connecting to: test
  > use openlibrary
  switched to db openlibrary
  > db.authors.count()
  25758
  > db.works.count()
  36043
  > db.editions.count()
  97298
  > 

--------------------------------------------
Verificar contagem de registros via Python
--------------------------------------------

Primeiro, um exemplo de como se conectar a um database específico ``mongo_util.py``:

.. literalinclude:: openlibrary/mongo_util.py


Agora, a contagem ``contar_registros.py``:

.. literalinclude:: openlibrary/contar_registros.py

----------------------
Exemplo com MapReduce
----------------------

Operações de agregação mais complexas são feitas definindo pares de funções *map* e *reduce*, em JavaScript, para execução no MongoDB.

Para fazer uma contagem dos campos que ocorrem no primeiro nível dos documentos de uma coleção, usamos a seguinte função *map*:

.. code-block:: javascript

    function () { 
        for (field_name in this) 
            emit(field_name, 1);
    }

E a seguinte função *reduce*:

.. code-block:: javascript

    function (key, values) { 
        var total = 0;
        values.forEach(function(n) { total += n; });
        return total;
    }

Eis o código Python que usa dessas funções para gerar um relatório com a contagem de campos:

.. literalinclude:: openlibrary/fields_mapreduce.py

