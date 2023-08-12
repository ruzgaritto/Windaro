from tkinter import *
from tkinter import messagebox
import time

# This is the alfa version of Windaro

def on_validate_input(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False


def start():
    a = dakikagirisi.get()
    dakikagirisi.destroy()
    a = int(a)
    dakikagostergesi = Label(frame1, text=str(a),
                             font=("Comic Sans", 160),
                             bg="#313131",
                             fg="#5b5b85",
                             width=2,
                             justify="right"
                             )
    dakikagostergesi.pack(side=LEFT, padx=10, pady=10)
    ikinokta.pack(side=LEFT, padx=10, pady=10)
    saniyegostergesi.pack(side=LEFT, padx=10, pady=10)
    while a >= 0:
        b = 5
        while b >= 0:
            saniyegostergesi.config(text=b)
            saniyegostergesi.update()
            time.sleep(1)
            b -= 1
        a -= 1
        if a >= 0:
            c = str(a)
        else:
            c = str(00)
        dakikagostergesi.config(text=c)
        dakikagostergesi.update()
    o = 1
    windarosayisi.config(text=o)
    windarosayisi.pack(side=TOP, padx=10, pady=10)
    messagebox.showinfo(message="Done!")


window = Tk()
window.title("W I N D A R O")
window.geometry("2560x1600")
window.config(bg="#272727")
Label(window, text="W I N D A R O", font=("Tesla", 64), fg="#5b5b85", bg="#272727").pack()
frame1 = Frame(window, bg="#272727")
frame1.pack(expand=True)
frame2 = Frame(window, bg="#272727")
frame2.pack(expand=True)
colon = PhotoImage(file="colon.png")

vcmd = window.register(on_validate_input)

dakikagirisi = Entry(frame1,
                     font=("Comic Sans", 160),
                     bg="#313131",
                     fg="#5b5b85",
                     width=2,
                     justify="right",
                     validate="key", validatecommand=(vcmd, '%P'))
dakikagirisi.pack(side=LEFT, padx=10, pady=10)
ikinokta = Label(frame1, image=colon, bg="#272727")
# ikinokta.pack(side=LEFT, padx=10, pady=10)
saniyegostergesi = Label(frame1,
                         text="00",
                         font=("Comic Sans", 160),
                         bg="#313131",
                         fg="#5b5b85",
                         width=2,
                         justify="left")

startbutton = Button(frame2,
                     text="Start",
                     bg="#313131",
                     fg="#5b5b85",
                     relief=FLAT,
                     command=start,
                     overrelief=RIDGE)
startbutton.pack()
windarosayisi = Label(frame2,
                      font=("Comic Sans", 160),
                      bg="#313131",
                      fg="#5b5b85",
                      width=2,
                      justify="left")
Label(frame2, text="The alpha version of W I N D A R O", bg="#272727", fg="#5b5b85").pack(side=BOTTOM, padx=10, pady=10)

window.mainloop()
