def is_isogram(string):
    newString = string.replace(" ", "").replace("-", "").lower()
    return len(newString) == len(set(newString))