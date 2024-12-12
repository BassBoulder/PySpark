def is_valid(isbn):
    i = 10
    answer = 0

    for char in isbn:
        if char == "-":
            continue
            
        if char == "X":
            answer += 10 * 1
            i -= 1
            continue
            
        if char.isdigit():
            answer += int(char) * i
            i -= 1
            continue
            
        return False
        
    return i == 0 and answer % 11 == 0