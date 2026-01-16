
# Interactive Math Quiz for Kids
import random  # This helps pick random numbers for questions
# Welcome message
print("Welcome to the Fun Math Quiz, Kiddo! 🎉")
print("We'll do 5 easy addition questions. Type your answer and press Enter.")
print("Let's go! 🚀\n")
# Set up the game
score = 0  # Start with 0 points
questions = 5  # Total questions
# Loop for 5 questions
for i in range(questions):
    # Pick two small random numbers (1 to 10)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 + num2  # The right answer
    
    # Ask the question
    print(f"Question {i+1}: What is {num1} + {num2}?")
    user_answer = int(input("Your answer: "))  # Get kid's answer
    
    # Check if correct
    if user_answer == correct_answer:
        print("Yay! That's right! 🌟 You got a star!")
        score += 1  # Add 1 point
    else:
        print(f"Oops! It's {correct_answer}. No worries, try next time! 😊")
    
    print()  # Empty line for space
# End of game

# loop for 5  questions:

for i in range(questions):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    correct_answer = num1 + num2 

    print(f"question {i+1}: what is {num1} + {num2}?")
    user_answer = int(input("your asnwer:"))

    if user_answer == correct_answer:
        print("yay! that's right! you got a star!")
        score +=1 
    else:
        print(f"oops! its {correct_answer}. no worries, try next time! ")
        
    print()




