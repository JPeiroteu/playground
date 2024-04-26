"""
Module to manage student grades and assignments.
"""

class Student:
    """Class representing a student."""
    def __init__(self, name):
        self.name = name
        self.assignments = []

    def add_grade(self, grade, weight):
        """Add a grade for an assignment."""
        self.assignments.append(Work(grade, weight))

    def final_grade(self):
        """Calculate the final grade for the student."""
        return sum(assignment.grade * assignment.weight for assignment in self.assignments)

class Work:
    """Class representing a student's assignment."""
    def __init__(self, grade, weight):
        self.grade = grade
        self.weight = weight

def main():
    """Main function to interact with the user."""
    students = {}

    while True:
        stud_work = input("Insert student name, work, or class media: ").lower()

        if stud_work == "student name":
            name = input("Student Name: ")
            students[name] = Student(name)

        elif stud_work == "work":
            student_name = input("Enter Student Name: ")

            if student_name in students:
                grade = float(input("Student Grade: "))
                weight = float(input("Work Weight: "))

                students[student_name].add_grade(grade, weight)
                print(students[student_name].assignments)
                print(students[student_name].final_grade())
            else:
                print("Student not found.")

        else:
            students_media = sum(student.final_grade() for student in students.values())
            n_students = len(students)

            print(students_media / n_students)

if __name__ == "__main__":
    main()
