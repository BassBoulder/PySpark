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

    if ((temperature * neutrons_produced_per_second) / threshold) < 90:
        return 'LOW'
    if 0 > ((temperature * neutrons_produced_per_second) / threshold) < 10:
        return 'NORMAL'
    if ((temperature * neutrons_produced_per_second) / threshold) < 0:
        return 'DANGER'

fail_safe(100,1,80)