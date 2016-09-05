import tkinter as tk
from tkinter import ttk


LARGE_FONT= ('Verdana', 12)



class GUIBrewapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        #tk.Tk.iconbitmap(self, default="logo.ico")
        tk.Tk.wm_title(self, "GUI Brew")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        PhotoImage = ("/home/dustin/Documents/GuiBrew/GUIBrewdesktop.png")
        container.create_image(10, 10, image = image, anchor = NW)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label  = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text='Page One',
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button1 = ttk.Button(self, text='Page Two',
                            command=lambda: controller.show_frame(PageTwo))
        button1.pack()

        button1 = ttk.Button(self, text='Quit',
                            command=lambda: destroy(frame.self))
        button.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Back to Home',
                                command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button1 = ttk.Button(self, text='Page Two',
                            command=lambda: controller.show_frame(PageTwo))
        button1.pack()
        


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label  = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text='Home',
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button1 = ttk.Button(self, text='Page One',
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label  = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text='Home',
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button1 = ttk.Button(self, text='Page One',
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()


    

app = GUIBrewapp()
app.mainloop()
