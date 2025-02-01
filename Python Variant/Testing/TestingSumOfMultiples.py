def sum_of_multiples(limit, multiples):

    i = 1
    list_of_multipiles = []
    
    if any(value < 0 for value in multiples):
        raise ValueError("Need to be positive numbers only please.")

    for value in multiples:
        
        if value * i <= limit:
            
            list_of_multipiles.append(value * i)
 
        i += 1

    return list_of_multipiles

print(sum_of_multiples(10, [1,2,3]))