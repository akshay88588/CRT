'''
n =int(input("Enter a number: "))
for i in range(1,n//2+1):
    if n % i == 0:
        print(i,end=" ")
'''
'''
n = int(input("Enter a number:"))
counter = 0
for i  in  range(2,(n//2)+1):
    if n  % i == 0:
        counter += 1
print("prime" if counter == 0 else "not prime")
              
'''


 