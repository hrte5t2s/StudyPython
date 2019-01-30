import tkinter

MainForm = tkinter.Tk()
MainForm.geometry("250x150")
MainForm.title("this is title!")
MainForm['background'] = 'LightSlateGray'
btn_1 = tkinter.Button(MainForm, text="exit")
btn_1.pack()

MainForm.mainloop()