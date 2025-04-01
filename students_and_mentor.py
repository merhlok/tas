from functools import total_ordering

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in (self.courses_in_progress + self.finished_courses) and 0 <= grade <= 10:
            if course in lecturer.grades_lect:
                lecturer.grades_lect[course].append(grade)
            else:
                lecturer.grades_lect[course] = [grade]
        else:
            return 'Ошибка'

    def calculate_average(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            if grades:
                total += sum(grades)
                count += len(grades)
        return total / count if count > 0 else 0.0

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.calculate_average()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        return self.calculate_average() < other.calculate_average()
    
    def __eq__(self, other):
        return self.calculate_average() == other.calculate_average()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

@total_ordering
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lect = {}

    def calculate_average(self):
        total = 0
        count = 0
        for grades in self.grades_lect.values():
            if grades:
                total += sum(grades)
                count += len(grades)
        return total / count if count > 0 else 0.0

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.calculate_average()}"

    def __lt__(self, other):
        return self.calculate_average() < other.calculate_average()
    
    def __eq__(self, other):
        return self.calculate_average() == other.calculate_average()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

def average_homework_grade(students, course_name):
    total = 0
    count = 0
    for student in students:
        if course_name in student.grades:
            total += sum(student.grades[course_name])
            count += len(student.grades[course_name])
    return total / count if count else 0

def average_lecture_grade(lecturers, course_name):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course_name in lecturer.grades_lect:
            total += sum(lecturer.grades_lect[course_name])
            count += len(lecturer.grades_lect[course_name])
    return total / count if count else 0


lecturer1 = Lecturer("Иван", "Петров")
lecturer1.courses_attached = ["Python"]
lecturer2 = Lecturer("Петр", "Иванов")
lecturer2.courses_attached = ["JS"]

student1 = Student("Ольга", "Сидорова", "ж")
student1.courses_in_progress = ["Python"]
student2 = Student("Саша", "Дюшес", "м")
student2.courses_in_progress = ["JS"]

reviewer1 = Reviewer("Алексей", "Смирнов")
reviewer1.courses_attached = ["Python"]
reviewer2 = Reviewer("Антон", "Стулов")
reviewer2.courses_attached = ["JS"]


reviewer1.rate_hw(student1, "Python", 9)
reviewer1.rate_hw(student1, "Python", 8)
reviewer2.rate_hw(student2, "JS", 7)
reviewer2.rate_hw(student2, "JS", 10)

student1.rate_lect(lecturer1, "Python", 10)
student1.rate_lect(lecturer1, "Python", 9)
student2.rate_lect(lecturer2, "JS", 8)
student2.rate_lect(lecturer2, "JS", 9)


students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print(f"Средняя оценка за ДЗ по Python: {average_homework_grade(students, 'Python')}")
print(f"Средняя оценка за лекции по JS: {average_lecture_grade(lecturers, 'JS')}")

print("\nИнформация о студентах:")
print(student1)
print(student2)

print("\nИнформация о лекторах:")
print(lecturer1)
print(lecturer2)

print("\nСравнение средних оценок:")
print("Студент1 > Лектор1:", student1 > lecturer1)
print("Студент1 == Лектор1:", student1 == lecturer1)
print("Студент2 < Лектор2:", student2 < lecturer2)