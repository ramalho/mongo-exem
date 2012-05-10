# w=2 means the write will not succeed until it has
# been written to at least 2 servers in a replica set.
dbh.users.insert(user_doc, w=2)
