import typing as T
Numeric = T.Union[float, int]

def get_message():
    return "Hello, JPMC world"

m = get_message()
print(m)
print(get_message())

def show_message():
    msg = get_message()
    print(msg)

result = show_message()
print("result:", result)

def get_average(a: Numeric, b: Numeric) -> float:
    """
    Calculate and return the average of two numbers

    :param a: first operand
    :param b: second operand
    :return: average as a float
    """
    return (a + b) / 2

print(get_average(5, 18))
print(get_average(1, 1000))
print(get_average(6.9, 64.8))


def doit(x: Numeric, y: Numeric) -> None:
    print(f"x is {x} y is {y}")

doit(1, 2)
doit(5.3, 4.1)
doit('red', 'blue')
doit(None, False)

