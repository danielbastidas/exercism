def flatten(iterable):
    result = []

    for element in iterable:
        if element is not None:
            traverse(element, result)
    
    return result

def traverse(element, result):
    if isinstance(element, list):
        for sub_element in element:
            if sub_element is not None:
                traverse(sub_element, result)
    else:
        result.append(element)
