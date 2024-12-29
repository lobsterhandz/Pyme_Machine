# PyMe Machine - Advanced Python Operations

## Project Overview
The **PyMe Machine** module provides robust tools for advanced Python operations on lists and dictionaries. It focuses on complex tasks such as list comprehension, slicing, sorting, and dictionary manipulation. Additionally, it includes performance analysis tools to evaluate execution time and memory usage.

### Project Structure
This project is divided into two parts:
- **Advanced List Operations**
- **Advanced Dictionary Operations**

Both parts utilize the **PyMe_Machine** module, located in the `Modules` folder.

## Folder Structure
```
Project Root
│
├── Modules
│   ├── PyMe_Machine.py
│
├── advanced_list_operations.py
├── advanced_dict_operations.py
├── README.md
```

## Dependencies
Ensure Python 3.8+ is installed.

Install **pytest** for testing:
```bash
pip install pytest
```

## Module Features - PyMe Machine
The module contains the following functions:

### List Operations
- **`squares_list(n)`**  
  Generates a list of squares from 1 to n.

- **`reverse_sublist(lst, i, j)`**  
  Reverses a sublist within a list from index `i` to `j` (inclusive).

- **`merge_sorted_lists(list1, list2)`**  
  Merges two sorted lists into a single sorted list.

### Dictionary Operations
- **`merge_dicts(dict1, dict2)`**  
  Merges two dictionaries, preserving values from the second dictionary.

- **`intersect_dicts(dict1, dict2)`**  
  Finds keys common to both dictionaries with their values.

- **`word_frequency(words)`**  
  Counts the frequency of each word in a list.

### Performance Analysis
- **`analyze_function(func, *args)`**  
  Measures execution time and memory usage for any function.

## Scripts
### 1. Advanced List Operations - `advanced_list_operations.py`
Implements tasks for list comprehension, sublist reversal, and merging sorted lists.

#### Tasks:
- Generate squares of numbers from 1 to n.
- Reverse a sublist within a list.
- Merge two sorted lists into one sorted list.

**Run this script:**
```bash
python advanced_list_operations.py
```

### 2. Advanced Dictionary Operations - `advanced_dict_operations.py`
Implements tasks for merging dictionaries, finding intersections, and counting word frequencies.

#### Tasks:
- Merge two dictionaries, preserving values from the second.
- Find the intersection of two dictionaries.
- Count the frequency of each word in a list.

**Run this script:**
```bash
python advanced_dict_operations.py
```

## Testing
Unit tests are implemented using **pytest**. To run all tests:
```bash
pytest Modules/Pyme_Machine.py
```

## Examples
### List Operations
```python
from Modules.Pyme_Machine import PyMeMachine
print(PyMeMachine.squares_list(5))  # Output: [1, 4, 9, 16, 25]
print(PyMeMachine.reverse_sublist([1, 2, 3, 4], 1, 3))  # Output: [1, 4, 3, 2]
print(PyMeMachine.merge_sorted_lists([1, 3], [2, 4]))  # Output: [1, 2, 3, 4]
```

### Dictionary Operations
```python
from Modules.Pyme_Machine import PyMeMachine
print(PyMeMachine.merge_dicts({'a': 1}, {'b': 2}))  # Output: {'a': 1, 'b': 2}
print(PyMeMachine.intersect_dicts({'a': 1}, {'a': 2}))  # Output: {'a': 1}
print(PyMeMachine.word_frequency(['apple', 'banana', 'apple']))  # Output: {'apple': 2, 'banana': 1}
```

### Performance Testing
Example:
```python
from Modules.Pyme_Machine import PyMeMachine
_, time_taken, memory_used = PyMeMachine.analyze_function(PyMeMachine.squares_list, 10000)
print(f"Time Taken: {time_taken}s, Memory Used: {memory_used} bytes")
```

## Key Learnings and Goals
- Master advanced Python techniques for lists and dictionaries.
- Analyze performance implications through time and space complexity evaluation.
- Develop problem-solving and optimization skills for Python data structures.

## License
This project is open-source and available under the **MIT License**.

