
# Create a compound index on first_name and last_name properties
# with ascending index direction
dbh.users.create_index([("first_name", pymongo.ASCENDING), ("last_name", pymongo.ASCENDING)])
# Delete this index
dbh.users.drop_index([("first_name", pymongo.ASCENDING), ("last_name", pymongo.ASCENDING)])
