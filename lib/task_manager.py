# lib/task_manager.py
from datetime import datetime
import json

TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "completed": False, "timestamp": str(datetime.now())})
    save_tasks(tasks)
    print(f"Added task: {title}")

def complete_task(idx):
    tasks = load_tasks()
    if 0 <= idx < len(tasks):
        tasks[idx]["completed"] = True
        save_tasks(tasks)
        print(f"Marked done: {tasks[idx]['title']}")
    else:
        print("Invalid task index")

def list_tasks():
    tasks = load_tasks()
    for i, t in enumerate(tasks):
        status = "✔" if t["completed"] else "✖"
        print(f"{i}. [{status}] {t['title']}")