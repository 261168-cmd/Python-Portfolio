# fix_the_policy.py
# Check new password length and username match.

MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

# Syntax Error: Forgot the colon at the end of the line
# Fix: Add ':'
if len(password) < MIN_LENGTH:
    print("- Too short.")

# Semantic Error: 'elif' skips this check if the password is too short
# Fix: Change 'elif' to 'if' so it checks both rules
if password == username:
    print("- Must not be the same as the username.")

# Semantic Error: Wrong test order; >= 12 blocks >= 16 from working
# Fix: Put >= 16 first in the chain
if len(password) >= 16:
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"

# Indentation Error: Print was trapped inside the else block
# Fix: Move it to the left to run every time
print(f"Length: {len(password)} ({strength})")

# --- END OF PROGRAM ---