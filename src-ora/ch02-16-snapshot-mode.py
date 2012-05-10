
# Traverse the entire users collection, employing Snapshot Mode
# to eliminate potential duplicate results.
for user in dbh.users.find(snapshot=True):
    print user.get("username"), user.get("score", 0)
