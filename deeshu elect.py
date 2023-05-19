#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import time
import threading
import winsound

class Switch:
    def __init__(self, master, row, col):
        self.state = False
        self.timer = None
        self.time_remaining = 0

        self.frame = tk.Frame(master)
        self.frame.grid(row=row, column=col)

        self.switch_label = tk.Label(self.frame, text=f"Switch {row * 4 + col + 1}")
        self.switch_label.pack()

        self.switch_button = tk.Button(self.frame, text="Off", command=self.toggle_state)
        self.switch_button.pack()
        
        
        self.timer_label = tk.Label(self.frame)
        self.timer_label.pack()

        self.timer_button = tk.Button(self.frame, text="Set Timer", command=self.set_timer)
        self.timer_button.pack()

    def toggle_state(self):
        self.state = not self.state
        if self.state:
            self.switch_button.config(text="On",bg='green',padx=20,pady=20)
        else:
            self.switch_button.config(text="Off",bg='red',padx=20,pady=20)
    
    def set_timer(self):
        if self.timer:
            self.timer.cancel()
        
        self.time_remaining = 5
        self.update_timer_label()
        self.timer = threading.Timer(5, self.timer_up)
        self.timer.start()
    
    def update_timer_label(self):
        seconds = self.time_remaining % 5
        self.timer_label.config(text=f"{seconds:02d}")
        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.timer_label.after(1000, self.update_timer_label)
    
    def timer_up(self):
        self.timer = None
        self.toggle_state()
        winsound.Beep(1000, 500)
        self.timer_label.config(text="ALERT: Timer has ended!!!",fg='red')
        

class Application:
    def __init__(self, master):
        self.master = master
        self.switches = []
        for i in range(4):
            for j in range(4):
                switch = Switch(master, i, j)
                self.switches.append(switch)
        
        all_on_button = tk.Button(master, text="All On", command=self.all_on,bg='green',padx=30,pady=30)
        all_on_button.grid(row=4, column=0)
        all_on_button = tk.Button(master, text="All On", command=self.all_on,bg='green',padx=30,pady=30)
        all_on_button.grid(row=4, column=0)
        
        all_off_button = tk.Button(master, text="All Off", command=self.all_off,bg='red',padx=30,pady=30)
        all_off_button.grid(row=4, column=1)
        
        all_off_button.grid(row=4, column=2)


    def all_on(self):
        for switch in self.switches:
            switch.state = True
            switch.switch_button.config(text="On",bg='green',padx=20,pady=20)
    
    def all_off(self):
        for switch in self.switches:
            switch.state = False
            switch.switch_button.config(text="Off",bg='red',padx=20,pady=20)


root = tk.Tk()
root.title("SWITCH CONTROL")
root.geometry("1920x1000")
background_image = tk.PhotoImage(file='deeshu.png')
background_label = tk.Label(root,image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
app = Application(root)
root.mainloop()

