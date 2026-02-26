# lib/cli.py
import argparse
from lib.task_manager import add_task, complete_task, list_tasks

parser = argparse.ArgumentParser(description="Task Manager CLI")
parser.add_argument("--add-task", type=str, help="Add a new task")
parser.add_argument("--complete-task", type=int, help="Complete a task by index")
parser.add_argument("--list-tasks", action="store_true", help="List all tasks")
args = parser.parse_args()

if args.add_task:
    add_task(args.add_task)
elif args.complete_task is not None:
    complete_task(args.complete_task)
elif args.list_tasks:
    list_tasks()
else:
    parser.print_help()