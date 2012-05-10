
# Update the score for the current week
import datetime
username = "foouser"
now = datetime.datetime.utcnow()
current_year = now.year
current_month = new.month
current_week = now.isocalendar()[1]
current_day = now.timetuple().tm_yday
# Use atomic update modifier to increment by 24
dbh.users.update({"username":username},
    {"$inc":{
        "scores_weekly.%s-%s" %(current_year, current_week):24,
        "scores_daily.%s-%s" %(current_year, current_day):24,
        "scores_monthly.%s-%s" %(current_year, current_month):24,
        "score_total":24,
        }
    },
    safe=True)
