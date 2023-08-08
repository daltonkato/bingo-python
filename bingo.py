import random
import string
import os
import sys

def main():

    # Color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

    # Style codes
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


    os.system("clear")
    print(BOLD + "\n\nWelcome to Bingo!\n\n" + RESET)
    
    numbers = random.sample(range(1, 76), 75)
    numbers_called = []

    for x in range (0, 75):
        if (numbers[x] > 0 and numbers[x] < 16):
            letter = "B"
        elif numbers[x] > 15 and numbers[x] < 31:
            letter = "I"
        elif numbers[x] > 30 and numbers[x] < 46:
            letter = "N"
        elif numbers[x] > 45 and numbers[x] < 61:
            letter = "G"
        elif numbers[x] > 60:
            letter = "O"

        print ("\n\n *** SEQUENTIAL NR => ", x+1, " **** ",BOLD, "Letter ==> " ,GREEN,  letter, RESET, BOLD, "==> NUMBER ==> ",GREEN,  numbers[x] , RESET, BOLD ,"<==")

        numbers_called.append(numbers[x])
        numbers_called.sort()
        print (BOLD, "\n\nNumbers Called! => ",RESET, numbers_called)
        input("\n\nPress Enter to continue...or CRTL+C to finish...")
        os.system("clear")
        if (x < 74):
            print(BOLD + "\n\nWelcome to Bingo!\n\n" + RESET)
        else:
            print(BOLD + "\n\nWelcome to Bingo!\n\n" + RESET)
            print ("\n\n *** SEQUENTIAL NR => ", x+1, " **** ",BOLD, "Letter ==> " ,GREEN,  letter, RESET, BOLD, "==> NUMBER ==> ",GREEN,  numbers[x] , RESET, BOLD ,"<==")
            print (BOLD, "\n\nNumbers Called! => ",RESET, numbers_called)
            print (BOLD, "\n\nThanks for play BINGO!!!\n\n")
            
if __name__ == "__main__":
    main()