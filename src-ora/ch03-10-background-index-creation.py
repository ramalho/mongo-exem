
# Create index in the background
# Database remains usable
dbh.users.create_index("username", background=True)
