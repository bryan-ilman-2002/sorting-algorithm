import random


def generate_dataset(length):
    available_values = list(range(length))

    sorted_dataset = []

    # Membuat dataset yang diurutkan
    current_index = 0
    for i in range(length):
        current_index = random.randint(current_index, len(available_values) - length + i)
        sorted_dataset.append(available_values.pop(current_index))

    random_dataset = sorted_dataset.copy()

    # Membuat dataset acak dengan menukar elemen secara acak
    for i in range(len(random_dataset)):
        j = random.randint(0, i)
        random_dataset[i], random_dataset[j] = random_dataset[j], random_dataset[i]

    half_len = len(sorted_dataset) // 2
    reversed_dataset = sorted_dataset.copy()

    # Membuat dataset terbalik dengan menukar elemen pertama dengan terakhir, kedua dengan kedua terakhir, dst.
    for i in range(half_len):
        reversed_dataset[i], reversed_dataset[-(i + 1)] = reversed_dataset[-(i + 1)], reversed_dataset[i]

    return sorted_dataset, random_dataset, reversed_dataset


def counting_sort(arr):
    # Temukan elemen maksimum dalam array masukan secara manual
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num

    # Buat array hitungan untuk menyimpan jumlah setiap elemen
    count = [0] * (max_element + 1)

    # Hitung kemunculan setiap elemen dalam array masukan
    for num in arr:
        count[num] += 1

    # Rekonstruksi array terurut
    sorted_array = []
    for i in range(max_element + 1):
        sorted_array.extend([i] * count[i])

    return sorted_array


"""
Adnan Saher Mohammed, S¸ahin Emrah Amrahov, and Fatih V C¸ elebi.
Bidirectional Conditional Insertion Sort algorithm;
An efficient progress on the classical insertion sort.
Future Generation Computer Systems, 71:102–112, 2017.
"""


def bidirectional_conditional_insertion_sort(array, left, right):
    sort_left = left
    sort_right = right

    while sort_left < sort_right:
        swap(array, sort_right, sort_left + (sort_right - sort_left) // 2)

        if array[sort_left] == array[sort_right]:
            equal_result = is_equal(array, sort_left, sort_right)
            if equal_result == -1:
                return

        if array[sort_left] > array[sort_right]:
            swap(array, sort_left, sort_right)

        i = sort_left + 1
        if (sort_right - sort_left) >= 100:
            while i <= int((sort_right - sort_left) ** 0.5):
                if array[sort_right] < array[i]:
                    swap(array, sort_right, i)
                elif array[sort_left] > array[i]:
                    swap(array, sort_left, i)

                i += 1
        else:
            i = sort_left + 1

        left_comparator = array[sort_left]
        right_comparator = array[sort_right]

        while i < sort_right:
            current_item = array[i]
            if current_item >= right_comparator:
                array[i] = array[sort_right - 1]
                insert_right(array, current_item, sort_right, right)
                sort_right -= 1
            elif current_item <= left_comparator:
                array[i] = array[sort_left + 1]
                insert_left(array, current_item, sort_left, left)
                sort_left += 1
                i += 1
            else:
                i += 1

        sort_left += 1
        sort_right -= 1


def is_equal(array, sort_left, sort_right):
    for k in range(sort_left + 1, sort_right):
        if array[k] != array[sort_left]:
            swap(array, k, sort_left)
            return k
    return -1


def insert_right(array, current_item, sort_right, right):
    j = sort_right
    while j <= right and current_item > array[j]:
        array[j - 1] = array[j]
        j += 1
    array[j - 1] = current_item


def insert_left(array, current_item, sort_left, left):
    j = sort_left
    while j >= left and current_item < array[j]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = current_item


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
