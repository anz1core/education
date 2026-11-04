math_students = {"Alice", "Bob", "Charlie", "David"}
physics_students = {"Bob", "David", "Eve", "Frank"}
cs_students = {"Alice", "Charlie", "Eve", "Grace"}

all_three = math_students & physics_students & cs_students

only_math = math_students - physics_students - cs_students
only_physics = physics_students - math_students - cs_students
only_cs = cs_students - math_students - physics_students
only_one = only_math | only_physics | only_cs

math_not_physics = math_students - physics_students

total = math_students | physics_students | cs_students

print("Все три курса:", all_three)
print("Только один курс:", only_one)
print("Математика но не физика:", math_not_physics)
print("Всего студентов:", len(total))