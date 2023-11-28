num = int(input("Введите число: "))
print("Делители числа", num, " :")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
