
# User X adds $20 to his/her account, so we atomically increment
# account_balance and return the resulting document
ret = dbh.users.find_and_modify({"username":username},
    {"$inc":{"account_balance":20}}, safe=True, new=True)
new_account_balance = ret["account_balance"]
