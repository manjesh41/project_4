'''
Write a Python program that accepts a string and calculate the number of
digits and letters
'''
a=input('enter the string:')
x=y=0
for i in a:
    if i.isalpha():
        x=x+1
    elif i.isdigit():
        y=y+1

print(f'there is {x} alphabet')
print(f'there is {y} digits')
