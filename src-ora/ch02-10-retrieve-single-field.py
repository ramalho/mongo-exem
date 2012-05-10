
# Only retrieve the "email" field from each matching document.
users = dbh.users.find({"firstname":"jane"}, {"email":1})
for user in users:
    print user.get("email")
