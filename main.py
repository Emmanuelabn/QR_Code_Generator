import pyqrcode as qr
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk


def btn_browse_cmd():
    path = filedialog.askdirectory(title="Select a File")
    tBoxBrowse.delete(1.0, END)
    tBoxBrowse.insert('end', path)


def btn_generate_cmd():
    link = tBoxLink.get("1.0", "end-1c")
    file = qr.create(link)
    file_name = "/myQr.png"
    path = tBoxBrowse.get("1.0", "end-1c")
    path += file_name
    print(link, path)
    file.png(path, scale=8)
    file.show()


# Define the main Window
win = Tk()
win.geometry("660x300")
win.title("QR Generator")
win.iconbitmap("QRicon.ico")
win.resizable(False, False)

# Window title
lblTitle = Label(win, text="QR Code Generator", font='Aerial 18 bold')
lblTitle.pack(pady=20)

# Link Instructions
lblLink = Label(win, text="Paste the link: ")
lblLink.pack(pady=20)
lblLink.place(x=30, y=150)

# Text Box to paste a link
tBoxLink = Text(win, height=1, width=40)
tBoxLink.pack(expand=True)
tBoxLink.config(state='normal')
tBoxLink.place(x=210, y=150)
tBoxLink.insert('end', "https://github.com/Emmanuelabn")

btnConvert = ttk.Button(win, text="Generate", command=btn_generate_cmd)
btnConvert.pack(ipadx=5, pady=15)
btnConvert.place(x=550, y=147)

# Browsing Instructions
lblBrowse = Label(win, text="Choose a location for your QR: ")
lblBrowse.pack(pady=20)
lblBrowse.place(x=30, y=100)

# Text Box to paste/choose directory
tBoxBrowse = Text(win, height=1, width=40)
tBoxBrowse.pack(expand=True)
tBoxBrowse.config(state='normal')
tBoxBrowse.place(x=210, y=100)
tBoxBrowse.insert('end', os.getcwd().replace('\\', '/'))

# Button that opens a folder dialog
btnBrowse = ttk.Button(win, text="Browse", command=btn_browse_cmd)
btnBrowse.pack(ipadx=5, pady=15)
btnBrowse.place(x=550, y=97)

# image
temp = Image.open("githubQR.png").resize((75, 75), Image.ANTIALIAS)
bgImage = ImageTk.PhotoImage(temp)
lblImage = ttk.Label(image=bgImage)
lblImage.image = bgImage
lblImage.place(x=20, y=200)

separator = ttk.Separator(
    master=win,
    orient=HORIZONTAL,
    style='TSeparator',
    class_=ttk.Separator,
    takefocus=1,
    cursor='plus'
)
lblCredits = Label(win, text="Created by Emmanuel Abdelnour\n\n\nScan The QR to see my projects☺")
lblCredits.pack(pady=20)
lblCredits.place(x=100, y=205)
separator.pack(fill=X, expand=True)

win.mainloop()
