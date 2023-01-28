from tkinter import *
from math import *
def Area_finder():
    Are = Tk()
    Are.title("AREA FINDER")
    Are.config(bg="orange")
    Are.geometry("750x506+100+100")
    L1 = Label(Are, text="Area Finder", font=("Arial", 30), bg="orange")
    L1.pack()


    def Rectangle():
        def clear():
            E1.delete(0, END)
            E2.delete(0, END)

        L2 = Label(Are, text="Length=", font=("Arial", 20), bg="orange")
        L2.place(x=10, y=150)
        L3 = Label(Are, text="Breadth=", font=("Arial", 20), bg="orange")
        L3.place(x=300, y=150)
        E1 = Entry(Are, width=6, font=("Arial", 20))
        E1.place(x=150, y=150)
        E2 = Entry(Are, width=6, font=("Arial", 20))
        E2.place(x=450, y=150)

        def calculate():
            a1 = int(E1.get())
            a2 = int(E2.get())
            A = a1 * a2
            Lab = Label(Are, text=f"Area = {A}", font=("Arial", 20), bg="orange")
            Lab.place(x=10, y=250)

            def clear_everything():
                L2.destroy()
                L3.destroy()
                E1.destroy()
                E2.destroy()
                Lab.destroy()
                button1.destroy()
                button2.destroy()

            Button_sample = Button(Are, text="Clear", command=clear_everything)
            Button_sample.place(x=340, y=80)
        button1 = Button(Are, text="Submit", font=("Arial", 10), padx=10, pady=7, command=calculate)
        button1.place(x=50, y=200)
        button2 = Button(Are, text="clear", font=("Arial", 10), padx=10, pady=7, command=clear)
        button2.place(x=150, y=200)

    def Square():
        def clear():
            E1.delete(0, END)

        L2 = Label(Are, text="Length of Side=", font=("Arial", 20), bg="orange")
        L2.place(x=10, y=150)
        E1 = Entry(Are, width=6, font=("Arial", 20))
        E1.place(x=220, y=150)

        def calculate():
            a1 = int(E1.get())
            A = a1 ** 2
            Lab = Label(Are, text=f"Area = {A}", font=("Arial", 20), bg="orange")
            Lab.place(x=10, y=250)
            def clear_everything():
                L2.destroy()
                E1.destroy()
                Lab.destroy()
                button1.destroy()
                button2.destroy()
            Button_sample = Button(Are, text="Clear", command=clear_everything)
            Button_sample.place(x=340, y=80)
        button1 = Button(Are, text="Submit", font=("Arial", 10), padx=10, pady=7, command=calculate)
        button1.place(x=50, y=200)
        button2 = Button(Are, text="clear", font=("Arial", 10), padx=10, pady=7, command=clear)
        button2.place(x=150, y=200)

    def Triangle1():
        def clear():
            E1.delete(0, END)
            E2.delete(0, END)

        L2 = Label(Are, text="Base=", font=("Arial", 20), bg="orange")
        L2.place(x=10, y=150)
        L3 = Label(Are, text="Height=", font=("Arial", 20), bg="orange")
        L3.place(x=220, y=150)
        E1 = Entry(Are, width=6, font=("Arial", 20))
        E1.place(x=100, y=150)
        E2 = Entry(Are, width=6, font=("Arial", 20))
        E2.place(x=330, y=150)

        def calculate():
            a1 = int(E1.get())
            a2 = int(E2.get())
            A =  (a1 * a2)/2
            def clear_everything():
                L2.destroy()
                L3.destroy()
                E1.destroy()
                E2.destroy()
                Lab.destroy()
                button1.destroy()
                button2.destroy()

            Lab = Label(Are, text=f"Area = {A}", font=("Arial", 20), bg="orange")
            Lab.place(x=10, y=250)
            Button_sample = Button(Are, text="Clear", command=clear_everything)
            Button_sample.place(x=340, y=80)
        button1 = Button(Are, text="Submit", font=("Arial", 10), padx=10, pady=7, command=calculate)
        button1.place(x=50, y=200)
        button2 = Button(Are, text="clear", font=("Arial", 10), padx=10, pady=7, command=clear)
        button2.place(x=150, y=200)

    def Triangle2():
        def clear():
            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)

        L2 = Label(Are, text="Side-1=", font=("Arial", 20), bg="orange")
        L2.place(x=10, y=150)
        L3 = Label(Are, text="Side-2=", font=("Arial", 20), bg="orange")
        L3.place(x=220, y=150)
        L4 = Label(Are, text="Side-3=", font=("Arial", 20), bg="orange")
        L4.place(x=430, y=150)
        E1 = Entry(Are, width=6, font=("Arial", 20))
        E1.place(x=110, y=150)
        E2 = Entry(Are, width=6, font=("Arial", 20))
        E2.place(x=320, y=150)
        E3 = Entry(Are, width=6, font=("Arial", 20))
        E3.place(x=530, y=150)

        def calculate():
            a1 = int(E1.get())
            a2 = int(E2.get())
            a3 = int(E3.get())
            s = (a1 + a2 + a3)/2
            A = round(sqrt(abs(s * (s - a1) * (s - a2) * (s - a3))), 4)
            Lab = Label(Are, text=f"Area = {A}", font=("Arial", 20), bg="orange")
            Lab.place(x=10, y=250)

            def clear_everything():
                E1.destroy()
                E2.destroy()
                E3.destroy()
                Lab.destroy()
                L2.destroy()
                L3.destroy()
                L4.destroy()
                button1.destroy()
                button2.destroy()

            Button_sample = Button(Are, text="Clear", command=clear_everything)
            Button_sample.place(x=340, y=80)
        button1 = Button(Are, text="Submit", font=("Arial", 10), padx=10, pady=7, command=calculate)
        button1.place(x=50, y=200)
        button2 = Button(Are, text="clear", font=("Arial", 10), padx=10, pady=7, command=clear)
        button2.place(x=150, y=200)

    def Trapezium():
        def clear():
            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)

        L2 = Label(Are, text="Base Length=", font=("Arial", 20), bg="orange")
        L2.place(x=10, y=150)
        L3 = Label(Are, text="Height=", font=("Arial", 20), bg="orange")
        L3.place(x=285, y=150)
        L4 = Label(Are, text="Top Length=", font=("Arial", 20), bg="orange")
        L4.place(x=490, y=150)
        E1 = Entry(Are, width=6, font=("Arial", 20))
        E1.place(x=190, y=150)
        E2 = Entry(Are, width=6, font=("Arial", 20))
        E2.place(x=390, y=150)
        E3 = Entry(Are, width=6, font=("Arial", 20))
        E3.place(x=650, y=150)

        def calculate():
            a1 = int(E1.get())
            a2 = int(E2.get())
            a3 = int(E3.get())
            A = round(((a1 + a3)/2) * a2, 4)
            Lab = Label(Are, text=f"Area = {A}", font=("Arial", 20), bg="orange")
            Lab.place(x=10, y=250)
            def clear_everything():
                E1.destroy()
                E2.destroy()
                E3.destroy()
                Lab.destroy()
                L2.destroy()
                L3.destroy()
                L4.destroy()
                button1.destroy()
                button2.destroy()

            Button_sample = Button(Are, text="Clear", command=clear_everything)
            Button_sample.place(x=340, y=80)

        button1 = Button(Are, text="Submit", font=("Arial", 10), padx=10, pady=7, command=calculate)
        button1.place(x=50, y=200)
        button2 = Button(Are, text="clear", font=("Arial", 10), padx=10, pady=7, command=clear)
        button2.place(x=150, y=200)

    def Parallelogram():
        def clear():
            E1.delete(0, END)
            E2.delete(0, END)

        L2 = Label(Are, text="Length=", font=("Arial", 20), bg="orange")
        L2.place(x=10, y=150)
        L3 = Label(Are, text="Breadth=", font=("Arial", 20), bg="orange")
        L3.place(x=300, y=150)
        E1 = Entry(Are, width=6, font=("Arial", 20))
        E1.place(x=150, y=150)
        E2 = Entry(Are, width=6, font=("Arial", 20))
        E2.place(x=450, y=150)

        def calculate():
            a1 = int(E1.get())
            a2 = int(E2.get())
            A = a1 * a2
            Lab = Label(Are, text=f"Area = {A}", font=("Arial", 20), bg="orange")
            Lab.place(x=10, y=250)
            def clear_everything():
                L2.destroy()
                L3.destroy()
                E1.destroy()
                E2.destroy()
                Lab.destroy()
                button1.destroy()
                button2.destroy()

            Button_sample = Button(Are, text="Clear", command=clear_everything)
            Button_sample.place(x=340, y=80)

        button1 = Button(Are, text="Submit", font=("Arial", 10), padx=10, pady=7, command=calculate)
        button1.place(x=50, y=200)
        button2 = Button(Are, text="clear", font=("Arial", 10), padx=10, pady=7, command=clear)
        button2.place(x=150, y=200)

    def Circle():
        def clear():
            E1.delete(0, END)

        L2 = Label(Are, text="Radius=", font=("Arial", 20), bg="orange")
        L2.place(x=10, y=150)
        E1 = Entry(Are, width=6, font=("Arial", 20))
        E1.place(x=150, y=150)

        def calculate():
            a1 = int(E1.get())
            A = round((pi*a1**2), 4)
            Lab = Label(Are, text=f"Area = {A}", font=("Arial", 20), bg="orange")
            Lab.place(x=10, y=250)
            def clear_everything():
                L2.destroy()
                E1.destroy()
                Lab.destroy()
                button1.destroy()
                button2.destroy()
            Button_sample = Button(Are, text="Clear", command=clear_everything)
            Button_sample.place(x=340, y=80)

        button1 = Button(Are, text="Submit", font=("Arial", 10), padx=10, pady=7, command=calculate)
        button1.place(x=50, y=200)
        button2 = Button(Are, text="clear", font=("Arial", 10), padx=10, pady=7, command=clear)
        button2.place(x=150, y=200)

    def SemiCircle():
        def clear():
            E1.delete(0, END)

        L2 = Label(Are, text="Radius=", font=("Arial", 20), bg="orange")
        L2.place(x=10, y=150)
        E1 = Entry(Are, width=6, font=("Arial", 20))
        E1.place(x=150, y=150)

        def calculate():
            a1 = int(E1.get())
            A = round((pi*a1**2)/2, 4)
            Lab = Label(Are, text=f"Area = {A}", font=("Arial", 20), bg="orange")
            Lab.place(x=10, y=250)
            def clear_everything():
                L2.destroy()
                E1.destroy()
                Lab.destroy()
                button1.destroy()
                button2.destroy()
            Button_sample = Button(Are, text="Clear", command=clear_everything)
            Button_sample.place(x=340, y=80)
        button1 = Button(Are, text="Submit", font=("Arial", 10), padx=10, pady=7, command=calculate)
        button1.place(x=50, y=200)
        button2 = Button(Are, text="clear", font=("Arial", 10), padx=10, pady=7, command=clear)
        button2.place(x=150, y=200)

    def show():
        opt = clicked.get()
        if opt == "1.Rectangle":
            Rectangle()
        if opt == "2.Square":
            Square()
        if opt == "3.Triangle(2-sides known)":
            Triangle1()
        if opt == "4.triangle(3-sides known)":
            Triangle2()
        if opt == "5.Trapezium":
            Trapezium()
        if opt == "6.Parallelogram":
            Parallelogram()
        if opt == "7.Circle":
            Circle()
        if opt == "8.Semi-Circle":
            SemiCircle()

    option = ["1.Rectangle", "2.Square", "3.Triangle(2-sides known)", "4.triangle(3-sides known)",
              "5.Trapezium", "6.Parallelogram", "7.Circle", "8.Semi-Circle"]
    clicked = StringVar(Are)
    clicked.set("Select an option")
    drop = OptionMenu(Are, clicked, *option)
    drop.place(x=10, y=80)
    button = Button(Are, text="Submit", padx=10, command=show)
    button.place(x=240, y=80)
    button_clear = Button(Are, text="Clear", command=NONE)
    button_clear.place(x=340,y=80)

    Are.mainloop()
