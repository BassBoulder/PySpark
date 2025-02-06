def sum_of_multiples(limit, multiples):

    list_of_multipiles = 0;
    
    if any(value < 0 for value in multiples):
        raise ValueError("Need to be positive numbers only please.")

    for i in range(limit):
        for j in multiples:
            if j != 0 and i % j == 0:
                list_of_multipiles += i;
                break;

    return list_of_multipiles