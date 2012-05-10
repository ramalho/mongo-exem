
# Return at most 10 users sorted by score in descending order
# This may be used as a "top 10 users highscore table"
users = dbh.users.find().sort(("score", pymongo.DESCENDING)).limit(10)
for user in users:
    print user.get("username"), user.get("score", 0)
