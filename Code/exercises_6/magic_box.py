import random
import time
import sys
answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
 	 "As I see it, yes", "Most Likely", "Outlook Good",
 	 "Yes", "Signs point to yes",  
  	 "Better not to tell you now", "Cannot predict now", "Concentrate and ask again",
   	 "Don't count on it", "My reply is no", "My sources say no", "Obviously no", "Very Doubtful"]

# Magic Box Graphics
print('  __  __          _____ _____ _____  ______    ___  __    __  ')
print(' |  \/  |   /\   / ____|_   _/ ____| |     |  /   \ \ \  / /  ')
print(' | \  / |  /  \ | |  __  | || |      |  ___| |     | \ \/ /   ')
print(' | |\/| | / /\ \| | |_ | | || |      | |___  |     |  \ \/    ')
print(' | |  | |/ ____ \ |__| |_| || |____  |     | |     |  /\ \    ')
print(' |_|  |_/_/    \_\_____|_____\_____| |_____|  \___/  /_/\_\   ')
print('')
print('')
print('')

name = input('Hello world! I am the Magic Box, what is your name?')
print('hello ' + name)
          
def MagicBox():
    question()
    Replay()
           
def question():
    question = input("You may ask your yes/no question \n")
    print("Thinking...")
    time.sleep(random.randrange(0,4))
    print(answers[random.randint(0, len(answers)-1)])
    print("I hope that helped!")

def Replay():
    reply = input("Do you have another question? [Y/N]")
    if reply == 'Y' or reply == 'y':
        MagicBox()
    elif reply == 'N' or reply == 'n':
          sys.exit()
    else:
          print("I apologize I did not catch that. Please repeat")
          Replay()

MagicBox()
