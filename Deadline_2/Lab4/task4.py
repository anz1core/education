temp = [12,15,14,14,15,15,15,10,9,6,5,3,2,1]
days_above = 0

print(f"Температуры: {temp}, \nМаксимальная: {max(temp)}°C \nМинимальная: {min(temp)}°C")

avg = sum(temp) / len(temp)
print(f"Средняя: {round(avg,1)}°C")

for i in temp:
    if i > avg:
        days_above += 1
print(f"Дней выше средней: {days_above}")
print(f"Отсортированный список: {sorted(temp)}")

farin = [round(C * 9/5 + 32, 1) for C in temp]
print(f"Список в Фарингейтах: {farin}")