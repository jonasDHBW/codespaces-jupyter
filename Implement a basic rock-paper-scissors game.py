
import random



def get_user_choice():

    print("Choose Rock, Paper, or Scissors:")

    user_choice = input().capitalize()

    while user_choice not in ['Rock', 'Paper', 'Scissors']:

        print("Invalid choice. Please choose Rock, Paper, or Scissors:")

        user_choice = input().capitalize()

    return user_choice



def get_computer_choice():

    return random.choice(['Rock', 'Paper', 'Scissors'])



def determine_winner(user_choice, computer_choice):

    print(f"You chose {user_choice}.")

    print(f"Computer chose {computer_choice}.")



    if user_choice == computer_choice:

        return "It's a tie!"

    elif (

        (user_choice == 'Rock' and computer_choice == 'Scissors') or

        (user_choice == 'Paper' and computer_choice == 'Rock') or

        (user_choice == 'Scissors' and computer_choice == 'Paper')

    ):

        return "You win!"

    else:

        return "You lose!"



def main():

    print("Welcome to Rock-Paper-Scissors!")

    play_again = True



    while play_again:

        user_choice = get_user_choice()

        computer_choice = get_computer_choice()

        result = determine_winner(user_choice, computer_choice)



        print(result)

        

        print("Do you want to play again? (yes/no)")

        play_again_input = input().lower()

        play_again = play_again_input == 'yes'



    print("Thanks for playing!")



if __name__ == "__main__":

    main()



