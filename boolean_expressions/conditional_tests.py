# conditional_tests.py
# Description: Writing 10 conditional tests to predict True or False.


user = "analyst"
role = "viewer"
failed = 3
port = 22

# --- TRUE TESTS ---

# Test 1: Check if user is analyst
print("Is user == 'analyst'? I predict True.")
print(user == "analyst")

# Test 2: Check if failed is 3 or more
print("\nIs failed >= 3? I predict True.")
print(failed >= 3)

# Test 3: Check port and role together
print("\nIs port != 80 and role == 'viewer'? I predict True.")
print(port != 80 and role == "viewer")

# Test 4: Check if port is 22 or failed is 0
print("\nIs port == 22 or failed == 0? I predict True.")
print(port == 22 or failed == 0)

# Test 5: Reverse a False condition using 'not'
print("\nIs not failed < 2? I predict True.")
print(not failed < 2)

# --- FALSE TESTS ---

# Test 6: Check if failed is greater than 5
print("\nIs failed > 5? I predict False.")
print(failed > 5)

# Test 7: Check if port is 10 or less
print("\nIs port <= 10? I predict False.")
print(port <= 10)

# Test 8: Check if role is admin
print("\nIs role == 'admin'? I predict False.")
print(role == "admin")

# Test 9: Both sides must be true for 'and'
print("\nIs user == 'analyst' and port == 80? I predict False.")
print(user == "analyst" and port == 80)

# Test 10: Both sides are false for 'or'
print("\nIs failed == 5 or not port == 22? I predict False.")
print(failed == 5 or not port == 22)

# --- END OF TESTS ---