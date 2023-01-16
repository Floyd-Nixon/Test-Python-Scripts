def fibonacci(terms):
    fibsequence = [1, 1]
    i = 2
    while i < terms:
        oneback = fibsequence[i-1]
        twoback = fibsequence[i-2]
        current = oneback + twoback
        fibsequence.append(current)
        i += 1
    print(fibsequence)


x = int(input("How many Fibonacci terms would you like? "))
fibonacci(x)
