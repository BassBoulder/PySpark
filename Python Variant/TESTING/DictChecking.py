cart1 = {'Orange': 1}
aisleMapping1 = {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False],'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]}



def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    combinedCart = {}

    for key in cart.keys():
        combinedCart[key] = [cart[key]] + aisle_mapping[key]

    #return dict(sorted(combinedCart.items(), reverse = True))
    return combinedCart

print(send_to_store(cart1, aisleMapping1))

print(cart1[key])
print(cart1[value])