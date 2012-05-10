
# Fetch the score for the current week
import datetime
now = datetime.datetime.utcnow()
current_year = now.year
current_week = now.isocalendar()[1]
# Default missing keys to a score of zero
user_doc["scores_weekly"].get("%d-%d" %(current_year, current_week), 0)
