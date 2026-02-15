#!/usr/bin/env python
# coding: utf-8




from tkinter import *
from time import strftime

# ---------------- WINDOW ----------------
root = Tk()
root.title("Smart Digital Clock")
root.geometry("750x400")
root.resizable(False, False)

# ---------------- THEME COLORS ----------------
dark_theme = {
    "bg": "#0f172a",
    "fg": "#e2e8f0",
    "accent": "#38bdf8"
}

light_theme = {
    "bg": "#f1f5f9",
    "fg": "#0f172a",
    "accent": "#0ea5e9"
}

current_theme = dark_theme
is_24 = False
blink = True

# ---------------- FUNCTIONS ----------------

def update_time():
    global blink

    if is_24:
        time_string = strftime('%H:%M:%S')
    else:
        time_string = strftime('%I:%M:%S %p')

    # Blinking colon effect
    if blink:
        time_string = time_string.replace(":", " ")
    blink = not blink

    date_string = strftime('%A, %d %B %Y')

    hour = int(strftime('%H'))
    greeting = "Good Morning ☀" if hour < 12 else \
               "Good Afternoon 🌤" if hour < 18 else \
               "Good Evening 🌙"

    time_label.config(text=time_string)
    date_label.config(text=date_string)
    greeting_label.config(text=greeting)

    root.after(1000, update_time)

def toggle_format():
    global is_24
    is_24 = not is_24

def apply_theme(theme):
    root.configure(bg=theme["bg"])
    main_frame.configure(bg=theme["bg"])
    title.configure(bg=theme["bg"], fg=theme["accent"])
    greeting_label.configure(bg=theme["bg"], fg=theme["fg"])
    time_label.configure(bg=theme["bg"], fg=theme["accent"])
    date_label.configure(bg=theme["bg"], fg=theme["fg"])
    theme_btn.configure(bg=theme["accent"], fg="black")
    format_btn.configure(bg=theme["accent"], fg="black")

def toggle_theme():
    global current_theme
    current_theme = light_theme if current_theme == dark_theme else dark_theme
    apply_theme(current_theme)

# ---------------- UI ----------------

main_frame = Frame(root)
main_frame.pack(expand=True)

title = Label(main_frame,
              text="SMART DIGITAL CLOCK",
              font=("Helvetica", 18, "bold"))
title.pack(pady=10)

greeting_label = Label(main_frame,
                       font=("Helvetica", 16))
greeting_label.pack()

time_label = Label(main_frame,
                   font=("Helvetica", 70, "bold"))
time_label.pack(pady=10)

date_label = Label(main_frame,
                   font=("Helvetica", 18))
date_label.pack()

format_btn = Button(main_frame,
                    text="Switch 12/24 Hour",
                    font=("Helvetica", 11, "bold"),
                    relief="flat",
                    padx=15,
                    command=toggle_format)
format_btn.pack(pady=10)

theme_btn = Button(main_frame,
                   text="Toggle Theme",
                   font=("Helvetica", 11, "bold"),
                   relief="flat",
                   padx=15,
                   command=toggle_theme)
theme_btn.pack(pady=5)

# Apply default theme
apply_theme(dark_theme)

# Start clock
update_time()
root.mainloop()







