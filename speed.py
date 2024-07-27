from tkinter import *
import speedtest as stcli

def speedcheck():
    st = stcli.Speedtest()
    st.get_servers()
    down = str(round(st.download()/(10**6),3))+ " Mbps"
    up = str(round(st.upload()/(10**6),3))+ " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("700x700")
sp.config(bg="white")

lab = Label(sp, text="Internet Speed Test", font=("Times New Roman", 50, "bold"), bg="white", fg="red")
lab.place(x=40, y=40, height=60, width=620)

lab_download = Label(sp, text="Download Speed", font=("Times New Roman", 30, "bold"), bg="white", fg="red")
lab_download.place(x=40, y=130, height=60, width=620)

lab_down = Label(sp, text="00", font=("Times New Roman", 50, "bold"), bg="white", fg="red")
lab_down.place(x=40, y=200, height=60, width=620)

lab_upload = Label(sp, text="Upload Speed", font=("Times New Roman", 30, "bold"), bg="white", fg="red")
lab_upload.place(x=40, y=300, height=60, width=620)

lab_up = Label(sp, text="00", font=("Times New Roman", 50, "bold"), bg="white", fg="red")
lab_up.place(x=40, y=370, height=60, width=620)

button = Button(sp, text="Check Speed", font=("Times New Roman", 30, "bold"), bg="white", relief=RAISED, command=speedcheck)
button.place(x=40, y=450, height=60, width=620)

sp.mainloop()
