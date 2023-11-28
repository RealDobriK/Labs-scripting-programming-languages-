try:
    num = int(input("Введите число: "))
    result = 10 / num
except ZeroDivisionError:
    print("Деление на ноль!")
except ValueError:
    print("Ошибка ввода числа!")
finally:
    print("Конец программы")