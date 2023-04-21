import tkinter
import customtkinter
from pytube import YouTube
# https://www.youtube.com/shorts/AEwwgzB17Ww
def startDownload():
    try:
        ytLInk = linkInput.get()
        ytObject = YouTube(ytLInk,on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title,text_color="white")
        finishLabel.configure(text="")
        finishLabel.configure(text="Yuklash yakunlandi",text_color="blue")
        video.download()
    except: 
        finishLabel.configure(text="Yuklashda xatolik mavjud",text_color="red") 
    
def on_progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text = per + '%')
    pPercentage.update()

    # update progress bar
    progressBar.set(float(percentage_of_completion) / 100)


#System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube playlist yuklovchi")
# sinov qilindi
urlType =customtkinter.CTkLabel(app,text="Formatni tanlang")
urlType.pack(padx=10,pady=10)

onVideo =tkinter.StringVar()
onAudio =tkinter.StringVar()
def checkbox_event():
    videoType = {"video":True,"audio":False}
    if (onVideo.get()) == 'yes':
        videoType.update({"video":True})
    if  (onVideo.get()) == 'no':
        videoType.update({"video":False})
    if  (onAudio.get()) == 'yes':
        videoType.update({"audio":True})
    if  (onAudio.get()) == 'no':
        videoType.update({"audio":False})
       
    print(videoType)


checkbox =customtkinter.CTkCheckBox(app,text="Video",command=checkbox_event, variable=onVideo, onvalue="yes",offvalue="no")
checkbox.pack(padx=10,pady=10)


checkbox1 =customtkinter.CTkCheckBox(app,text="Audio",command=checkbox_event, variable=onAudio, onvalue="yes",offvalue="no")
checkbox1.pack(padx=10,pady=10)


# app UI elements
title = customtkinter.CTkLabel(app,text="Youtube havolani joylang")
title.pack(padx=10,pady=10)

# link input
urlVar = tkinter.StringVar()
linkInput = customtkinter.CTkEntry(app,width=350,height=40,textvariable=urlVar)
linkInput.pack()

# finished downloading
finishLabel = customtkinter.CTkLabel(app,text="")
finishLabel.pack()


# progress percentage
pPercentage = customtkinter.CTkLabel(app,text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app,width=400)
progressBar.set(0)
progressBar.pack(padx=10,pady=10)

# download button
downloadBtn = customtkinter.CTkButton(app,text="Yuklash",command=startDownload)
downloadBtn.pack(padx=10,pady=10)

# run app
app.mainloop()