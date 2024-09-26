# daily_reminder.py
#Prompt for a single task
task = input("Enter your task: ")
# Prompt for the task's priority
priority = input("Priority (high, medium, low): ").lower()
# Ask if the task is time-sensitive
time_bound = input("Is it time-bound? (yes or no): ").lower()
# Initialize the reminder message
reminder = f"Reminder: '{task}' is a {priority} priority task"
# Process the task based on priority
match priority:
    case "high": reminder += " that requires immediate attention today!"
    case "medium": reminder += " This is a medium priority task."
    case "low": reminder += ". Consider completing it when you have free time."
    case _: reminder += " Priority level not recognized."
# Modify the reminder if the task is time-bound
if time_bound == "yes": reminder += " This task requires immediate attention today!"
# Print the customized reminder
print(reminder)
