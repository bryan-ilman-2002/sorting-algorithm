from bidirectional_conditional_insertion_sort import bidirectional_conditional_insertion_sort
from counting_sort import counting_sort
from utils import generate_dataset


def analyze_sorting_algorithm(arr_size):
    sorted_array, random_array, reversed_array = generate_dataset(arr_size)

    arrays = {
        'Sorted Array': sorted_array,
        'Random Array': random_array,
        'Reversed Array': reversed_array,
    }

    for name, array in arrays.items():
        print()
        print(name + ':')
        counting_sort(array)
        bidirectional_conditional_insertion_sort(array, 0, len(array) - 1)


if __name__ == '__main__':
    sizes = [500, 5_000, 50_000]

    for size in sizes:
        print()
        print(f'Array Size: {size} items')
        analyze_sorting_algorithm(size)
