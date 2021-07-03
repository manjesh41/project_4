'''
. Write a program to find the factorial of a number
'''
num=int(input('Enter the number:'))
factorial=1
if num<0:
    print('error')
elif num==0:
    print('the factoral of 0 s 1')
else:
    for i in range(1,num+1):
        factorial*=i
    print(f'The factorial of  {num} is {factorial}')