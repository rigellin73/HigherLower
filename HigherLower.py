from random import sample
from ascii_art import logo
from participants_dictionary import participants

print(logo)

def game():
    while True:
        competitors = sample(list(participants.keys()), 2)
        winner = "B"
        if participants[competitors[0]] > participants[competitors[1]]:
            winner = "A"

        print(f"Compare A: {competitors[0]}")
        print(f"Against B: {competitors[1]}")
        player_choice = input("Who is heavier? Type 'A' or 'B': ")
        if player_choice == winner:
            print("Correct!")
        else:
            print("Nope!")
            break

game()
