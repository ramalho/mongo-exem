
# Create index on username property called "username_idx"
dbh.users.create_index("username", name="username_idx")
# Delete index called "username_idx"
dbh.users.drop_index("username_idx")
