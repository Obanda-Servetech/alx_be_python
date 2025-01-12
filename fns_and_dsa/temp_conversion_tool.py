# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Main function to handle user interaction for temperature conversion.
    """
    try:
        # Prompt the user to enter a temperature
        temperature_input = input("Enter the temperature to convert: ")
        # Ensure the input is numeric
        if not temperature_input.replace('.', '', 1).isdigit() and not temperature_input.lstrip('-').replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temperature = float(temperature_input)
        # Prompt the user to specify the temperature unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == "F":
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        elif unit == "C":
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        else:
            print("Invalid unit. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

