import tkinter as tk
from views.Pages import *
from functionalities.gen import Gen
import pandas as pd


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Estate Management')
        self.geometry("800x600")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, UserPage, ManagerPage, AdminPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#
app = Application()
app.mainloop()


# df = pd.read_csv('./data/data.csv')
# # newId = Gen.ranGen()
# ls = ["Tailor's Vila", "+1-5675595551", 'Paul', 'Ohio']
# # df = pd.DataFrame([ls], columns=['name', 'contact', 'manager', 'location'])
# dd = pd.DataFrame([ls], columns=['name', 'contact', 'manager', 'location'])
# df = df.append(dd, ignore_index=True)
# df.to_csv('./data/data.csv', index=False)
