import random


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    return random.choice(cards)


def calculate_score(cards):
    """Take a list of cards and return the score."""

    # Check for blackjack (Ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # 0 represents blackjack

    # If Ace is 11 and score > 21, convert Ace to 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    """Compare final scores and return result string."""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    print("Welcome to Blackjack!")

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        # Check for blackjack or bust
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_continue = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if user_should_continue == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer draws until score >= 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Start the game
play_game()
