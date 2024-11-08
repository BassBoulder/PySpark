lista = [2, 5, 1, 7, 4, 12, 6, 3, 13] 
listb = [3, 17, 6, 15]


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.
    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """

    first, second, *theRest = each_wagons_id
    missing_wagons.append(theRest)
    missing_wagons.append(first)
    missing_wagons.append(second)

    
    return missing_wagons



fix_list_of_wagons(lista, listb)



## desired result:
## [1, 3, 17, 6, 15, 7, 4, 12, 6, 3, 13, 2, 5]