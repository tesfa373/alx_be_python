# daily_reminder.py

while True:
    # Prompt for task input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process based on priority using match-case
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' has an unknown priority level"
    
    # Add time-sensitivity message
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    # Print the final reminder
    print("\nReminder:", reminder)

    # Ask if user wants to run again
    again = input("\nDo you want to enter another task? (yes/no): ").lower()
    if again != "yes":
        print("Good luck with your tasks!")
        break
