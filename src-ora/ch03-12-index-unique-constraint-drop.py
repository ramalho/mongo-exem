
# Create index with unique constraint on username property
# instructing MongoDB to drop all duplicates after the first document it finds.
dbh.users.create_index("username", unique=True, drop_dups=True)
# Could equally be written:
# dbh.users.create_index("username", unique=True, dropDups=True)
