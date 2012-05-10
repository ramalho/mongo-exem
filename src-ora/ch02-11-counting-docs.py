
# Find out how many documents are in users collection, efficiently
userscount = dbh.users.find().count()
print "There are %d documents in users collection" % userscount
