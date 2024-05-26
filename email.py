import tkinter as tk
from tkinter import ttk, messagebox, font
from PIL import Image, ImageTk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

review_entry = None
happiness_var = None
review_window = None
main_window = None
DO_NOT_SHOW_FILE = "do_not_show_review.txt"

def send_email(review, happiness_meter):
    email_sender = "binasahmed8@gmail.com"
    email_receiver = "random08296@gmail.com"
    password = "dnbw xfqq rypv obds"

    subject = "Movie App Review, what should we improve on?"
    body = f"Review: {review}\nHappiness Meter: {happiness_meter}"

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(email_sender, password)
        smtp.send_message(msg)
    print("Email sent successfully.")

def gui():
    global main_window
    WIDTH = 1000
    HEIGHT = 500

    main_window = tk.Tk()
    main_window.title("MOVIE FILTER APPLICATION")
    main_window.geometry(f"{WIDTH}x{HEIGHT}")

    heading = tk.Label(main_window, text="ULTIMATE MOVIE FILTER", font=('Helvetica', 12))
    heading.pack(ipadx=25, ipady=10)

    canvas = tk.Canvas(main_window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(main_window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    image_path = 'D:/python/Ultimate_Movie_Filter/pic_for_ultimatemovies.jpg'
    img = Image.open(image_path)

    img = img.resize((100, 100), Image.LANCZOS)
    tk_img = ImageTk.PhotoImage(img)

    main_window.iconphoto(True, tk_img)

    main_window.protocol("WM_DELETE_WINDOW", on_closing)

    main_window.mainloop()

def review_box():
    global review_entry, happiness_var, review_window
    review_window = tk.Toplevel(main_window)
    review_window.title("Review")
    review_window.geometry("400x300")

    review_label = tk.Label(review_window, text="Enter your review:")
    review_label.pack()

    review_entry = tk.Entry(review_window, width=50)
    review_entry.pack()

    happiness_label = tk.Label(review_window, text="Rate your happiness:")
    happiness_label.pack()

    happiness_var = tk.StringVar()

    happiness_frame = tk.Frame(review_window)
    happiness_frame.pack(pady=10)

    emoji_font = font.Font(family='Helvetica', size=30)  

    happiness_levels = [
        ("☹️", "Bad"),
        ("😊", "Good"),
        ("🙃", "Great"),
        ("☠️", "Insane")
    ]

    for emoji, text in happiness_levels:
        button_frame = tk.Frame(happiness_frame)
        button_frame.pack(side=tk.LEFT, padx=10)
        radio_button = tk.Radiobutton(button_frame, text=emoji, variable=happiness_var, value=text, font=emoji_font)
        radio_button.pack()
        label = tk.Label(button_frame, text=text)
        label.pack()

    submit_button = tk.Button(review_window, text="Submit", command=send_review)
    submit_button.pack(pady=10)

    do_not_show_button = tk.Button(review_window, text="Don't show this box again", command=disable_review_prompt)
    do_not_show_button.pack(pady=5)

    review_window.protocol("WM_DELETE_WINDOW", close_all_windows)

def send_review():
    review = review_entry.get()
    happiness_meter = happiness_var.get()
    if review.strip() and happiness_meter:
        send_email(review, happiness_meter)
        close_all_windows()
    else:
        messagebox.showerror("Error", "Please enter both review and happiness rating.")

def disable_review_prompt():
    with open(DO_NOT_SHOW_FILE, "w") as f:
        f.write("do_not_show")
    close_all_windows()

def close_all_windows():
    if review_window:
        review_window.destroy()
    if main_window:
        main_window.destroy()

def on_closing():
    if not os.path.exists(DO_NOT_SHOW_FILE):
        review_box()
    else:
        main_window.destroy()

if __name__ == "__main__":
    gui()
