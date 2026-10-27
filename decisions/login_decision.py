# login_decision.py
# Description: This program Check login inputs and decide to allow or block the user

# Main settings for the login system
MAX_FAILED = 5
KNOWN_USER = "analyst"
STORED_PASSWORD = "Blue#Falcon72"

# Get username, failed attempts , and password from the user
username = input("Username: ")
failed = int(input("Failed attempts so far: "))
password = input("Password: ")

# Check if the account is locked first
if failed >= MAX_FAILED:
    print("Account locked.")
# Check if the username is wrong
elif username != KNOWN_USER:
    print("Unknown user.")
# Check if the password is wrong and show attempts left
elif password != STORED_PASSWORD:
    attempts_left = MAX_FAILED - failed - 1
    print(f"Access denied. Attempts left: {attempts_left}")
# If everything is correct, grant access
else:
    print("Access granted.")

# --- END OF PROGRAM ---
