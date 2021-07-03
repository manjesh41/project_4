'''
Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
'''
num = 6
for i in range(0,num):
    if i==3:
        continue
    elif i==6:
        continue
    print(i)