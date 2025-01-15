from random import sample
from ascii_art import logo
from animal_weights_dictionary import animal_weights_dict

print(logo)

def game():
    score = 0
    while True:
        competitors = sample(list(animal_weights_dict.keys()), 2)
        winner = "B"
        if animal_weights_dict[competitors[0]] > animal_weights_dict[competitors[1]]:
            winner = "A"

        print(f"Compare A: {competitors[0]}")
        print(f"Against B: {competitors[1]}")
        player_choice = input("Who is heavier? Type 'A' or 'B': ")
        if player_choice == winner:
            print("Correct!")
            score += 1
        else:
            print(f"Nope! Your score is: {score}")
            break

game()
