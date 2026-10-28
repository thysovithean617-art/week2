from datetime import datetime
import json
from json.tool import main

class StudentList:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
# if __name__ == "__main__":
#     students = StudentList()
#     print("Student list Initialized")
    def add_task(self, description):
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.tasks.append(task)
        print(f"Task'{description}'added successfully!")
        self.save_tasks()
# if __name__ == "__main__":
#     students = StudentList()
#     students.add_task("Learn Python")
#     students.add_task("Build a project")
#     print(students.tasks)
    def view_tasks(self):
        if not self.tasks:
            print("f\nNo tasks found!")
            return
# if __name__ == "__main__":
#     students = StudentList()
#     students.add_task("Learn Python")
#     students.add_task("Build a project")
#     students.view_tasks()
    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                print(f"Task {task_id} marked as completed!")
                self.save_tasks()
                return
        print(f"Task with ID {task_id} not found!")
# if __name__ == "__main__":
#     students = StudentList()
#     students.add_task("Learn Python")
#     students.add_task("Build a project")
#     students.view_tasks()
#     students.complete_task(1)
#     students.view_tasks()
    def delete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                print(f"Task {task_id} deleted!")
                return
        print(f"Task with ID {task_id} not found!")
        self.save_tasks()
# if __name__ == "__main__":
#     students = StudentList()
#     students.add_task("Learn Python")
#     students.add_task("Build a project")
#     students.view_tasks()
#     students.delete_task(2)
#     students.view_tasks()
    def search_tasks(self, keyword):
        keyword = keyword.strip().lower()
        results = [
        task for task in self.tasks
        if keyword in task['description'].lower()
        ]
        if not results:
            print(f"\nNo tasks found matching '{keyword}'")
            return
        print(f"\nSearch results for '{keyword}':")
        print("-" * 50)
        for task in results:
            status = "Completed" if task['completed'] else " "
            print(f"{task['id']}. [{status}] {task['description']}")
            print(f"-" * 50)
# if __name__ == "__main__":
#     students = StudentList()
#     students.add_task("Learn Python")
#     students.add_task("Build a project")
#     students.add_task("Learn Excel")
#     students.search_tasks("Learn")
#     students.search_tasks("xyz")
    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)
    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()
    def main():
        students = StudentList()
        while True:
            print("\n===Student List Application===")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Complete Task")
            print("4. Delete Task")
            print("5. Search Tasks")
            print("6. Exit")
            choice = input("\nEnter your choice (1-5): ")
            if choice == "1":
                description = input("Enter task description: ")
                students.add_task(description)
            elif choice == "2":
                students.view_tasks()
            elif choice == "3":
                students.view_tasks()
                try:
                    task_id = int(input("Enter task ID: "))
                    students.complete_task(task_id)
                except ValueError:
                    print("Please enter a valid task ID!")
            elif choice == "4":
                students.view_tasks()
                try:
                    task_id = int(input("Enter task ID to delete: "))
                    students.delete_task(task_id)
                except ValueError:
                    print("Please enter a valid task ID!")
            elif choice == "5":
                keyword = input("Enter a keyword to search for: ")
                students.search_tasks(keyword)
            elif choice == "6":
                print("Thank you for using the To-Di List application.")
                break
            else:
                print("Invalid choice! Please try again.")
# if __name__ == "__main__":
#     main()
