from tkinter import *
from tkinter import filedialog
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Karakter ke')
        self.lbl2=Label(win, text='karakter')
        self.lbl3=Label(win, text='Folder')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.btn1 = Button(win, text='OK')
        self.btn2=Button(win, text='Subtract')
        self.lbl1.place(x=70, y=50)
        self.t1.place(x=180, y=50)
        self.lbl2.place(x=70, y=100)
        self.t2.place(x=180, y=100)
        self.b1=Button(win, text='OK', command=self.add)
        self.b2=Button(win, text='...')
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=180, y=180)
        self.b2.place(x=300, y=150)
        self.lbl3.place(x=70, y=150)
        self.t3.place(x=180, y=150)

    def add(self):
        num1=int(self.t1.get())
        char = num1-1
        import os
        directory = self.t3.get()
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            # checking if it is a file
            depan = filename[0:char]
            belakang = filename[num1:len(filename)]
            gabung = os.path.join(directory, depan+belakang)
            if os.path.isfile(f):
                fi = filename[0:num1]
                if fi.find(self.t2.get()) != -1:
                    os.rename(f, gabung)
                    print(gabung)

    def sub(self, event):
        direktori =  filedialog.askdirectory()
        self.t3.insert(END, str(direktori))

window=Tk()
mywin=MyWindow(window)
window.title('Delete Karakter')
window.geometry("400x300+10+10")
window.mainloop()