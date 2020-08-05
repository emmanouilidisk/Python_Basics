import random

def num_bet():
    gamble = int(input("\n Gamble in number:"))
    temp = random.randint(0,36)
    print("\n The spin resulted in... %d" %temp)
    if gamble == temp:
        outcome = True
    else:
        outcome = False
    return outcome

def col_bet():
    gamble = int(input("Select color:\n Press 1 for red \n Press 2 for black"))
    temp = random.randint(1,2)
    if temp == 1:
        color = 'red'
    else:
        color = 'black'
    print("\n The spin resulted in ..." + color)
    if gamble == temp:
        outcome = True
    else:
        outcome = False
    return outcome

def OddVsEven():
    num = int(input("Press 1 for odd and 2 for even.Select: "))
    temp = random.randint(0,36)
    if (temp % 2 == 0 and num == 2) or (temp % 2 != 0 and num == 1):
        outcome = True
    else:
        outcome = True
    return outcome

def outcome(x):
    money = 100
    if x:
        print("You won 100 Euro!!!")
        money += 100
        print("Money remaining: %d" %money)
    else:
        print("You lost...Pay 10 Euro")
        money -= 10
        print("Money remaining: %d" %money)

print("Welcome to the BIG BET!")
print("Press Enter to play!")

while(input() != ('s' or 'S')):
    print("Choose bet:\n Press 1 for a number bet \n Press 2 for a red-black")
    choice = input("Press a button:")
    if choice == '1':
        outcome(num_bet())
    elif choice == '2':
        outcome(col_bet())
    elif choice == '3':
        outcome(OddVsEvent())

    print("\nPress Enter to continue and s to exit the game")
