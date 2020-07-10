from tkinter import *
import random

fontsize = 30
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'cyan', 'purple']


def on_spam():
    popup = Toplevel()
    color = random.choice(colors)
    Label(popup, text='Popup', bg='black', fg=color).pack(fill=BOTH)
    mainLabel.config(fg=color)


def on_flip():
    mainLabel.config(fg=random.choice(colors))
    main.after(250, on_flip)


def on_grow():
    global fontsize
    fontsize += 5
    mainLabel.config(font=('arial', fontsize, 'italic'))
    main.after(100, on_grow)


main = Tk()
mainLabel = Label(main, text='Fun Gui!', relief=RAISED)
mainLabel.config(font=('arial', fontsize, 'italic'), fg='cyan', bg='navy')
mainLabel.pack(side=TOP, expand=YES, fill=BOTH)

Button(main, text='spam', command=on_spam).pack(fill=X)
Button(main, text='flip', command=on_flip).pack(fill=X)
Button(main, text='grow', command=on_grow).pack(fill=X)
main.mainloop()
