
# Create geospatial index on "user_location" property.
dbh.users.create_index([("user_location", pymongo.GEO2D), ("username", pymongo.ASCENDING)])
