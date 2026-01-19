"""counter = 0
while counter < 5:
    print("hello world")
    counter += 1
    """
"""
start = int(input())
end= int(input())   
while start <= end:
    if start % 2 == 0:
        print(start, end=" ")
    start += 1
    """
'''
start = int(input())
stop = int(input())
while start <= stop:
    if start % 3 == 0 and start % 5 == 0:
        print("FizzBuzz")
    elif start % 3 == 0:
        print("Fizz")
    elif start % 5 == 0:
        print("Buzz")
    else:
        print(start)
    start += 1
'''
'''
for i in range(0,n):
    print("Hello World!")
'''
n = int(input())
for i in range(n,0,-1):
    print(i,end=" ")