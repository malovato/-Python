__author__ = 'Матвеев Александр Юрьевич'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# Решение нужно раскомментировать

# for i in range (3):
#     answer = input('Введите целое число или "exit" для выхода')
#     if answer != "exit" and answer:
#         number = int(answer)
#         while number>0:
#             print(number%10)
#             number = number // 10
#         break
#     elif answer != "exit":
#         print('Вы не ввели число!')
#     else:
#         print('До свидания!')
#         break
#     i+=1

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

# Решенние задачи 2

#
# number1 = int(input('Введите значение переменной 1'))
# number2 = int(input('Введите значение переменной 2'))
# print(" number1 = ", number1, "\n number2 = ", number2)
# number1,number2 = number2,number1
# print(" number1 = ", number1, "\n number2 = ", number2)
#

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

# Решенние задачи 3


for i in range (3):
    age = input('Введите Ваш возраст целым числом или "exit" для выхода')
    if age != "exit" and age:
        number = int(age)
        if number >= 18:
            print('Доступ разрешен')
            break
        else:
            print('Извините, пользование данным ресурсом только с 18 лет')
            break
    elif age != "exit":
        print('Вы не ввели число!')
    else:
        print('До свидания!')
        break
    i+=1