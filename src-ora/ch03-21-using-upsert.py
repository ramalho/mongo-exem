
# Using upsert=True
def edit_or_add_session(description, session_id):
    dbh.sessions.update({"session_id":session_id},
        {"$set":{"session_description":description}}, safe=True, upsert=True)
