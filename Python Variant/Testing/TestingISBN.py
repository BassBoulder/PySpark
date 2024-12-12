def is_valid(isbn):
    i = 10
    answer = 0

    for char in isbn:

        if char != "x" and char != "-":
            answer += int(char) * i
            i -= 1

        else:
            answer += 10

    return answer % 11 == 0


print(is_valid("3-598-21508-8"))