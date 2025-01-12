from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Print the current date and time in a readable format
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    # Prompt the user to enter the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Calculate the future date
    future_date = datetime.now() + timedelta(days=days_to_add)
    # Print the future date
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

