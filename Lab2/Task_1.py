def count_vowels_consonants(s):
    vowels = 0
    consonants = 0
    for char in s:
        if char.lower() in "aeiou":
            vowels += 1
        elif char.isalpha():
            consonants += 1
    return vowels, consonants

string = input("Введите строку: ")
v, c = count_vowels_consonants(string)
print(f"Количество гласных: {v}, количество согласных: {c}")
