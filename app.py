import random
import matplotlib.pyplot as plt
# =============EXTENDED FUNCTIONALITY=================

# Read file and convert file data into python data
file = open("database.txt", "r").read()
users_data = eval(file)

# Login as ADMIN or INDIVIDUAL
print("Select 1 to Login as Administrator (Admin)")
print("Select 2 to Login as User")

# Input Login Category
login_category = input("Input: ")


# Add New User Function
def add_new_user():
    new_username = input("Username: ")
    new_user_pin = input("Enter 4-Digits Pin: ")
    new_user_pin1 = input("Confirm your 4-Digit pin: ")

    if new_user_pin == new_user_pin1 and new_username != " " or new_username != "":
        # Open and Read DB files
        with open("database.txt", "r") as db:
            db_file = eval(db.read())
            # Create New User Data
            new_user_data = {"username": new_username, "pin": new_user_pin1, 'login_attempt': 0, 'available_balance': 0,
                             'category': 'user'}
            # Add New User to Database
            db_file.append(new_user_data)
        # Save updated files to the Database
        with open("database.txt", "w") as f:
            f.write(str(db_file))

        print(f"'{new_username}' account has been created Successfully")
    else:
        print("Invalid input or Pin mismatched")

# {'username': 'user1', 'pin': '1111', 'login_attempt': 0, 'available_balance': 10000, 'category': 'user'}


# Delete User Function
def delete_user():
    # Input username to Delete
    del_username = input("Enter the Username of the User you want to Delete: ")
    # Check if username exist
    if next((user_to_del for user_to_del in users_data if user_to_del["username"] == del_username), None):
        # Confirm if Admin really want to delete this user
        are_you_sure = input(f"Are you sure you want to delete {del_username}? Yes/No: ").lower()
        # Go ahead and delete user
        if are_you_sure == "yes":
            with open("database.txt", "r") as new_db_file:
                new_db = eval(new_db_file.read())

            new_db = [users_left for users_left in new_db if users_left["username"] != del_username]

            with open("database.txt", "w") as new_db_f:
                new_db_f.write(str(new_db))

            print("User Deleted Successfully")
    else:
        print(f"{del_username} does not exist")


#   Plot Pie Chart Function
def plot_account_balances():
    # Extract Each user available balance into a new dictionary
    available_balances = {acct_bal["username"]: acct_bal["available_balance"] for acct_bal in users_data}

    # colors for each category
    colors = ['#FF0000', '#1D3366', '#046FC6', "#94D1E0", '#82AEC0', '#2F7889']

    # Plotting Pie Chart
    fig, ax = plt.subplots()
    ax.pie(available_balances.values(), labels=available_balances.keys(), autopct='%1.1f%%', startangle=90,
           colors=colors)
    ax.axis('equal')

    plt.show()

    print("Chart Plotted Successfully")


# User Authentication Function
def auth_user():
    global login_user
    global login_pin
    global username
    global pin

    # INPUT USER CREDENTIALS
    username = input("Please enter your username: ")
    pin = input(f"Enter your 4-character PIN: ")
    # ----------------------AUTHENTICATE USER----------------------
    # Check if username exist
    login_user = next((user for user in users_data if user['username'] == username), None)
    # Check if PIN is correct
    login_pin = next((pin for pin in users_data if pin['pin'] == pin), None)


# --------------------------------------------


# Authenticate User/Admin
if login_category == "1":
    # -------Login ADMIN------
    # INPUT ADMIN CREDENTIALS
    admin_user = input("Enter Admin Username: ")
    admin_pin = input("Enter Admin Password: ")

    # Check if admin exist
    admin_login_user = next((admin for admin in users_data if admin['username'] == admin_user), None)
    # Check if PIN is correct
    admin_login_pin = next((admin for admin in users_data if admin['pin'] == admin_pin), None)

    # Confirm if password is correct and the category is admin
    if admin_login_user is not None and admin_login_pin["pin"] == admin_pin and admin_login_user["category"] == "admin":
        print("===========Menu Options===========")
        print("Press 1 to Add New User")
        print("Press 2 to Delete User")
        print("Press 3 to Plot Account Balances")
        print("Press 0 to Exit")
        menu = (input("Input: "))
        if menu == "1":
            print("===========Add New User===========")
            add_new_user()
        elif menu == "2":
            print("===========Delete User===========")
            delete_user()
        elif menu == "3":
            print("===========Plot Account Balances===========")
            plot_account_balances()
        else:
            print("Exit")

    else:
        print("error! Invalid Admin login credentials")

elif login_category == "2":
    # -------Login USER------
    auth_user()
    # Confirm if password is correct again before Performing any Transaction
    if login_user is not None and login_user["pin"] == pin:
        available_balance = login_user['available_balance']
        print(f"----------------------Welcome {username}----------------------")

        # CHECK WHICH TRANSACTION OPTION WAS SELECTED
        print("PRESS 1 to Check Account Balance")
        print("PRESS 2 to Withdraw")
        print("PRESS 3 to Deposit")
        print("PRESS 4 to Change PIN")
        print("PRESS 0 to Exit")
        transaction_option = input("Input: ")

        if transaction_option == "1":
            print("----------------------ACCOUNT BALANCE----------------------")
            print(f"Your Account Balance is ${available_balance:,}")
        elif transaction_option == "2":
            print("----------------------WITHDRAWAL----------------------")
            print(f"Available Balance: ${available_balance:,}")
            try:
                amount = int(input(f"Enter the amount you want to withdraw: "))
                # CHECK IF THERE IS SUFFICIENT FUND
                if available_balance >= amount:
                    # Check if amount is not more than $1000 and it is multiple of 10
                    if amount <= 1000 and amount % 10 == 0:
                        new_balance = int(available_balance) - amount
                        login_user['available_balance'] = new_balance

                        # Read from db.txt
                        with open("database.txt", "r") as withdrawal_db:
                            withdrawal_file = eval(withdrawal_db.read())
                        # Update withdrawal
                        for withdrawal in withdrawal_file:
                            if withdrawal["username"] == username:
                                withdrawal["available_balance"] -= amount
                        # Write update data back to file
                        with open("database.txt", "w") as new_bal:
                            new_bal.write(str(withdrawal_file))

                        print("Withdrawal Successful")
                        print(f"Available Balance: ${new_balance:,}")
                        print("Press 1 to go to Home")
                        print("Press 0 to exist")
                        perform_another_transaction = input("Input: ")
                    else:
                        print("---ERROR!---")
                        print("$1,000 is the maximum per withdrawal and amount must be multiple of $10")
                else:
                    print("Insufficient Balance")
            except ValueError:
                print("Error! Please enter a valid Amount in Integer")
        elif transaction_option == "3":
            print("----------------------DEPOSIT----------------------")
            print("Please enter the amount you want to deposit")
            try:
                # INPUT AMOUNT TO DEPOSIT
                amount_deposit = int(input("Amount: "))

                # MAKING SURE THAT DEPOSITED AMOUNT IS NOT $0
                if amount_deposit > 0:
                    # Read data from database
                    with open("database.txt", "r") as deposit_db:
                        deposit_file = eval(deposit_db.read())
                    # Update Available balance
                    for depositor in deposit_file:
                        if depositor["username"] == username:
                            new_bal = depositor["available_balance"] + amount_deposit
                            depositor["available_balance"] = new_bal

                    # write the update data back to txt file
                    with open("database.txt", "w") as updated_f:
                        updated_f.write(str(deposit_file))

                    print(f"Deposit Successful")
                    print(f"Confirmation Number: {random.randrange(10 ** 13, 10 ** 14)}")
                    print(f"Deposited Amount: ${amount_deposit:,}")
                    print(f"Available Balance: ${amount_deposit + available_balance:,}")
                    print("Press 1 to perform another transaction")
                    print("Press 0 to exit")
                    another_transaction = input("Input: ")
                else:
                    print("ERROR! Amount to deposit must be more than $0")
            except ValueError:
                print("Error! Please enter a valid Amount in Integer")
        elif transaction_option == "4":
            print("----------------------CHANGE PIN----------------------")
            old_pin = input("Enter your OLD PIN: ")
            if old_pin == login_user["pin"]:
                new_pin1 = input("Enter NEW 4-digits PIN: ")
                if len(new_pin1) == 4:
                    new_pin2 = input("Confirm NEW 4-digits PIN: ")
                    # Check if New PIN1 matches with New PIN2
                    if new_pin2 == new_pin1:
                        # Update Database with user's new Pin
                        with open("database.txt", "r") as file:
                            data = eval(file.read())
                        for user in data:
                            if user["username"] == login_user["username"]:
                                user["pin"] = new_pin2
                        # Save updated PIN back into database
                        with open("database.txt", "w") as file:
                            file.write(str(data))
                            print("Your 4-digits PIN has been changed successfully.")
                    else:
                        print("PIN does not match")
                else:
                    print("Error! Your PIN must be 4 digits")
            else:
                print("Incorrect PIN")
        elif transaction_option == "0":
            print(f"----------------------Thank You {login_user['username']}----------------------")
        else:
            print("Invalid Input")
    else:
        print(f"Invalid User: '{username}' does not exist or Incorrect PIN")
else:
    # -------Unauthorized Login Attempt------
    print("Invalid Input! Please try again")
# ===============================================================================
