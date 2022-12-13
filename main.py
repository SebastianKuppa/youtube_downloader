import tkinter
from tkinter.filedialog import askdirectory
from pytube import YouTube

# init tkinter window
root = tkinter.Tk()
root.title("Youtube Downloader")
root.geometry("500x300")
root.resizable(False, False)

tkinter.Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()

# label for entering the youtube link
link = tkinter.StringVar()
tkinter.Label(root, text='Paste link here:', font='arial 15 bold').place(x=160, y=60)
tkinter.Entry(root, width=70, textvariable=link).place(x=32, y=90)


def video_downloader():
    # added an empty label widget, for deleting the DOWNLOADED Label after starting new download
    tkinter.Label(root, text=' '*30, font='arial 15').place(x=180, y=200)
    # opens window for the user to enter the download destination path
    path = askdirectory()
    # start downloading the youtube video
    url = YouTube(str(link.get()))
    url_filtered_mp4 = url.streams.filter(mime_type="video/mp4").get_highest_resolution()
    url_filtered_mp4.download(output_path=path)
    # display when download is finished
    tkinter.Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=200)


# button for running video_downloader()
tkinter.Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2,
               command=video_downloader).place(x=180, y=150)


if __name__ == '__main__':
    root.mainloop()
