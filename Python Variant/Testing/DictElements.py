my_list = ["Dog","Cat", "Cat", "Cat", "Dog"]
my_other_list = ["Dog","Dog","Dog"]

from collections import Counter

my_dict = Counter(my_list)
my_other_dict = Counter(my_other_list)
dict_subtract_other_dict = my_dict.subtract(my_other_dict)

#print (my_dict - my_other_dict)
dict_subtract_other_dict