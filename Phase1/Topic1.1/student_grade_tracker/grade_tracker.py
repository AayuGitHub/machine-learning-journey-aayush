# grade_tracker.py  

students = [] # list of student dictionaries

'''
Method to Add a new student record
'''
def add_student():
    print("\n--- Add new student ---")
    name = input("Enter student name: ")
    subject = input("Enter subject: ")

    marks_input = input("Enter marks (0-100): ") 
    # convert to int carefully
    try:
        marks = int(marks_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        marks = 0

    student_record = {
        "name": name,
        "subject": subject,
        "marks": marks
    }   

    students.append(student_record) 
    print(f"Student record added: {student_record}")

#  List: students
# dictionary: student_record

'''
Method to show all student records
'''
def show_all_students():
    print("\n--- All students ---")
    if not students:
        print("No students found.")
    else:
        for record in students:
            print(f"Name: {record['name']}, Subject: {record['subject']}, Marks: {record['marks']}")

'''
Method to show unique subject of all students
'''

def show_unique_subjects():
    print("\n--- Unique Subjects ---")
    if not students:
        print("No records yet.")
        return

    subjects = set()  # empty set
    for record in students:
        subjects.add(record["subject"])

    print("Subjects:", subjects)

'''
Method to show average marks of each student
'''
def show_average_marks():
    print("\n--- Average Marks per Student ---")
    if not students:
        print("No records yet.")
        return

    marks_by_name = {} # name -> list of marks 

    for record in students:
        name = record["name"]
        marks = record["marks"]

        if name not in marks_by_name:
            marks_by_name[name] = []
        marks_by_name[name].append(marks)
    
    for name, marks in marks_by_name.items():
        average = sum(marks) / len(marks)
        print(f"{name}: {average}")

'''
Main method to run the program
'''
def main():
    while True:
        print("\n==== Student Grade Tracker ====")
        print("1. Add student record")
        print("2. Show all student records")
        print("3. Show unique subjects")
        print("4. Show average marks per student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_all_students()
        elif choice == "3":
            show_unique_subjects()
        elif choice == "4":
            show_average_marks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()

