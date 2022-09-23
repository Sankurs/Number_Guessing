import random

computer_guessed_number = random.randint(1, 100)
continue_game = True
user_guesses = []

while(continue_game):
    user_guess = int(input("Guess the number between 1 and 100: "))
    user_guesses.append(user_guess)

    if user_guess == computer_guessed_number:
        print('You win!')
        continue_game = False
    elif user_guess < computer_guessed_number:
        print('Number is higher!')
    elif user_guess > computer_guessed_number:
        print('Number is lower!')
    else:
        print('Error!')

sum_of_difference = 0
for n in user_guesses:
    sum_of_difference += abs(n - computer_guessed_number)
ave_of_difference = sum_of_difference / len(user_guesses)



print('Game over!')
print(user_guesses)
print(f'average difference was: {ave_of_difference}')
