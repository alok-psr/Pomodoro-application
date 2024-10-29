
from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#399918"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 10/60
SHORT_BREAK_MIN = 5/60
LONG_BREAK_MIN = 8/60
REPS=0
CYCLES_COMPLETED=0
timer=None


# ---------------------------- TIMER RESET ------------------------------- #
def Reset():
    global REPS, CYCLES_COMPLETED
    tk.after_cancel(timer)
    can.itemconfig(cur_time,text='00:00')
    tit.config(text='')
    marker.config(text='')
    REPS=0
    CYCLES_COMPLETED=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def clock(count):
    global REPS,CYCLES_COMPLETED
    sh_br=SHORT_BREAK_MIN*60
    lg_br=LONG_BREAK_MIN*60
    wrk=WORK_MIN*60
    global timer
    if REPS in [0,2,4,6,8]and count ==0:
        tk.attributes('-topmost',False)
        count=wrk
        REPS+=1
        tit.config(text=f'WORKING ')

    elif REPS in [1,3,5,7]and count==0:
        tk.attributes('-topmost',True)
        count=sh_br
        REPS+=1
        tit.config(text=f'SHORT BREAK ')
    elif REPS==9 and count ==0:
        REPS=0
        CYCLES_COMPLETED+=1
        count=lg_br
        tit.config(text=f'LONG BREAK ')
        marker.config(text='✔️'*CYCLES_COMPLETED)
    can.itemconfig(cur_time, text=f'{count // 60}:{count % 60}')
    if count > 0:
        timer=tk.after(50, clock, count - 1)

# ---------------------------- UI SETUP ------------------------------- #


tk=Tk()
tk.minsize(width=400,height=500)
tk.title('POMODORO CLOCK')
tk.config(background=YELLOW,padx=50,pady=50)

# canvas
can=Canvas(width=220,height=224,bg=YELLOW,highlightthickness=0)
image=PhotoImage(file='tomato.png')
can.create_image(110,112,image=image)
cur_time=can.create_text(110,130,text='00:00',font=(FONT_NAME,35,'bold'),fill='#FAF7F0')
can.grid(row=1,column=1)


# HINT
tit=Label(text='',font=(FONT_NAME,25,'bold'),bg=YELLOW,fg=GREEN)
tit.grid(row=4,column=1)

# HEADING [TIMER]
heading=Label(text='Timer',font=(FONT_NAME,35,'bold'),bg=YELLOW,fg=GREEN)
# heading.place(x=150,y=30)
heading.grid(row=0,column=1)


#button to start the timer
def Start():
    tit.config(text=f'WORKING ')
    clock(0)

start=Button(text='START',font=(FONT_NAME,15,'bold'),bg=YELLOW,fg=PINK,activeforeground=YELLOW,activebackground=RED,command=Start)
start.grid(row=2,column=0)




# button to reset
reset=Button(text='RESET',font=(FONT_NAME,15,'bold'),bg=YELLOW,fg=PINK,activeforeground=YELLOW,activebackground=RED,command=Reset)
reset.grid(row=2,column=2)


#tick marker
marker=Label(text=' ',font=(FONT_NAME,20,'normal'),bg=YELLOW,fg=GREEN)
marker.grid(row=2,column=1)







tk.mainloop()
