grades = []

print("Введите 5 оценок: ")
for i in range(5):
    gr = int(input(f"{i+1} оценка: "))
    grades.append(gr)
print(f"Текущие оценки: {grades}")

grades.pop(0)
grades.pop()
mid = sum(grades) / len(grades)
print(f"Средний балл студентов: {mid}")
print(f"Итоговые оценки: {grades}")
