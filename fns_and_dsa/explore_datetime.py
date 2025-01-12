from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format and print the date and time
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    # Ask the user for the number of days
    days = int(input("Enter the number of days to add: "))
    # Add the number of days to the current date
    future_date = datetime.now() + timedelta(days=days)
    # Print the future date
    print("Future Date:", future_date.strftime("%Y-%m-%d"))

# Main program
print("Welcome to the Date and Time Program!")
display_current_datetime()
calculate_future_date()
