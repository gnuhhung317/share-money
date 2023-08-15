from tkinter import *
from tkinter import messagebox
class GUI:
    def __init__(self) -> None:
        self.truong_money = 0
        self.tuan_money = 0
        self.hung_money = 0

        self.hung_entry = None
        self.truong_entry = None
        self.tuan_entry = None

        self.hung_get_money = 0
        self.truong_get_money = 0
        self.tuan_get_money = 0

        self.entire_money = 0

        self.win = None
        self.create_window()
    def create_window(self):
        self.win = Tk()
        self.win.geometry("1200x700")
        self.win.iconbitmap("hacker.ico")
        self.win.bind("<Left>",self.select_previous_entry)
        self.win.bind("<Right>",self.select_next_entry)
        title = Label(self.win,text="Tính tiền",font=("Arial",20))
        title.pack()

        frame = Frame(self.win)
        frame.pack()

        hung_label = Label(frame, text= "Hùng",font=("Arial",16))
        hung_label.grid(row=0,column=0,padx=20,pady=20)
        self.hung_entry = Entry(frame,font=("Arial",16))
        self.hung_entry.grid(row = 1, column=0,padx=20,pady=20)
        self.hung_entry.focus()

        tuan_label = Label(frame,text="Tuấn",font=("Arial",16))
        tuan_label.grid(column=1,row = 0,padx=20,pady=20)
        self.tuan_entry = Entry(frame, font=("Arial",16))
        self.tuan_entry.grid(row = 1, column=1,padx=20,pady=20)

        truong_label = Label(frame,text="Trường",font=("Arial",16))
        truong_label.grid(row=0,column=2,padx=20,pady=20)
        self.truong_entry = Entry(frame,font=("Arial",16))
        self.truong_entry.grid(row=1,column=2,padx=20,pady=20)

        calculate_button = Button(self.win,text="Tính toán",width=20,height=3,command=self.caculate)
        calculate_button.pack()
        self.win.bind("<Return>",self.click_button)
        self.result = Text(self.win,font=("Arial",18),fg="blue",yscrollcommand=True)
        self.result.pack(padx=50,pady=10)

        self.entries = [self.hung_entry,self.tuan_entry,self.truong_entry]

        self.win.mainloop()
    def click_button(self,event):
        self.caculate()
    def caculate(self):
        self.result.delete("1.0",END)
        self.get_money()
        list_name = ["Hùng","Tuấn","Trường"]
        list_get_money = [self.hung_get_money,self.tuan_get_money,self.truong_get_money]
        for name,money in zip(list_name,list_get_money):
            verb = "nhận"
            if (money>=0):
                verb = "nộp"
            else:
                money = -money
            statement = f"{name} {verb} {money}"
            self.result.insert(END,f"{statement}\n")

    def get_money(self):
        try:
            self.hung_money = int(self.hung_entry.get()) 
            self.truong_money = int(self.truong_entry.get()) 
            self.tuan_money = int(self.tuan_entry.get()) 
            self.entire_money = self.hung_money + self.truong_money + self.tuan_money
            avg = self.entire_money/3
            self.hung_get_money =round( avg - self.hung_money,2)
            self.truong_get_money = round(avg - self.truong_money,2)
            self.tuan_get_money = round(avg - self.tuan_money,2)
        except:
            messagebox.showerror("Error","Check the input")
    
    def select_next_entry(self,event):
        current_index = self.entries.index(self.win.focus_get())
        next_index = (current_index +1)%len(self.entries)
        self.entries[next_index].focus()
    def select_previous_entry(self,event):
        current_index = self.entries.index(self.win.focus_get())
        next_index = (current_index -1)%len(self.entries)
        self.entries[next_index].focus()
    

gui = GUI()