class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            print('Miejsca zapełnione')

    def avg_grade(self):
        var = 0
        for i in range(len(self.students)):
            var += self.students[i].grade
        return var / len(self.students)



s1 = Student('Janek', 19, 95)
s2 = Student('Kuba', 21, 80)
s3 = Student('Bill', 30, 67)

Nauka_programowanie = Course('Nauka programowania', 2)
Nauka_programowanie.add_student(s1)
Nauka_programowanie.add_student(s2)
# Nauka_programowanie.add_student(s3)

print(Nauka_programowanie.avg_grade())

