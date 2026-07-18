accounts = {}
while True:
  print("\n----- ATM Simulator -----")
  print("1. Create Account")
  print("2. Check Balance")
  print("3. Deposit Money")
  print("4. Withdraw Money")
  print("5. Change Pin")
  print("6. Delete Account")
  print("7. Exit")
  choice = input("Enter your Choice: ")
  if choice == "1" :
    name = input("Enter the name of account holder: ")
    if name in accounts:
      print("Account already exists")
    else:
      pin = int(input("Enter pin: "))
      balance = int(input("Enter opening balance: "))
      accounts[name] = {
                      "pin": pin,
                      "balance": balance
                      }
      print("Account created successfully!")
  
  elif choice == "2":
    name = input("Enter Account holder's name: ")
    if name in accounts:
      pin = int(input("Enter PIN:"))
      if pin == accounts[name]["pin"]:
        print("Balance:",accounts[name]["balance"])
      else:
        print("Invalide PIN")
    else:
      print("Account not found")                         

  elif choice == "3":
    name = input("Enter Account holder's name:")
    if name in accounts:
      pin = int(input("Enter the PIN:"))
      if pin == accounts[name]["pin"]:
        deposit = int(input("Enter the amount to deposit:"))
        if deposit <= 0:
          print("Invalid amount")
        else:
          accounts[name]["balance"] += deposit
          print("Money deposited successfully!")
      else:
        print("invalid PIN")
    else:
      print("Account not found!")                                    

  elif choice == "4":
    name = input("Enter account holder's name:")
    if name in accounts:
      pin = int(input("Enter PIN:"))
      if pin == accounts[name]["pin"]:
        withdraw = int(input("Enter the Withdrawl amount:"))
        if withdraw <= 0:
          print("Invalid amount ")
        elif accounts[name]["balance"] >= withdraw:
          accounts[name]["balance"]-=withdraw
          print("Money Withdrawn successfully! ")
        else:
          print("Insufficient Balance")
      else:
        print("incorrect PIN!")
    else:
      print("Account not found!")          

  elif choice == "5":
    name = input("Enter card holder's name:")
    if name in accounts:
      pin = int(input("Enter old PIN:"))
      if pin == accounts[name]["pin"]:
        new_pin = int(input("Enter new pin:"))
        accounts[name]["pin"] = new_pin
        print("PIN changed successfully")
      else:
        print("PIN invalide")
    else:
      print("Account not found!")

  elif choice == "6":
    name = input("Enter account holder's name:")
    if name in accounts:
      pin = int(input("Enter PIN:"))
      if pin == accounts[name]["pin"]:
        del accounts[name]
        print("Account deleted successfully!")
      else:
        print("Invalid PIN")
    else:
      print("Account not found")

  elif choice == "7":
    print("Thankyou for choosing our bank!")
    break
