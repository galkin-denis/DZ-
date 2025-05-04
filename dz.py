class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturer(self,lecturer, course, grade):
        if isinstance(lecturer,Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def avg_grades(self):
        count = 0
        len_grades = 0
        if len(self.grades) != 0:
            for k, v in self.grades.items():
                for i in v:
                    count += i
                    len_grades += 1
            return count / len_grades
        return f'Нет оценок'

    def __eq__(self, other):
        return self.avg_grades() == other.avg_grades()

    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avg_grades()} '
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def avg_grades(self):
        count = 0
        len_grades = 0
        if len(self.grades) != 0:
            for k, v in self.grades.items():
                for i in v:
                    count += i
                    len_grades += 1
            return count / len_grades
        return f'Нет оценок'
    def __eq__(self, other):
        return self.avg_grades() == other.avg_grades()

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grades()}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'




student_1 = Student('Ruoy', 'Eman', 'male')
student_2 = Student('John', 'Brown', 'male')
student_1.courses_in_progress += ['Python']
student_2.courses_in_progress += ['C++']
student_2.courses_in_progress += ['Python']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
lecturer_1 = Lecturer('Gimli', 'Dwarf')
lecturer_1.courses_attached += ['Python']


student_1.rate_lecturer(lecturer_1, 'Python', 10)

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_2, 'Python', 7)



def avg_grade_students(students, course):
    grades = []
    for student in students:
        if course in student.courses_in_progress:
            for i in student.grades[course]:
                grades.append(i)
    return sum(grades) / len(grades)
def avg_grade_lecturers(lecturers, course):
    grades = []
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            for i in lecturer.grades[course]:
                grades.append(i)
    return sum(grades) / len(grades)


print(avg_grade_lecturers([lecturer_1], 'Python'))
