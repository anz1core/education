student = [
    ("Петр", 14, 4.5),
    ("Анна", 15, 4.4),
    ("Диас", 18, 4.8),
    ("Матвей", 17, 3.6),
    ("Александр", 20, 3.0),
]
print("Студенты старше 18: ")

for name,age,score in student:
    if age > 18:
        print(f"- {name} ({age}), средний балл: {score}")
best = max(student, key=lambda s: s[2])

print(f"\nЛучший студент: {best[0]}, средний балл: {best[2]}")
sorted_student = sorted(student, key=lambda s: s[0])

print("\nОтсортированные по имени стунденты:")
for i in sorted_student:
    print(i)