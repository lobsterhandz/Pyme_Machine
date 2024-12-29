# Import the PyMeMachine module
from Modules.Pyme_Machine import PyMeMachine

# Task 1: Merge two dictionaries, preserving the values of common keys from the second dictionary
def task_1_merge_dicts(dict1, dict2):
    print(f"Dictionary 1: {dict1}")
    print(f"Dictionary 2: {dict2}")
    print(f"Merged dictionary: {PyMeMachine.merge_dicts(dict1, dict2)}")

# Task 2: Find the intersection of two dictionaries
def task_2_intersect_dicts(dict1, dict2):
    print(f"Dictionary 1: {dict1}")
    print(f"Dictionary 2: {dict2}")
    print(f"Intersection: {PyMeMachine.intersect_dicts(dict1, dict2)}")

# Task 3: Count the frequency of each unique word in a list using a dictionary
def task_3_word_frequency(words):
    print(f"Words list: {words}")
    print(f"Word frequencies: {PyMeMachine.word_frequency(words)}")

if __name__ == "__main__":
    # Test cases for each task
    task_1_merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    task_2_intersect_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    task_3_word_frequency(['apple', 'banana', 'apple', 'orange', 'banana', 'banana'])
