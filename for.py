# Цикл for --------------
#--------------------------

'''
# Простейший for
for i in range(10): # range(start, stop, step)
    print(i)
    if i == 5: break


answer = None
for i in range(7):
    answer = input('Какая лучшая марка автомобиля?')
    if answer == 'Volvo':
        print('Вы абсолютно правы!')
        break
'''

for i in range(10):
    if i == 9: break
    if i < 3: continue
    else: print(i)
