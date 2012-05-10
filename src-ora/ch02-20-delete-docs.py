
# Delete all documents in user collection with score 1
dbh.users.remove({"score":1}, safe=True)
