import tkinter as tk
import random
import smtplib
from tkinter import messagebox

def send_otp():
    email = entry_email.get()

    if not email:
        messagebox.showerror("Error", "Please enter your email address.")
        return

    send_email(email, otp)
    messagebox.showinfo("OTP Sent", "OTP has been sent to your email. Please check your inbox.")

def generate_otp():
    return str(random.randint(100000, 999999))

def send_email(email, otp):
    # Replace 'your_email@gmail.com' and 'your_password' with your Gmail credentials
    sender_email = 'shashikantsurlakar7651@gmail.com'
    sender_password = 'afjanoxlojqptplu'
    
    subject = 'OTP Verification'
    body = f'Your OTP is: {otp}'

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
            server.login(sender_email, sender_password)
            message = f'Subject: {subject}\n\n{body}'
            server.sendmail(sender_email, email, message)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while sending the OTP: {e}")

def otp_verify():
    OTP = entry_Otp.get()
    if OTP == otp:
        messagebox.showinfo("OTP Verify","OTP has been Verified.")
    else:
        messagebox.showinfo("OTP Verify","Wrong OTP , Please Enter Correct OTP")


otp = generate_otp()

root = tk.Tk()
root.title("OTP Verification")

label_main = tk.Label(root, text="Otp Verification",font=("Times New Roman",40),background="Light Blue")
label_main.pack(fill="both")


label_email = tk.Label(root, text="Enter your email address:",font=("Times New Roman",20))
label_email.place(x=400,y=100)


entry_email = tk.Entry(root,font=("Times New Roman",15),width=40)
entry_email.place(x=700,y=110)


button_send = tk.Button(root, text="Send OTP", command=send_otp)
button_send.place(x=650,y=150)

label_Otp = tk.Label(root, text="Enter OTP : ",font=("Times New Roman",20))
label_Otp.place(x=550,y=200)

entry_Otp = tk.Entry(root,font=("Times New Roman",15),width=40)
entry_Otp.place(x=700,y=200)

button_Otp = tk.Button(root, text="Verify", command=otp_verify)
button_Otp.place(x=650,y=250)

root.mainloop()
