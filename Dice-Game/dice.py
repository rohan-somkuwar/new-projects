import random
again = True
while again:
    print(random.randint(1,8))
    another_roll = input("Want to roll dice again? :(y/n)")

    if another_roll.lower() =="y":
        continue
    else:
        break