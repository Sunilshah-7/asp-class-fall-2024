# from the fibonacci series, return the nth number in the series and print out the result in decimal, binary, and hex
n = int(input("Enter the nth number in the fibonacci series: "))

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
result = fib(n)
print(f"The {n}th number in the fibonacci series is {result}")
print(f"Decimal: {result}")
print(f"Binary: {bin(result)}")
print(f"Hex: {hex(result)}")

