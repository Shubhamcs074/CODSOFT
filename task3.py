def task_management():
    tasks = []  # List to store tasks

    while True:
        print("\n>>>>> To-Do List <<<<<")
        print("1. ADD TASK")
        print("2. SHOW TASKS")
        print("3. MARK TASK AS DONE")
        print("4. EXIT")

        choice = input("Please enter your choice between (1-4): ")

        if choice == '1':
            print()
            try:
                no_of_tasks = int(input("How many tasks do you want to ADD: "))
                for i in range(no_of_tasks):
                    task = input(f"Enter task {i + 1}: ")
                    tasks.append({"task": task, "done": False})
                    print("Task Added!")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '2':
            print("\nTasks:")
            if not tasks:
                print("No tasks to show.")
            else:
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            try:
                task_index = int(input("Enter the task number to mark as completed/done: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]["done"] = True
                    print("Task marked as done!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a valid task number.")

        elif choice == '4':
            print("Exiting the To-Do List")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    task_management()
