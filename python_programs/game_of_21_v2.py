import random

# Initialize game variables
wins = 0
losses = 0

def draw_card():
    """Function to draw a card."""
    return random.randint(2, 11)

def player_turn():
    """Function to handle the player's turn."""
    score = draw_card() + draw_card()
    print(f"Your starting score is {score}.")
    
    while True:
        choice = input("Do you want another card? (yes/no): ").strip().lower()
        if choice == "no":
            break
        if choice == "yes":
            card = draw_card()
            score += card
            print(f"You drew a {card}. Your current score is {score}.")
            if score > 21:
                print("You busted!")
                return score
    return score

def dealer_turn():
    """Function to handle the dealer's turn."""
    score = draw_card() + draw_card()
    print(f"Dealer's starting score is {score}.")
    
    while score < 16:
        card = draw_card()
        score += card
        print(f"Dealer drew a {card}. Dealer's current score is {score}.")
    if score > 21:
        print("Dealer busted!")
    return score

def play_round():
    """Function to play a single round of the game."""
    global wins, losses
    print("\nStarting a new round...")
    
    player_score = player_turn()
    if player_score > 21:
        print("You lost this round.")
        losses += 1
        return

    dealer_score = dealer_turn()
    print(f"Final scores - Player: {player_score}, Dealer: {dealer_score}")

    if dealer_score > 21 or player_score > dealer_score:
        print("You win this round!")
        wins += 1
    elif player_score < dealer_score:
        print("You lose this round.")
        losses += 1
    else:
        print("This round is a tie.")

# Main game loop
while True:
    play_round()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break

# Print final scores
print(f"\nFinal scores - Wins: {wins}, Losses: {losses}")
print("Thanks for playing!")