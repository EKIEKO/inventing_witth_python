#guess the number
import random
tries = 6
number = random.randint(1, 20)
while tries > 0:
    guess = input('What number do you think it is?')
    guess = int(guess)
    if guess < number:
        tries = tries -1
        if tries == 0:
            print('You did not manage to guess the number. You fail.')
            break
        print('Too low try again')
        print('tries left', tries)
    elif guess > number:
        tries = tries -1
        if tries == 0:
            print('You did not manage to guess the number. You fail.')
            break
        print('Too high try again')
        print('tries left', tries)
    else:
        print('Correct! The answer is', str(number) + '!')
        print()
        PlayAgain = input('Do you want to play again? Yes or no?')
        PlayAgain = PlayAgain.lower()
        if PlayAgain == 'yes':
            tries = 6
            number = random.randint(1, 20)
            print('New number selected')
            print()
            print()
        elif PlayAgain == 'no':
            print()
            print('Program terminated')
            break
