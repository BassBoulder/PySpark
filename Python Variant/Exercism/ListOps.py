def append(list1, list2):
    list1 += (list2)
    return list1

def concat(lists):
    return [x for list in lists for x in list]

def filter(function, list):
    return [x for x in list if function(x)]

def length(list):
    return sum(1 for x in list)

def map(function, list):
    return [function(x) for x in list]

def foldl(function, list, initial):
    for x in list:
        initial = function(initial, x)
    return initial

def foldr(function, list, initial):
    for x in list[::-1]:
        initial = function(initial, x)
    return initial

def reverse(list):
    return list[::-1]