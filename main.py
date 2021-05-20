import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('800x600')
        self.title('Estate Management')


app = Application()
app.mainloop()
