# access_check.py
# Description: Check user login access using boolean logic.

MAX_FAILED = 5

# Ask the user for security details
role = input("Role: ")
mfa_passed = input("MFA passed (yes/no): ")
failed = int(input("Failed attempts: "))

# Check if MFA word is yes
mfa_ok = mfa_passed == "yes"

# Check if role is admin or root
is_privileged = role == "admin" or role == "root"

# Can log in only if MFA is OK and failed attempts are less than 5
can_log_in = mfa_ok and failed < MAX_FAILED

# Display the final security results
print(f"MFA OK: {mfa_ok}")
print(f"Privileged role: {is_privileged}")
print(f"Can log in: {can_log_in}")

# --- END OF PROGRAM ---