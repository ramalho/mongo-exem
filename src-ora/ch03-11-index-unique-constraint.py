
# Create index with unique constraint on username property
dbh.users.create_index("username", unique=True)
