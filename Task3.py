import pyshorteners
import tkinter
import webbrowser

def shorten_url():
    

    shortener = pyshorteners.Shortener()
    url_to_shorten = Url.get()
    shortened_url = shortener.tinyurl.short(url_to_shorten)
    result.config(text="Result : "+ shortened_url)
    openB.config(command=lambda :webbrowser.open(shortened_url),state=tkinter.NORMAL)

root = tkinter.Tk()
root.title("shortner")

label = tkinter.Label(text="URL SHORTNER",background="blue",font=("Times New Roman",37),foreground="White")
label.pack(fill= 'both')


label = tkinter.Label(text="Enter the url : ",font=("Times New Roman",20))
label.place(x=550,y=120)


Url = tkinter.Entry(root,font=("Times New Roman",15),width=50)
Url.place(x=740,y=130)


submit = tkinter.Button(text="Submit",command=shorten_url,font=(9))
submit.place(x=750,y=180)

result = tkinter.Label(root,text="Result",font=("Times New Roman",20))
result.place(x=600,y=250)

openB = tkinter.Button(root,text="Open Link",font=(9),state=tkinter.DISABLED)
openB.place(x=750,y=300)

root.mainloop()