from random import randint

randomNumbers = []

for i in range(10):
    randomNumbers.append(randint(1,100))

for num in randomNumbers:
    print(num)

