def fibonacci(n):

    first = 0
    second = 1

    for _ in range(n):

        print(first, end=" ")

        first, second = second, first + second


fibonacci(10)