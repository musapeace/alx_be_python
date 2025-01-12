# Defining global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    print("Temperature Conversion Tool")
    
    temp = input("Enter the temperature (e.g., 100C or 212F): ").strip().upper()
    
    if temp.endswith("C"):
        try:
            celsius = float(temp[:-1])
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit:.2f}°F.")
        except ValueError:
            print("Invalid temperature. Please enter a valid number followed by 'C'.")
    
    elif temp.endswith("F"):
        try:
            fahrenheit = float(temp[:-1])
            celsius = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius:.2f}°C.")
        except ValueError:
            print("Invalid temperature. Please enter a valid number followed by 'F'.")
    
    else:
        print("Invalid input. Please enter a temperature ending with 'C' or 'F'.")

if __name__ == "__main__":
    main()
