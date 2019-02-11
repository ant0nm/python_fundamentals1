distance_traveled = 0
home_flag = True
energy = 10
while home_flag:
    print("Would you like to walk or run?")
    user_action = input()
    if user_action == "walk":
        distance_traveled += 1
        energy += 2;
    elif user_action == "run" and energy > 0:
        distance_traveled += 5
        energy -= 5;
    elif user_action == "go home":
        home_flag = False
        print("Great job, workout is done!")
    elif user_action == "rest":
        energy += 10
    elif user_action == "eat":
        energy += 5
    else:
        if user_action == "run" and energy <= 0:
            print("Not enough energy to run! Take a walk, rest or eat something to replenish your energy!")
        else:
            print("Please enter a valid command.")
    print("Distance from home is {}km.".format(distance_traveled))
    print("Current energy level is {} units.".format(energy))
