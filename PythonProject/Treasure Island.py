print("Welcome to the treasure Island\n Your mission is to find the treasure.")
left_or_right = input("Which way would you like to go? Left or Right? ")

if left_or_right == "Left":
    print("Game Over!")
else:
    wait_or_swim = input("Do you want to wait or swim? ")
    if wait_or_swim == "swim":
        print("game Over!")
    else:
        door = input("Which door would you like to go? Red, Blue or Yellow?")
        if door == "Red" or door == "Blue":
            print("Game Over!")
        else:
            print("You win")