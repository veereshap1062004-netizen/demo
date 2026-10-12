
import os

FILE_NAME = "tasks.txt"


# Load tasks from the text file
def load_tasks():
    tasks = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split("|", 1)

                if len(parts) == 2:
                    tasks.append({
                        "task": parts[1],
                        "completed": parts[0] == "1"
                    })

    return tasks


# Save tasks to the text file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            status = "1" if task["completed"] else "0"
            file.write(status + "|" + task["task"] + "\n")


# Display all tasks
def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n--- To-Do List ---")

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['task']} - {status}")


# Main program
tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter task name: ").strip()

        if task_name and "|" not in task_name:
            tasks.append({
                "task": task_name,
                "completed": False
            })
            save_tasks(tasks)
            print("Task added successfully!")
        else:
            print("Please enter a valid task name.")

    elif choice == "2":
        display_tasks(tasks)

    elif choice == "3":
        display_tasks(tasks)

        if tasks:
            try:
                number = int(input("Enter task number to complete: "))

                if 1 <= number <= len(tasks):
                    tasks[number - 1]["completed"] = True
                    save_tasks(tasks)
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        display_tasks(tasks)

        if tasks:
            try:
                number = int(input("Enter task number to remove: "))

                if 1 <= number <= len(tasks):
                    removed = tasks.pop(number - 1)
                    save_tasks(tasks)
                    print("Removed task:", removed["task"])
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Tasks saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
