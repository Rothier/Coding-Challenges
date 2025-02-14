def fibonacci(i, j, limit):
    sum = 0

    if j < limit:
        if j % 2 == 0:
            sum += j
        aux = i + j
        i = j
        j = aux
        sum += fibonacci(i, j, limit)
        return sum
    else:
        return sum


print("The sum of all even numbers in the Fibonacci sequence below 40000000 equals", fibonacci(1, 2, 4000000))