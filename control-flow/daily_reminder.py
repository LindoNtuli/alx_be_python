# daily_reminder.py
#Prompt for a single task
Task = input("Enter your task: ")
# Prompt for the task's priority
Priority = input("Priority (high/medium/low): ").lower()
# Ask if the task is time-sensitive
Time_bound = input("Is it time-bound? (yes/no): ").lower()
# Initialize the reminder message
Reminder = f"Reminder: '{Task}' is a {Priority} priority task"
# Process the task based on priority
match Priority:
    case "high": Reminder += " that requires immediate attention today!"
    case "medium": Reminder += " This is a medium priority task."
    case "low": Reminder += ". Consider completing it when you have free time."
    case _: Reminder += " Priority level not recognized."
# Modify the reminder if the task is time-bound
if Time_bound == "yes": Reminder += ""
# Print the customized reminder
print (f"Reminder: {Reminder}!")
