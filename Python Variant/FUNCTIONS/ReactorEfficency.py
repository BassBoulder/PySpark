def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """

    generated_power = voltage * current

    reactor_efficiency_value = (generated_power / theoretical_max_power) * 100

    if reactor_efficiency_value >= 80:
        return "green"
    if reactor_efficiency_value >= 60 and reactor_efficiency_value < 80:
        return "orange"
    if reactor_efficiency_value >= 30 and reactor_efficiency_value < 60:
        return "red"
    if reactor_efficiency_value < 30:
        return "black"

reactor_efficiency(1,10,100)