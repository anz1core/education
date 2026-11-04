def format_report(report_title:str, *data: str, **properties: str) -> None:
    print(f"--- Отчет: {report_title} ---")
    if data:
        print("Данные: ")
        for item in data:
            print(f" - {item}")
    if properties:
        print("\nСвойства:")
        for key, value in properties.items():
            print(f" - {key}: {value}")
    print("-" * 30)
    
title = input("Введите название отчёта: ")

format_report(
    title,
    "Ежедневный отчет",
    "Продажи выросли на 10%",
    "Новых клиентов: 5",
    author="Сидоров А.В.",
    date="2025-11-04"
)