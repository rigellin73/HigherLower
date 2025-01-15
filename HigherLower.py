from random import shuffle
from ascii_art import logo
from animal_weights_dictionary import animal_weights_dict

print(logo)

def game():
    score = 0
    animals = list(animal_weights_dict.keys())
    shuffle(animals)
    first_animal = animals.pop()
    while animals:
        second_animal = animals.pop()
        winner = "B"
        if animal_weights_dict[first_animal] > animal_weights_dict[second_animal]:
            winner = "A"

        print(f"Compare A: {first_animal}")
        print(f"Against B: {second_animal}")
        player_choice = input("Who is heavier? Type 'A' or 'B': ")
        if player_choice == winner:
            print("Correct!")
            score += 1
            first_animal = second_animal
            print(f"Your current score is: {score}")
        else:
            print(f"Nope!")
            break
    print(f"Your final score is: {score}")

game()
