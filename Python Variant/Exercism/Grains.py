def square(number):
    if number >= 1 and number <= 64:
        if number in range(1, 65):
            return 2**(number-1)
    else:
        raise ValueError("square must be between 1 and 64")
        
def total():
    return sum(square(num) for num in range(1, 65))
