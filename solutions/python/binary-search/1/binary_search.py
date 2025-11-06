def find(search_list, value):
    found = False
    empty = False
    found_at = 0
    start_index = 0
    end_index = len(search_list) - 1
    while not found and not empty and end_index >= 0:
        middle_index = start_index + (end_index - start_index) // 2
        if search_list[middle_index] == value :
            found = True
            found_at = middle_index
        elif search_list[middle_index] < value:
            start_index = middle_index + 1
        elif search_list[middle_index] > value:
            end_index = middle_index - 1
        if end_index < start_index:
             empty = True

    if not found:
        raise ValueError("value not in array")
    return found_at
