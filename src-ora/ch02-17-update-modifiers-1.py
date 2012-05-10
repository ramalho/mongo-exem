
# run the update query, using the $set update modifier.
# we do not need to know the current contents of the document
# with this approach, and so avoid an initial query and
# potential race condition.
dbh.users.update({"username":"janedoe"},
    {"$set":{"email":"janedoe74@example2.com"}}, safe=True)
