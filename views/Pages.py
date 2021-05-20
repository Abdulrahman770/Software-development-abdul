import tkinter as tk
import pandas as pd
from tkinter import *
from functionalities.authenticate import Authenticate
from functionalities.crud import *

LARGE_FONT = ("Verdana", 12)
USER_DATA_PATH = "./data/users.csv"


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Login", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label1 = tk.Label(self, text="Enter your user Id")
        label1.pack(pady=10)

        userIdInput = tk.Entry(self, width=30)
        userIdInput.pack(pady=5)

        button = tk.Button(self, text="Login", width=15, height=1,
                           command=lambda: self.redirectUser(userIdInput.get()))
        button.pack(pady=30)

        # button2 = tk.Button(self, text="Visit Page 2",
        #                     command=lambda: controller.show_frame(ManagerPage))
        # button2.pack()
        #
        # button3 = tk.Button(self, text="Visit Page 2",
        #                     command=lambda: controller.show_frame(AdminPage))
        # button3.pack()

    def redirectUser(self, userId):
        [b, t] = Authenticate.auth(userId)
        if (b != -1):
            if (t == 1):
                self.controller.show_frame(UserPage)
            elif (t == 2):
                self.controller.show_frame(ManagerPage)
            elif (t == 3):
                self.controller.show_frame(AdminPage)


class ManagerPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="User", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        l1 = tk.Label(self, text="Create Thoroughfare")
        l1.pack(pady=10)

        lb1=tk.Label(self, text="Thoroughfare Type")
        lb1.pack()
        e1 = tk.Entry(self )
        e1.pack()
        lb2 = tk.Label(self, text="Thoroughfare Type")
        lb2.pack()
        e2 = tk.Entry(self)
        e2.pack()
        b1 = tk.Button(self, text="Add")
        b1.pack()

        l2 = tk.Label(self, text="Create Properties")
        l2.pack(pady=10)

        l3 = tk.Label(self, text="Generate Invoice")
        l3.pack(pady=10)

        l4 = tk.Label(self, text="Print Invoice")
        l4.pack(pady=10)




class AdminPage(tk.Frame):
    estateLs = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.viewEstate()
        label = tk.Label(self, text="Admin", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label1 = tk.Label(self, text="Create Estate")
        label1.pack(pady=10)
        l2 = tk.Label(self, text="Name")
        l2.pack()
        e2 = tk.Entry(self)
        e2.pack()
        l3 = tk.Label(self, text="Conatact")
        l3.pack()
        e3 = tk.Entry(self)
        e3.pack()
        l4 = tk.Label(self, text="Manager")
        l4.pack()
        e4 = tk.Entry(self)
        e4.pack()
        l5 = tk.Label(self, text="Location")
        l5.pack()
        e5 = tk.Entry(self)
        e5.pack()

        button = tk.Button(self, text="Add",
                           command=lambda: self.createEstate(e2.get(), e3.get(), e4.get(), e5.get()))
        button.pack(pady=5)
        lb1 = tk.Label(self, text="View Estates:")
        lb1.pack(pady=10)

        for i in range(len(self.estateLs)):
            ll = tk.Label(self, text=self.estateLs[i][0] + " " + self.estateLs[i][1] + " " + self.estateLs[i][2] + " " + self.estateLs[i][3])
            ll.pack()

        lp = tk.Label(self, text="Add manager and User")
        lp.pack(pady=10)
        l6 = tk.Label(self, text="Type 1, 2 or 3")
        l6.pack()
        e6 = tk.Entry(self)
        e6.pack()
        l7 = tk.Label(self, text="Estate")
        l7.pack()
        e7 = tk.Entry(self)
        e7.pack()
        buttona = tk.Button(self, text="Add",
                           command=lambda: self.createUser(e6.get(), e7.get()))
        buttona.pack(pady=5)

    def createUser(self, type, estate):
        if(type!="" or estate!=""):
            AdminCrud().createUser(type, estate)

    def createEstate(self, name, contact, manager, location):
        if name != "" or contact != "" or manager != "" or location != "":
            AdminCrud().createEstate(name, contact, manager, location)
            self.viewEstate()

    def viewEstate(self):
        self.estateLs = AdminCrud().viewEstate()


class UserPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
