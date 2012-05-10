
# Return at most 20 users sorted by name,
# skipping the first 20 results in the set
users = dbh.users.find().sort(
    ("surname", pymongo.ASCENDING)).limit(20).skip(20)
