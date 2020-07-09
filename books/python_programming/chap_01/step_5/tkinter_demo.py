from tkinter import *
from tkinter.messagebox import showinfo


def tkinter01():
    Label(text='Spam').pack()
    mainloop()


def tkinter02():
    window = Tk()
    button = Button(window, text='press', command=reply)
    button.pack()
    window.mainloop()


def tkinter03():
    window = MyGui()
    window.pack()
    window.mainloop()


def tkinter04():
    mainwin = Tk()
    Label(mainwin, text=__name__).pack()

    # 弹出窗口
    popup = Toplevel()
    Label(popup, text='Attach').pack(side=LEFT)
    MyGui(popup).pack(side=RIGHT)
    mainwin.mainloop()


def tkinter05():
    CustomGui().pack()
    mainloop()


class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='press', command=self.reply)
        button.pack()

    def reply(self):
        showinfo(title='popup', message='Button pressed2!')


class CustomGui(MyGui):
    def reply(self):
        showinfo(title='popup', message='Ouch!')


def reply():
    showinfo(title='popup', message='Button pressed!')


def main():
    # tkinter01()
    # tkinter02()
    # tkinter03()
    # tkinter04()
    tkinter05()


if __name__ == '__main__':
    main()
