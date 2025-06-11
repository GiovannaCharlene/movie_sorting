
def multisort(data, sort_keys):
    """
    Sort a list of dictionaries based on multiple keys.

    Parameters:
        data (list): List of dictionaries to be sorted.
        sort_keys (list of tuples): Each tuple contains (key_name, reverse).

    Returns:
        list: Sorted list of dictionaries.
    """
    if not isinstance(data, list):
        raise ValueError("Data must be a list.")

    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Each item in data must be a dictionary.")

    if not isinstance(sort_keys, list):
        raise ValueError("sort_keys must be a list of (key, reverse) tuples.")

    for key, reverse in reversed(sort_keys):
        if not isinstance(key, str) or not isinstance(reverse, bool):
            raise ValueError("Each sort key must be a (str, bool) pair.")
        data.sort(key=lambda x: x.get(key, ""), reverse=reverse)

    return data