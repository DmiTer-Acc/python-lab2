def validation_by_manager(func, user_id, data, criteria):
  for user in func(data, criteria):
    if user == user_id:
      print("skip the user")else:
      print("valdate teh user")validation_by_manager(flag_the_user, "U1", txns, 500)

def flag_the_user(txn_data: list[dict], criteria: int) -> list[str]:
  flagged_users = []for txn in txn_data: # hardcocodedamount = txn["amount"] # readuser_id = txn["user_id"]if amount > criteria:
      txn["flag"] = "flagged" # write insert into tableflagged_users.append(user_id)# print("you are being flagged")# print(txn)return flagged_usersprint(flag_the_user(txns, 500))print(flag_the_user(txns, 10000))
# 1. algorithm,2. write the business logic3. check if this is a fucntional candidate. If yes, define a function just above the logic.4. Make the logic part of the fucniton.4. Check if there is any external factors in the code.5. If yes, replace it with a variable.6. Now pass it as a functional parameter7. Return if there is any. Else write None explicitly8. An# notate the function.9. Run the function.

txns = [{"txn_id": "T101", "user_id": "U1", "amount": 600, "location": "NY", "history": ["NY", "NY"]},{"txn_id": "T102", "user_id": "U2", "amount": 12000, "location": "NY", "history": ["NY"]},{"txn_id": "T103", "user_id": "U1", "amount": 100, "location": "London", "history": ["NY", "NY"]},]

# """Rule 1: If the amount is greater than 10,000, flag it as FLAGGEDRule 2: If the current location is NOT in the user's history list, flag it as REVIEW_REQUIREDRule 3: If both Rule A and Rule B are met, set the status to BLOCKEDAdd a new key fraud_metrics to each dictionary containing the results of these checks.
