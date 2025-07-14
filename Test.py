
dict_list = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30}
]
key= "age"

def sort_dicts_by_key(dict_list, key):
    """
    Sorts a list of dictionaries by the specified key.

    Args:
        dict_list (list): List of dictionaries to sort.
        key (str): The key to sort by.

    Returns:
        list: Sorted list of dictionaries.
    """
    print(sort_dicts_by_key(dict_list, key))
    return sorted(dict_list, key=lambda d: d.get(key))
