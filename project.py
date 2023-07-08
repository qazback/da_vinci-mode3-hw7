def main():
    tasks = []
    while True:
        print("Task Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter task name: ")
            add_task(tasks, task)
            print("Task added successfully!")

        elif choice == "2":
            list_tasks(tasks)

        elif choice == "3":
            task = input("Enter task name to complete: ")
            complete_task(tasks, task)
            print("Task marked as complete!")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


def add_task(tasks, task):
    tasks.append({"name": task, "completed": False})


def list_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task in tasks:
            status = " [x]" if task["completed"] else " [ ]"
            print(f"{task['name']}{status}")


def complete_task(tasks, task):
    for t in tasks:
        if t["name"] == task:
            t["completed"] = True
            return
    print("Task not found.")


if __name__ == "__main__":
    main()
