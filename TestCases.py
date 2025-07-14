import pytest
"""
Sorts a list of dictionaries by the specified key.
If a dictionary is missing the specified key, its value is treated as None,
and such dictionaries will be sorted before those with actual values for the key.
Args:
    dicts (list of dict): The list of dictionaries to sort.
    key (str): The key to sort the dictionaries by.
Returns:
    list of dict: The sorted list of dictionaries.
"""

def sort_dicts_by_key(dicts, key):
    # Sorts list of dicts by the given key, treating missing keys as None
    return sorted(dicts, key=lambda d: d.get(key, None))

def test_sort_dicts_by_key_basic():
    dicts = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    sorted_dicts = sort_dicts_by_key(dicts, 'age')
    assert [d['name'] for d in sorted_dicts] == ['Bob', 'Alice', 'Charlie']

def test_sort_dicts_by_key_missing_key():
    dicts = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob'},
        {'name': 'Charlie', 'age': 35}
    ]
    sorted_dicts = sort_dicts_by_key(dicts, 'age')
    # Bob has no 'age', so should be first (None sorts before int)
    assert [d['name'] for d in sorted_dicts] == ['Bob', 'Alice', 'Charlie']

def test_sort_dicts_by_key_empty_list():
    assert sort_dicts_by_key([], 'age') == []

def test_sort_dicts_by_key_key_not_present_in_any():
    dicts = [
        {'name': 'Alice'},
        {'name': 'Bob'},
        {'name': 'Charlie'}
    ]
    sorted_dicts = sort_dicts_by_key(dicts, 'age')
    # All have None for 'age', so order should be preserved
    assert [d['name'] for d in sorted_dicts] == ['Alice', 'Bob', 'Charlie']

def test_sort_dicts_by_key_with_negative_and_zero():
    dicts = [
        {'name': 'Alice', 'score': 0},
        {'name': 'Bob', 'score': -5},
        {'name': 'Charlie', 'score': 10}
    ]
    sorted_dicts = sort_dicts_by_key(dicts, 'score')
    assert [d['name'] for d in sorted_dicts] == ['Bob', 'Alice', 'Charlie']