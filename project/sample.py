
# 

  

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

# Clear Screen Function
def clear_screen():
    for widget in root.winfo_children():
        if widget != title:
            widget.destroy()

# Alphabet Learning
def learn_alphabets():
    clear_screen()
    tk.Label(root, text="🔤 Learn Alphabets", font=("Arial", 16, "bold"),
             bg="#E3F2FD").pack(pady=10)

    alphabets = ["A - Apple 🍎", "B - Ball ⚽", "C - Cat 🐱", "D - Dog 🐶"]
    for a in alphabets:
        tk.Label(root, text=a, font=("Arial", 14),
                 bg="#E3F2FD").pack()

    tk.Button(root, text="⬅ Back", command=main_menu,
              bg="#4CAF50", fg="white").pack(pady=20)

# Number Learning
def learn_numbers():
    clear_screen()
    tk.Label(root, text="🔢 Learn Numbers", font=("Arial", 16, "bold"),
             bg="#E3F2FD").pack(pady=10)

    numbers = ["1 - One", "2 - Two", "3 - Three", "4 - Four"]
    for n in numbers:
        tk.Label(root, text=n, font=("Arial", 14),
                 bg="#E3F2FD").pack()

    tk.Button(root, text="⬅ Back", command=main_menu,
              bg="#4CAF50", fg="white").pack(pady=20)

# Quiz Section
def quiz():
    clear_screen()
    tk.Label(root, text="❓ Fun Quiz", font=("Arial", 16, "bold"),
             bg="#E3F2FD").pack(pady=10)

    tk.Label(root, text="What comes after A?",
             font=("Arial", 14), bg="#E3F2FD").pack(pady=10)

    def check(ans):
        if ans == "B":
            messagebox.showinfo("Result", "✅ Correct Answer! Great Job!")
        else:
            messagebox.showerror("Result", "❌ Wrong Answer! Try Again!")

    tk.Button(root, text="B", width=10,
              command=lambda: check("B"),
              bg="#2196F3", fg="white").pack(pady=5)

    tk.Button(root, text="C", width=10,
              command=lambda: check("C"),
              bg="#2196F3", fg="white").pack(pady=5)

    tk.Button(root, text="⬅ Back", command=main_menu,
              bg="#4CAF50", fg="white").pack(pady=20)

# Main Menu
def main_menu():
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




