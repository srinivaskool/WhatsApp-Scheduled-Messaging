import pywhatkit
import tkinter as tk
from tkinter import *


def send_msg():
    # print("here ", type(e1.get()), type(e2.get()), type(int(e3.get())), (int(e4.get())))
    print("Going to send")
    pywhatkit.sendwhatmsg(e1.get(), e2.get(), int(e3.get()), int(e4.get()))
    return None


root = Tk()
root.geometry("400x400")
root.title("Schedule Whatsapp Message")
root.iconbitmap(r"wh_ico.ico")

text = Label(root, text="Fill below to schedule the message")
text.pack()

photo = PhotoImage(file="wh_png.png")
label = Label(root, image=photo)
label.pack()

Phone = Label(root, text="Phone Number").pack()
e1 = Entry(root)
e1.pack()

Message = Label(root, text="Message").pack()
e2 = Entry(root)
e2.pack()

Hours = Label(root, text="Hours").pack()
e3 = Entry(root)
e3.pack()

Minutes = Label(root, text="Minutes").pack()
e4 = Entry(root)
e4.pack()

Button(root, text="Send", command=send_msg).pack()

root.mainloop()
