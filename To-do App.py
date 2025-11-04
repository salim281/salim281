tasks = ['wash', 'haircut', 'shopping']

def createTask():
    tasksName = input("Create name for your new Task: \n")
    tasks.append(tasksName.title())
    print("Task created Successfully!\n")
    print()
    #print(tasks)

def deleteTask():
    chooseTask = input("Choose task to Delete:\n")
    print(tasks)

    if chooseTask in tasks:
        tasks.remove(chooseTask)
        print(f"{chooseTask} deleted successfully!")
        print()
        #print(tasks)
    else:
        print()
        print(f"The task '{chooseTask}' NOT FOUND!")

def viewTask():
    print()
    for i, task in enumerate(tasks, start = 1):
        print(i, task)
    #print(f"Total Tasks Available\n{tasks}")

def main():
    while True:
        print()
        print('What do you want to do:')
        print("\nEnter C to [C]reate new task\nD to [D]elete task\nV to [V]iew Task and Q to [Quit]")

        option = input("\nSelect an Option: ").upper()
        if option == 'C':
            createTask()
        elif option == 'D':
            deleteTask()
        elif option == 'V':
            viewTask()
        elif option == 'Q':
            print("Bye!, Bye!!")
            break
        else:
            print("Invalid option. Please try again.")

main()