
# Assuming we already have a database handle in scope named dbh
# find all documents with the firstname "jane".
# Then iterate through them and print out the email address.
users = dbh.users.find({"firstname":"jane"})
for user in users:
    print user.get("email")
