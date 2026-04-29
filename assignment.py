# Banking Transaction System Assignment


#code explanation

"""
This program is a simple banking system that runs in terminal.
it starts from main.py where user can login, create account or delete account.

after login, user goes to ATM menu where they can deposit, withdraw,
transfer money, check balance and see mini statement and this program runs in a loop until user exits.
"""


"""
how transactions work:
transactions are handled in atm_menu().
first data is loaded from JSON file.
then based on user input:
-balance is updated
-transaction is added
-data is saved again
-json is updated.
"""


"""
how data is stored:
data is stored in accounts.json file.
each account has:
name, pin, balance and transactions list.
json.load() is used to read data
json.dump() is used to save data
"""


"""
deposit, withdraw, transfer:
deposit:
ammount is added to balance and transaction is stored.
withdraw:
checks if balance is enough, then subtracts amount.
transfer:
checks receiver exists and balance is enough,
then transfers money and updates both accounts.
"""


#flaws

"""
1 user can transfer money to same account
2 amount validation is weak
3 pin is stored in plain text
4 no handling if Json file breaks
5 login system is basic
"""


#fix

"""
fixing self transfer
earlier user could transfer money to their own account
now I added a check for that.
"""


def transfer_fixed(data, acc, to, amt):
    if to == acc:
        return "cannot transfer to same account as receiver is same as sender"

    if to in data and amt and amt <= data[acc]["balance"]: #if receiver exists, amount is valid, and balance is enough
        data[acc]["balance"] -= amt #money goes from sender
        data[to]["balance"] += amt #money goes to receiver
        data[acc]["transactions"].append(f"Sent {amt} to {to}") #save history of transation
        data[to]["transactions"].append(f"Received {amt} from {acc}")

        return "Transfer successful"

    return "Transfer failed"


# 4. Tests

def test_deposit():
    data = {"1111": {"balance": 1000, "transactions": []}} #fake data
    acc = "1111"
    amt = 500
    old_balance = data[acc]["balance"] #trying fake datafor transaction
    data[acc]["balance"] += amt
    assert data[acc]["balance"] == old_balance + amt #check if balance is updated correctly
def test_withdraw_fail():
    data = {"1111": {"balance": 1000, "transactions": []}}
    acc = "1111"
    amt = 5000
    if amt > data[acc]["balance"]:
        result = False
    else:
        result = True
    assert result == False



#improvements

"""
store PIN securely
improve transaction structure
reduce repeated code
add error handling
improve testing
"""



