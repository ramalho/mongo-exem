
# Find the 10 users nearest to the point 40, 40 with max distance 5 degrees
nearest_users = dbh.users.find(
    {"user_location":
        {"$near" : [40, 40],
         "$maxDistance":5}}).limit(10)
# Print the users
for user in nearest_users:
    # assume user_location property is array x,y
    print "User %s is at location %s,%s" %(user["username"], user["user_location"][0],
        user["user_location"[1])
