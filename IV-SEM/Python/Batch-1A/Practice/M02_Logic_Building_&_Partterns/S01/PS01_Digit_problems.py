'''
Number of Digits
N =  int(input())

count = 0
while N > 0:
    
    N = N//10
    count += 1

print(count)
'''
''' PRINT SUM OF ALL DIGITS
N = int(input())
s = 0
while N > 0:
    s  += (N%10)
    N = (N//10)
print(s)
'''
'''

def reverse(num):
    rev = 0
    while num > 0:
        rev = (rev*10) + (num % 10)
        num = num // 10
    return rev
n = reverse(int(input()))
while n>0:
    d = n%10
    if d % 2 == 0:
        print(d,end =" ")
    n = n//10
'''