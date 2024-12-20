# personal daily reminder
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generating reminder message based on priority and time sensitivity
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = "Invalid priority level."

if time_bound == "yes" and priority in ["high", "medium", "low"]:
    message += " that requires immediate attention today!"
elif time_bound == "no" and priority in ["high", "medium", "low"]:
    message += ". Consider completing it when you have free time."

# Printing final reminder
print(f"Reminder:", {message})