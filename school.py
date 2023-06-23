class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.id = id
        self.current_class = current_class

    def __repr__(self) -> str:
        return f'Student with name: {self.name}, class: {self.current_class}, id: {self.id} '

class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher: {self.name}, subject: {self.subject}'
    
class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []
    
    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'Not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'
        
    def __repr__(self) -> str:
        print('Welcome to', self.name)
        print('---------OUR TEACHER--------')
        for teacher in self.teachers:
            print(teacher)
        print('---------OUR STUDENTS--------')
        for student in self.students:
            print(student)
        return 'All Done for now'

# Roku = Student('Roko Ramin', 9, 1)
# Khalid = Teacher('Khalid Farhan', 'Alogorith', 101)

# print(Roku)
# print(Khalid)

phitron = School('Phitronik')
phitron.enroll('Zara', 5200)
phitron.enroll('Musfik', 8000)
phitron.enroll('Kabir', 7000)
phitron.enroll('Sufi', 9000)

phitron.add_teacher('Kawshik', 'Math')
phitron.add_teacher('Reza', 'CP')
phitron.add_teacher('Arif', 'SPL')

print(phitron)
