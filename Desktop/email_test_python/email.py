import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

review_entry = None
happiness_level_var = None
review_window = None

def send_email(review, happiness_level):
    email_sender = "binasahmed8@gmail.com"
    email_receiver = "random08296@gmail.com"
    password = "dnbw xfqq rypv obds"

    subject = "Movie App Review, what should we improve on?"
    body = f"Review: {review}\nHappiness Level: {happiness_level}"

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

def review_box():
    global review_entry, happiness_level_var, review_window
    review_window = tk.Toplevel()
    review_window.title("Review")
    review_window.geometry("300x250")

    review_label = tk.Label(review_window, text="Enter your review:")
    review_label.pack()

    review_entry = tk.Entry(review_window, width=30)
    review_entry.pack()

    happiness_label = tk.Label(review_window, text="Select your happiness level:")
    happiness_label.pack()

    happiness_levels = ["☹️", "😊", "🙃", "☠️"]
    happiness_texts = ["bad", "good", "great", "insane"]

    happiness_level_var = tk.StringVar()
    happiness_level_var.set(happiness_levels[1])

    for level, text in zip(happiness_levels, happiness_texts):
        frame = tk.Frame(review_window)
        frame.pack(anchor=tk.W)

        rb = tk.Radiobutton(frame, text=level, variable=happiness_level_var, value=level)
        rb.pack(side=tk.LEFT)

        label = tk.Label(frame, text=text)
        label.pack(side=tk.LEFT)

    submit_button = tk.Button(review_window, text="Submit", command=send_email_wrapper)
    submit_button.pack()

def send_email_wrapper():
    review = review_entry.get()
    happiness_level = happiness_level_var.get()
    if review.strip():
        send_email(review, happiness_level)
        review_window.destroy()
    else:
        messagebox.showerror("Error", "Please enter your review.")

def gui():
    WIDTH = 1000
    HEIGHT = 500

    window = tk.Tk()
    window.title("MOVIE FILTER APPLICATION")
    window.geometry(f"{WIDTH}x{HEIGHT}")

    heading = tk.Label(window, text="ULTIMATE MOVIE FILTER", font=('Helvetica', 12))
    heading.pack(ipadx=25, ipady=10)

    canvas = tk.Canvas(window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    image_path = 'D:/python/Ultimate_Movie_Filter/pic_for_ultimatemovies.jpg'
    img = Image.open(image_path)

    img = img.resize((100, 100), Image.LANCZOS)
    tk_img = ImageTk.PhotoImage(img)

    window.iconphoto(True, tk_img)

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

def on_closing():
    window.destroy()

gui()
