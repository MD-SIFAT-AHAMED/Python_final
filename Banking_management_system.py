class Bank:
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.totalBalance=0
        self.totalLoan=0
        self.loanStatus=True
        self.accounts=[]

    def CreatAccount(self,name,email,address,account_type):
        account=Account(name,email,address,account_type)
        self.accounts.append(account)
        return account

    def DeleteAccount(self,accountNo):
        for account in self.accounts:
            if account.accountNo == accountNo:
                self.accounts.remove(account)
                del account
                return

    def ShowUsers(self):
        for account in self.accounts:
            print(f"Account NO: {account.accountNo} of {account.name}")

    def TotalBalance(self):
        print(f"Total Balance: {self.totalBalance}")
        
    def TotalLoan(self):
        print(f"Total Laon: {self.totalLoan}")

    def LoanStart(self):
        self.loanStatus=True

    def LoanStop(self):
        self.loanStatus=False    


class Account:
    CountAccount=0

    def __init__(self,name,email,address,account_type):
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        Account.CountAccount+=1
        self.accountNo=Account.CountAccount
        self.balance=0
        self.countLoan=0
        self.amount_loan=0
        self.transactions=[]
        self.transactionId=self.accountNo*100  

    def AvailableBalanceCheck(self):
        print(f"Name: {self.name}")
        print(f"Account No: {self.accountNo}")
        print(f"Balance: {self.balance}")

    def Transfer(self,bank,transferId,amount):
        for account in bank.accounts:
            if transferId == account.accountNo:
                other=account
                if self.balance >= amount:
                    self.balance-=amount
                    other.balance+=amount
                    print(f"{amount} from {self.name} to {other.name} Transferred Succesfully!!")

                    transaction={}
                    self.transactionId+=1
                    transaction["id"]=self.transactionId
                    transaction["type"]="transfer"
                    transaction["from"]=self.name
                    transaction["to"]=other.name
                    transaction["amount"]=amount

                    self.transactions.append(transaction)
                else:
                    print(f"Insufficient Amount!")

                return
        print("Account does not exist!!")

    def deposit(self,bank,amount):
        if amount > 0:
            bank.totalBalance += amount
            self.balance += amount

            transaction={}
            self.transactionId+=1
            transaction["id"]=self.transactionId
            transaction["type"]="deposit"
            transaction["amount"]=amount

            self.transactions.append(transaction)
        else:
            print("Invalid Amount")

    
    def withdraw(self,bank,amount):
        if amount > 0 and bank.totalBalance >= amount and self.balance >= amount:
            bank.totalBalance -= amount
            self.balance -= amount

            transaction={}
            self.transactionId+=1
            transaction["id"]=self.transactionId
            transaction["type"]="withdraw"
            transaction["amount"]=amount

            self.transactions.append(transaction)
        else:
            print("Withdrawal amount exceeded")
    
    def takeLoan(self,bank,amount):
        if bank.loanStatus== True and amount > 0 and bank.totalBalance >= amount and self.countLoan < 2:
            self.amount_loan += amount
            self.balance += amount
            self.countLoan +=1
            bank.totalLoan += amount

            transaction={}
            self.transactionId+=1
            transaction["id"]=self.transactionId
            transaction["type"]="loan"
            transaction["amount"]=amount

            self.transactions.append(transaction)
        else:
            print("Invalid Loan Request")

    def ShowTransactionHistory(self):
        print(f"Transaction History of {self.name}")

        for transaction in self.transactions:
            if "to" in transaction:
                print(f"{transaction['id']}: {transaction['type']} of tk {transaction['amount']} to {transaction['to']}")

            elif "id" in transaction:
                 print(f"{transaction['id']}: {transaction['type']} of tk {transaction['amount']}")
            

bank=Bank("Sifat bank ltd","Gazipur")
admin=bank.CreatAccount("admin","admin978@gmail.com","gazipur","admin")
user=bank.CreatAccount("MD SIFAT AHAMED","sifat@gmail.com","kaliganj,Gazipur","user")

currentUser=admin
changeUser=True
currentUser=None

while True:
    print("""
        1. Admin
        2. User
        3. Exit
        """)
    op=int(input("Enter your choice :"))
    if op==1:
        print("Admin Id = admin, Admin Pass 123")
        id=input("Enter Id :")
        pas=input("Enter Password : ")

        print("\n<--------------->")
        print("Welcome to ADMIN")
        print("\n<--------------->")

        while True:
            print()
            print("1: Create Account")
            print("2: Delete Account")
            print("3: Show Users")
            print("4: Check Total Balance")
            print("5: Check Total Loan")
            print("6: On Loan")
            print("7: Off Loan")
            print("8: Log Out")

            ch=int(input("Enter option :"))

            if ch==1:
                name=input("Enter Your Name :")
                email=input("Enter Yoyr Email :")
                address=input("Enter Your Address :")
                account_type=input("Enter Account type (Saving/Current) :")

                bank.CreatAccount(name,email,address,account_type)
                print("Account create succesfully!!")

            elif ch==2:
                accountNo=int(input("Enter Account No :"))
                bank.DeleteAccount(accountNo)
                print("Account Delete Succesfully!!")

            elif ch==3:
                bank.ShowUsers()

            elif ch==4:
                bank.TotalBalance()

            elif ch==5:
                bank.TotalLoan()

            elif ch==6:
                bank.LoanStart()
            
            elif ch==7:
                bank.LoanStop()
                print("Loan is OFF")

            elif ch==8:
                break
            
            else:
                print("Invalid Option!")

    elif op==2:
        while op==2:
            if currentUser==None:
                print("No logged in User \n")
                cho=input("Login or Register (L/R) :")

                if cho=="R":
                    name=input("Enter Your Name :")
                    email=input("Enter Yoyr Email :")
                    address=input("Enter Your Address :")
                    account_type=input("Enter Account type (Saving/Current) :")

                    user=bank.CreatAccount(name,email,address,account_type)

                    currentUser=user
                    changeUser=True

                else:
                    id=int(input("Enter Account No :"))

                    found=False
                    for user in bank.accounts:
                        if id == user.accountNo:
                            currentUser = user
                            changeUser = True
                            found =True
                            break
                    if found == False:
                        print("\n User not found\n")

            else:
                print(f"\nWelcome to {currentUser.name}\n")
                print()
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Check Transaction History")
                print("5. Take Loan")
                print("6. Transfer")
                print("7. Logout")

                user_ch=int(input("Enter your choice: "))
                if user_ch==1:
                    amount = int(input("Enter amount to deposit: "))
                    currentUser.deposit(bank, amount)
                elif user_ch== 2:
                    amount = int(input("Enter amount to withdraw: "))
                    currentUser.withdraw(bank, amount)
                    
                elif user_ch == 3:
                    currentUser.AvailableBalanceCheck()
                    
                elif user_ch == 4:
                    currentUser.ShowTransactionHistory()
                    
                elif user_ch == 5:
                    amount = int(input("Enter loan amount: "))
                    currentUser.takeLoan(bank, amount)
                    
                elif user_ch == 6:
                    target_account_number = int(input("Enter target account number for transfer: "))
                    amount = int(input("Enter amount to transfer: "))
                    currentUser.Transfer(bank, target_account_number, amount)
                
                elif user_ch == 7:
                    currentUser = None
                    break

                else:
                    print("Invalid choice. Please enter a valid option.")

    elif op == 3:
        break