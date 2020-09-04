class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.id = self.name[0] + self.last_name + self.birth_year


student_name = input()
student_last = input()
student_birth = input()

new_student = Student(student_name, student_last, student_birth)
print(new_student.id)