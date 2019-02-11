# my secret number
secret_number = 43

# request the user to enter a number
print("Hi user, try to guess my secret number:")
guess_number_str = input()

diff = int(guess_number_str) - secret_number
if diff == 0:
    print("You win!")
elif abs(diff) == 1:
    print("So close!")
else:
    print("Try again!")
