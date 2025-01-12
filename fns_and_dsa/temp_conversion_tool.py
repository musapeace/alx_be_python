# Defining global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    print("Welcome to the Temperature Conversion Tool!")

    # Getting temperature and unit from user
    temp_input = input("Enter the temperature (e.g., 100C or 212F): ").strip().upper()

    # Checking if input ends with 'C' or 'F' for Celsius or Fahrenheit
    if temp_input.endswith("C"):
        try:
            celsius = float(temp_input[:-1])  
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
        except ValueError:
            print("Invalid temperature. Please enter a numeric value followed by 'C'.")
    elif temp_input.endswith("F"):
        try:
            fahrenheit = float(temp_input[:-1])  
            celsius = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")
        except ValueError:
            print("Invalid temperature. Please enter a numeric value followed by 'F'.")
    else:
        print("Invalid input. Please end the temperature with 'C' or 'F'.")

if __name__ == "__main__":
    main()
