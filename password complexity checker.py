import tkinter as tk
from tkinter import messagebox
import re

# Function to assess the strength of a password
def assess_password_strength(password):
    # Initialize variables to track the password properties
    length = len(password) >= 8
    has_uppercase = bool(re.search(r"[A-Z]", password))  # Convert to boolean
    has_lowercase = bool(re.search(r"[a-z]", password))  # Convert to boolean
    has_digit = bool(re.search(r"\d", password))  # Convert to boolean
    has_special_char = bool(re.search(r"[@$!%*?&]", password))  # Convert to boolean
    
    # Feedback to the user on missing criteria
    feedback = []
    if not length:
        feedback.append("Password must be at least 8 characters long.")
    if not has_uppercase:
        feedback.append("Password must include at least one uppercase letter.")
    if not has_lowercase:
        feedback.append("Password must include at least one lowercase letter.")
    if not has_digit:
        feedback.append("Password must include at least one number.")
    if not has_special_char:
        feedback.append("Password must include at least one special character (@, $, !, %, *, ?, &).")
    
    # Calculate password strength
    strength = sum([length, has_uppercase, has_lowercase, has_digit, has_special_char])
    
    if strength == 5:
        return "Strong", feedback
    elif strength >= 3:
        return "Moderate", feedback
    else:
        return "Weak", feedback

# Function to display the password strength assessment
def check_password():
    password = password_entry.get()
    strength, feedback = assess_password_strength(password)
    
    # Update the label to show the strength
    strength_label.config(text=f"Password Strength: {strength}")
    
    # Update the feedback text area
    feedback_text.delete(1.0, tk.END)
    if feedback:
        feedback_text.insert(tk.END, "\n".join(feedback))
    else:
        feedback_text.insert(tk.END, "Your password meets all criteria.")

# Function to toggle between showing and hiding the password
def toggle_password_visibility():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
        toggle_button.config(text='Hide Password')
    else:
        password_entry.config(show='*')
        toggle_button.config(text='Show Password')

# Setting up the GUI window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x400")

# Password Entry
tk.Label(root, text="Enter Password:").pack(pady=10)
password_entry = tk.Entry(root, width=30, show='*')
password_entry.pack()

# Toggle button to show/hide password
toggle_button = tk.Button(root, text='Show Password', command=toggle_password_visibility)
toggle_button.pack(pady=5)

# Button to check password strength
check_button = tk.Button(root, text="Check Password Strength", command=check_password)
check_button.pack(pady=10)

# Label to display the strength of the password
strength_label = tk.Label(root, text="Password Strength: ")
strength_label.pack(pady=10)

# Text area to display feedback on missing criteria
tk.Label(root, text="Feedback:").pack(pady=5)
feedback_text = tk.Text(root, height=6, width=40)
feedback_text.pack()

# Start the GUI event loop
root.mainloop()
