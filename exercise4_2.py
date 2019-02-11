# request user's age
print("Hi user, please enter your age:")
age_str = input()

# my age vs. user's age
user_age = int(age_str)
my_age = 25

if my_age > user_age:
    print("I am {} year(s) older than you.".format(my_age - user_age))
elif my_age == user_age:
    print("We are the same age.")
elif my_age < user_age:
    print("I am {} year(s) younger than you.".format(user_age - my_age))

if user_age > 105:
    print("I'm not sure I believe you.")
