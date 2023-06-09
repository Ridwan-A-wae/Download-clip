from tkinter import *
from pytube import YouTube
from moviepy.editor import *


root = Tk()
root.title("Youtube Downloader")
canvas = Canvas(root,width=400,height=200)
canvas.pack()

def download():
    video_path = link.get()
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)
    video_clip.close()


app_title = Label(root,text="ดาวน์โหลดวิดีโอจากยูทูป",font=("Arial",20,"bold"))
canvas.create_window(200,30,window=app_title)

label = Label(root,text="ป้อนลิ้งค์วิดีโอ (URL)")
canvas.create_window(200,80,window=label)

link = Entry(root,width=60)
canvas.create_window(200,100,window=link)

btn = Button(root,text="ดาวน์โหลด",command=download)
canvas.create_window(200,150,window=btn)


root.mainloop()