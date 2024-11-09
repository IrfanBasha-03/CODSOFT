import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "win"
    else:
        return "lose"

def print_result(user_choice, computer_choice, result):
    print(f"\nYou chose {user_choice}. The computer chose {computer_choice}.")
    if result == "win":
        print("You win!")
    elif result == "lose":
        print("You lose!")
    else:
        print("It's a tie!")

def play_game():
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play.")
    
    while True:
        user_choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = get_computer_choice()
        
        result = determine_winner(user_choice, computer_choice)
        
        print_result(user_choice, computer_choice, result)
        
        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1
        
        print(f"\nCurrent Score: You: {user_score} | Computer: {computer_score}")
        
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Final scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

if __name__ == "__main__":
    play_game()
