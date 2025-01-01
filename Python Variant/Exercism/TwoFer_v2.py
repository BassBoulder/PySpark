def two_fer(name = "you"):
    """Returns a string with either a name, or a default of 'you'."""
    return f"One for {name}, one for me."


print(two_fer("Nick"))