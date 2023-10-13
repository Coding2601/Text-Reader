from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image
import tkinter as tk
from PIL import ImageTk
import pyttsx3
import PyPDF2

engine = pyttsx3.init()

root = Tk()
root.title("Text Reader")
root.geometry('1100x900')
frame = Frame(root, borderwidth=8)
Label(frame, text="TEXT READER",fg='grey',font="Times 33 bold italic").pack(side=TOP)
frame.place(x=480, y=10)

askVol = tk.Label(root, text="Volume: ", font=("Aerial", 17))
askVol.place(x=450, y=237)
setVol = tk.Entry(root, width=10, font=("Aerial", 20))
setVol.place(x=550, y=237)
setVol.insert(0, "100")

def setVolume():
    engine.setProperty('volume', float(int(setVol.get()))/100)

def clear_text_box():
    my_text.delete(1.0, END)

def setEditable():
    my_text.config(state="normal")

def save_file():
    file = filedialog.asksaveasfile(defaultextension= ".txt",
                            filetypes=[("Text file", ".txt"),
                                       ("HTML file", ".html"), ("PDF file",".pdf"), ("All files", ".*")])
    file_text = str(my_text.get(1.0, END))
    file.write(file_text)
    file.close()

def speak_text():
    engine.setProperty('voice', voices[v.get()-1].id)
    engine.say(my_text.get(1.0, "end-1c"))
    engine.runAndWait()

setVolBut = tk.Button(root, text="SET", font=("Aerial"), relief="groove", command=setVolume)
setVolBut.place(x=720, y=237)

LsetRate = tk.Label(root, text="Rate: ", font=('Aerial', 17))
LsetRate.place(x=850, y=237)
setRateT = tk.Entry(root, width=10, font=("Aerial", 20))
setRateT.place(x=920, y=237)
setRateT.insert(0, "130")

def setRate():
    engine.setProperty('rate', int(setRateT.get()))

setRateBut = tk.Button(root, text="SET", font=("Aerial"), relief="groove", command=setRate)
setRateBut.place(x=1090, y=237)

voices = engine.getProperty('voices')

v = tk.IntVar() 
v.set(1)

my_text = Text(root, height=20, width=155)
my_text.place(x=18, y=300)

def open_pdf():
    global page_stuff
    try:
        open_file = filedialog.askopenfilename(initialdir="C/",
                                                filetypes=[("PDF files", "*.pdf"), ("All Files", '*.*')])
        if open_file:
            pdf_file = PyPDF2.PdfReader(open_file)
            num_pages = len(pdf_file.pages)
            page_stuff = ''
            for i in range(num_pages):
                page = pdf_file.pages[i]
                page_stuff += page.extract_text()
            my_text.insert(1.0, page_stuff)
            browse_text.set("UPLOAD FILE")
            my_text.config(state="disabled")
    except:
        my_text.destroy()
        Label(root, text="Not Able to Load the File", font=("Aerial", 17, "bold"), fg='red')

browse_text = StringVar()
button = Button(root, textvariable= browse_text, relief="flat", command=open_pdf, bg='pink',font="Raleway", fg="black",height=3,width=16,compound="center")
browse_text.set("UPLOAD FILE")
button.place(x=30, y=110)

button_text = StringVar()
button2 = Button(root, text="EDIT", relief="groove", bg='light blue', font="Raleway",fg="black", height=3,width=16,command=setEditable)
button_text.set("EDIT")
button2.place(x=380 , y=110)

button4 = Button(root, text="SPEAK", relief="groove", height=3, width=15, bg='snow', font="Raleway",fg="black",command=speak_text)
button4.place(x=750, y=110)

button4 = Button(root, text="SAVE", relief="groove", height=3, width=15,bg='snow', font="Raleway", fg="black", command=save_file)
button4.place(x=1080, y=110)

voiceLabel = tk.Label(root, text="Choose voice: ", font=("Aerial", 17, "bold"))
voiceLabel.place(x=20, y=237)

a = tk.Radiobutton(root, text="David", variable=v, value=1, font=("Aerial", 17))
a.place(x=200, y=237)
b = tk.Radiobutton(root, text="Zira", value=2, variable=v, font=("Aerial", 17))
b.place(x=315, y=237)

root.mainloop()