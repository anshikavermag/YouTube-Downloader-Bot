import tkinter as tk
import customtkinter as ck
from pytube import YouTube


def startDownload():
    try:
        ytLink=link.get()
        ytObj=YouTube(ytLink, on_progress_callback=on_progress)
        video= ytObj.streams.get_highest_resolution()
        title.configure(text=ytObj.title, text_color="white")
        finishLabel.configure(text="") #reset 
        video.download()
        finishLabel.configure(text="Downloaded", text_color="green")
    except:
        print("YouTube link is invalid")
        finishLabel.configure(text="Download Error", text_color="red")
#print("Download Complete!") instead of this writing custom donwload complete
        
percent_completed=0
def on_progress(stream, chunk,bytes_remaining):
    total_size=stream.filesize()
    bytes_downloaded= total_size-bytes_remaining
    percent_completed= (bytes_downloaded/total_size)*100
    per=str(int(percent_completed))
    pPercent.configure(text=per+'%')
    pPercent.update()

#System settings
ck.set_appearance_mode("System")
ck.set_default_color_theme("blue")

#My app frame
app= ck.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# adding ui elements
title= ck.CTkLabel(app, text="Insert a YouTube Link")
title.pack(padx=10, pady=10)

#link input
url_var=tk.StringVar()
link=ck.CTkEntry(app,width=350,height=40,textvariable=url_var)
link.pack()

#Finished Downloading
finishLabel=ck.CTkLabel(app,text="")
finishLabel.pack()

#Progress percentage
pPercent=ck.CTkLabel(app,text="0%")
pPercent.pack()
progressBAr=ck.CTkProgressBar(app,width=400)
progressBAr.set(0)
progressBAr.pack(padx=10, pady=10)

#Update Progressbar
progressBAr.set(float(percent_completed)/100)

#Download button
download=ck.CTkButton(app, text="Download", command=startDownload)
download.pack(pady=10, padx=10)

#run app
app.mainloop()



