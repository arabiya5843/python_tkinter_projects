from tkinter import *

def btn_click(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btn_clear_display():
    global operator
    operator = ""
    text_Input.set("")

def btn_equals_input():
    global operator
    sum = str(eval(operator))
    text_Input.set(sum)
    operator = ""


cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()

txtDisplay = Entry(cal, font = ('arial', 20, 'bold'), textvariable = text_Input, bd = 20, insertwidth = 4,
                   bg = "powder blue",justify = 'right').grid(columnspan = 4)

btn7 = Button(cal,padx=25,pady=29,bd = 10, fg="black", bg = "powder blue",font=('arial', 20, 'bold'),
               text = '7', command = lambda : btn_click(7)).grid(row = 1, column = 0)

btn8 = Button(cal,padx=25,pady=30,bd = 8, fg="black",bg = "powder blue",font=('arial', 20, 'bold'),
               text = '8', command = lambda : btn_click(8)).grid(row = 1, column = 1)

btn9 = Button(cal,padx=25,pady=30, bd = 8, fg="black",bg = "powder blue",font=('arial', 20, 'bold'),
               text = '9', command = lambda : btn_click(9)).grid(row = 1, column = 2)

Addition = Button(cal,padx=24,pady=30, bd = 8, fg="black",bg = "powder blue",font=('arial', 20, 'bold'),
               text = '+', command = lambda : btn_click("+")).grid(row = 1, column = 3)

btn4 = Button(cal,padx=25,pady=30,bd = 8, fg="black", bg = "powder blue",font=('arial', 20, 'bold'),
               text = '4', command = lambda : btn_click(4)).grid(row = 2, column = 0)

btn5 = Button(cal,padx=25,pady=30,bd = 8, fg="black",bg = "powder blue",font=('arial', 20, 'bold'),
               text = '5', command = lambda : btn_click(5)).grid(row = 2, column = 1)

btn6 = Button(cal,padx=25,pady=30, bd = 8, fg="black",bg = "powder blue",font=('arial', 20, 'bold'),
               text = '6', command = lambda : btn_click(6)).grid(row = 2, column = 2)

Subtraction = Button(cal,padx=25, pady = 30,bd = 8, fg="black",bg = "powder blue",font=('arial', 20, 'bold'),
               text = '-', command = lambda : btn_click("-")).grid(row = 2, column = 3)

btn1 = Button(cal,padx=25,pady=30,bd = 8, fg="black", bg = "powder blue",font=('arial', 20, 'bold'),
               text = '1', command = lambda : btn_click(1)).grid(row = 3, column = 0)

btn2 = Button(cal,padx=25,pady=30,bd = 8, fg="black",bg = "powder blue",font=('arial', 20, 'bold'),
               text = '2', command = lambda : btn_click(2)).grid(row = 3, column = 1)

btn3 = Button(cal,padx=25,pady=30, bd = 8, fg="black",bg = "powder blue",font=('arial', 20, 'bold'),
               text = '3', command = lambda : btn_click(3)).grid(row = 3, column = 2)

Multiply = Button(cal,padx=25,pady=30, bd = 8, fg="black",bg = "powder blue",font=('arial', 20, 'bold'),
               text = '*', command = lambda : btn_click("*")).grid(row = 3, column = 3)

btn0 = Button(cal,padx=25,pady=30,bd = 8, fg="black",bg = "powder blue",font=('arial', 20, 'bold'),
               text = '0', command = lambda : btn_click(0)).grid(row = 4, column = 0)

btnClear = Button(cal,padx=25,pady=30, bd = 8, fg="black",bg = "powder blue",font=('arial', 20, 'bold'),
               text = 'C', command = lambda : btn_clear_display()).grid(row = 4, column = 1)

Equals = Button(cal,padx=25, pady=30,bd = 8, fg="black",bg = "powder blue",font=('arial', 20, 'bold'),
               text = '=', command = lambda : btn_equals_input()).grid(row = 4, column = 2)

Division = Button(cal,padx=25, pady=30,bd = 8, fg="black",bg = "powder blue",font=('arial', 20, 'bold'),
               text = '/', command = lambda : btn_click("/")).grid(row = 4, column = 3)


cal.mainloop()