# daily_reminder.py
def main():
    while True: # Ask the user for a task
        task = input("Please enter a task: ")
        # Ask the user for the priority level
        priority = input("Please enter the priority level (high, medium, low): ").lower()
        # Ask if the task is time-sensitive
        time_sensitive = input("Is this task time-sensitive? (yes/no): ").lower()
        # Generate the reminder message
        reminder = f"Reminder: You have a task to '{task}' with a priority level of '{priority}'."
        if time_sensitive == 'yes': reminder += " This task is time-sensitive!"
        print(reminder)
        # Ask if the user wants to add another task
        another = input("Would you like to add another task? (yes/no): ").lower()
        if another != 'yes': break
        if __name__ == "__main__": main()
