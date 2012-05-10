
total_score = 0
for username in ("jill", "sam", "cathy"):
    user_doc = dbh.users.find_one({"username":username})
    total_score += user_doc.get("score", 0)
