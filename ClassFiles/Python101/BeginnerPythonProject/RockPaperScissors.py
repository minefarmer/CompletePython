import random

while True:
    my_answer = input("Choose: rock, paper, scissors: ")
    my_answer = my_answer.lower()

    if my_answer != "rock" and my_answer != "paper" and my_answer != "scissors":
        print("Please choose a correct answer")
        continue

    computer_answer = random.choice(["rock", "paper", "scissors"])
    print(f"Computer choose: {computer_answer}")

    if my_answer == computer_answer:
        print("You tied")
        continue
    elif my_answer == "paper" and computer_answer == "rock":
        print("YOU WIN!")
        break
    elif my_answer == "rock" and computer_answer == "scissors":
        print("You win!")
        break
    elif my_answer == "scissors" and computer_answer == "paper":
        print("You win!")
        break
    else:
        print("You lose. Try again!")
    


