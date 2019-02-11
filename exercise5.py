distance_traveled = 0
while True:
    print("Would you like to walk or run?")
    user_action = input()
    if user_action == "walk":
        distance_traveled += 1
    elif user_action == "run":
        distance_traveled += 5
    print("Distance from home is {}km.".format(distance_traveled))
