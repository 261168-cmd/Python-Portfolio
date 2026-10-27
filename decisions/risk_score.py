# File: risk_score.py
# Description: Calculates login risk score and classifies the risk level.

score = 0

# Get values from the user input
failed_attempts = int(input("Failed attempts in the last hour: "))
login_hour = int(input("Login hour (0-23): "))
new_device = input("New device (yes/no): ")

# Add points based on security rules
if failed_attempts >= 3:
    score += 40

if login_hour < 6:
    score += 30

if new_device == "yes":
    score += 30

# Check level to find the final risk
if score >= 70:
    risk_level = "HIGH"
elif score >= 30:
    risk_level = "MEDIUM"
else:
    risk_level = "LOW"

print(f"Risk score: {score} ({risk_level})")

# --- END OF PROGRAM ---