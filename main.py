import tkinter
from pytube import YouTube

root = tkinter.Tk()
root.title("Youtube Downloader")
root.geometry("500x300")
root.resizable(0, 0)

tkinter.Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()

link = tkinter.StringVar()
tkinter.Label(root, text='Paste link here:', font='arial 15 bold').place(x=160, y=60)
tkinter.Entry(root, width=70, textvariable=link).place(x=32, y=90)

