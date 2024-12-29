# Import the PyMeMachine module
from Modules.Pyme_Machine import PyMeMachine

# Task 1: List comprehension to generate squares of numbers from 1 to n
def task_1_squares_list(n):
    print(f"Squares from 1 to {n}: {PyMeMachine.squares_list(n)}")

# Task 2: Reverse a sublist within a list from index i to j (inclusive)
def task_2_reverse_sublist(lst, i, j):
    try:
        print(f"Original list: {lst}")
        print(f"Reversed sublist ({i}-{j}): {PyMeMachine.reverse_sublist(lst, i, j)}")
    except Exception as e:
        print(f"Error: {e}")

# Task 3: Merge two sorted lists into a single sorted list
def task_3_merge_sorted_lists(list1, list2):
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print(f"Merged and sorted: {PyMeMachine.merge_sorted_lists(list1, list2)}")

if __name__ == "__main__":
    # Test cases for each task
    task_1_squares_list(10)
    task_2_reverse_sublist([1, 2, 3, 4, 5], 1, 3)
    task_3_merge_sorted_lists([1, 3, 5], [2, 4, 6])
