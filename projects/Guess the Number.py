import random
print('Let me think of a number between 1 and 50!')
level = input("Choose 'easy' or 'difficult' level for game:").lower()
if level == 'easy':
    attempts = 10
else:
    attempts = 5
print(f'You have {attempts} attempts')
num = random.randint(1, 50)
for i in range(1, attempts):
    if i == 1:
        guess = int(input('Enter your guess about number I choose:'))
        if guess == num:
            print('You are right. You won!')
            break
        elif guess > num:
            print('Your guess is To o high')
        elif guess < num:
            print('Your guess is Too low')
    if i == attempts - 1:
        print(f'You are left with {attempts - i}')
        guess = int(input('Guess last time:'))
        if guess == num:
            print('You are right. You won!')
            break
        else:
            print(f'You loose number chosen by me was {num}')
    else:
        print('Guess again')
        print(f'You are left with {attempts - i}')
        guess = int(input('Enter Your Guess:'))
        if guess == num:
            print('You are right. You won!')
            break
        elif guess > num:
            print('Your guess is Too high')
        elif guess < num:
            print('Your guess is Too low')

