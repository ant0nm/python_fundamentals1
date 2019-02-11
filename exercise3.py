# ask for the user's name
print("What is your name?")
user_name = input()
print("Hello, {}".format(user_name))

#
print("How old are you?")
age = input()
year_born = 2019 - int(age)
print("Given that you are {} years old, you must have been born in {}.".format(age, year_born))
