
# Atomically remove an email address from a user document race-free using the
# $pull update modifier
user_doc = {
    "username":"foouser",
    "emails":[
        {
         "email":"foouser1@example.com",
         "primary":True
        },
        {
         "email":"foouser2@example2.com",
         "primary":False
        },
        {
         "email":"foouser3@example3.com",
         "primary":False
        }
    ]
}
# Insert the user document
dbh.users.insert(user_doc, safe=True)
# Use $pull to atomically remove the "foouser2@example2.com" email sub-document
dbh.users.update({"username":"foouser"},
    {"$pull":{"emails":{"email":"foouser2@example2.com"}}}, safe=True)
