distance_traveled = 0
home_flag = True
while home_flag:
    print("Would you like to walk or run?")
    user_action = input()
    if user_action == "walk":
        distance_traveled += 1
    elif user_action == "run":
        distance_traveled += 5
    elif user_action == "go home":
        home_flag = False
        print("Great job, workout is done!")
    else:
        print("Please enter a valid command.")
    print("Distance from home is {}km.".format(distance_traveled))
