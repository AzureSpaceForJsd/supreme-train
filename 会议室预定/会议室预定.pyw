from tkinter import *
import tkinter as tk
import tkinter.messagebox
import control

class App:
    def __init__(self,root):
    


        self.labelStrat = tk.Label(root,text="起始时间：")
        self.labelEnd = tk.Label(root,text="结束时间：")
        self.labelmeetingRoom = tk.Label(root,text="会议室：")
        self.sbmeetingRoom = tk.Spinbox(root,values=mtRoom)

        self.labelStrYear = tk.Label(root,text="年：")
        self.sbStrYear = tk.Spinbox(root,from_=2020,to=2030)

        self.labelStrMonth = tk.Label(root,text="月：")
        self.sbStrMonth = tk.Spinbox(root,from_=1,to=12)

        self.labelStrDay = tk.Label(root,text="日：")
        if(self.sbStrMonth.get() in ["1","3","5","7","8","10","12"]):
            self.sbStrDay = tk.Spinbox(root,from_=1,to=31)
        else:
            if(self.sbStrMonth.get() in ["2"]):
                self.sbStrDay = tk.Spinbox(root,from_=1,to=28)
            else:
                self.sbStrDay = tk.Spinbox(root,from_=1,to=30)
        
        self.labelStrHour = tk.Label(root,text="时：")
        self.sbStrHour = tk.Spinbox(root,from_=0,to=24)

        self.labelStrMinute = tk.Label(root,text="分：")
        self.sbStrMinute = tk.Spinbox(root,from_=0,to=60)

        self.labelEndYear = tk.Label(root,text="年：")
        self.sbEndYear = tk.Spinbox(root,from_=2020,to=2030)

        self.labelEndMonth = tk.Label(root,text="月：")
        self.sbEndMonth = tk.Spinbox(root,from_=1,to=12)

        self.labelEndDay = tk.Label(root,text="日：")
        if(self.sbEndMonth.get() in ["1","3","5","7","8","10","12"]):
            self.sbEndDay = tk.Spinbox(root,from_=1,to=31)
        else:
            if(self.sbEndMonth.get() in ["2"]):
                self.sbEndDay = tk.Spinbox(root,from_=1,to=28)
            else:
                self.sbEndDay = tk.Spinbox(root,from_=1,to=30)
        
        self.labelEndHour = tk.Label(root,text="时：")
        self.sbEndHour = tk.Spinbox(root,from_=0,to=24)

        self.labelEndMinute = tk.Label(root,text="分：")
        self.sbEndMinute = tk.Spinbox(root,from_=0,to=60)
        
        self.reserve = tk.Button(root,text="预约",fg="black",command = self.roomReserve)
        
        self.labelStrYear.grid(row=0, column=1, padx=10, pady=5)
        self.sbStrYear.grid(row=0, column=2, padx=10, pady=5)
        self.labelStrMonth.grid(row=0, column=3, padx=10, pady=5)
        self.sbStrMonth.grid(row=0, column=4, padx=10, pady=5)
        self.labelStrDay.grid(row=0, column=5, padx=10, pady=5)
        self.sbStrDay.grid(row=0, column=6, padx=10, pady=5)
        self.labelStrHour.grid(row=0, column=7, padx=10, pady=5)
        self.sbStrHour.grid(row=0, column=8, padx=10, pady=5)
        self.labelStrMinute.grid(row=0, column=9, padx=10, pady=5)
        self.sbStrMinute.grid(row=0, column=10, padx=10, pady=5)
        
        self.labelEndYear.grid(row=2, column=1, padx=10, pady=5)
        self.sbEndYear.grid(row=2, column=2, padx=10, pady=5)
        self.labelEndMonth.grid(row=2, column=3, padx=10, pady=5)
        self.sbEndMonth.grid(row=2, column=4, padx=10, pady=5)
        self.labelEndDay.grid(row=2, column=5, padx=10, pady=5)
        self.sbEndDay.grid(row=2, column=6, padx=10, pady=5)
        self.labelEndHour.grid(row=2, column=7, padx=10, pady=5)
        self.sbEndHour.grid(row=2, column=8, padx=10, pady=5)
        self.labelEndMinute.grid(row=2, column=9, padx=10, pady=5)
        self.sbEndMinute.grid(row=2, column=10, padx=10, pady=5)
        self.reserve.grid(row=1, column=11, padx=10, pady=5)
        self.labelmeetingRoom.grid(row=1, column=0, padx=10, pady=5)
        self.sbmeetingRoom.grid(row=1, column=0, padx=10, pady=5)
        self.labelStrat.grid(row=0, column=0, padx=10, pady=5)
        self.labelEnd.grid(row=2, column=0, padx=10, pady=5)

    def roomReserve(self):
        strYmd = self.sbStrYear.get() + control.zeroPad(self.sbStrMonth.get()) + control.zeroPad(self.sbStrDay.get())
        strHm = control.zeroPad(self.sbStrHour.get()) + control.zeroPad(self.sbStrMinute.get())
        endYmd = self.sbEndYear.get() + control.zeroPad(self.sbEndMonth.get()) + control.zeroPad(self.sbEndDay.get())
        endHm = control.zeroPad(self.sbEndHour.get()) + control.zeroPad(self.sbEndMinute.get())
        resFlag = control.dateCheck(strYmd,strHm,endYmd,endHm,self.sbmeetingRoom.get())
        if resFlag == 0:
            control.insertReserve(strYmd,strHm,endYmd,endHm,self.sbmeetingRoom.get())
            tk.messagebox.showinfo(title = "预定信息",message = "预定成功")
        else:
            tk.messagebox.showinfo(title = "预定信息",message = "该时间段已经被占用，请重新选择")

mtRoom = control.setMeetingRoom();
root = tk.Tk()
root.title("会议室预定系统")
app = App(root)

root.mainloop()
    
