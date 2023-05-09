class school:
    def __init__(self, name, students):
        self.name = name
        self.students = students
    def admit_student(self, student):
        self.students.append(student)
        print(f'{student.name} byv dodani do shkoli {self.name}')


class student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
