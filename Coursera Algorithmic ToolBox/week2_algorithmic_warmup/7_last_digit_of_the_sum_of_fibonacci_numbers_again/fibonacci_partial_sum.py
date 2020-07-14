# Python3 program to calculate 
# Last Digit of the sum of the 
# Fibonacci numbers from M to N 

# Calculate the sum of the first 
# N Fibonacci numbers using Pisano 
# period 
import sys
def fib(n): 

    # The first two Fibonacci numbers 
    f0 = 0
    f1 = 1

    # Base case 
    if (n == 0): 
        return 0
    if (n == 1): 
        return 1
    else: 

        # Pisano Period for % 10 is 60 
        rem = n % 60

        # Checking the remainder 
        if(rem == 0): 
            return 0

        # The loop will range from 2 to 
        # two terms after the remainder 
        for i in range(2, rem + 3): 
            f =(f0 + f1)% 60
            f0 = f1 
            f1 = f 

        s = f1-1
        return(s) 

# Driver code 
if __name__ == '__main__': 

    input = sys.stdin.read();
    m, n = map(int, input.split())    
    final = fib(n)-fib(m-1) 
    print(final % 10) 
