import schedule
import time

def job():
    print("Task is a scheduled task.")

# Schedule a task to run every day at 2 PM
schedule.every().day.at("05:17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)