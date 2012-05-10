.. Exemplos MongoDB documentation master file, created by
   sphinx-quickstart on Thu May 10 05:32:22 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

========================================================
Exemplos do livro MongoDB and Python, de Niall O'Higgins
========================================================

Capítulo 2: Lendo e escrevendo
==============================

2.1. Exemplo de documento
-------------------------

.. literalinclude:: src-ora/ch02-01-document-example.py
   :linenos:


2.2. Conexão com o MongoDB
--------------------------

.. literalinclude:: src-ora/ch02-02-connecting-to-mongodb.py
   :linenos:


2.3. Python handle to mongodb
-----------------------------

.. literalinclude:: src-ora/ch02-03-python-handle-to-mongodb.py
   :linenos:


2.4. Inserting a document
-------------------------

.. literalinclude:: src-ora/ch02-04-inserting-a-document.py
   :linenos:


2.5. Typo example
-----------------

.. literalinclude:: src-ora/ch02-05-typo-example.py
   :linenos:


2.6. Synchronous writes
-----------------------

.. literalinclude:: src-ora/ch02-06-synchronous-writes.py
   :linenos:


2.7. Guaranteeing writes to multiple nodes
------------------------------------------

.. literalinclude:: src-ora/ch02-07-guaranteeing-writes-to-multiple-nodes.py
   :linenos:


2.8. Find single doc
--------------------

.. literalinclude:: src-ora/ch02-08-find-single-doc.py
   :linenos:


2.9. Find multiple docs
-----------------------

.. literalinclude:: src-ora/ch02-09-find-multiple-docs.py
   :linenos:


2.10. Retrieve single field
---------------------------

.. literalinclude:: src-ora/ch02-10-retrieve-single-field.py
   :linenos:


2.11. Counting docs
-------------------

.. literalinclude:: src-ora/ch02-11-counting-docs.py
   :linenos:


2.12. Sorting docs
------------------

.. literalinclude:: src-ora/ch02-12-sorting-docs.py
   :linenos:


2.13. Sorting2
--------------

.. literalinclude:: src-ora/ch02-13-sorting2.py
   :linenos:


2.14. Limit docs
----------------

.. literalinclude:: src-ora/ch02-14-limit-docs.py
   :linenos:


2.15. Skip docs
---------------

.. literalinclude:: src-ora/ch02-15-skip-docs.py
   :linenos:


2.16. Snapshot mode
-------------------

.. literalinclude:: src-ora/ch02-16-snapshot-mode.py
   :linenos:


2.17. Update modifiers 1
------------------------

.. literalinclude:: src-ora/ch02-17-update-modifiers-1.py
   :linenos:


2.18. Update modifiers 2
------------------------

.. literalinclude:: src-ora/ch02-18-update-modifiers-2.py
   :linenos:


2.19. Updating multiple documents
---------------------------------

.. literalinclude:: src-ora/ch02-19-updating-multiple-documents.py
   :linenos:


2.20. Delete docs
-----------------

.. literalinclude:: src-ora/ch02-20-delete-docs.py
   :linenos:


2.21. Delete all docs
---------------------

.. literalinclude:: src-ora/ch02-21-delete-all-docs.py
   :linenos:


Capítulo 3: Padrões comuns
==========================

3.1. Subdocs 1
--------------

.. literalinclude:: src-ora/ch03-01-subdocs-1.py
   :linenos:


3.2. Subdocs 2
--------------

.. literalinclude:: src-ora/ch03-02-subdocs-2.py
   :linenos:


3.3. Atomic subdoc remove
-------------------------

.. literalinclude:: src-ora/ch03-03-atomic-subdoc-remove.py
   :linenos:


3.4. Atomic subdoc append
-------------------------

.. literalinclude:: src-ora/ch03-04-atomic-subdoc-append.py
   :linenos:


3.5. Atomic subdoc update
-------------------------

.. literalinclude:: src-ora/ch03-05-atomic-subdoc-update.py
   :linenos:


3.6. Btree index
----------------

.. literalinclude:: src-ora/ch03-06-btree-index.py
   :linenos:


3.7. Create btree index
-----------------------

.. literalinclude:: src-ora/ch03-07-create-btree-index.py
   :linenos:


3.8. Create compound btree index
--------------------------------

.. literalinclude:: src-ora/ch03-08-create-compound-btree-index.py
   :linenos:


3.9. Create compound btree index 2
----------------------------------

.. literalinclude:: src-ora/ch03-09-create-compound-btree-index-2.py
   :linenos:


3.10. Background index creation
-------------------------------

.. literalinclude:: src-ora/ch03-10-background-index-creation.py
   :linenos:


3.11. Index unique constraint
-----------------------------

.. literalinclude:: src-ora/ch03-11-index-unique-constraint.py
   :linenos:


3.12. Index unique constraint drop
----------------------------------

.. literalinclude:: src-ora/ch03-12-index-unique-constraint-drop.py
   :linenos:


3.13. Drop anonymous index
--------------------------

.. literalinclude:: src-ora/ch03-13-drop-anonymous-index.py
   :linenos:


3.13. Named index
-----------------

.. literalinclude:: src-ora/ch03-13-named-index.py
   :linenos:


3.14. Create geo index
----------------------

.. literalinclude:: src-ora/ch03-14-create-geo-index.py
   :linenos:


3.15. Query geo index point
---------------------------

.. literalinclude:: src-ora/ch03-15-query-geo-index-point.py
   :linenos:


3.16. Query geo index box
-------------------------

.. literalinclude:: src-ora/ch03-16-query-geo-index-box.py
   :linenos:


3.17. Query geo index circle
----------------------------

.. literalinclude:: src-ora/ch03-17-query-geo-index-circle.py
   :linenos:


3.18. Query geo index spherical model
-------------------------------------

.. literalinclude:: src-ora/ch03-18-query-geo-index-spherical-model.py
   :linenos:


3.19. Avoid keyerrors
---------------------

.. literalinclude:: src-ora/ch03-19-avoid-keyerrors.py
   :linenos:


3.20. Avoid keyerrors 2
-----------------------

.. literalinclude:: src-ora/ch03-20-avoid-keyerrors-2.py
   :linenos:


3.21. Using upsert
------------------

.. literalinclude:: src-ora/ch03-21-using-upsert.py
   :linenos:


3.22. Findandmodify
-------------------

.. literalinclude:: src-ora/ch03-22-findAndModify.py
   :linenos:


3.23. Fast accounting lookup
----------------------------

.. literalinclude:: src-ora/ch03-23-fast-accounting-lookup.py
   :linenos:


3.24. Fast accounting update
----------------------------

.. literalinclude:: src-ora/ch03-24-fast-accounting-update.py
   :linenos:


3.25. Fast accounting multiple time periods
-------------------------------------------

.. literalinclude:: src-ora/ch03-25-fast-accounting-multiple-time-periods.py
   :linenos:


Capítulo 4: Web frameworks
==========================

4.1. Pylons pymongo app globals
-------------------------------

.. literalinclude:: src-ora/ch04-1-pylons-pymongo-app-globals.py
   :linenos:


4.2. Pylons pymongo sample controller
-------------------------------------

.. literalinclude:: src-ora/ch04-2-pylons-pymongo-sample-controller.py
   :linenos:


4.3. Pyramid pymongo sample view callable
-----------------------------------------

.. literalinclude:: src-ora/ch04-3-pyramid-pymongo-sample-view-callable.py
   :linenos:


4.4. Django pymongo sample view
-------------------------------

.. literalinclude:: src-ora/ch04-4-django-pymongo-sample-view.py
   :linenos:
