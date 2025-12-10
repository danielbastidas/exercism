def append(list1, list2):
    appended_list = [None]*(length(list1) + length(list2))
    index = 0
    for element in list1:
        appended_list[index] = element
        index = index + 1

    for element in list2:
        appended_list[index] = element
        index = index + 1

    return appended_list

def concat(lists):
    union = []
    index = 0
    for list in lists:
        union = append(union, list)
    return union    

def filter(function, list):
    filtered_list = []
    index = 0
    for element in list:
        if function(element):
            filtered_list.insert(index, element)
            index = index + 1
    return filtered_list

def length(list):
    counter = 0
    for element in list:
        counter = counter + 1
    return counter

def map(function, list):
    mapped_list = []
    index = 0
    for element in list:
        mapped_list.insert(index, function(element))
        index = index + 1
    return mapped_list

def foldr(function, list, initial):
    return foldl(function, reverse(list), initial)

def foldl(function, list, initial):
    result = initial
    for element in list:
        result = function(result, element)
    return result

def reverse(list):
    reversed_list = []
    index = 0
    len = length(list)
    for i in range(len-1, -1, -1):
        reversed_list.insert(index, list[i])
        index = index + 1
    return reversed_list
        
