# Importance: Fixing syntax and runtime errors in server records.
# File Name: fix_the_record.py

device_name = "edge-router"

# Wrong: 2nd_ip = "192.0.2.1"
# Reason: Name cannot start with a number.
# System Error: SyntaxError: invalid decimal literal
# Fix: Rename to backup_ip.
backup_ip = "192.0.2.1"

# Wrong: class = "router"
# Reason: class is a reserved system keyword in Python.
# System Error: SyntaxError: invalid syntax
# Fix: Rename to device_type.
device_type = "router"

# Wrong: port = int("twenty-two")
# Reason: Cannot convert text letters into int value number.
# System Error: ValueError: invalid literal for int()
# Fix: Change text to numeric "22".
port = int("20")

# Wrong: print("Device:", device_nam)
# Reason: Misspelled name, variable not defined.
# System Error: NameError: name 'device_nam' is not defined
# Fix: Change to device_name.
print("-" * 30)
print("Device Record Data:")
print("Device Name:", device_name)
print("Backup IP:  ", backup_ip)
print("Device Type:", device_type)
print("Port Number:", port)
print("-" * 30)

# Note:
# Python checks SyntaxError first before running the code.
# So, the first two bugs stop the program immediately.
