def count_non_zero_columns(matrix):
    non_zero_columns = 0
    for col in zip(*matrix):
        if 0 not in col:
            non_zero_columns += 1
    return non_zero_columns

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Введите элемент на позиции ({i+1},{j+1}): "))
        row.append(element)
    matrix.append(row)

# Выводим матрицу
print("Введенная матрица:")
for row in matrix:
    print(row)
print(f"Количество столбцов без нулевых элементов: {count_non_zero_columns(matrix)}")