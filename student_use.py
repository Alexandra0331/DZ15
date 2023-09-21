from student import Student

# Пример использования:
student = Student("Роман Андреевич", "subjects.csv")
student.add_score("Алгебра", 5)
student.add_test_result("Алгебра", 95)
print(student.average_test_score("Алгебра"))
print(student.average_score())