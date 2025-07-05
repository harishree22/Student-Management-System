import tkinter as tk
from tkinter import messagebox
import os

FILENAME = "students.txt"

# Function to add student
def add_student():
    name = name_var.get()
    roll = roll_var.get()
    branch = branch_var.get()
    
    if not (name and roll and branch):
        messagebox.showerror("Input Error", "All fields are required!")
        return
    
    with open(FILENAME, "a") as f:
        f.write(f"{name},{roll},{branch}\n")
    messagebox.showinfo("Success", "Student added successfully!")
    clear_fields()
    view_students()

# Function to view all students
def view_students():
    if not os.path.exists(FILENAME):
        return
    listbox.delete(0, tk.END)
    with open(FILENAME, "r") as f:
        for line in f:
            name, roll, branch = line.strip().split(",")
            listbox.insert(tk.END, f"Name: {name} | Roll: {roll} | Branch: {branch}")

# Function to clear input fields
def clear_fields():
    name_var.set("")
    roll_var.set("")
    branch_var.set("")

# Function to delete student by roll number
def delete_student():
    roll = roll_var.get()
    if not roll:
        messagebox.showerror("Input Error", "Enter roll number to delete.")
        return

    if not os.path.exists(FILENAME):
        messagebox.showerror("Error", "No records found.")
        return

    lines = []
    found = False
    with open(FILENAME, "r") as f:
        for line in f:
            _, r, _ = line.strip().split(",")
            if r != roll:
                lines.append(line)
            else:
                found = True
    if found:
        with open(FILENAME, "w") as f:
            f.writelines(lines)
        messagebox.showinfo("Success", "Student deleted.")
    else:
        messagebox.showinfo("Info", "Roll number not found.")
    view_students()

# Function to update student by roll number
def update_student():
    roll = roll_var.get()
    name = name_var.get()
    branch = branch_var.get()

    if not roll:
        messagebox.showerror("Input Error", "Enter roll number to update.")
        return

    if not os.path.exists(FILENAME):
        messagebox.showerror("Error", "No records found.")
        return

    updated = []
    found = False
    with open(FILENAME, "r") as f:
        for line in f:
            n, r, b = line.strip().split(",")
            if r == roll:
                updated.append(f"{name},{roll},{branch}\n")
                found = True
            else:
                updated.append(line)
    if found:
        with open(FILENAME, "w") as f:
            f.writelines(updated)
        messagebox.showinfo("Success", "Student updated.")
    else:
        messagebox.showinfo("Info", "Roll number not found.")
    view_students()

# GUI Setup
root = tk.Tk()
root.title("Student Management System")
root.geometry("600x500")
root.resizable(False, False)

# Variables
name_var = tk.StringVar()
roll_var = tk.StringVar()
branch_var = tk.StringVar()

# Title
tk.Label(root, text="Student Management System", font=("Arial", 18, "bold")).pack(pady=10)

# Input Frame
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(frame, textvariable=name_var, width=30).grid(row=0, column=1, pady=5)

tk.Label(frame, text="Roll No.").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(frame, textvariable=roll_var, width=30).grid(row=1, column=1, pady=5)

tk.Label(frame, text="Branch").grid(row=2, column=0, padx=10, pady=5)
tk.Entry(frame, textvariable=branch_var, width=30).grid(row=2, column=1, pady=5)

# Buttons
tk.Button(root, text="Add Student", command=add_student, width=15, bg="lightgreen").pack(pady=5)
tk.Button(root, text="Update Student", command=update_student, width=15, bg="lightblue").pack(pady=5)
tk.Button(root, text="Delete Student", command=delete_student, width=15, bg="salmon").pack(pady=5)

# Listbox to show students
listbox = tk.Listbox(root, width=70)
listbox.pack(pady=20)

# Load existing data
view_students()

# Run GUI
root.mainloop()
