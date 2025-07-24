# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide tailored reminders based on input
if priority == "high" and time_bound == "yes":
    print(f"Reminder: '{task}' is a HIGH priority and time-sensitive task. Handle it immediately!")
elif priority == "high" and time_bound == "no":
    print(f"Reminder: '{task}' is a HIGH priority task. Plan to do it soon.")
elif priority == "medium" and time_bound == "yes":
    print(f"Reminder: '{task}' is a MEDIUM priority task that is time-sensitive. Try to finish it today.")
elif priority == "medium" and time_bound == "no":
    print(f"Reminder: '{task}' is a MEDIUM priority task. Do it when possible.")
elif priority == "low" and time_bound == "yes":
    print(f"Reminder: '{task}' is a LOW priority task but time-sensitive. Consider completing it soon.")
elif priority == "low" and time_bound == "no":
    print(f"Reminder: '{task}' is a LOW priority and not urgent. Do it at your convenience.")
else:
    print("Reminder: Invalid input detected. Please use 'high', 'medium', or 'low' for priority and 'yes' or 'no' for time-bound.")
