numbers = tuple(map(int, input("Введите кортеж целых чисел через пробел: ").split(' ')))
sum_positive = sum(x for x in numbers if x > 0)
print("Сумма положительных элементов:", sum_positive)