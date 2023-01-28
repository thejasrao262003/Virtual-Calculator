from tkinter import *
from math import *


def volume_finder():
    Vol = Tk()
    Vol.title("VOLUME FINDER")
    Vol.config(bg="cyan")
    Vol.geometry("680x506+100+100")
    L1 = Label(Vol, text="Volume Finder", font=("Arial", 30), bg="cyan")
    L1.pack()
    def Cuboid():
        def clear():
            E1.delete(0, END)
            E2.delete(0, END)

        L2 = Label(Vol, text="Length=", font=("Arial", 20), bg="cyan")
        L2.place(x=10, y=150)
        L3 = Label(Vol, text="Breadth=", font=("Arial", 20), bg="cyan")
        L3.place(x=225, y=150)
        L4 = Label(Vol, text="Height=", font=("Arial", 20), bg="cyan")
        L4.place(x=450, y=150)
        E1 = Entry(Vol, width=6, font=("Arial", 20))
        E1.place(x=120, y=150)
        E2 = Entry(Vol, width=6, font=("Arial", 20))
        E2.place(x=350, y=150)
        E3 = Entry(Vol, width=6, font=("Arial", 20))
        E3.place(x=555, y=150)

        def calculate():
            a1 = int(E1.get())
            a2 = int(E2.get())
            a3 = int(E3.get())
            A = a1 * a2 * a3
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
            Lab = Label(Vol, text=f"Volume={A}", font=("Arial", 20), bg = "cyan")
            Lab.place(x=10, y=250)
            Button_sample = Button(Vol, text="Clear", command=clear_everything)
            Button_sample.place(x=300, y=80)
        button1 = Button(Vol, text="Submit", font=("Arial", 10), padx=10, pady=7, command=calculate)
        button1.place(x=50, y=200)
        button2 = Button(Vol, text="clear", font=("Arial", 10), padx=10, pady=7, command=clear)
        button2.place(x=150, y=200)

    def Cube():
        def clear():
            E1.delete(0, END)

        L2 = Label(Vol, text="Length of Side=", font=("Arial", 20), bg="cyan")
        L2.place(x=10, y=150)
        E1 = Entry(Vol, width=6, font=("Arial", 20))
        E1.place(x=250, y=150)

        def calculate():
            a1 = int(E1.get())
            A = a1 ** 3
            def clear_everything():
                L2.destroy()
                E1.destroy()
                Lab.destroy()
                button1.destroy()
                button2.destroy()
            Lab = Label(Vol, text=f"Volume={A}", font=("Arial", 20), bg="cyan")
            Lab.place(x=10, y=250)
            Button_sample = Button(Vol, text="Clear", command=clear_everything)
            Button_sample.place(x=300, y=80)

        button1 = Button(Vol, text="Submit", font=("Arial", 10), padx=10, pady=7, command=calculate)
        button1.place(x=50, y=200)
        button2 = Button(Vol, text="clear", font=("Arial", 10), padx=10, pady=7, command=clear)
        button2.place(x=150, y=200)

    def Cone():
        def clear():
            E1.delete(0, END)
            E2.delete(0, END)

        L2 = Label(Vol, text="Base Radius=", font=("Arial", 20), bg="cyan")
        L2.place(x=10, y=150)
        L3 = Label(Vol, text="Height=", font=("Arial", 20), bg="cyan")
        L3.place(x=340, y=150)
        E1 = Entry(Vol, width=6, font=("Arial", 20))
        E1.place(x=220, y=150)
        E2 = Entry(Vol, width=6, font=("Arial", 20))
        E2.place(x=450, y=150)

        def calculate():
            a1 = int(E1.get())
            a2 = int(E2.get())
            A = round((pi*a1*a1*a2)/3, 4)
            Lab = Label(Vol, text=f"Volume={A}", font=("Arial", 20), bg="cyan")
            Lab.place(x=10, y=250)
            def clear_everything():
                L2.destroy()
                L3.destroy()
                Lab.destroy()
                E1.destroy()
                E2.destroy()
                button1.destroy()
                button2.destroy()
            Button_sample = Button(Vol, text="Clear", command=clear_everything)
            Button_sample.place(x=300, y=80)
        button1 = Button(Vol, text="Submit", font=("Arial", 10), padx=10, pady=7, command=calculate)
        button1.place(x=50, y=200)
        button2 = Button(Vol, text="clear", font=("Arial", 10), padx=10, pady=7, command=clear)
        button2.place(x=150, y=200)

    def Cylinder():
        def clear():
            E1.delete(0, END)
            E2.delete(0, END)

        L2 = Label(Vol, text="Radius=", font=("Arial", 20), bg="cyan")
        L2.place(x=10, y=150)
        L3 = Label(Vol, text="Height=", font=("Arial", 20), bg="cyan")
        L3.place(x=230, y=150)
        E1 = Entry(Vol, width=6, font=("Arial", 20))
        E1.place(x=120, y=150)
        E2 = Entry(Vol, width=6, font=("Arial", 20))
        E2.place(x=330, y=150)

        def calculate():
            a1 = int(E1.get())
            a2 = int(E2.get())
            A = round((pi*a1*a1*a2), 4)
            def clear_everything():
                L2.destroy()
                L3.destroy()
                Lab.destroy()
                E1.destroy()
                E2.destroy()
                button1.destroy()
                button2.destroy()

            Button_sample = Button(Vol, text="Clear", command=clear_everything)
            Button_sample.place(x=300, y=80)
            Lab = Label(Vol, text=f"Volume={A}", font=("Arial", 20), bg="cyan")
            Lab.place(x=10, y=250)

        button1 = Button(Vol, text="Submit", font=("Arial", 10), padx=10, pady=7, command=calculate)
        button1.place(x=50, y=200)
        button2 = Button(Vol, text="clear", font=("Arial", 10), padx=10, pady=7, command=clear)
        button2.place(x=150, y=200)

    def Square_Pyramid():
        def clear():
            E1.delete(0, END)
            E2.delete(0, END)

        L2 = Label(Vol, text="Base Side=", font=("Arial", 20), bg="cyan")
        L2.place(x=10, y=150)
        L3 = Label(Vol, text="Height=", font=("Arial", 20), bg="cyan")
        L3.place(x=300, y=150)
        E1 = Entry(Vol, width=6, font=("Arial", 20))
        E1.place(x=180, y=150)
        E2 = Entry(Vol, width=6, font=("Arial", 20))
        E2.place(x=450, y=150)

        def calculate():
            a1 = int(E1.get())
            a2 = int(E2.get())
            A = round((a1**2*a2)/3, 4)
            Lab = Label(Vol, text=f"Volume={A}", font=("Arial", 20), bg="cyan")
            Lab.place(x=10, y=250)
            def clear_everything():
                L2.destroy()
                L3.destroy()
                Lab.destroy()
                E1.destroy()
                E2.destroy()
                button1.destroy()
                button2.destroy()

            Button_sample = Button(Vol, text="Clear", command=clear_everything)
            Button_sample.place(x=300, y=80)

        button1 = Button(Vol, text="Submit", font=("Arial", 10), padx=10, pady=7, command=calculate)
        button1.place(x=50, y=200)
        button2 = Button(Vol, text="clear", font=("Arial", 10), padx=10, pady=7, command=clear)
        button2.place(x=150, y=200)

    def Torus():
        def clear():
            E1.delete(0, END)
            E2.delete(0, END)

        L2 = Label(Vol, text="Major Radius=", font=("Arial", 20), bg="cyan")
        L2.place(x=10, y=150)
        L3 = Label(Vol, text="Minor Radius=", font=("Arial", 20), bg="cyan")
        L3.place(x=340, y=150)
        E1 = Entry(Vol, width=6, font=("Arial", 20))
        E1.place(x=215, y=150)
        E2 = Entry(Vol, width=6, font=("Arial", 20))
        E2.place(x=550, y=150)

        def calculate():
            a1 = int(E1.get())
            a2 = int(E2.get())
            A = round((2*pi*a1)*(pi*a2**2),4)
            Lab = Label(Vol, text=f"Volume={A}", font=("Arial", 20), bg="cyan")
            Lab.place(x=10, y=250)
            def clear_everything():
                L2.destroy()
                L3.destroy()
                Lab.destroy()
                E1.destroy()
                E2.destroy()
                button1.destroy()
                button2.destroy()

            Button_sample = Button(Vol, text="Clear", command=clear_everything)
            Button_sample.place(x=300, y=80)

        button1 = Button(Vol, text="Submit", font=("Arial", 10), padx=10, pady=7, command=calculate)
        button1.place(x=50, y=200)
        button2 = Button(Vol, text="clear", font=("Arial", 10), padx=10, pady=7, command=clear)
        button2.place(x=150, y=200)

    def Sphere():
        def clear():
            E1.delete(0, END)

        L2 = Label(Vol, text="Radius=", font=("Arial", 20), bg="cyan")
        L2.place(x=10, y=150)
        E1 = Entry(Vol, width=6, font=("Arial", 20))
        E1.place(x=150, y=150)

        def calculate():
            a1 = int(E1.get())
            A = round((4*pi*a1**3)/3, 4)
            def clear_everything():
                L2.destroy()
                E1.destroy()
                Lab.destroy()
                button1.destroy()
                button2.destroy()
            Lab = Label(Vol, text=f"Volume={A}", font=("Arial", 20), bg="cyan")
            Lab.place(x=10, y=250)
            Button_sample = Button(Vol, text="Clear", command=clear_everything)
            Button_sample.place(x=300, y=80)

        button1 = Button(Vol, text="Submit", font=("Arial", 10), padx=10, pady=7, command=calculate)
        button1.place(x=50, y=200)
        button2 = Button(Vol, text="clear", font=("Arial", 10), padx=10, pady=7, command=clear)
        button2.place(x=150, y=200)

    def Hemisphere():
        def clear():
            E1.delete(0, END)

        L2 = Label(Vol, text="Radius=", font=("Arial", 20), bg="cyan")
        L2.place(x=10, y=150)
        E1 = Entry(Vol, width=6, font=("Arial", 20))
        E1.place(x=150, y=150)

        def calculate():
            a1 = int(E1.get())
            A = round((2*pi*a1**3)/3, 4)
            def clear_everything():
                L2.destroy()
                E1.destroy()
                Lab.destroy()
                button1.destroy()
                button2.destroy()
            Lab = Label(Vol, text=f"Volume={A}", font=("Arial", 20), bg="cyan")
            Lab.place(x=10, y=250)
            Button_sample = Button(Vol, text="Clear", command=clear_everything)
            Button_sample.place(x=300, y=80)

        button1 = Button(Vol, text="Submit", font=("Arial", 10), padx=10, pady=7, command=calculate)
        button1.place(x=50, y=200)
        button2 = Button(Vol, text="clear", font=("Arial", 10), padx=10, pady=7, command=clear)
        button2.place(x=150, y=200)

    def Tetrahedron():
        def clear():
            E1.delete(0, END)

        L2 = Label(Vol, text="Side Length=", font=("Arial", 20), bg="cyan")
        L2.place(x=10, y=150)
        E1 = Entry(Vol, width=6, font=("Arial", 20))
        E1.place(x=200, y=150)

        def calculate():
            a1 = int(E1.get())
            A = round(((a1 ** 3) / 6) * sqrt(2), 4)
            def clear_everything():
                L2.destroy()
                E1.destroy()
                Lab.destroy()
                button1.destroy()
                button2.destroy()
            Lab = Label(Vol, text=f"Volume={A}", font=("Arial", 20), bg="cyan")
            Lab.place(x=10, y=250)
            Button_sample = Button(Vol, text="Clear", command=clear_everything)
            Button_sample.place(x=300, y=80)
        button1 = Button(Vol, text="Submit", font=("Arial", 10), padx=10, pady=7, command=calculate)
        button1.place(x=50, y=200)
        button2 = Button(Vol, text="clear", font=("Arial", 10), padx=10, pady=7, command=clear)
        button2.place(x=150, y=200)

    def show():

        opt = clicked.get()
        if opt == "1.Cuboid":
            Cuboid()
        if opt == "2.Cube":
            Cube()
        if opt == "3.Cone":
            Cone()
        if opt == "4.Cylinder":
            Cylinder()
        if opt == "5.Square_Pyramid":
            Square_Pyramid()
        if opt == "6.Torus":
            Torus()
        if opt == "7.Sphere":
            Sphere()
        if opt == "8.Hemisphere":
            Hemisphere()
        if opt == "9.Tetrahedron":
            Tetrahedron()

    option = ["1.Cuboid", "2.Cube", "3.Cone", "4.Cylinder", "5.Square_Pyramid", "6.Torus", "7.Sphere",
              "8.Hemisphere", "9.Tetrahedron"]
    clicked = StringVar(Vol)
    clicked.set("Select an option")
    drop = OptionMenu(Vol, clicked, *option)
    drop.place(x=10, y=80)
    button = Button(Vol, text="Submit", command=show)
    button.place(x=200, y=80)
    button_clear = Button(Vol, text="Clear", command=NONE)
    button_clear.place(x=300, y=80)

    Vol.mainloop()
