
# Return all user with firstname "jane" sorted
# in descending order by birthdate (ie youngest first)
users = dbh.users.find({"firstname":"jane"},
    sort=[("dateofbirth", pymongo.DESCENDING)])
for user in users:
    print user.get("email")
