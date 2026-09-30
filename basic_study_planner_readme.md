# 🎓 Basic Study Planner

Welcome to the **Basic Study Planner**! 👋 

If you're looking at this repository for the first time, this is a lightweight, command-line interface (CLI) application built entirely in Python. It's designed to help students and professionals manage their study sessions or daily tasks directly from the terminal. 

Instead of juggling multiple apps, this tool combines a daily task scheduler, background alarm notifications, a countdown timer, and a stopwatch—all in one place!

## ✨ Features
* **Interactive CLI Menu:** Easy-to-read, color-coded terminal interface.
* **Task Management:** Add, edit, view, and delete study tasks for specific days and times.
* **Smart Background Alarms:** A background thread constantly monitors your schedule and alerts you when it's time to start a task, without interrupting your terminal usage.
* **Built-in Focus Tools:** Includes a countdown timer and a stopwatch to track your active study sessions.
* **Persistent Storage:** Automatically saves your schedule to a local JSON file so you never lose your data between sessions.

---

## 🚀 Getting Started

Follow these simple step-by-step instructions to get the planner up and running on your local machine.

### 1. Prerequisites (Environment Setup)
Before you begin, you will need the following installed on your computer:
* **Python 3.7 or higher:** You can download it from [python.org](https://www.python.org/downloads/).
* **Operating System:** 🪟 **Windows is highly recommended.** 
  *(Note to Evaluator: The stopwatch feature utilizes the `msvcrt` library to detect keystrokes, which is a built-in module specific to Windows. Running the stopwatch option on macOS or Linux will result in an `ImportError`. All other features are cross-platform).*

### 2. Downloading the Project
Clone this repository to your local machine using Git, or download it as a ZIP file and extract it.
```bash
git clone <your-repository-url>
cd <repository-folder-name>
```

### 3. Dependency Installation
Good news! This project is built entirely using Python's Standard Library (modules like `time`, `json`, `threading`, and `datetime`). 
**There are no external dependencies or `requirements.txt` files to install.** You do not need to use `pip install` to run this application.

*(Optional but good practice: If you prefer to run Python apps in isolated environments, you can create a virtual environment using `python -m venv venv` and activate it, though it is not strictly required here).*

### 4. Configuration
No manual configuration is needed! The application handles its own data management. 
When you add your first task, the app will automatically generate a `data.json` file in the root directory to safely store your schedule.

### 5. Execution (Running the App)
To launch the planner, open your terminal or command prompt, ensure you are in the root directory of the project, and run the following command:

```bash
python main.py
```
*(Depending on your system setup, you might need to use `python3 main.py`)*

---

## 📖 How to Use

Once the app is running, you'll be greeted with a numbered menu. Simply type the number of the option you want to use and press **Enter**.

1. **View Schedule:** Lists all your currently saved tasks.
2. **Add a Study Task:** Prompts you for a task name, the days you want to do it (e.g., "monday, wednesday" or "everyday"), and the time (24-hour format).
3. **Edit a Task:** Lets you modify an existing task using its ID.
4. **Delete a Task:** Removes a task from your schedule and re-numbers the remaining tasks to keep things tidy.
5. **Stopwatch:** Starts a stopwatch. Press `Enter` to stop it. (Windows only).
6. **Countdown Timer:** Prompts you for hours, minutes, and seconds, then counts down to zero.
7. **Exit:** Safely shuts down the background alarm service and closes the application.

Happy studying! 📚