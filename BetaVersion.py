from tkinter import *
from tkinter import messagebox
import time


windarotime = 0


def main():

    global windarotime

    def start():
        startbutton.destroy()
        dakikaentry.pack(side=LEFT)
        startbutton2.pack(side=TOP)

    def start2():
        global windarotime
        x = int(dakikaentry.get())
        y = int(dakikaentry.get())
        dakikaentry.destroy()
        startbutton2.destroy()
        dakikalabel = Label(frame2, font=("Helvetica", 128), width=2, fg="#5b5b85", bg="#313131")
        saniyelabel = Label(frame2, font=("Helvetica", 128), width=2, fg="#5b5b85", bg="#313131")
        boslabel = Label(frame2, font=("Helvetica", 128), text=" ", bg="#313131", fg="#5b5b85")
        dakikalabel.pack(side=LEFT)
        boslabel.pack(side=LEFT)
        saniyelabel.pack(side=LEFT)
        while x >= 0:
            dakikalabel.config(text=x)
            dakikalabel.update()
            saniye = 60
            while saniye >= 0:
                if saniye == 60:
                    saniyelabel.config(text="00")
                    saniyelabel.update()
                else:
                    saniyelabel.config(text=saniye)
                    saniyelabel.update()
                time.sleep(1)
                saniye -= 1
                if y == x:
                    x -= 1
                    dakikalabel.config(text=x)
                    dakikalabel.update()
            x -= 1
        windarotime += 1
        messagebox.showinfo(message="Geri sayim tamamlandi!")
        window.destroy()
        main()

    window = Tk()
    window.geometry("2560x1600")
    window.config(bg="#313131")
    window.title("W I N D A R O")

    frame1 = Frame(window, bg="#313131")
    frame1.pack(expand=True)
    frame2 = Frame(window, bg="#313131")
    frame2.pack(expand=True)
    frame3 = Frame(window, bg="#313131")
    frame3.pack(expand=True)

    Label(frame1, text="W I N D A R O", font=("Tesla", 64), fg="#5b5b85", bg="#313131").pack()

    startbutton = Button(frame2, text="Start", fg="#313131", command=start, bg="#313131", highlightbackground="#313131")
    startbutton.pack()

    dakikaentry = Entry(frame2, font=("Helvetica", 128), width=2, justify=RIGHT, fg="#5b5b85", bg="#313131", highlightbackground="#5b5b85")
    startbutton2 = Button(frame3, text="Start", bg="#313131", command=start2, highlightbackground="#313131")

    windarotimelabel = Label(frame3, text=windarotime, font="Helvetica", bg="#313131", fg="#5b5b85")
    windarotimelabel.pack()

    Label(frame3, text="W I N D A R O Beta Version", font="Helvetica", bg="#313131", fg="#5b5b85").pack(side=BOTTOM)

    tarih = str(time.ctime())
    tarihlabel = Label(frame3, text=tarih, font="Helvetica", fg="#5b5b85", bg="#313131")
    tarihlabel.pack(side=BOTTOM)

    window.mainloop()


if __name__ == '__main__':
    main()
