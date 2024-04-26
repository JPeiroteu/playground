import unittest
from grades import Student, Work

class TestStudent(unittest.TestCase):

    def test_add_grade(self):
        student = Student("John")
        student.add_grade(85, 0.5)
        self.assertEqual(len(student.assignments), 1)  # Corrigido para assignments
        self.assertEqual(student.assignments[0].grade, 85)
        self.assertEqual(student.assignments[0].weight, 0.5)

    def test_final_grade(self):
        student = Student("Alice")
        student.add_grade(90, 0.3)
        student.add_grade(80, 0.7)
        self.assertEqual(student.final_grade(), 83)  # Calculated manually

class TestWork(unittest.TestCase):

    def test_work_attributes(self):
        work = Work(75, 0.4)
        self.assertEqual(work.grade, 75)
        self.assertEqual(work.weight, 0.4)

if __name__ == '__main__':
    unittest.main()
