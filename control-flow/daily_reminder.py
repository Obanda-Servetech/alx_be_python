# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Validate priority input
if priority not in ["high", "medium", "low"]:
    print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")
    exit()

# Validate time-bound input
if time_bound not in ["yes", "no"]:
    print("Invalid input for time-bound. Please enter 'yes' or 'no'.")
    exit()

# Use Match Case to determine priority level response
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."

# Modify the reminder if the task is time-sensitive
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Display the reminder
print(f"\nReminder: {reminder}")

