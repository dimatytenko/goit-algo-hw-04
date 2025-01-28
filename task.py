# Python має дві вбудовані функції сортування: sorted і sort. Функції сортування Python використовують Timsort — гібридний алгоритм сортування,
#  що поєднує в собі сортування злиттям і сортування вставками.

# Порівняйте три алгоритми сортування: злиттям, вставками та Timsort за часом виконання. Аналіз повинен бути підтверджений емпіричними даними,
# отриманими шляхом тестування алгоритмів на різних наборах даних. Емпірично перевірте теоретичні оцінки складності алгоритмів, наприклад, сортуванням на великих масивах.
# Для заміру часу виконання алгоритмів використовуйте модуль timeit.


# Покажіть, що поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим, і саме з цієї причини програмісти,
# в більшості випадків, використовують вбудовані в Python алгоритми, а не кодують самі. Зробіть висновки.

# Виконано порівняльний аналіз алгоритмів за часом виконання шляхом їх тестування на різних наборах даних.
# Емпірично перевірено теоретичні оцінки складності алгоритмів та доведено, що поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим.
# Зроблено висновки щодо ефективності алгоритмів для даного випадку. Висновки оформлено у вигляді файлу readme.md до домашнього завдання.

import random
import timeit


def merge_sort(arr):
    """Сортування злиттям"""
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


def insertion_sort(arr):
    """Сортування вставками"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def generate_data(size, data_type="random"):
    """Генерація тестових даних"""
    if data_type == "sorted":
        return list(range(size))
    elif data_type == "reversed":
        return list(range(size, 0, -1))
    elif data_type == "random":
        return [random.randint(0, size) for _ in range(size)]


def test_sorting_algorithms():
    """Тестування алгоритмів"""
    sizes = [1000, 5000, 10000, 20000]  # Розміри масивів
    data_types = ["random", "sorted", "reversed"]  # Типи даних
    results = []

    for size in sizes:
        for data_type in data_types:
            data = generate_data(size, data_type)
            results.append({
                "size": size,
                "type": data_type,
                "insertion_sort": timeit.timeit(lambda: insertion_sort(data.copy()), number=1),
                "merge_sort": timeit.timeit(lambda: merge_sort(data.copy()), number=1),
                "timsort": timeit.timeit(lambda: sorted(data.copy()), number=1),
            })

    return results


# Виконання аналізу
results = test_sorting_algorithms()

# Виведення результатів
for result in results:
    print(f"Size: {result['size']}, Type: {result['type']}")
    print(f"Insertion Sort: {result['insertion_sort']:.6f}s")
    print(f"Merge Sort: {result['merge_sort']:.6f}s")
    print(f"Timsort: {result['timsort']:.6f}s\n")
