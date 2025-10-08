
# # Interactive Math Quiz for Kids
# import random  # This helps pick random numbers for questions
# # Welcome message
# print("Welcome to the Fun Math Quiz, Kiddo! 🎉")
# print("We'll do 5 easy addition questions. Type your answer and press Enter.")
# print("Let's go! 🚀\n")
# # Set up the game
# score = 0  # Start with 0 points
# questions = 5  # Total questions
# # Loop for 5 questions
# for i in range(questions):
#     # Pick two small random numbers (1 to 10)
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)
#     correct_answer = num1 + num2  # The right answer
    
#     # Ask the question
#     print(f"Question {i+1}: What is {num1} + {num2}?")
#     user_answer = int(input("Your answer: "))  # Get kid's answer
    
#     # Check if correct
#     if user_answer == correct_answer:
#         print("Yay! That's right! 🌟 You got a star!")
#         score += 1  # Add 1 point
#     else:
#         print(f"Oops! It's {correct_answer}. No worries, try next time! 😊")
    
#     print()  # Empty line for space
# # End of game

# # loop for 5  questions:

# for i in range(questions):
#     num1 = random.randint(1,10)
#     num2 = random.randint(1,10)
#     correct_answer = num1 + num2 

#     print(f"question {i+1}: what is {num1} + {num2}?")
#     user_answer = int(input("your asnwer:"))

#     if user_answer == correct_answer:
#         print("yay! that's right! you got a star!")
#         score +=1 
#     else:
#         print(f"oops! its {correct_answer}. no worries, try next time! ")
        
#     print()





# Interactive Math, Animals & Fruits Quiz for Kids
import random  # This helps pick random questions from categories

# Dictionary for animals and their typical colors (using animal names as keys)
animals_colors = {
    "tiger": "orange",
    "elephant": "gray",
    "flamingo": "pink",
    "penguin": "black",
    "lion": "yellow",
    "zebra": "white",
    "frog": "green",
    "polar bear": "white",
    "parrot": "green",
    "cow": "brown"  # Added one more for variety
}

# Dictionary for fruits and their typical colors (using fruit names as keys)
fruits_colors = {
    "apple": "red",
    "banana": "yellow",
    "orange": "orange",
    "grape": "purple",
    "strawberry": "red",
    "watermelon": "green",
    "lemon": "yellow",
    "blueberry": "blue",
    "cherry": "red",
    "pear": "green"
}

# List of categories
categories = ["math", "animal", "fruit"]

# Welcome message
print("Welcome to the Math, Animals & Fruits Adventure, Kiddo! 🧮🐯🍎")
print("We'll do 5 fun questions mixing math, animal names/colors, and fruit names/colors.")
print("For math: Type a number. For colors: Type the color (like 'red' or 'Red'). Press Enter.")
print("Let's learn and play! 🌟\n")

# Set up the game
score = 0  # Start with 0 points
questions = 5  # Total questions

# Loop for 5 questions
for i in range(questions):
    # Pick a random category
    category = random.choice(categories)
    
    if category == "math":
        # Math question: Simple addition
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 + num2
        print(f"Question {i+1} (Math): What is {num1} + {num2}?")
        try:
            user_answer = int(input("Your number: "))  # Expect a number
        except ValueError:
            user_answer = 0  # If not a number, treat as wrong but gentle
        if user_answer == correct_answer:
            print(f"Yay! That's right! {num1} + {num2} = {correct_answer}! 🌟 You got a star!")
            score += 1
        else:
            print(f"Oops! It's {correct_answer}. Keep practicing math! 😊")
    
    elif category == "animal":
        # Animal question: Color of animal name
        animal = random.choice(list(animals_colors.keys()))
        correct_color = animals_colors[animal]
        print(f"Question {i+1} (Animal): What color is a {animal}?")
        user_answer = input("Your color guess: ").strip().lower()
        if user_answer == correct_color:
            print(f"Yay! That's right! A {animal} is {correct_color}! 🐾 You got a star!")
            score += 1
        else:
            print(f"Oops! A {animal} is usually {correct_color}. Animals are colorful! 😊")
    
    else:  # category == "fruit"
        # Fruit question: Color of fruit name
        fruit = random.choice(list(fruits_colors.keys()))
        correct_color = fruits_colors[fruit]
        print(f"Question {i+1} (Fruit): What color is a {fruit}?")
        user_answer = input("Your color guess: ").strip().lower()
        if user_answer == correct_color:
            print(f"Yay! That's right! A {fruit} is {correct_color}! 🍒 You got a star!")
            score += 1
        else:
            print(f"Oops! A {fruit} is usually {correct_color}. Fruits are yummy colors! 😊")
    
    print()  # Empty line for space

# End of the game
print(f"Adventure over! You got {score} out of {questions} correct. Amazing job with math, animals, and fruits! 🏆")
if score == questions:
    print("Perfect score! You're a super learner in everything! ⭐⭐⭐")
elif score >= 3:
    print("Awesome! You rock at math, animals, and fruits—keep exploring! 👍")
else:
    print("Good try! Play again to master more names and colors! 💪")
