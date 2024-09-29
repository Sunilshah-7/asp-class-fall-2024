import random

#function to generate a fibonacci number less than the divisor
def fib_less(divisor):
    fib_sequence = []
    a, b = 0, 1
    while a < divisor:
        fib_sequence.append(a)
        a, b = b, a + b
     
    return fib_sequence

#loop guarded command function
def lgc(x, y, z):
    if x == y:
        raise ValueError("The first two values cannot be equal")
    # ensure range is in ascending order
    if x > y:
        x, y = y, x
    
    #generating boolean expressions for divisibility from x to y
    commands = []
    for divisor in range(x, y+1):
        if z % divisor == 0:
            commands.append((f"z % {divisor} == 0", fib_less(divisor)))

    #if no commands are added, throw an error
    if not commands:
        raise RuntimeError("No divisibility commands were satisfied.")
    
    #randomly select a command
    command = random.choice(commands)
    #return the result of the command
    return command


def main():
    try:
        #ask for 3 input from user which should be a number
        x = int(input("Enter the first non zero positive number: "))
        y = int(input("Enter the second non zero positive number: "))
        z = int(input("Enter the third non zero positive number: "))
        # validate if the inputs are non zero positive numbers, if not raise an error
        if x <= 0 or y <= 0 or z <= 0:
            raise ValueError("Please enter a non zero positive number")
        # call the function lgc with the 3 inputs
        result = lgc(x, y, z)
        # print the result
        print(f'For {result[0]}, the fibonacci numbers are {result[1]}')
    except ValueError as e:
        print(f"Input error: {e}")
    except RuntimeError as e:
        print(f"Runtime error: {e}")

main()