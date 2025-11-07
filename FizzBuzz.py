for i in range(1, int(input("Zahlenbereich: "))):
    print(i, ":", bool(i%3==0) * "Fizz" + bool(i%5==0) * "Buzz")