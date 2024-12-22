# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case 'high':
        reminder = f"Reminder: '{task}' is a high priority task"
    case 'medium':
        reminder = f"Reminder: '{task}' is a medium priority task"
    case 'low':
        reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' has an invalid priority level"

# Handle time-bound condition
if time_bound == 'yes':
    reminder += " that requires immediate attention today!"
else:
    reminder += " and can be completed when you have free time."

# Output the final reminder
print(reminder)

