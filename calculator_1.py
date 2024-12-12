import logging

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        a / b
        logging.info(f"successful divide {a} / {b}")
        return a / b
    except ZeroDivisionError as err:
        logging.error("Na nol' ne delyat!!", exc_info=True)
        return 0

def sqrt(a):
    return a**0.5

def pow(a, b):
    return a**b

if __name__ == "__main__":
    print(add(100, 3))
    logging.basicConfig(level=logging.INFO, filemode='w', filename="py.log",
                        format='%(asctime)s | %(levelname)s | %(message)s')

    print(div(3, 5))
    print(div(3, 0))