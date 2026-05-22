# Simple To-Do List Manager

tasks = []

while True:
    print("\n1.Add Task")
    print("2.View Tasks")
    print("3.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

        file = open("tasks.txt", "a")
        file.write(task + "\n")
        file.close()

        print("Task Added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for t in tasks:
            print("-", t)

    elif choice == "3":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")