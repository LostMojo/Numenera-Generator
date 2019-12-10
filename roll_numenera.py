import random

def roll(add=0):
    #A quick function to roll a d20 and add the modifier
    return random.randint(1,20) + add

def get_difficulty(level=1, mod=0):
    #finds the target number using Numenera Rules
    return (level-mod)*3

def check_roll(level=1, mod=0, add=0):
    #checks whether a Numenera roll suceeds
    #returns a tuple of sucess status and raw roll
    result = roll()
    return (get_difficulty(level, mod) < result+add, result)

def print_roll_results(level=1, mod=0, add=0):
    #a function to roll and tell you results
    #returns a tuple of success and the die roll
    success, result = check_roll(level, mod, add)
    if result == 1:
        print("Major Failure! Free DM intrusion.")
    elif result == 20:
        print("Major Crit!")
    elif result == 19:
        print("Minor Crit!")
    if success:
        print("You succeed with a {}.".format(result))
        return (success, result)
    else:
        print("You failed with a {}".format(result))
        return (success, result)