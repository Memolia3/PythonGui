from tkinter import *
from tkinter import Label


def click(type):
    if type == "chii":
        print("Chiikawa button clicked.")
        clickWindow = Tk()
        clickWindow.title("ちいかわの説明")
        clickWindow.geometry('500x500')
        clickWindow.resizable(False, False)

        clickFrame = Frame(clickWindow, width=500, height=500, relief='solid')
        clickFrame.propagate(False)
        clickFrame.grid(row=0, column=0)

        clickWindowImage = PhotoImage(file='images/chiikawaWindow.png', master=clickWindow)
        clickCanvas = Canvas(clickFrame, width=500, height=500, bg='white')
        clickCanvas.place(x=0, y=0)
        clickCanvas.create_image(250, 150, image=clickWindowImage)

        clickLabel = Label(clickFrame, text='ちょっぴり泣き虫だけど優しい性格。', font=('HGP創英角ポップ体', 20), fg='#ff3399',
                           bg='white', height=3)
        clickLabel.pack(anchor='center')

        clickWindow.mainloop()
    elif type == "hachi":
        print("hachiware button clicked.")
        clickWindow = Tk()
        clickWindow.title("ハチワレの説明")
        clickWindow.geometry('500x500')
        clickWindow.resizable(False, False)

        clickFrame = Frame(clickWindow, width=500, height=500, relief='solid')
        clickFrame.propagate(False)
        clickFrame.grid(row=0, column=0)

        clickWindowImage = PhotoImage(file='images/chiikawaWindow.png', master=clickWindow)
        clickCanvas = Canvas(clickFrame, width=500, height=500, bg='white')
        clickCanvas.place(x=0, y=0)
        clickCanvas.create_image(250, 150, image=clickWindowImage)

        clickLabel = Label(clickFrame, text='ちいかわのともだち。明るくてポジティブ。', font=('HGP創英角ポップ体', 20), fg='#00aeef',
                           bg='white', height=3)
        clickLabel.pack(anchor='center')

        clickWindow.mainloop()
    elif type == "usa":
        print("usagi button clicked.")
        clickWindow = Tk()
        clickWindow.title("うさぎの説明")
        clickWindow.geometry('500x500')
        clickWindow.resizable(False, False)

        clickFrame = Frame(clickWindow, width=500, height=500, relief='solid')
        clickFrame.propagate(False)
        clickFrame.grid(row=0, column=0)

        clickWindowImage = PhotoImage(file='images/chiikawaWindow.png', master=clickWindow)
        clickCanvas = Canvas(clickFrame, width=500, height=500, bg='white')
        clickCanvas.place(x=0, y=0)
        clickCanvas.create_image(250, 150, image=clickWindowImage)

        clickLabel = Label(clickFrame, text='ちいかわのともだち。\n「ウラ」「ヤハ」など大声でよく叫ぶ。', font=('HGP創英角ポップ体', 20), fg='#FCE224',
                           bg='white', height=3)
        clickLabel.pack(anchor='center')

        clickWindow.mainloop()
    elif type == "kuri":
        print("kurimanjyu button clicked.")
        clickWindow = Tk()
        clickWindow.title("くりまんじゅうの説明")
        clickWindow.geometry('500x500')
        clickWindow.resizable(False, False)

        clickFrame = Frame(clickWindow, width=500, height=500, relief='solid')
        clickFrame.propagate(False)
        clickFrame.grid(row=0, column=0)

        clickWindowImage = PhotoImage(file='images/chiikawaWindow.png', master=clickWindow)
        clickCanvas = Canvas(clickFrame, width=500, height=500, bg='white')
        clickCanvas.place(x=0, y=0)
        clickCanvas.create_image(250, 150, image=clickWindowImage)

        clickLabel = Label(clickFrame, text='見た目はかわいいけど…!?\nグルメで面倒見がいい。', font=('HGP創英角ポップ体', 20), fg='#8b4513',
                           bg='white', height=3)
        clickLabel.pack(anchor='center')

        clickWindow.mainloop()
    else:
        return


def mainWindow():
    fr1.tkraise()
    fr2.tkraise()
    fr3.tkraise()
    fr4.tkraise()
    fr5.tkraise()


window = Tk()
window.title('ちいかわキャラ解説！')
window.geometry('600x600')
window.resizable(False, False)

fr1 = Frame(window, width=600, height=100, borderwidth=1, relief='solid', bg='white')
fr2 = Frame(window, width=300, height=250, borderwidth=1, relief='solid')
fr3 = Frame(window, width=300, height=250, borderwidth=1, relief='solid')
fr4 = Frame(window, width=300, height=250, borderwidth=1, relief='solid')
fr5 = Frame(window, width=300, height=250, borderwidth=1, relief='solid')

fr1.propagate(False)
fr2.propagate(False)
fr3.propagate(False)
fr4.propagate(False)
fr5.propagate(False)

fr1.grid(row=0, column=0, columnspan=2)
fr2.grid(row=1, column=0)
fr3.grid(row=1, column=1)
fr4.grid(row=2, column=0)
fr5.grid(row=2, column=1)

titleLabel = Label(fr1, text='ちいかわキャラ解説！', font=('HGP創英角ポップ体', 20), fg='#ff3399', bg='white')
titleLabel.pack(anchor='center', expand=1)

chiikawabg = PhotoImage(file='images/chiikawa.png')
chiikawaButton = Button(fr2, command=lambda: click("chii"), image=chiikawabg)
chiikawaButton.place(x=0, y=0, width=300, height=250)

hachiwarebg = PhotoImage(file='images/hachiware.png')
hachiwareButton = Button(fr3, command=lambda: click("hachi"), image=hachiwarebg)
hachiwareButton.place(x=0, y=0, width=300, height=250)

usagibg = PhotoImage(file='images/usagi.png')
usagiButton = Button(fr4, command=lambda: click("usa"), image=usagibg)
usagiButton.place(x=0, y=0, width=300, height=250)

kurimanjyubg = PhotoImage(file='images/kurimanjyu.png')
kurimanjyuButton = Button(fr5, command=lambda: click("kuri"), image=kurimanjyubg)
kurimanjyuButton.place(x=0, y=0, width=300, height=250)

mainWindow()

window.mainloop()
