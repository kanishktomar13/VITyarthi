import sys
import os
import math
import time
from models import ScheduleManager
from alarm_service import AlarmService

os.system('')

BLUE = "\033[34m"
YELLOW = "\033[33m"
RED = "\033[31m"
CYAN = "\033[36m"
RESET = "\033[0m"
ALL_DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
WEEKDAYS = set(ALL_DAYS)

# This function takes the user input of days.
def days(prompt):
    while True:
        days_input = input(prompt).strip().lower()
        if days_input == "everyday":
            return ALL_DAYS.copy()

        days = days_input.replace(",", " ").split()
        if days and all(day in WEEKDAYS for day in days):
            return days
        print(f"{RED}Error: Enter valid weekdays, or 'everyday'. Please try again.{RESET}")
# This function takes the user input of the time.
def start_time():
    while True:
        try:
            hour = int(input("At which hour? (0-23): ").strip())
            minute = int(input("At which minute? (0-59): ").strip())
        except ValueError:
            print(f"{RED}Error: Enter the hour and minute as numbers.{RESET}")
            continue

        if not 0 <= hour <= 23:
            print(f"{RED}Error: Hour must be between 0 and 23. Please try again.{RESET}")
            continue
        if not 0 <= minute <= 59:
            print(f"{RED}Error: Minute must be between 0 and 59. Please try again.{RESET}")
            continue
        return f"{hour:02d}:{minute:02d}"

# This function adds a clock in our code.
def clock(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# Here we are displaying the clock.
def show_clock(label, seconds):
    print(f"\r{label}: {clock(seconds)}\033[K", end="", flush=True)

# This function is for a stopwatch.
def stopwatch():
    import msvcrt

    started_at = time.monotonic()
    print(f"{CYAN}Stopwatch running. Press Enter to stop.{RESET}")
    while True:
        elapsed = int(time.monotonic() - started_at)
        show_clock("Stopwatch", elapsed)
        if msvcrt.kbhit() and msvcrt.getwch() in ("\r", "\n"):
            break
        time.sleep(0.1)
    print()

# This function runs the timer.
def timer():
    duration = timer_duration()
    end_time = time.monotonic() + duration
    while True:                         
        remaining = max(0, math.ceil(end_time - time.monotonic()))
        show_clock("Timer", remaining)
        if remaining == 0:
            break
        time.sleep(min(1, remaining))
    print()
    print("\aTimer finished!")

# This function is for a timer input.
def timer_duration():
    while True:
        try:
            hours = int(input("Timer hours: ").strip())
            minutes = int(input("Timer minutes (0-59): ").strip())
            seconds = int(input("Timer seconds (0-59): ").strip())
        except ValueError:
            print(f"{RED}Enter hours, minutes, and seconds as numbers.{RESET}")
            continue

        if hours < 0 or not 0 <= minutes <= 59 or not 0 <= seconds <= 59:
            print(f"{RED}Use non-negative hours and minutes/seconds from 0 to 59.{RESET}")
            continue

        duration = hours * 3600 + minutes * 60 + seconds
        if duration == 0:
            print(f"{RED}Timer duration must be greater than zero.{RESET}")
            continue
        return duration

# This is the layout for our code.
def menu():
    print("\n" * 10)
    print(f"\n{BLUE}--- Basic Study Planner ---{RESET}")
    print(f"{YELLOW}1{RESET}. View Schedule")
    print(f"{YELLOW}2{RESET}. Add a Study Task")
    print(f"{YELLOW}3{RESET}. Edit a Task")
    print(f"{YELLOW}4{RESET}. Delete a Task")
    print(f"{YELLOW}5{RESET}. Stopwatch")
    print(f"{YELLOW}6{RESET}. Countdown Timer")
    print(f"{YELLOW}7{RESET}. Exit")

# This is the main function which runs the code.
def main():
    manager = ScheduleManager()
    alarm = AlarmService(manager)
    alarm.start_monitoring()

    while True:
        menu()
        choice = input("Select an option: ")

        if choice == '1':
            if not manager.tasks:
                print("Your schedule is empty.")
            else:
                for t in manager.tasks:
                    print(f"[{t.task_id}] {t.name} | Days: {', '.join(t.days).title()} | Time: {t.start_time}")
        
        elif choice == '2':
            name = input("Task Name (e.g., Math Study): ")
            if not name.strip():
                print(f"{RED}Error: Task name cannot be empty.{RESET}")
            else:
                days = days("Days (weekday names, comma or space separated): ")
                if days is not None:
                    time_str = start_time()
                    manager.add_task(name, days, time_str)
                    print("Task added successfully.")

        elif choice == '3':
            if not manager.tasks:
                print("No tasks found.")
            else:
                try:
                    task_id = int(input("Enter Task ID to edit: "))
                except ValueError:
                    print("Task ID not found. Please try again.")
                else:
                    if not any(task.task_id == task_id for task in manager.tasks):
                        print("Task ID not found. Please try again.")
                    else:
                        name = input("New Task Name: ")
                        days = days("New days (weekday names, comma or space separated): ")
                        if days is not None:
                            time_str = start_time()
                            if manager.edit_task(task_id, name, days, time_str):
                                print("Task updated successfully.")
                            else:
                                print("Task ID not found. Please try again.")

        elif choice == '4':
            if not manager.tasks:
                print("No tasks found.")
            else:
                try:
                    task_id = int(input("Enter Task ID to delete: "))
                except ValueError:
                    print("Task ID not found. Please try again.")
                else:
                    if manager.delete_task(task_id):
                        print("Task deleted successfully.")
                    else:
                        print("Task ID not found. Please try again.")

        elif choice == '7':
            print("Exiting Study Planner...")
            alarm.stop()
            sys.exit(0)

        elif choice == '5':
            stopwatch()

        elif choice == '6':
            timer()
            
        else:
            print("Invalid option. Please try again.")

        input(f"\n{CYAN}Press Enter to return to the menu...{RESET}")

if __name__ == "__main__":
    main()