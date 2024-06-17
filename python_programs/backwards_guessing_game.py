import random

def backwards_guessing_game():
    print("Time to play Guessing Game!")
    
    low = 1
    high = 100
    attempts = 5

    for _ in range(attempts):
        if low > high:
            break
        
        guess = random.randint(low, high)
        print(f"I think the number is {guess}.")
        
        response = input("How’d I do? (High/Low/Correct): ").strip().lower()
        
        if response == "correct":
            print("Yes! I won!")
            return
        elif response == "high":
            high = guess - 1
        elif response == "low":
            low = guess + 1
        else:
            print("Invalid response. Please type 'High', 'Low', or 'Correct'.")
            continue
    
    print("Oh no! I'm sad that I didn't guess the number in 5 tries.")

# Run the game
backwards_guessing_game()