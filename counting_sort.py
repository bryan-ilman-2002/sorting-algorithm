from utils import memory_usage

import time


def counting_sort(arr):
    start_time = time.time()

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

    end_time = time.time()
    execution_time = (end_time - start_time) * 1000

    print(f"Execution Time: {execution_time:.2f} milliseconds")
    print(f"Memory Usage: {memory_usage():.2f} KB")

    return sorted_array
