def score(x, y):
    powerSum = ((x ** 2) + (y ** 2)) ** 0.5
    
    if powerSum <= 1:
        return 10
    if powerSum <= 5:
        return 5
    if powerSum <= 10:
        return 1
    if powerSum > 10:
        return 0