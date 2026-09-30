import threading
import time
from datetime import datetime


class AlarmService:
    def __init__(self, schedule_manager):
        self.schedule_manager = schedule_manager
        self.running = True
        self.triggered_tasks = set()

    def start_monitoring(self):
        def monitor():
            while self.running:
                now = datetime.now()
                current_day = now.strftime("%A").lower()
                current_time = now.strftime("%H:%M")

                for task in self.schedule_manager.tasks:
                    if current_day in task.days and current_time == task.start_time:
                        # Stop the same task from ringing more than once in a minute
                        task_key = f"{task.task_id}_{current_day}_{current_time}"

                        if task_key not in self.triggered_tasks:
                            print(
                                f"\n\n🔔 ALARM! IT'S TIME TO START: "
                                f"{task.name.upper()} 🔔\n"
                                "Press Enter to continue..."
                            )
                            self.triggered_tasks.add(task_key)

                # Reset the set when the minute changes
                if (
                    len(self.triggered_tasks) > 0
                    and current_time != list(self.triggered_tasks)[0].split("_")[2]
                ):
                    self.triggered_tasks.clear()

                time.sleep(15)  # Check for alarms every 15 seconds

        thread = threading.Thread(target=monitor, daemon=True)
        thread.start()

    def stop(self):
        self.running = False