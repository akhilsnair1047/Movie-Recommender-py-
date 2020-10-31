from tkinter import Tk, Label, Button, StringVar, Entry, Radiobutton, END, OptionMenu, IntVar, messagebox, PhotoImage, Canvas, GROOVE
from tkinter.ttk import Combobox
import tkinter as tk
from PIL import ImageTk, Image
import password_checker as pc
import Data_b_Func
import os


def M_error():
    messagebox.showinfo(
        "warning", "No Movie Found With Your Combination!!\nPlease try again.")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Main Recommendation Page
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def finallll():

    # Creating master Tkinter window
    root = Tk()

    # Creating object of photoimage class
    p1 = PhotoImage(file=os.path.dirname(
        os.path.abspath(__file__))+r'\icon.png')

    # Setting icon of master window
    root.iconphoto(False, p1)

    loc = os.path.dirname(os.path.abspath(__file__))+r"\main_page_.jpg"
    img = ImageTk.PhotoImage(Image.open(loc))
    l1 = tk.Label(root, image=img)
    l1.pack(side="bottom", fill="both")
    Button(root, text="X", width=4, bg="red", font=10,
           command=root.destroy).place(x=875, y=260)

    def qui():
        root.destroy()
        finallll()

    Label(root, text="Movie Recommender",
          background='black', foreground="yellow",  # headline using lable
          font=("Cooper Black", 30)).place(x=460, y=10)  # grid used for setting position in the GUI

    class Test:  # class for getting information from the user
        def __init__(self, tk):

            self.var = StringVar()
            Label(root, text="Select the Genres :",
                  # grid used for setting position in the GUI
                  font=("Times New Roman", 10), width=30).place(x=410, y=100)
            self.data = ("All", 'Action',
                         'Adventure',
                         'Fantasy',
                         'Science Fiction',
                         'Crime',
                         'Drama',
                         'Thriller',
                         'Animation',
                         'Family',
                         'Western',
                         'Comedy',
                         'Romance',
                         'Horror',
                         'Mystery',
                         'History',
                         'War',
                         'Music',
                         'Documentary',
                         'Foreign',
                         'TV Movie')
            # combobox used for dropdown menu
            self.cb = Combobox(root, values=self.data, width=30)
            # sets the default value 'ALL' from the data refered as 0
            self.cb.current(0)
            self.cb.place(x=660, y=100)  # for setting position in the GUI

            Label(tk, text="Select the language :",  # printing statement
                  font=("Times New Roman", 10), width=30).place(x=410, y=140)
            self.data_l = ('All', 'en', 'es', 'fr', 'it', 'de', 'tr', 'el', 'zh', 'th', 'is', 'ru', 'sv', 'ro', 'ja', 'la', 'hi', 'pt', 'bo', 'fa', 'ur', 'ar', 'sa', 'gd', 'cs',
                           'cn', 'ko', 'no', 'ta', 'nv', 'he', 'da', 'nl', 'af', 'ga', 'so', 'fi', 'sw', 'bg', 'yi', 'vi', 'hu', 'uk', 'eo', 'am', 'km', 'ce', 'pl', 'co', 'pa',
                           'et', 'sq', 'sr', 'bs', 'hr', 'tl', 'sh', 'sk', 'kk', 'ml', 'te', 'cy', 'hy', 'iu', 'wo', 'xh', 'ny', 'st', 'zu', 'kw', 'si', 'ne', 'ps', 'mn', 'xx',
                           'gl', 'ka', 'bn', 'ku', 'mi', 'to', 'ca', 'br', 'dz', 'ky', 'id', 'bm', 'sl'
                           )  # data for language

            # combobox used for dropdown menu language
            self.cl = Combobox(root, values=self.data_l, width=30)
            # default value 'ALL' which is at zeroth position is taken
            self.cl.current(0)
            self.cl.place(x=660, y=140)  # for setting position in the GUI

            Label(tk, text="Select the Rating :",  # printing to select rating
                  font=("Times New Roman", 10), width=30).place(x=410, y=180)
            self.data_rate = ('All', '3',  # data
                              '4', '5', '6', '7', '8', '9', '10')

            self.cr = Combobox(root, values=self.data_rate,
                               width=30)  # dropdown menu
            self.cr.current(0)
            self.cr.place(x=660, y=180)  # setting position in GUI

            Label(tk, text="Select the Run-Time :",
                  font=("Times New Roman", 10), width=30).place(x=410, y=220)
            self.data_time = ('All', '2hr+',
                              '1.5hr+',)

            self.ct = Combobox(root, values=self.data_time, width=30)
            self.ct.current(0)
            self.ct.place(x=660, y=220)

            # button for getting the recommended movie list
            Button(root, text="Get Recommendation",
                   command=self.select, fg='white', bg="green", width=20, font=2).place(x=415, y=260)
            Button(root, text="Reset", width=20,
                   command=qui, fg='white', bg='blue', font=2).place(x=645, y=260)

        def select(self):
            try:
                recommended = Data_b_Func.find_movie_by_genre(self.cb.get(), Data_b_Func.find_movie_by_language(self.cl.get(), Data_b_Func.find_movie_by_rating(
                    "All" if self.cr.get() == "All" else int(self.cr.get()), Data_b_Func.find_movie_by_runtime(self.ct.get(), Data_b_Func.return_orig_df())))).head(5)[["title", "tagline", "popularity", "homepage"]]

                movie_list = recommended.values.tolist()

                e1 = Entry(root, width=65, fg='red',
                           font=('Arial', 10, 'bold'))

                e1.place(x=10, y=340)
                e1.insert(END, "TITLE")

                e1 = Entry(root, width=65, fg='red',
                           font=('Arial', 10, 'bold'))

                e1.place(x=310, y=340)
                e1.insert(END, "TAGLINE")

                e1 = Entry(root, width=65, fg='red',
                           font=('Arial', 10, 'bold'))

                e1.place(x=610, y=340)

                e1.insert(END, "POPULARITY")

                e1 = Entry(root, width=65, fg='red',
                           font=('Arial', 10, 'bold'))

                e1.place(x=910, y=340)

                e1.insert(END, "HOMEPAGE")

                pole = 360

                for i in range(len(movie_list)):
                    oru = 10
                    for j in range(len(movie_list[0])):
                        e = Entry(root, width=60, fg='black',
                                  font=('Arial', 10, 'bold'))

                        e.place(x=oru, y=pole)
                        e.insert(END, movie_list[i][j])
                        oru = oru+300

                    pole = pole+20

            except:
                M_error()

    root.attributes("-fullscreen", True)
    root.title("Movie Recommender")  # title of the program
    Test(root)  # declaring class object
    root.mainloop()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Login Page
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def login():
    # Creating master Tkinter window
    root = Tk()

    # Creating object of photoimage class
    # Image should be in the same folder
    # in which script is saved
    p1 = PhotoImage(file=os.path.dirname(
        os.path.abspath(__file__))+r'\icon.png')

    # Setting icon of master window
    root.iconphoto(False, p1)

    loc = os.path.dirname(os.path.abspath(__file__))+r"\3.jpg"
    img = ImageTk.PhotoImage(Image.open(loc))
    l1 = tk.Label(root, image=img)
    l1.pack(side="bottom", fill="both")

    # this creates 'Label' widget for Registration Form and uses place() method.

    label_0 = Label(root, text="Login Form", width=30,
                    font=("bold", 30), fg='white', bg='black')
    # place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    label_0.place(x=250, y=60)

    class Test:
        def __init__(self, root):
            self.var = StringVar()

            # this creates 'Label' widget for Email and uses place() method.
            label_3 = Label(root, text="Username", width=20,
                            font=("bold", 13), fg='white', bg='black')
            label_3.place(x=420, y=180)

            self.entry_3 = Entry(root, width=30)
            self.entry_3.place(x=600, y=180)

            label_4 = Label(root, text="Password", width=20,
                            font=("bold", 13), fg='white', bg='black')
            label_4.place(x=420, y=230)

            self.entry_4 = Entry(root, width=30)
            self.entry_4.place(x=600, y=230)

            Button(root, text="Sign IN",
                   command=self.select, bg='green', fg='white', width=20, font=7).place(x=480, y=280)
            Button(root, text="X", width=4, bg="red",
                   font=10, command=root.destroy).place(x=720, y=280)

        def select(self):
            """This function performs the following operations:

                    1: Get the value from the Username and Password entry field
                    2: Calls the check_authorisation function with the value
                    3: Fetch the response from the called function"""
            chk = pc.check_authorisation(
                self.entry_3.get(), self.entry_4.get())

            print(chk)

            if(chk == "yes"):
                root.destroy()
                finallll()
            else:
                messagebox.showinfo(
                    "warning", "Please check username or password.\nNew users please Register!!")

    root.attributes("-fullscreen", True)
    root.title("Login Page")
    Test(root)
    root.mainloop()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Registration Page
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def regis():
    # Creating object 'root' of Tk()
    root = Tk()
    # Creating object of photoimage class
    p1 = PhotoImage(file=os.path.dirname(
        os.path.abspath(__file__))+r'\icon.png')

    # Setting icon of master window
    root.iconphoto(False, p1)

    loc = os.path.dirname(os.path.abspath(__file__))+r"\5.jpg"

    img = ImageTk.PhotoImage(Image.open(loc))
    l1 = tk.Label(root, image=img)
    l1.pack(side="top", fill="both")

    root.attributes("-fullscreen", True)

    # Providing title to the form
    root.title('Registration form')

    def valueee():
        pc.enter_autho_details(entry_1.get(), entry_2.get(),
                               entry_3.get(), var.get())

        Label(text="Successfully Registed ", font=(
            "bold", 25), fg='red').place(x=100, y=450)

    # this creates 'Label' widget for Registration Form and uses place() method.
    label_0 = Label(root, text="Registration form",
                    width=20, font=("bold", 30), fg='white', bg='SpringGreen4')
    # place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    label_0.place(x=420, y=100)

    # this creates 'Label' widget for Fullname and uses place() method.
    label_1 = Label(root, text="Full Name", width=20, font=(
        "bold", 10), fg='white', bg='turquoise4')
    label_1.place(x=450, y=200)

    # this will accept the input string text from the user.
    entry_1 = Entry(root, width=30)
    entry_1.place(x=640, y=200)

    # this creates 'Label' widget for Email and uses place() method.
    label_3 = Label(root, text="Email", width=20, font=(
        "bold", 10), fg='white', bg='turquoise4')
    label_3.place(x=450, y=240)

    entry_2 = Entry(root, width=30)
    entry_2.place(x=640, y=240)

    label_3 = Label(root, text="Password", width=20, font=(
        "bold", 10), fg='white', bg='turquoise4')
    label_3.place(x=450, y=280)

    entry_3 = Entry(root, show="*", width=30)
    entry_3.place(x=640, y=280)

    # this creates 'Label' widget for Gender and uses place() method.
    label_4 = Label(root, text="Gender", width=20, font=(
        "bold", 10), fg='white', bg='turquoise4')
    label_4.place(x=450, y=320)

    # the variable 'var' mentioned here holds Integer Value, by deault 0
    var = IntVar()

    # this creates 'Radio button' widget and uses place() method
    Radiobutton(root, text="Male", padx=5, variable=var, fg='white', bg='turquoise4', width=9,
                value=1).place(x=640, y=320)
    Radiobutton(root, text="Female", padx=20,
                variable=var, value=2, fg='white', bg='turquoise4').place(x=750, y=320)

    # this creates button for submitting the details provides by the user
    Button(root, text='Submit', width=20, bg="SteelBlue2", font=5,
           fg='white', command=lambda: [valueee(), root.destroy(), login()]).place(x=450, y=400)
    Button(root, text="X", width=4, bg="red", font=10,
           command=root.destroy).place(x=750, y=400)

    # this will run the mainloop.
    root.mainloop()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Start Page
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


root = Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.attributes("-fullscreen", True)
root.title("Movie Recommender")
# Creating object of photoimage class
p1 = PhotoImage(file=os.path.dirname(os.path.abspath(__file__))+r'\icon.png')

# Setting icon of master window
root.iconphoto(False, p1)
loc = os.path.dirname(os.path.abspath(__file__))+r"\23463.jpg"

img = ImageTk.PhotoImage(Image.open(loc))
l1 = tk.Label(root, image=img)
l1.pack(side="top", fill="both")
Label(root, text="Movie Recommender", foreground="black", bg="grey",  # headline using lable
      font=("Cooper Black", 60)).place(x=300, y=300)

b1 = Button(root, text="SIGN IN", width=20, bg="white", fg='blue',
            command=lambda: [root.destroy(), login()], relief=GROOVE, font=7)
b2 = Button(root, text="SIGN UP", width=20, bg="white", fg='red',
            command=lambda: [root.destroy(), regis()], relief=GROOVE, font=7)
Button(root, text="X", width=4, bg="red", font=10,
       command=root.destroy).place(x=900, y=450)


b1.place(x=400, y=450)
b2.place(x=650, y=450)
root.mainloop()
