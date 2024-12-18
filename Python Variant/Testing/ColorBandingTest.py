colourDict = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}


def value(colors):
    answer = ""
    iter = 0
    
    for color in colors:
        if color in colourDict.keys() and iter < 2:
            answer += str(colourDict.get(color))
            iter += 1
    
    return int(answer)