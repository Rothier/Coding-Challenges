number = 20
notFound = True

while notFound:
    for i in range(1, 21):
        if number % i != 0:
            number += 1
            break
        elif i == 20 and number % i == 0:
            notFound = False
            break

print("The smallest positive number that is divisible by all numbers from 1 to 20 is", number)
