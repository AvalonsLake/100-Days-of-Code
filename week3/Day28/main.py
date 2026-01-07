from tkinter import *
import math

# --------------------------------- Constants(Change at your own risk) ---------------------------------------------#
PINK = "#e2979c"
RED = "#E7305B"
GREEN = "#9BDEAC"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
work_min = 25
short_break_min = 5
long_break_min = 20
reps = 0
timer = None

# ------------------------------------ Timer Reset Functions ---------------------------------------------#

def timer_reset():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="", fg=GREEN, bg=YELLOW)
    reps = 0

# ----------------------------------------- Timer Setup ---------------------------------------------#

def start_timer():
    global reps
    reps += 1
    work_sec = work_min * 60
    short_break_sec = short_break_min * 60
    long_break_sec = long_break_min * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        # count_down(2) <--- for testing
        timer_label.config(text="Break", fg=PINK, bg=YELLOW)
    else:
        count_down(work_sec)
        # count_down(3) <--- for testing
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW)


# -------------------------------------- Countdown functions ---------------------------------------------#

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks =""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks +="✔"
            check_mark.config(text=marks)




# ------------------------------------------- UI setup ---------------------------------------------#
window = Tk()

window.title("Kamatis")
window.config(padx=100, pady=50, bg=YELLOW)

window.after(1000,)

canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
kamatis_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=kamatis_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1, columnspan=3)

timer_label = Label(window, text="Timer", font= (FONT_NAME, 35), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0, columnspan=3)

start_btn = Button(window, text='Start', command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(window, text='Reset', command=timer_reset)
reset_btn.grid(column=4, row=2)

check_mark = Label(window, text="", font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
check_mark.grid(column=2, row=3)

window.mainloop()