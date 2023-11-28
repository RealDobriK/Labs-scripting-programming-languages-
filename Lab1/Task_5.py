#data = dict()
#n = int(input('введите кол-во названий товаров '))
#for i in range(1, n + 1):
#    key = input('введите название товара: ')
#    price = int(input('введите цену товара: '))
#    amount = int(input('введите кол-во товара: '))
#    data[key] = (price, amount)


# Исходный словарь с информацией о продуктах в магазине
store_inventory = {
    'кружка': [10, 5],  # [цена, количество]
    'коврик': [20, 8],
    'стул': [15, 12],
    'тарелка': [25, 3],
    'подушка': [30, 7]
}

while True:
    print("\nМеню:")
    print("1. Просмотр цены")
    print("2. Просмотр количества")
    print("3. Вся информация")
    print("4. Покупка")
    print("5. До свидания")

    choice = input("Выберите пункт меню (1-5): ")

    if choice == '1':
        product_name = input("Введите название товара: ")
        if product_name in store_inventory:
            print(f"Цена {product_name}: {store_inventory[product_name][0]}")
        else:
            print("Товар не найден")

    elif choice == '2':
        product_name = input("Введите название товара: ")
        if product_name in store_inventory:
            print(f"Количество {product_name}: {store_inventory[product_name][1]}")
        else:
            print("Товар не найден")

    elif choice == '3':
        for product, info in store_inventory.items():
            print(f"{product}: Цена - {info[0]}, Количество - {info[1]}")

    elif choice == '4':
        total_cost = 0
        while True:
            product_name = input("Введите название товара (или 'выход' для выхода): ")
            if product_name.lower() == 'выход':
                break
            if product_name in store_inventory:
                quantity = int(input(f"Введите количество {product_name}: "))
                if quantity <= store_inventory[product_name][1]:
                    total_cost += quantity * store_inventory[product_name][0]
                    store_inventory[product_name][1] -= quantity
                else:
                    print("Недостаточно товара на складе.")
            else:
                print("Товар не найден")

        print(f"Общая стоимость покупок: {total_cost}")
        print("Остаток товаров на складе:")
        for product, info in store_inventory.items():
            print(f"{product}: {info[1]}")

    elif choice == '5':
        print("До свидания!")
        break

    else:
        print("Неверный ввод. Пожалуйста, выберите число от 1 до 5.")