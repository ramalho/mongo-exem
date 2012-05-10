
# Assuming we already have a database handle in scope named dbh
# find a single document with the username "janedoe".
user_doc = dbh.users.find_one({"username" : "janedoe"})
if not user_doc:
    print "no document found for username janedoe"
