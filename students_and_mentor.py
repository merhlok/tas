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
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.calculate_average()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"




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
        if isinstance(other, (Lecturer, Student)):
            return self.calculate_average() < other.calculate_average()
    def __eq__(self, other):
        if isinstance(other, (Lecturer, Student)):
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


lecturer1 = Lecturer("Иван", "Петров")
lecturer1.courses_attached = ["Python"]

student1 = Student("Ольга", "Сидорова", "ж")
student1.courses_in_progress = ["Python"]


reviewer1 = Reviewer("Алексей", "Смирнов")
reviewer1.courses_attached = ["Python"]
reviewer1.rate_hw(student1, "Python", 9)
reviewer1.rate_hw(student1, "Python", 10)


student1.rate_lect(lecturer1, "Python", 9)
student1.rate_lect(lecturer1, "Python", 10)

print(lecturer1)
print(student1)
print("Сравнение средних оценок:")
print("Студент > Лектор:", student1 >= lecturer1)
print("Студент < Лектор:", student1 <= lecturer1)