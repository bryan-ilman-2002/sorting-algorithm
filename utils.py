import psutil
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


def memory_usage():
    process = psutil.Process()
    mem_info = process.memory_info()

    return mem_info.rss / (1024.0 * 1024.0)  # Convert to MB
