# Оператор условия---------
#--------------------------

brand = 'Volvo'      # бренд
engine_volume = 1.5  # объем двигателя
horsepower = 110     # мощность двигателя
sunroof = False      # наличие люка



# Проверка условия

#if horsepower < 80: print('No Tax')
#else: print('Tax')



# Проверка условия if/elif/elif/else
'''
tax = 0
if horsepower < 80:
    tax = 0
elif  horsepower < 100:
    tax = 10000
elif  horsepower < 150:
    tax = 20000
else:
    tax = 50000
print(tax)

# Проверка условия if для присваивания
'''
cool_car = 0

cool_car = 1 if sunroof == 1 else 0
print(cool_car)


if sunroof == 1:
    cool_car = 1
else:
    ool_car = 0
print(cool_car)
