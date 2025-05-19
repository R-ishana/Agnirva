import random
# Function to check if the input is a valid number
def is_valid_number(value):
    return value.isdigit()

# Function for the game logic
def play_game():
    # Choosing Difficulty Level
    print('Welcome to the number guessing game! Please choose the difficulty level you wish to play: \n 1. Easy (1-10 number range)\n 2. Medium (1-50 number range)\n 3. Hard (1-100 number range)')
    level=int(input("Enter your choice: "))
    if level==1:
        secret_number=random.randint(1, 10)
    elif level==2:
        secret_number=random.randint(1, 50)
    elif level==3:
        secret_number=random.randint(1, 100)
    else:
        print('Please choose in the specified range')
        return

    # Choosing whether the user wants restricted attempts
    print("I have chosen a number! Do you wish to have restricted attempts? \n 1. Yes (Easy-5 Attempts, Medium-10 Attempts, Hard-15 Attempts) \n 2. No")
    level2=int(input("Enter your choice: "))

    # Unlimited Attempts
    if level2==2:
        while True:
            guess_input=input("Enter Your guess: ")
            if is_valid_number(guess_input):
                guess=int(guess_input)
                if guess>secret_number:
                    print('Too High!!')
                elif guess<secret_number:
                    print('Too Low!!')
                elif guess==secret_number:
                    print("Congratulations! You guessed Correct")
                    break
            else:
                print("Please enter a valid number")

    # Easy Level
    elif level2==1 and level==1:
        attempts=5
        for i in range(attempts):
            guess_input=input("Enter Your guess: ")
            if is_valid_number(guess_input):
                guess=int(guess_input)
                if guess>secret_number:
                    print('Too High!!')
                elif guess<secret_number:
                    print('Too Low!!')
                elif guess==secret_number:
                    print("Congratulations! You guessed Correct")
                    break
            else:
                print("Please enter a valid number")
        else:
            print(f"Oops! Your attempts are up! The number was:{secret_number}")

    # Medium Level
    elif level2==1 and level==2:
        attempts=10
        for i in range(attempts):
            guess_input=input("Enter Your guess: ")
            if is_valid_number(guess_input):
                guess=int(guess_input)
                if guess>secret_number:
                    print('Too High!!')
                elif guess<secret_number:
                    print('Too Low!!')
                elif guess==secret_number:
                    print("Congratulations! You guessed Correct")
                    break
            else:
                print("Please enter a valid number")
        else:
            print(f"Oops! Your attempts are up! The number was:{secret_number}")

    # Hard Level
    elif level2==1 and level==3:
        attempts=15
        for i in range(attempts):
            guess_input=input("Enter Your guess: ")
            if is_valid_number(guess_input):
                guess=int(guess_input)
                if guess>secret_number:
                    print('Too High!!')
                elif guess < secret_number:
                    print('Too Low!!')
                elif guess==secret_number:
                    print("Congratulations! You guessed Correct")
                    break
            else:
                print("Please enter a valid number")
        else:
            print(f"Oops! Your attempts are up! The number was:{secret_number}")

    else:
        print("Please choose in the specified range")

# Function to ask if the user wants to play again
def ask_replay():
    while True:
        replay=input("Do you want to play again? (yes/no): ").lower()
        if replay=='yes':
            return True
        elif replay=='no':
            print("Thanks for playing! Goodbye!")
            return False
        else:
            print("Please enter 'yes' or 'no'.")
# Main program loop
def main():
    while True:
        play_game()
        if ask_replay()==False:
            break
# Call the game
main()
