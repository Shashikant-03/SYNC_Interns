import tkinter
import time

def Set_alaram():
    alarm_time = entry.get()
    if Check(alarm_time):
        start_timer(alarm_time)
         
def Check(alarm_time):
    try :
        time1 = time.strptime(alarm_time, "%H:%M")
        result.config(text="Alarm Has Been set on : "+ str(time1.tm_hour)+" : "+str(time1.tm_min))
        return True
    except:
        result.config(text= "Enter the time as Hour : Minute In 24 hour clock")
        return False

def start_timer(alarm_time):
    current_time = time.strftime("%H:%M")
    if current_time == alarm_time:
        result.config(text="Wake up!")
    else:
        root.after(1000, lambda: start_timer(alarm_time))
    
root = tkinter.Tk()
root.title("Alarm Clock")

label = tkinter.Label(root,text = "Alarm Clock",background="Light Blue",font=("Times New Roman",37))
label.pack(fill="both")

entry = tkinter.Entry(root,font=("Times New Roman",20))
entry.place(x=600,y=160)

submit = tkinter.Button(root,text = "Set Alarm",command= Set_alaram,width=10)
submit.place(x=700,y=200)

result = tkinter.Label(text="",font=("Times New Roman",20))
result.place(x=600,y=250)

root.mainloop()