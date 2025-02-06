def square_of_sum(number):

    square_of_sum_results = 0;
    i = 1;
    for i in range(1, number + 1):
        square_of_sum_results += i;
        
    return square_of_sum_results * square_of_sum_results;


def sum_of_squares(number):

    sum_of_squares_results = 0;
    i = 1;
    for i in range(1, number + 1):
        sum_of_squares_results += i * i;
    
    return sum_of_squares_results;


def difference_of_squares(number):
    
    return square_of_sum(number) - sum_of_squares(number);
