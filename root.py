from tkinter import *
from datetime import date
root = Tk()
root.title("Getting started with widgets")
root.geometry("400x300")
lbl = Label(text="hey there!", fg="white", bg="gray", height=1, width=300)
namelbl = Label(text="full name", bg="blue")
name_entry = Entry()
def Display():
    name = name_entry.get()
    global message
    message = "Welcome to applicatiion! \nToday's date is:"
    greet = "hello "+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END,date.today())
text_box = Text(height=3)
btn = Button(text= "begin", command=Display, height=1, bg = "white", fg = "gray")
lbl.pack()
namelbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()
