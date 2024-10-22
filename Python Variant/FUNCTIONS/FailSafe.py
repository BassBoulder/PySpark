def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    fail_safe_value = (temperature * neutrons_produced_per_second)
    
    min_threshold = threshold * 0.9
    max_threshold = threshold * 1.1
    
    if fail_safe_value < min_threshold:
        return 'LOW'
    if min_threshold <= fail_safe_value <= max_threshold:
        return 'NORMAL'
    else:
        return 'DANGER'


fail_safe(100,1,80)

