

def fibonacci(n):
    """
    generator to compute the first n Fibonacci numbers

    param n: total number of fibonacci numbers
    """
    a,b = 1,1

    for i in range(n):
        yield a
        a, b = b, a+b

if __name__ == '__main__':

    result = list(fibonacci(10))

    print(result)