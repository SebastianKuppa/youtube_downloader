import tkinter
from pytube import YouTube

root = tkinter.Tk()
root.title("Youtube Downloader")
root.geometry("500x300")
root.resizable(False, False)

tkinter.Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()

link = tkinter.StringVar()
tkinter.Label(root, text='Paste link here:', font='arial 15 bold').place(x=160, y=60)
tkinter.Entry(root, width=70, textvariable=link).place(x=32, y=90)


def video_downloader():
    url = YouTube(str(link.get()))
    url_filtered_mp4 = url.streams.filter(mime_type="video/mp4").get_highest_resolution()
    url_filtered_mp4.download()
    tkinter.Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)


tkinter.Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2,
               command=video_downloader).place(x=180, y=150)

root.mainloop()
