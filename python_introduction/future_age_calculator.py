# Prompt the user for their current age
current_age = int(input("How old are you? "))

# Year to calculate the future age (assuming current year is 2023)
target_year = 2050

# Calculate age in the target year (add 27 years)
age_in_2050 = current_age + (target_year - 2023)

# Print the result in a user-friendly format
print(f"In {target_year}, you will be {age_in_2050} years old.")
