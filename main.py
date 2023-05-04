class student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def into(self):
        print(f"Імя: {self.name}, vik: {self.age}")
student = student("vasya", 23)
student.info()