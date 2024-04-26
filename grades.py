class Student:
    def __init__(self, name):
        self.name = name
        self.assignments = []

    def add_grade(self, grade, weight):
        self.assignments.append(Work(grade, weight))

    def final_grade(self):
        final_grade = 0

        for assignment in self.assignments:
            assignment_grade = assignment.grade * assignment.weight
            final_grade += assignment_grade

        return final_grade

class Work:
    def __init__(self, grade, weight):
        self.grade = grade
        self.weight = weight

def main():
    students = []

    while True:
        stud_work = input("Insert student name, work, or class media: ")

        if stud_work == "student name":
            name = input("Student Name: ")
            students.append(Student(name))

        elif stud_work == "work":
            student_name = input("Enter Student Name: ")

            found = False
            for student in students:
                if student.name == student_name:
                    grade = float(input("Student Grade: "))
                    weight = float(input("Work Weight: "))

                    student.add_grade(grade, weight)
                    print(student.assignments)
                    print(student.final_grade())
                    found = True
        
            if not found:
                print("Student not found.")
        
        else:
            students_media = 0
            n_media = 0 

            for student in students:
                students_media += student.final_grade()
                n_media += 1

            print(students_media / n_media)

if __name__ == "__main__":
    main()
