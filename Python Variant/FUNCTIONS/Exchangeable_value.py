def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
 
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    
    spread_val = (exchange_rate / 100) * spread
    exchanged_value = int(budget / (exchange_rate + spread_val))
    remove_overflow_exchanged_value = exchanged_value % denomination
    
    return exchanged_value - remove_overflow_exchanged_value