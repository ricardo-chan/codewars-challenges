def high_and_low(numbers):
    numbers = list(map(int,numbers.split(" ")))
    print(numbers)
    return str(max(numbers)) + " " + str(min(numbers))

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))