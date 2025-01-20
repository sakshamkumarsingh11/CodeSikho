import tkinter
var= tkinter.Tk()
var.title("STUDENT REGESTRATION FORM")
first_textbox= tkinter.Entry(var)
first_textbox.pack()

first_label= tkinter.Label(var, text="Enter your name")
first_label.pack()



second_textbox=tkinter.Entry(var)
second_textbox.pack()

second_label=tkinter.Label(var, text="Enter your class")
second_label.pack()



third_textbox=tkinter.Entry(var)
third_textbox.pack()

third_label=tkinter.Label(var, text="Enter your class")
third_label.pack()

var.mainloop()