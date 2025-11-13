
print("Welcome to THE DICE GAME! \npresented by Horlicks \ncopowered by Boost")

import random

WIN = 25

def game():
    # validate number of players
    while True:
        try:
            players = int(input("Enter number of players (2-4): "))
        except ValueError:
            print("Please enter a number.")
            continue
        if 2 <= players <= 4:
            break
        print("Invalid number of players. Please enter a number between 2 and 4.")

    # collect names
    names = []
    for i in range(players):
        names.append(input(f"Enter name of player {i+1}: "))

    scores = [0] * players
    print("\nLet's start the game! First to reach 25 points wins\n")
    dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]


    current = 0
    while True:
        name = names[current]
        print(f"{name}'s turn (current score: {scores[current]})")
        input("Press Enter to roll the dice...")
        dice = random.randint(1, 6)
        print(f"You rolled a {dice} {dice_faces[dice - 1]}!")
        scores[current] += dice
        print(f"{name}'s new score: {scores[current]}\n")

        if scores[current] >= WIN:
            print(f"Congratulations {name}! You have won the game with a score of {scores[current]}!")
            return

        current = (current + 1) % players

if __name__ == "__main__":
    game()
