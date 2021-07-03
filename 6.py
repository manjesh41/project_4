'''
Write a Python program to count the number of even and odd numbers from a
series of numbers.

'''
num=(10, 12, 15, 16, 17, 20, 22, 35)
n=0
m=0
for i in num:
    if i%2!=0:
        n+=1
    elif i%2==0:
        m+=1
print(f'there is {m} even number')
print(f'there is {n} odd number')

