from random import shuffle
from ascii_art import logo
from game_data import data

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

def get_output_str(item):
    return f"{item['name']}, {item['description']}, from {item['country']}"

def game():
    print_logo()
    score = 0
    shuffle(data)
    first_item = data.pop()
    player_won = True
    while data:
        second_item = data.pop()
        winner = "B"
        if first_item['follower_count'] > second_item['follower_count']:
            winner = "A"

        print(f"Compare A: {get_output_str(first_item)}")
        print(f"Against B: {get_output_str(second_item)}")
        player_choice = input("Who has more followers? Type 'A' or 'B': ")
        if player_choice == winner:
            score += 1
            first_item = second_item
            print_intermediate_result(score)
        else:
            player_won = False
            break
    print_logo()
    print_result(player_won, score)

game()
