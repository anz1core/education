market = {'яблок':'5',
          'бананов':'3',
          'апельсинов':'10',
          'арбуза':'33'
}

print("За прилавком есть: ")
for idx, value in market.items():
    print(value, idx)
    
print("Взяли 2 яблока")
market['яблок'] = '3'
print("Арбузы украли")
market.pop('арбуза') #ашот украл арбузы :(
    
print("За прилавком осталось: ")
for idx, value in market.items():
    print(value, idx)