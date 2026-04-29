from database import load_accounts,save_accounts
from utils import line,get_amount
from datetime import datetime

def atm_menu(acc):
    while True:
        data=load_accounts()
        line()
        print(f"welcome,{data[acc]['name']}")
        print("1 deposit")
        print("2 withdraw")
        print("3 transfer")
        print("4 balance")
        print("5 mini statement")
        print("6 logout")
        line()
        ch=input("choose option: ")
        if ch=="1":
            amt=get_amount()
            if amt:
                data[acc]["balance"]+=amt
                data[acc]["transactions"].append(f"{datetime.now()} +{amt}")
                save_accounts(data)
                print("deposit successful")
        elif ch=="2":
            amt=get_amount()
            if amt and amt<=data[acc]["balance"]:
                data[acc]["balance"]-=amt
                data[acc]["transactions"].append(f"{datetime.now()} -{amt}")
                save_accounts(data)
                print("withdrawal successful")
            else:
                print("insufficient balance")
        elif ch=="3":
            to=input("receiver account number: ")
            amt=get_amount()
            if to==acc:
                print("cannot transfer to same account")
            elif to not in data:
                print("receiver account not found")
            elif not amt:
                print("invalid amount")
            elif amt>data[acc]["balance"]:
                print("insufficient balance")
            else:
                data[acc]["balance"]-=amt
                data[to]["balance"]+=amt
                data[acc]["transactions"].append(f"{datetime.now()} sent {amt} to {to}")
                data[to]["transactions"].append(f"{datetime.now()} received {amt} from {acc}")
                save_accounts(data)
                print("transfer successful")
        elif ch=="4":
            print("current balance:",data[acc]["balance"])
        elif ch=="5":
            print("last transactions:")
            for t in data[acc]["transactions"][-5:]:
                print(t)
        elif ch=="6":
            break