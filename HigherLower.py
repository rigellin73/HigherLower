from random import shuffle
from ascii_art import logo
from animal_weights_dictionary import animal_weights_dict

def print_logo():
    print("\n" * 20)
    print(logo)

def print_intermediate_result(current_score):
    print_logo()
    print(f"You right! Your current score is: {current_score}")

def print_result(has_won, final_score):
    if has_won:
        print("Congratulations! You guessed all.")
    else:
        print("Sorry, that's wrong.")
    print(f"Your final score is: {final_score}")

def game():
    print_logo()
    score = 0
    animals = list(animal_weights_dict.keys())
    shuffle(animals)
    first_animal = animals.pop()
    player_won = True
    while animals:
        second_animal = animals.pop()
        winner = "B"
        if animal_weights_dict[first_animal] > animal_weights_dict[second_animal]:
            winner = "A"

        print(f"Compare A: {first_animal}")
        print(f"Against B: {second_animal}")
        player_choice = input("Who is heavier? Type 'A' or 'B': ")
        if player_choice == winner:
            score += 1
            first_animal = second_animal
            print_intermediate_result(score)
        else:
            player_won = False
            break
    print_logo()
    print_result(player_won, score)

game()
