import random
from game_data import data
from art import logo, vs

print(logo)

def format_account(account):
    """Format the accounts and return them in string format"""
    name = account["name"]
    description = account['description']
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

game_on = True
score = 0
account_b = random.choice(data)

while game_on:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_account(account_a)}")
    print(vs)
    print(f"Against B: {format_account(account_b)}")

    guess = input("Who has more followers Type A or B ").lower()

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers, b_followers)
    if is_correct:
        score += 1
        print(f"You are right! current score: {score}")
    else:
        print(f"Sorry you are wrong, Final score: {score}")
        game_on = False
