
# Demonstrate usage of the positional operator ($) to modify
# matched sub-documents in-place.
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
# Now make the "foouser2@example2.com" email address primrary
dbh.users.update({"emails.email":"foouser2@example2.com"},
    {"$set":{"emails.$.primary":True}}, safe=True)
# Now make the "foouser1@example.com" email address not primary
dbh.users.update({"emails.email":"foouser1@example.com"},
    {"$set":{"emails.$.primary":False}}, safe=True)
