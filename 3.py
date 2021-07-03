'''
Write a Python program to guess a number between 1 to 9.
 Note : User is prompted to enter a guess. If the user guesses wrong then the
prompt appears again until the guess is correct, on successful guess, user will
get a "Well guessed!" message, and the program will exit.

'''

for i in range(1,10):
    guess = int(input('enter the guess:'))

    if guess!=4:
        continue
    else:
        print('well guess!!')
        break



