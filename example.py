#Задачи на циклы и оператор условия------
#----------------------------------------


#Задача 1
#Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
n = 1
while n <= 5:
    print(n, '.', ' 0', sep='')
    n = n + 1



#Задача 2
#Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
numeral = int(input())
n = 1
m = 0
while n < 10:
    if numeral == 5:
        m = m + 1
    n = n + 1
    numeral = int(input())
print(m)



#Задача 3
#Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
sum = 0
for i in range(1,101):
    sum += i
print(sum)



#Задача 4
#Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
composition = 1
for i in range(1,11,1):
    composition *= i
print(composition)



#Задача 5
#Вывести цифры числа на каждой строчке.
integer_number = 1006
while integer_number > 0:
    print(integer_number % 10)
    integer_number = integer_number // 10



#Задача 6
#Найти сумму цифр числа.
number = 1598
sum = 0
while number > 0:
    sum = (number % 10) + sum
    number = number // 10
print(sum)



#Задача 7
#Найти произведение цифр числа.
number = 352
composition = 1
while number > 0:
    composition = (number % 10) * composition
    number = number // 10
print(composition)



#Задача 8
#Дать ответ на вопрос: есть ли среди цифр числа 5?
integer_number = 357
while integer_number > 0:
    if integer_number % 10 == 5:
        print('Yes')
        break
    integer_number = integer_number // 10
else: print('No')



#Задача 9
#Найти максимальную цифру в числе
integer_number = 1700901
n = 0
nMax = 0
while integer_number > 0:
    n = integer_number % 10
    if n >= nMax:
        nMax = n
    integer_number = integer_number // 10
print(nMax)


#Задача 10
#Найти количество цифр 5 в числе
integer_number = 75438568099542158
n = 0
while integer_number > 0:
    if integer_number % 10 == 5:
        n += 1
    integer_number = integer_number // 10
print(n)

print(n)