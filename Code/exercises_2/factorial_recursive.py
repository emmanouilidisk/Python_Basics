def recur_factorial(n):
    if n < 0 :
        print("Factorial doesn’t exist for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * recur_factorial(n-1)

