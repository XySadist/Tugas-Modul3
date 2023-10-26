import math


def split_numbers(number):
    return {
        'ratusan': math.floor(number / 100),
        'puluhan': math.floor((number % 100) / 10),
        'satuan': number % 10
    }


def classify_numbers(numbers):
    float_numbers = []
    int_numbers = []
    string_numbers = []

    for number in numbers:
        if isinstance(number, float):
            float_numbers.append(number)
        elif isinstance(number, int):
            int_numbers.append(number)
        elif isinstance(number, str):
            string_numbers.append(number)

    return float_numbers, int_numbers, string_numbers


def classify_and_split_numbers(numbers):
    float_numbers, int_numbers, string_numbers = classify_numbers(numbers)
    int_numbers_splitted = list(map(split_numbers, int_numbers))
    return float_numbers, int_numbers_splitted, string_numbers


random_list = [3.1, 2.7, 5.5, 105, 737, 412, "Hello", "Python", "world", "AI"]

floats, ints, strings = classify_and_split_numbers(random_list)

print("Data Float:")
for f in floats:
    print(f)

print("\nData Int:")
for i in ints:
    print(i)

print("\nData String:")
for s in strings:
    print(s)
