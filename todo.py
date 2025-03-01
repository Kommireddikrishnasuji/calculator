import os
def add_task(tasks,description,due_date):
    tasks.append({"description":description,"due date":due_date})
def view_task(tasks):
    if not tasks:
        print("No Tasks Found.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
           print(f"{idx}.{task['description']}- Due Date: {tasks['due_date']}")

def delete_task(tasks,task_index):
    if 1<= task_index <= len(tasks):
        del tasks [task_index-1]
        print("Task Delete Succesfully")
    else:
        print("Invalid task index.")

def save_task_to_file(tasks, file_path):
    with open(file_path,'w') as f:
        for task in tasks:
            f.write(f"{task['description']} [{task['due_date']}\n") 

def load_task_From_file(file_path):
    tasks=[]
    if os.path.exists(file_path):
        with open(file_path,'r') as f:
            for line in f:
                description,due_data = line,strip().split('|')
                tasks.append({"description": description, "due_data": due_date})
    return tasks   

def main():
    tasks =[]
    file_path = "tasks.txt" 
    tasks = load_task_from_file (file_path)
    while True:
        print("\noption:")
        print("1. Add Task")
        print("2. view Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter you Choice (1/2/3/4)")
        if choice =='1':
            description = input("Enter task Description:")
            due_task = input("Enter Due Date:")
            add_task(tasks,description,due_task)
            save_task_to_file(tasks,file_path)
        elif choice =="2":
             view_task(tasks) 
        elif choice == "3":        
             view_task (tasks)
             task_index = int ((input("Enter the task index to delete:")))
             delete_task(tasks,task_index)
             save_task_to_file(tasks,file_path)
        elif choice =="4":
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please Try again")

if __name__ == "_main_": 
    main()                
                                   
