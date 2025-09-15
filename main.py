import csv
import os
from datetime import datetime

# Create log folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Log file path
log_file = "logs/log.txt"

def generate_email(full_name):
    email = full_name.lower().replace(" ", ".") + "@company.com"
    return email

def log_action(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def onboard_user(full_name, department, role):
    email = generate_email(full_name)
    temp_password = "Welcome123!"  # Could randomize later
    print(f"✅ Onboarded: {email} | Role: {role}")
    log_action(f"Onboarded {full_name} ({department}) - Email: {email}, Role: {role}, Temp Password: {temp_password}")

def offboard_user(full_name, department, role):
    email = generate_email(full_name)
    print(f"🔒 Offboarded: {email} | Account deactivated")
    log_action(f"Offboarded {full_name} ({department}) - Email: {email}, Account deactivated and archived")

def process_users(csv_file):
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["full_name"]
            dept = row["department"]
            role = row["role"]
            action = row["action"].lower()

            if action == "onboard":
                onboard_user(name, dept, role)
            elif action == "offboard":
                offboard_user(name, dept, role)
            else:
                print(f"⚠️ Unknown action for {name}: {action}")
                log_action(f"Skipped {name} due to unknown action: {action}")

# Run the script
if __name__ == "__main__":
    process_users("users.csv")