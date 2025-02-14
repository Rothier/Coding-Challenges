primeNumbers = [2]
i = 3

while len(primeNumbers) < 10001:
    isPrime = True
    for x in primeNumbers:
        if i % x == 0:
            isPrime = False
            break
    if isPrime:
        primeNumbers.append(i)
    i += 2

print("The 10001st prime number is", primeNumbers[-1])