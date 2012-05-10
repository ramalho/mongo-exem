
box = [[50.73083, -83.99756], [50.741404,  -83.988135]]
users_in_boundary = dbh.users.find({"user_location":{"$within": {"$box":box}}})
