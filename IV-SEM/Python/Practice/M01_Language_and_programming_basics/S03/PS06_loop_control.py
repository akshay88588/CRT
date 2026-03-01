'''
for i in range(1,11):
    if i == 5:
        continue
    print(i)
OUTPUT:1 2 3 4 5 6 7 8 9 10
'''
'''
for i in range(1,11):
    if i == 5:
        break
    print(i)
OUTPUT:1 2 3 4
'''
p1 = "aa11"
for i in range(3):
    p2=input()
    if p1 == p2:
        print("login successful")
        break
else:
    print("account locked")