from bidirectional_conditional_insertion_sort import bidirectional_conditional_insertion_sort
from counting_sort import counting_sort
from utils import generate_dataset


if __name__ == '__main__':
    sorted_array, random_array, reversed_array = generate_dataset(50_000)

    counting_sort(random_array)

    bidirectional_conditional_insertion_sort(random_array, 0, len(random_array) - 1)
