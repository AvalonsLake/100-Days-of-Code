import tkinter

window = tkinter.Tk()
kilometers = 0
def miles_to_km():
    global kilometers
    miles = float(miles_amount.get())
    kilometers = miles * 1.609
    kilometers_label_1.config(text=kilometers)

window.title("Convert Miles to Kilometers!!")
window.minsize(200, 175)

window.padding = 50

miles_amount = tkinter.Entry(window)
miles_amount.pack()

miles_label = tkinter.Label(window, text="Miles is")
miles_label.pack()

kilometers_label_1 = tkinter.Label(window, text=f"0")
kilometers_label_1.pack()

kilometers_label_2 = tkinter.Label(window, text="Kilometers")
kilometers_label_2.pack()

exit_window = tkinter.Button(window, text="Exit", command=window.quit)
exit_window.pack(side="bottom")

btn = tkinter.Button(window, text="Calculate", command=miles_to_km)
btn.pack(side="bottom")

window.mainloop()