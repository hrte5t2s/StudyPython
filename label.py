import tkinter

Mainfrom = tkinter.Tk()
Mainfrom.title("this is label")
Mainfrom.geometry("400x400")

'''
label
'''
# win：父窗体
# text：显示的文本内容
# bg：背景色
# fg：字体颜色
# font：字体
# wraplength：指定text文本中多宽之后换行
# justify：设置换行后的对齐方式
# anchor：位置 n北，e东，w西，s南，center居中；还可以写在一起：ne东北方向
label = tkinter.Label(
    Mainfrom,
    text="this is label",
    bg="grey", fg="red",
    
    width=20,
    height=10,
    wraplength=100,
    justify='left',
    anchor="center"
)

label.pack()
Mainfrom.mainloop()