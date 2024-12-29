import timeit
import sys
import pytest

class PyMeMachine:
    """
    A module providing advanced operations on Python lists and dictionaries,
    along with time and space complexity analysis.
    """

    # ---- List Operations ----

    @staticmethod
    def squares_list(n):
        """
        Generates a list of squares from 1 to n using list comprehension.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not isinstance(n, int) or n < 1:
            raise ValueError("Input must be a positive integer.")
        result = [i ** 2 for i in range(1, n + 1)]
        return result

    @staticmethod
    def reverse_sublist(lst, i, j):
        """
        Reverses a sublist from index i to j (inclusive).
        Time Complexity: O(j - i + 1) => O(k), where k is the length of the sublist.
        Space Complexity: O(1) (in-place modification)
        """
        if not isinstance(lst, list):
            raise TypeError("Input must be a list.")
        if not (0 <= i <= j < len(lst)):
            raise IndexError("Invalid indices for sublist.")
        lst[i:j + 1] = lst[i:j + 1][::-1]
        return lst

    @staticmethod
    def merge_sorted_lists(list1, list2):
        """
        Merges two sorted lists into a single sorted list.
        Time Complexity: O(n + m), where n and m are the lengths of the lists.
        Space Complexity: O(n + m) for the output list.
        """
        if not (isinstance(list1, list) and isinstance(list2, list)):
            raise TypeError("Inputs must be lists.")
        if not all(isinstance(i, (int, float)) for i in list1 + list2):
            raise ValueError("Lists must contain only numbers.")
        result = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        result.extend(list1[i:])
        result.extend(list2[j:])
        return result

    # ---- Dictionary Operations ----

    @staticmethod
    def merge_dicts(dict1, dict2):
        """
        Merges two dictionaries, preserving values from the second dictionary.
        Time Complexity: O(n + m), where n and m are the sizes of the dictionaries.
        Space Complexity: O(n + m) for the resulting dictionary.
        """
        if not (isinstance(dict1, dict) and isinstance(dict2, dict)):
            raise TypeError("Inputs must be dictionaries.")
        merged = {**dict1, **dict2}
        return merged

    @staticmethod
    def intersect_dicts(dict1, dict2):
        """
        Finds the intersection of two dictionaries.
        Time Complexity: O(min(n, m)), where n and m are the sizes of the dictionaries.
        Space Complexity: O(k), where k is the size of the intersection.
        """
        if not (isinstance(dict1, dict) and isinstance(dict2, dict)):
            raise TypeError("Inputs must be dictionaries.")
        result = {key: dict1[key] for key in dict1 if key in dict2}
        return result

    @staticmethod
    def word_frequency(words):
        """
        Counts the frequency of each unique word in a list using a dictionary.
        Time Complexity: O(n), where n is the number of words.
        Space Complexity: O(u), where u is the number of unique words.
        """
        if not isinstance(words, list):
            raise TypeError("Input must be a list of words.")
        frequency = {}
        for word in words:
            if not isinstance(word, str):
                raise ValueError("List must contain only strings.")
            frequency[word] = frequency.get(word, 0) + 1
        return frequency

    # ---- Utility Functions ----

    @staticmethod
    def analyze_function(func, *args):
        """
        Measures execution time and memory usage of a function.
        """
        start_time = timeit.default_timer()
        result = func(*args)
        end_time = timeit.default_timer()
        memory_usage = sys.getsizeof(result)
        return result, end_time - start_time, memory_usage


# ---- Pytest Unit Tests ----

def test_squares_list():
    assert PyMeMachine.squares_list(3) == [1, 4, 9]
    with pytest.raises(ValueError):
        PyMeMachine.squares_list(-1)


def test_reverse_sublist():
    assert PyMeMachine.reverse_sublist([1, 2, 3, 4, 5], 1, 3) == [1, 4, 3, 2, 5]
    with pytest.raises(IndexError):
        PyMeMachine.reverse_sublist([1, 2], 1, 3)


def test_merge_sorted_lists():
    assert PyMeMachine.merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    with pytest.raises(TypeError):
        PyMeMachine.merge_sorted_lists(123, [1, 2])


def test_merge_dicts():
    assert PyMeMachine.merge_dicts({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}
    with pytest.raises(TypeError):
        PyMeMachine.merge_dicts({'a': 1}, [1, 2])


def test_intersect_dicts():
    assert PyMeMachine.intersect_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == {'b': 2}


def test_word_frequency():
    assert PyMeMachine.word_frequency(['apple', 'banana', 'apple']) == {'apple': 2, 'banana': 1}
    with pytest.raises(TypeError):
        PyMeMachine.word_frequency('apple')
