
# update modifiers such as $set also support the dot notation
dbh.users.update({"facebook.username":"foofacebook"},
    {"$set":{"facebook.username":"bar"}}, safe=True)
