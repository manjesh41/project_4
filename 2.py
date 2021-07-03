'''
Write a Python program to convert temperatures to and from celsius, fahrenheit.C = (5/9) * (F -32)3
'''
temp=int(input('enter the temperature:'))
unit=input('enter the unit(C,F):').lower()
if unit=='f':
    c= (5 / 9) * (temp- 32)
    print(f'the temperature in celcious is {c}')
elif unit=='c':
    f=(9/5)*temp+32
    print(f'the temperature in foreignheight {f}')
else:
    print('error')