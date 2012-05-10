
# safe=True ensures that your write
# will succeed or an exception will be thrown
dbh.users.insert(user_doc, safe=True)
