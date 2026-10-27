# fix_the_rules.py
# Description: Fixing bugs in the connection rules program.

role = input("Role: ")
port = input("Port: ")

# Wrong Code: is_admin = role = "admin"
# Fix semantic error: use '==' to compare instead of single '=' assignment
is_admin = role == "admin"

# Wrong Code: is_system_port = port =< 1023
# Fix runtime error (str to int) and syntax error (convert '=<' to '<=')
is_system_port = int(port) <= 1023

# Wrong Code: is_web_port = port == 80 or 443
# Fix semantic error: write full comparison on both sides of 'or'
is_web_port = int(port) == 80 or int(port) == 443

# Display the final results
print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")

# --- END OF PROGRAM ---
