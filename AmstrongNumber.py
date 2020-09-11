n = int(input())

l = [int(d) for d in str(n)]
x = 0

for i in l:
    x = i**3+x

if n==x:
    print('no is amstrong')
else:
    print('no is not an amstrong')

