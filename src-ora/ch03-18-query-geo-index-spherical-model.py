
# Find the 10 users nearest to the point 40, 40 with max distance 5 degrees
# Uses the spherical model provided by MongoDB 1.8.x and up

earth_radius_km = 6371.0
max_distance_km = 5.0
max_distance_radians = max_distance_km / earth_radius_km
nearest_users = dbh.users.find(
    {"user_location":
        {"$nearSphere" : [40, 40],
         "$maxDistance":max_distance_radians}}).limit(10)
# Print the users
for user in nearest_users:
    # assume user_location property is array x,y
    print "User %s is at location %s,%s" %(user["username"], user["user_location"][0],
        user["user_location"[1])
