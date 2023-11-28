def main():
    lst = list(map(int, input("Введите элементы списка через пробел: ").split()))
    max_even = None
    for num in lst:
        if num % 2 == 0 and (max_even is None or num > max_even):
            max_even = num

    if max_even is not None:
        print(f"Наибольший четный элемент: {max_even}")
    else:
        print(f"Четных элементов нет, выводим первый элемент: {lst[0]}")

    lst.sort(key=lambda x: x < 0)
    print("Преобразованный список:", lst)

if __name__ == "__main__":
    main()