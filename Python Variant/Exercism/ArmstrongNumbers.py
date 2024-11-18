def is_armstrong_number(number):
    numMoon = 0
##root number to length of number i.e. 111 (1 1 1 ||| cubed root/3 due to length being 3 of 111)
    for digit in [int(val) for val in str(number)]:
##add those numbers together together
        numMoon += digit ** len(str(number))
##does that number == number ? True : False
    return numMoon == number