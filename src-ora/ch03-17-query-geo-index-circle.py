
users_in_circle = dbh.users.find({"user_location":{"$within":{"$center":[40, 40, 5]}}}).limit(10)
