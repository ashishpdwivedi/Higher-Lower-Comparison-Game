# TODO Comparision Game :

# Display Art

from art import logo, vs
from game_data import data
import random

# format the account data into printable data
def format_data(account):
    """Take Account data and return a printable formatted string"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_description}, from {account_country}")


def check_answer(user_guess, a_follower, b_follower):
    """Take User Guess and the follower count and return if they are right or wrong """
    if a_follower > b_follower:
        return guess =="a"
    else:
        return guess =="b"

print(logo)
print("Welcome to the Higher Or Lower Board Game")
score = 0
game_should_continue = True
account_b = random.choice(data)

# make the guess repeatable
while game_should_continue:
    # Generate the random amount from game data
    # making the accout b to next position at account A.
    account_a = account_b

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Compare B : {format_data(account_b)}")




    # Ask user to guess
    guess = input("Guess Who have More Follower A or B : ").lower()

    # Clear the Screen after each guesses
    print("\n"*20)
    print(logo)
    # Check if user is correct


    ## Get follower count of each acount
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower, b_follower)
    ## Use if statement to to check if user is correct.

    if is_correct:
        # score keeping
        score += 1
        # Give the feedback on thier guess
        print(f" You are Right! Current Score: {score}")
    else:
        # Give the feedback on thier guess
        print(f" You are Wrong. Final Score: {score}")
        game_should_continue = False










