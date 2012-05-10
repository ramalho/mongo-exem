
# Update the score for the current week
import datetime
username = "foouser"
now = datetime.datetime.utcnow()
current_year = now.year
current_week = now.isocalendar()[1]
# Use atomic update modifier to increment by 24
dbh.users.update({"username":username},
    {"$inc":{"scores_weekly.%s-%s" %(current_year, current_week):24}},
    safe=True)
