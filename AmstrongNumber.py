# Armstrong number
# Description:
#     Any number, say n is called an Armstrong number if it is equal to the sum of its digits, where each is raised to the power of number of digits in n.
#For example:
#153=13+53+33

n = int(input())

l = [int(d) for d in str(n)]
x = 0

for i in l:
    x = i**3+x

if n==x:
    print('no is amstrong')
else:
    print('no is not an amstrong')

