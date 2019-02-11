# request user's name
print("Hi user, what's your name?")
user_name = input()

# user's name vs. my name
# making it not case-sensitive
user_name = user_name.lower()
my_name = "anton"
if user_name == my_name:
    print("We have the same name!")
