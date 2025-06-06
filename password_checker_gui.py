import re
import tkinter as tk
from tkinter import messagebox

# Create the GUI window
root = tk.Tk()
root.title("Password Strength Finder")
root.geometry("400x300")

# Function to check password strength (same as before)
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !@#$%^&*).")

    if score == 5:
        return "Strong", feedback
    elif score >= 3:
        return "Medium", feedback
    else:
        return "Weak", feedback

# Function to handle the "Check" button click
def check_password():
    password = entry.get()
    strength, feedback = check_password_strength(password)
    
    # Display the strength
    result_label.config(text=f"Password Strength: {strength}")
    
    # Display feedback in a messagebox if there are suggestions
    if feedback:
        messagebox.showinfo("Suggestions", "\n".join(f"- {s}" for s in feedback))

# GUI elements
label = tk.Label(root, text="Enter your password:", font=("Arial", 14))
label.pack(pady=20)

entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
entry.pack(pady=10)

check_button = tk.Button(root, text="Check Strength", font=("Arial", 12), command=check_password)
check_button.pack(pady=10)

result_label = tk.Label(root, text="Password Strength: ", font=("Arial", 12))
result_label.pack(pady=20)

# Start the GUI
root.mainloop()