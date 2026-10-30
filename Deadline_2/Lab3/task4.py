products = {
    "Ноутбук": {"price": 50000, "sold": 15},
    "Мышь": {"price": 1000, "sold": 45},
    "Клавиатура": {"price": 2500, "sold": 30},
    "Монитор": {"price": 30000, "sold": 8}
}

max_sold = 0
max_sold_name = ""
total_revenue = 0
max_revenue = 0
max_revenue_name = ""

for name, data in products.items():
    revenue = data["price"] * data["sold"]
    total_revenue += revenue

    if data["sold"] > max_sold:
        max_sold = data["sold"]
        max_sold_name = name

    if revenue > max_revenue:
        max_revenue = revenue
        max_revenue_name = name

print(f"Самый продаваемый товар: {max_sold_name} - {max_sold} шт")
print(f"Общая выручка магазина: {total_revenue} руб")
print(f"Товар с наибольшей выручкой: {max_revenue_name} - {max_revenue} руб")