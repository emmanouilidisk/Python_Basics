import random
money = 100
print("Welcome to the BIG BET!")
print("Press Enter to play!")

while( input() != ('s' or 'S')):
    print("Choose bet:\n Press 1 for number bet \n Press 2 for red-black bet \n Press 3 for an odd-even bet \n")
    choice = input("Press a button:")
    if choice == '1':
        gamble = int(input("\nGamble in number:"))
        temp = random.randint(0,36)
        print("\nThe spin resulted in ... %d" %temp)
        if gamble == temp:
            outcome = True
        else:
            outcome = False

    elif choice == '2':
        gamble = int(input("Select color:\n Press 1 for red \n Press 2 for black"))
        temp = random.randint(1,2)
        if temp == 1:
            color = 'red'
        else:
            color = 'black'
        print("\nThe spin resulted in ... " + color)
        if gamble == temp:
            outcome = True
        else:
            outcome = False

    elif choice == '3':
        num = int(input("Press 1 for odd and 2 for even.Select: "))
        if((temp % 2 ==0 and num == 2)or(temp % 2 != 0 and num == 1)):
            outcome = True
        else:
            outcome = False

    if outcome:
        print("You won 100 Euro!!!")
        money += 100
        print("Money remaining: %d" %money)
    else:
        print("You lost...Pay 10 Euro")
        money -= 10
        print("Money remaining: %d" %money)
    print("\n Press Enter to continue and s to exit")
            
