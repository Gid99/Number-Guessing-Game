import random
print()
print("Welcome to the number guessing game, you will provide a range\nof numbers from which the computer will generate a random number.\nYour task is to guess the secret number in the given attempts.")
print()
print("You are given 10 attempts")
print()
def num_guess_game():
    # Storing multiple inputs with one line
    while True:
        try:
            start_num, end_num = input("Specify range by using a commas in between: ").split(",")
            break
        except ValueError:
            print("Invalid input. Please enter integers.")

    # Change the range input into an integer
    start_num = int(start_num)
    end_num = int(end_num)
    
    # Computer generates a random number
    def random_num_generator(start, end):
        random_num = random.randrange(start, end)
        return random_num
    
    # Call the random_num_generator function and store the generated number
    generated_num = random_num_generator(start_num, end_num)
    # Keep this print for testing purpose
    print(generated_num)
    
    # Create a function for the player to guess the number
    def guess_num(num_to_guess):
        count = 0
        limitAttempts = 10
        while count < limitAttempts:
            count += 1
            try:
                # Use string interpolation to indicate the range to the user
                user_guess = int(input(f"Guess a number between {start_num} and {end_num}: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue
            
            if user_guess < start_num or user_guess > end_num:
                print("Your guess is out of range")
            else:
                if user_guess == num_to_guess:
                    return count 
                elif user_guess > num_to_guess:
                    print("Your guess is too high. Guess a lower number.")
                elif user_guess < num_to_guess:
                    print("Your guess is too low. Guess a higher number.")
                  
    num_of_attempts = guess_num(generated_num)
    if (num_of_attempts):
      print("Congratulations you got it right!") 
      print("Your number of attempts was:", num_of_attempts)
      print("Game over!")
    else:
      print("Game over!")
      print("You have exhausted your given attempts")
num_guess_game()

        