# prints the first n fibonacci numbers to the console
def print_fibonacci(n):
    previous = 0
    current = 1
    for i in range(1, n + 1):
        tmp = previous
        print(current)
        previous = current
        current += tmp


print_fibonacci(5)
