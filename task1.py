import random

def get_computer_choice():
    
    return random.choice(["rock","paper","scissors"])


def determine_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
          (user_choice == "scissors" and computer_choice == "paper") or \
          (user_choice == "paper" and computer_choice == "rock"):
          return "user"
    else:
         return "computer"
    

def display_result(user_choice, computer_choice, result):

     print(f"\nYou chose: {user_choice.capitalize()}") 
     print(f"\nComputer chose: {computer_choice.capitalize()}")

     if result == "tie":
          print("It's a Tie!")
     elif result == "user":
          print("Congratulations! You win!")


def play_game():

     user_score = 0
     computer_score = 0

     while True:
          print("\n-----Rock,Paper,Scissors-----")
          print("\n-----------------------------")
          print("\n-----------------------------")

          print("Enter your choice (rock, paper, or scissors)")
          print("Type 'exit' to quit the game.")


          user_choice = input("Your choice:").strip().lower()

          if user_choice == 'exit':
               print(f"\nFinal score : You {user_score} - {computer_score} computer")
               print("Thank you for playing! Goodbye!")
               break
          
          if user_choice not in ["rock","paper","scissors"]:
               print("Invalid choice. Please enter rock,paper, or scissors.")
               continue
          
          computer_choice = get_computer_choice()
          result = determine_winner(user_choice, computer_choice)

          if result == "user" :
             user_score +=1
          elif result == "computer":
            computer_score += 1
          
          display_result(user_choice, computer_choice, result)
          print(f"Current score : You {user_score} - {computer_score} Computer")

          play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
          if play_again not in ["yes","y"]:
               print(f"\nFinal Score: You {user_score}-{computer_score} Computer")
               print("Thank you for Playing! Goodbye! ")
               break
          

play_game()     
               
