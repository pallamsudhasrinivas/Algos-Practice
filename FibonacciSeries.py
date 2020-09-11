# Fibonacci Series
# Description
# Compute and display Fibonacci series upto n terms where n is a positive integer entered by the user.

n = int(input())
list = []

def fibonacci(n):

    if (n < 0):
        print('Incorrect number')
    elif n<=1:
        return n
    else:
       return  (fibonacci(n-1)+fibonacci(n-2))

for i in range(n):
    print(fibonacci(i))




