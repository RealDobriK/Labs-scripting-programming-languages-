data = dict()
n = int(input('введите кол-во эл в словаре '))
for i in range(1, n + 1):
    key = input('введите ключ: ')
    value = int(input('введите значение: '))
    data[key] = value
ascending_sorted_dict = dict(sorted(data.items(), key=lambda item: item[1]))
descending_sorted_dict = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
print("Отсортированный словарь по возрастанию значений:", ascending_sorted_dict)
print("Отсортированный словарь по убыванию значений:", descending_sorted_dict)
