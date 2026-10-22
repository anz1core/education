input()
products = {
    "Ноутбук": {"price": 50000, "sold": 15},
    "Мышь": {"price": 1000, "sold": 45},
    "Клавиатура": {"price": 2500, "sold": 30},
    "Монитор": {"price": 30000, "sold": 8}
}
max_sold = 0
earn = 0

for name, value in products.items():
    for nameof_offers, sold in value.items(): 
        if nameof_offers == 'sold' and sold > max_sold:
            max_sold = sold 
    earn = products.values()
    
print(f"Максимально продаваемый товар: {max_sold}")
print(earn)
