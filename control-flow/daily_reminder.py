def daily_reminder():
    # Step 1: Prompt for task input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Step 2: Match Case to handle priority
    match priority:
        case 'high':
            priority_message = "high priority"
        case 'medium':
            priority_message = "medium priority"
        case 'low':
            priority_message = "low priority"
        case _:
            priority_message = "unknown priority"

    # Step 3: Handling time sensitivity with if-else
    if time_bound == 'yes':
        time_message = "that requires immediate attention today!"
    else:
        time_message = "Consider completing it when you have free time."

    # Step 4: Print the reminder
    print(f"Reminder: '{task}' is a {priority_message} task {time_message}")


# Call the function to run the reminder program
if __name__ == "__main__":
    daily_reminder()

