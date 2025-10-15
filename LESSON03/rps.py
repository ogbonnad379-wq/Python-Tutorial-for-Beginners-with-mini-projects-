import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def main():
    print("")
    playerchoice = input(
        "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    try:
        player = int(playerchoice)
    except ValueError:
        sys.exit("You must enter a number: 1, 2, or 3.")

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")

    # choose from list of ints to ensure we get a valid value
    computerchoice = random.choice([1, 2, 3])
    computer = int(computerchoice)

    print("")
    print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
    print("")

    if player == 1 and computer == 3:
        print("\U0001F389 You win!")
    elif player == 2 and computer == 1:
        print("\U0001F389 You win!")
    elif player == 3 and computer == 2:
        print("\U0001F389 You win!")
    elif player == computer:
        print("\U0001F632 Tie game!")
    else:
        print("\U0001F40D Python wins!")


if __name__ == '__main__':
    main()


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
playerchoice = input(
    "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")

if player == 1 and computer == 3:
    print("🎉 You win!")
elif player == 2 and computer == 1:
    print("🎉 You win!")
elif player == 3 and computer == 2:
    print("🎉 You win!")
elif player == computer:
    print("😲 Tie game!")
else:
    print("🐍 Python wins!")
