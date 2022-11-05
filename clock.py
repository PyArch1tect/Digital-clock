from time import *
from tkinter import *

def clock():
    time_str = strftime("%I:%M:%S %p")
    time_lbl.config(text=time_str)
    time_lbl.after(1000,clock)

app = Tk()
app.title("Clock")
app.geometry("300x100")
app.resizable(0,0)
app.config(background="Black")
app.iconbitmap(r"C:\Users\PC\Downloads\Iynque-Ios7-Style-Clock.ico")

time_lbl = Label(app, font=("Digital-7",54), bg="black", foreground="red")
time_lbl.pack(anchor=CENTER,pady=10)

clock()

app.mainloop()