import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Interactive Learning Site for Kids")
root.geometry("1500x1000")
root.config(bg="#E3F2FD")

# Title
title = tk.Label(
    root,
    text="🎉 Interactive Learning Site for Kids 🎉",
    font=("Arial", 18, "bold"),
    bg="#E3F2FD",
    fg="#E91E63"
)
title.pack(pady=10)

def clear_screen():
    for widget in root.winfo_children():
        if widget != title:
            widget.destroy()


questions = [
    {
        "question": "What comes after A?",
        "options": ["B", "C", "D"],
        "answer": "B"
    },
    {
        "question": "Which number comes after 2?",
        "options": ["1", "3", "4"],
        "answer": "3"
    },
    {
        "question": "A for?",
        "options": ["Ball", "Apple", "Cat"],
        "answer": "Apple"
    }
]

current_q = 0
score = 0

def quiz():
    clear_screen()
    show_question()

def show_question():
    clear_screen()
    global current_q

    if current_q >= len(questions):
        messagebox.showinfo(
            "Quiz Finished",
            f"🎉 Quiz Over!\nYour Score: {score}/{len(questions)}"
        )
        main_menu()
        return

    q = questions[current_q]

    tk.Label(
        root,
        text=f"Q{current_q + 1}. {q['question']}",
        font=("Arial", 16, "bold"),
        bg="#E3F2FD"
    ).pack(pady=20)

    for opt in q["options"]:
        tk.Button(
            root,
            text=opt,
            width=20,
            font=("Arial", 12),
            bg="#2196F3",
            fg="white",
            command=lambda o=opt: check_answer(o)
        ).pack(pady=5)

def check_answer(selected):
    global current_q, score
    correct = questions[current_q]["answer"]

    if selected == correct:
        score += 1
        messagebox.showinfo("Result", "✅ Correct Answer!")
    else:
        messagebox.showerror(
            "Result",
            f"❌ Wrong Answer!\nCorrect Answer is: {correct}"
        )

    current_q += 1
    show_question()


def learn_alphabets():
    clear_screen()
    tk.Label(root, text="🔤 Learn Alphabets",
             font=("Arial", 16, "bold"),
             bg="#E3F2FD").pack(pady=10)

    alphabets = ["A - Apple 🍎", "B - Ball ⚽", "C - Cat 🐱", "D - Dog 🐶"]
    for a in alphabets:
        tk.Label(root, text=a, font=("Arial", 14),
                 bg="#E3F2FD").pack()

    tk.Button(root, text="⬅ Back",
              command=main_menu,
              bg="#4CAF50", fg="white").pack(pady=20)

def learn_numbers():
    clear_screen()
    tk.Label(root, text="🔢 Learn Numbers",
             font=("Arial", 16, "bold"),
             bg="#E3F2FD").pack(pady=10)

    numbers = ["1 - One", "2 - Two", "3 - Three", "4 - Four"]
    for n in numbers:
        tk.Label(root, text=n, font=("Arial", 14),
                 bg="#E3F2FD").pack()

    tk.Button(root, text="⬅ Back",
              command=main_menu,
              bg="#4CAF50", fg="white").pack(pady=20)


def main_menu():
    global current_q, score
    current_q = 0
    score = 0

    clear_screen()

    tk.Button(root, text="🔤 Learn Alphabets", width=25,
              command=learn_alphabets,
              bg="#FF9800", fg="white",
              font=("Arial", 12)).pack(pady=10)

    tk.Button(root, text="🔢 Learn Numbers", width=25,
              command=learn_numbers,
              bg="#03A9F4", fg="white",
              font=("Arial", 12)).pack(pady=10)

    tk.Button(root, text="❓ Fun Quiz", width=25,
              command=quiz,
              bg="#9C27B0", fg="white",
              font=("Arial", 12)).pack(pady=10)

# Start App
main_menu()
root.mainloop()
