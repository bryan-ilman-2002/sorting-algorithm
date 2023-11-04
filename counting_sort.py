from utils import memory_usage

import time


def counting_sort(arr):
    print()

    before_memory = memory_usage()
    start_time = time.perf_counter()

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

    end_time = time.perf_counter()
    after_memory = memory_usage()

    execution_time = (end_time - start_time) * 1000

    print('Counting Sort')
    print(f"Execution Time: {execution_time:.4f} milliseconds")
    print(f"Extra Space: {after_memory - before_memory:.4f} MB")

    return sorted_array
