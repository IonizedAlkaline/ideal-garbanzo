from tkinter import *

window = Tk()
window.title("GSWW")
window.geometry('500x500')
text = Label(text="Enter Your Name: ")
text.pack()
name = Entry()
name.pack()
def greeting():
    names = name.get()
    msg = "welcome " + names
    text.insert(END,msg) 
button = Button(text='Greeting',command=greeting)
button.pack()
text = Text()
text.pack() 
window.mainloop()