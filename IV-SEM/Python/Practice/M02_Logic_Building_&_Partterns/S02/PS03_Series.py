'''
a = int(input())
d = int(input())
for i  in range(10):
    print(a + i * d,end=" ")
'''
n = int(input())
li = [0,1]
for i in range(2,n):
    li.append(li[i-2] + li[i-1])
print(li)