
# Create a compound index called "name_idx" on first_name and last_name properties
# with ascending index direction
dbh.users.create_index([
    ("first_name", pymongo.ASCENDING),
    ("last_name", pymongo.ASCENDING)
    ],
    name="name_idx")
