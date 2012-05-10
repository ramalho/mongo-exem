#!/bin/bash
mongoimport -d openlibrary -c authors data/ol_authors_20120404_BR.mongoimport
mongoimport -d openlibrary -c works data/ol_works_20120404_BR.mongoimport
mongoimport -d openlibrary -c editions data/ol_editions_20120404_BR.mongoimport
