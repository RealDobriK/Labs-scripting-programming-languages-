def process_input(data):
    if isinstance(data, dict):
        top_keys = sorted(data, key=data.get, reverse=True)[:3]
        return f"Три ключа с самыми большими значениями: {top_keys}"
    elif isinstance(data, list):
        evens = sum(1 for num in data if num % 2 == 0)
        unique_elements = list(set(data))
        return f"Количество четных чисел: {evens}, Уникальные элементы: {unique_elements}"
    elif isinstance(data, int):
        digit_sum = sum(int(digit) for digit in str(data))
        return f"Сумма цифр: {digit_sum}"
    elif isinstance(data, str):
        cleaned_string = ' '.join(word.strip(".,!?") for word in data.split())
        word_count = len(cleaned_string.split())
        return f"Очищенная строка: {cleaned_string}, Количество слов: {word_count}"
    else:
        return "Неподдерживаемый тип данных"

input_data = eval(input("Введите данные (словарь, список, число или строку): "))
print(process_input(input_data))
