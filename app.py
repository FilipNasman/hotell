import tkinter as tk
import json
import os
from tkinter import *
from tkinter.ttk import Button, Menubutton
from turtle import left
from unittest import skip
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()
#Förnamn, Efternamn, Rum
class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def SubmitCommand():
            if CheckInTeleNmr.index("end") != 0 and CheckInFirstName.index("end") != 0 and CheckInLastName.index("end") != 0 and select_rooms.get() != "":
                print("Yes")
                GuestInfo = {"First": CheckInFirstName.get(), "Last": CheckInLastName.get(), "TelNmr": CheckInTeleNmr.get(), "Beds": select_rooms.get()}

                with open("json/Guests.json", "r") as f:
                    data = json.load(f)
                    data["Guests"].append(GuestInfo)

                with open("json/Guests.json", "w") as f:
                    json.dump(data, f, indent = 2)

                CheckInFirstName.delete(0,END)
                CheckInLastName.delete(0,END)
                CheckInTeleNmr.delete(0,END)
                
        

            else:
                print("no")
        root.columnconfigure(3, weight=1)
        
        select_rooms = tk.StringVar()
        
        CheckInTeleNmrLabel = tk.Label(self, text="Telephone:")
        CheckInTeleNmr = tk.Entry(self)

        CheckInTeleNmrLabel.grid(column=0, row=2, padx=2, pady=2)
        CheckInTeleNmr.grid(column=1, row=2, padx=2, pady=2)



        CheckInRoomSizeLabel = tk.Label(self, text="Number of beds:")
        CheckInRoomSize1 = tk.Radiobutton(self, text=2,value=2,variable=select_rooms)
        CheckInRoomSize2 = tk.Radiobutton(self, text=3,value=3,variable=select_rooms)
        CheckInRoomSize3 = tk.Radiobutton(self, text=4,value=4,variable=select_rooms)
        
        CheckInRoomSizeLabel.grid(column=0, row=3, padx=2, pady=2)
        CheckInRoomSize1.grid(column=1, row=3, padx=2, pady=2)
        CheckInRoomSize2.grid(column=2, row=3, padx=2, pady=2)
        CheckInRoomSize3.grid(column=3, row=3, padx=2, pady=2)


        CheckInFirstNameLabel = tk.Label(self, text="Firstname")
        CheckInLastNameLabel = tk.Label(self, text="Lastname")
        CheckInFirstName = tk.Entry(self)
        CheckInLastName = tk.Entry(self)
        
        CheckInFirstNameLabel.grid(column=0, row=0, padx=2, pady=2)
        CheckInLastNameLabel.grid(column=0, row=1, padx=2, pady=2)
        CheckInFirstName.grid(column=1, row=0, padx=2, pady=2)
        CheckInLastName.grid(column=1, row=1, padx=2, pady=2)

        CheckInSubmitButton = Button(self, text="Submit", command=SubmitCommand)
        

        CheckInSubmitButton.grid(column=1, columnspan=2, row=4, padx=2, pady=2)


class Page2(Page):
   def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        def SearchCommand():
            with open("json/Guests.json") as f:
                data = json.load(f)
    
            for Guests in data["Guests"]:
                if SearchGuest.get() == Guests["First"] or SearchGuest.get() == Guests["TelNmr"] or SearchGuest.get() == Guests["Last"]:
                    print("Yes")
                    del Guests

                else:
                    print("no")

            with open("json/Guests.json", "w") as f:
                json.dump(data, f, indent = 2)

        SearchGuestLabel = tk.Label(self, text="Search for Telephonenumber")
        SearchGuest = tk.Entry(self)
        SearchGuestButton = tk.Button(self, text="Search", command = SearchCommand)

        SearchGuestLabel.pack(padx=2, pady=2)
        SearchGuest.pack(padx=2, pady=2)
        SearchGuestButton.pack(padx=2, pady=2)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       
       def ShowAllCommand():
            with open("json/Guests.json") as f:
                data = json.load(f)
            print(data)
            for _ in data["Guests"]:
               Person = str("Name: " + _['First'] + " " + _["Last"] + "Telephone: " + _["TelNmr"])
               GuestLabel = tk.Label(self, text = Person)
               GuestLabel.pack(anchor=W, padx=2, pady=2)


       ShowAllButton = tk.Button(self, text="Show Rooms", command = ShowAllCommand)

       ShowAllButton.pack(anchor=NW, padx=2, pady=2)

class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 4")
        label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Check in", command=p1.show)
        b2 = tk.Button(buttonframe, text="Check out", command=p2.show)
        b3 = tk.Button(buttonframe, text="List guests", command=p3.show)
        b4 = tk.Button(buttonframe, text="Edit guests", command=p4.show)

        b1.grid(row=0, column=0, padx=17, pady=3)
        b2.grid(row=0, column=1, padx=17, pady=3)
        b3.grid(row=0, column=2, padx=17, pady=3)
        b4.grid(row=0, column=3, padx=17, pady=3)

        p1.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.geometry("400x400")
    root.resizable(False,False)
    root.mainloop()