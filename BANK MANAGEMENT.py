import pickle
import os
import pathlib

# Class to represent an Account
class Account:
    accNo = 0  # Account number
    name = ''  # Account holder's name
    deposit = 0  # Initial deposit amount
    type = ''  # Type of account (Current/Saving)
    
    # Method to create a new account
    def createAccount(self):
        self.accNo = int(input("ENTER THE ACCOUNT NO : "))  # Get account number from user
        self.name = input("ENTER THE ACCOUNT HOLDER NAME : ")  # Get account holder's name from user
        self.type = input("ENTER THE TYPE OF ACCOUNT [C/S] : ")  # Get account type (C for Current, S for Saving) from user
        self.deposit = int(input("ENTER THE INITIAL AMOUNT(>=500 FOR SAVING AND >=1000 FOR CURRENT):"))  # Get initial deposit amount from user
        print("\n\n\nACCOUNT CREATED")  # Confirm account creation
    
    # Method to display account details
    def showAccount(self):
        print("ACCOUNT NUMBER : ", self.accNo)  # Display account number
        print("ACCOUNT HOLDER NAME : ", self.name)  # Display account holder's name
        print("TYPE OF ACCOUNT", self.type)  # Display account type
        print("BALANCE : ", self.deposit)  # Display account balance
    
    # Method to modify account details
    def modifyAccount(self):
        print("ACCOUNT NUMBER : ", self.accNo)  # Display current account number
        self.name = input("MODIFY ACCOUNT HOLDER NAME : ")  # Get new account holder's name from user
        self.type = input("MODIFY TYPE OF ACCOUNT : ")  # Get new account type from user
        self.deposit = int(input("MODIFY BALANCE : "))  # Get new balance amount from user
        
    # Method to deposit an amount into the account
    def depositAmount(self, amount):
        self.deposit += amount  # Increase the account balance by the deposit amount
    
    # Method to withdraw an amount from the account
    def withdrawAmount(self, amount):
        self.deposit -= amount  # Decrease the account balance by the withdrawal amount
    
    # Method to print a brief report of the account
    def report(self):
        print(self.accNo, " ", self.name, " ", self.type, " ", self.deposit)  # Print account details
    
    # Getters to access private data members
    def getAccountNo(self):
        return self.accNo  # Return account number

    def getAcccountHolderName(self):
        return self.name  # Return account holder's name

    def getAccountType(self):
        return self.type  # Return account type

    def getDeposit(self):
        return self.deposit  # Return account balance
    

# Function to print an introduction message
def intro():
    print("\t\t\t\t**********************")  # Print decorative line
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")  # Print system title
    print("\t\t\t\t**********************")  # Print decorative line
    input()  # Wait for user to press enter

# Function to write a new account to file
def writeAccount():
    account = Account()  # Create a new Account object
    account.createAccount()  # Initialize the account with user input
    writeAccountsFile(account)  # Write the account to file

# Function to display all accounts
def displayAll():
    file = pathlib.Path("accounts.data")  # Define the path to the accounts file
    if file.exists():  # Check if the file exists
        infile = open('accounts.data', 'rb')  # Open the file in read-binary mode
        mylist = pickle.load(infile)  # Load the accounts list from the file
        for item in mylist:  # Iterate through the accounts
            print(item.accNo, " ", item.name, " ", item.type, " ", item.deposit)  # Print each account's details
        infile.close()  # Close the file
    else:
        print("NO RECORDS TO DISPLAY")  # Print message if no accounts are found

# Function to display a specific account based on account number
def displaySp(num):
    file = pathlib.Path("accounts.data")  # Define the path to the accounts file
    if file.exists():  # Check if the file exists
        infile = open('accounts.data', 'rb')  # Open the file in read-binary mode
        mylist = pickle.load(infile)  # Load the accounts list from the file
        infile.close()  # Close the file
        found = False  # Initialize found flag
        for item in mylist:  # Iterate through the accounts
            if item.accNo == num:  # Check if account number matches
                print("YOUR ACCOUNT BALANCE IS = ", item.deposit)  # Print account balance
                found = True  # Set found flag to True
    else:
        print("NO RECORDS TO SEARCH")  # Print message if no accounts are found
    if not found:
        print("NO EXISTING RECORD WITH THIS NUMBER")  # Print message if account number is not found

# Function to handle deposit and withdraw operations
def depositAndWithdraw(num1, num2):
    file = pathlib.Path("accounts.data")  # Define the path to the accounts file
    if file.exists():  # Check if the file exists
        infile = open('accounts.data', 'rb')  # Open the file in read-binary mode
        mylist = pickle.load(infile)  # Load the accounts list from the file
        infile.close()  # Close the file
        os.remove('accounts.data')  # Remove the old file
        for item in mylist:  # Iterate through the accounts
            if item.accNo == num1:  # Check if account number matches
                if num2 == 1:  # Check if operation is deposit
                    amount = int(input("ENTER THE AMOUNT TO DEPOSIT : "))  # Get deposit amount from user
                    item.deposit += amount  # Increase the account balance
                    print("YOUR ACCOUNT IS UPDATED")  # Confirm update
                elif num2 == 2:  # Check if operation is withdraw
                    amount = int(input("ENTER THE AMOUNT TO WITHDRAW : "))  # Get withdrawal amount from user
                    if amount <= item.deposit:  # Check if sufficient balance
                        item.deposit -= amount  # Decrease the account balance
                    else:
                        print("YOU CANNOT WITHDRAW LARGER AMOUNT")  # Print message if insufficient balance
    else:
        print("NO RECORDS TO SEARCH")  # Print message if no accounts are found
    outfile = open('newaccounts.data', 'wb')  # Open new file in write-binary mode
    pickle.dump(mylist, outfile)  # Write updated accounts list to new file
    outfile.close()  # Close the new file
    os.rename('newaccounts.data', 'accounts.data')  # Rename new file to original file name

# Function to delete an account
def deleteAccount(num):
    file = pathlib.Path("accounts.data")  # Define the path to the accounts file
    if file.exists():  # Check if the file exists
        infile = open('accounts.data', 'rb')  # Open the file in read-binary mode
        oldlist = pickle.load(infile)  # Load the accounts list from the file
        infile.close()  # Close the file
        newlist = []  # Initialize new list for remaining accounts
        for item in oldlist:  # Iterate through the accounts
            if item.accNo != num:  # Check if account number does not match
                newlist.append(item)  # Add account to new list
        os.remove('accounts.data')  # Remove the old file
        outfile = open('newaccounts.data', 'wb')  # Open new file in write-binary mode
        pickle.dump(newlist, outfile)  # Write remaining accounts to new file
        outfile.close()  # Close the new file
        os.rename('newaccounts.data', 'accounts.data')  # Rename new file to original file name

# Function to modify an account
def modifyAccount(num):
    file = pathlib.Path("accounts.data")  # Define the path to the accounts file
    if file.exists():  # Check if the file exists
        infile = open('accounts.data', 'rb')  # Open the file in read-binary mode
        oldlist = pickle.load(infile)  # Load the accounts list from the file
        infile.close()  # Close the file
        os.remove('accounts.data')  # Remove the old file
        for item in oldlist:  # Iterate through the accounts
            if item.accNo == num:  # Check if account number matches
                item.name = input("ENTER THE ACCOUNT HOLDER NAME : ")  # Get new account holder's name from user
                item.type = input("ENTER THE ACCOUNT TYPE : ")  # Get new account type from user
                item.deposit = int(input("ENTER THE AMOUNT : "))  # Get new balance amount from user
        outfile = open('newaccounts.data', 'wb')  # Open new file in write-binary mode
        pickle.dump(oldlist, outfile)  # Write updated accounts list to new file
        outfile.close()  # Close the new file
        os.rename('newaccounts.data', 'accounts.data')  # Rename new file to original file name

# Function to write accounts to file
def writeAccountsFile(account):
    file = pathlib.Path("accounts.data")  # Define the path to the accounts file
    if file.exists():  # Check if the file exists
        infile = open('accounts.data', 'rb')  # Open the file in read-binary mode
        oldlist = pickle.load(infile)  # Load the accounts list from the file
        oldlist.append(account)  # Add new account to list
        infile.close()  # Close the file
        os.remove('accounts.data')  # Remove the old file
    else:
        oldlist = [account]  # Initialize new list with the account
    outfile = open('newaccounts.data', 'wb')  # Open new file in write-binary mode
    pickle.dump(oldlist, outfile)  # Write updated accounts list to new file
    outfile.close()  # Close the new file
    os.rename('newaccounts.data', 'accounts.data')  # Rename new file to original file name

# Start of the program
ch = ''  # Initialize choice variable
num = 0  # Initialize account number variable
intro()  # Call intro function to display the introduction

# Main loop to display the menu and handle user input
while ch != 8:  # Continue loop until user chooses to exit
    print("\tMAIN MENU")  # Print main menu title
    print("\t1. NEW ACCOUNT")  # Print option 1
    print("\t2. DEPOSIT AMOUNT")  # Print option 2
    print("\t3. WITHDRAW AMOUNT")  # Print option 3
    print("\t4. BALANCE ENQUIRY")  # Print option 4
    print("\t5. ALL ACCOUNT HOLDER LIST")  # Print option 5
    print("\t6. CLOSE AN ACCOUNT")  # Print option 6
    print("\t7. MODIFY AN ACCOUNT")  # Print option 7
    print("\t8. EXIT")  # Print option 8
    print("\tSELECT YOUR OPTION (1-8) ")  # Prompt user to select an option
    ch = input()  # Get user input
    
    if ch == '1':  # If option 1 is selected
        writeAccount()  # Call function to write new account
    elif ch == '2':  # If option 2 is selected
        num = int(input("\tENTER THE ACCOUNT NO. : "))  # Get account number from user
        depositAndWithdraw(num, 1)  # Call function to deposit amount
    elif ch == '3':  # If option 3 is selected
        num = int(input("\tENTER THE ACCOUNT NO. : "))  # Get account number from user
        depositAndWithdraw(num, 2)  # Call function to withdraw amount
    elif ch == '4':  # If option 4 is selected
        num = int(input("\tENTER THE ACCOUNT NO. : "))  # Get account number from user
        displaySp(num)  # Call function to display account balance
    elif ch == '5':  # If option 5 is selected
        displayAll()  # Call function to display all accounts
    elif ch == '6':  # If option 6 is selected
        num = int(input("\tENTER THE ACCOUNT NO. : "))  # Get account number from user
        deleteAccount(num)  # Call function to delete account
    elif ch == '7':  # If option 7 is selected
        num = int(input("\tENTER THE ACCOUNT NO. : "))  # Get account number from user
        modifyAccount(num)  # Call function to modify account
    elif ch == '8':  # If option 8 is selected
        print("\tTHANK YOU FOR USING BANK MANAGEMENT SYSTEM")  # Print exit message
        break  # Exit the loop
    else:
        print("INVALID CHOICE")  # Print message for invalid choice
    
    ch = input("ENTER YOUR CHOICE : ")  # Prompt user to make another choice
        
