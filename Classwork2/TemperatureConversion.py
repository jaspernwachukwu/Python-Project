def celcius_to_fahrenheit(celcius: float) -> float:
    """
    Convert Celcius to Fahrenheit
    :param celcius:
    :return:
    """
    return celcius * 1.8 + 32


fahrenheit = celcius_to_fahrenheit(100)
print(fahrenheit)
