# Defining global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):

    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    print("Temperature Conversion Tool")
    try:
        # Prompting user for temperature input
        temp = input("Enter the temperature (e.g., 100C or 212F): ").strip().upper()
        if temp.endswith("C"):
            celsius = float(temp[:-1])
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit:.2f}°F.")
        elif temp.endswith("F"):
            fahrenheit = float(temp[:-1])
            celsius = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius:.2f}°C.")
        else:
            raise ValueError("Invalid input format. Please use 'C' or 'F' suffix.")
    except ValueError as e:
        print("Invalid temperature. Please enter a numeric value followed by 'C' or 'F'.")

if __name__ == "__main__":
    main()
