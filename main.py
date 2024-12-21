from tkinter import *
window=Tk()
window.title("EVENT HANDLER")
window.geometry("100x100")

def hk(event):
    print(event.char)

window.bind("<Key>",hk)

def bt(event):
    print('\nThe Button was pressed')
    
bt1=Button(text='Click me!')
bt1.pack()

bt1.bind("<Button-1>",bt)
window.mainloop()