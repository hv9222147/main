# # Interactive Learning Program for Kids

# print("🎉 Welcome to the Interactive Learning Program for Kids 🎉")
# print("Answer the questions and learn with fun!\n")

# score = 0

# # Question 1
# print("Q1. What is the capital of India?")
# print("a) Mumbai")
# print("b) Delhi")
# print("c) Kolkata")

# ans1 = input("Enter your answer (a/b/c): ")

# if ans1 == "b":
#     print("✅ Correct Answer!\n")
#     score += 1
# else:
#     print("❌ Wrong Answer! Correct answer is Delhi.\n")

# # Question 2
# print("Q2. 5 + 3 = ?")
# print("a) 6")
# print("b) 7")
# print("c) 8")

# ans2 = input("Enter your answer (a/b/c): ")

# if ans2 == "c":
#     print("✅ Correct Answer!\n")
#     score += 1
# else:
#     print("❌ Wrong Answer! Correct answer is 8.\n")

# # Question 3
# print("Q3. Which animal is called the King of Jungle?")
# print("a) Tiger")
# print("b) Elephant")
# print("c) Lion")

# ans3 = input("Enter your answer (a/b/c): ")

# if ans3 == "c":
#     print("✅ Correct Answer!\n")
#     score += 1
# else:
#     print("❌ Wrong Answer! Correct answer is Lion.\n")

# # Final Score
# print("🎯 Quiz Completed!")
# print("Your Score:", score, "/ 3")

# if score == 3:
#     print("🌟 Excellent! You are very smart!")
# elif score == 2:
#     print("👍 Good Job! Keep learning!")
# else:
#     print("😊 Nice try! Practice more and learn!")

# print("\nThank you for playing 💖")





import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-'])
    
    if operation == '-' and num1 < num2:
        num1, num2 = num2, num1  # Ensure positive results
    
    question = f"{num1} {operation} {num2}"
    answer = eval(question)  # Calculate the correct answer
    return question, answer

def main():
    print("Welcome to the Interactive Learning Program for Kids!")
    name = input("What's your name? ")
    try:
        age = int(input("How old are you? "))
        if age < 5 or age > 12:
            print("This program is best for kids aged 5-12. Let's play anyway!")
    except ValueError:
        print("That's not a number, but let's play!")
        age = 7  # Default
    
    print(f"Great, {name}! Let's learn some math. Answer 5 questions to earn points.")
    
    score = 0
    total_questions = 5
    
    for i in range(1, total_questions + 1):
        question, correct_answer = generate_question()
        print(f"\nQuestion {i}: What is {question}?")
        
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Awesome! That's correct. +1 point!")
                score += 1
            else:
                print(f"Oops, the right answer is {correct_answer}. Keep trying!")
        except ValueError:
            print("Please enter a number next time. The correct answer was", correct_answer)
    
    print(f"\nGame over, {name}! You got {score} out of {total_questions} correct.")
    if score == total_questions:
        print("Perfect! You're a math superstar!")
    elif score >= 3:
        print("Great job! You're getting better.")
    else:
        print("Nice try! Practice makes perfect. Want to play again?")
    
    play_again = input("Play again? (yes/no): ").lower()
    if play_again == 'yes':
        main()
    else:
        print("Thanks for playing! Bye!")

if __name__ == "__main__":
    main()