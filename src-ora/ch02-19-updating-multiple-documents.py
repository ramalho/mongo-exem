
# once we supply the "multi=True" parameter, all matched documents
# will be updated
dbh.users.update({"score":0},{"$set":{"flagged":True}}, multi=True, safe=True)
