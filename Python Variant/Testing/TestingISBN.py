def is_valid(isbn):
    i = 10
    answer = 0

    for char in isbn:

        if char != "X" and char != "-":
            answer += int(char) * i
            i -= 1

        elif char == "X":
            answer += 10 * 1
            
        else:
            return False
        
    return answer % 11 == 0

print(is_valid("3-598-21508-8"))