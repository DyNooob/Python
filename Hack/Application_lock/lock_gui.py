#!/usr/bin/env python
#-*- coding:utf-8 -*-

from tkinter import *
from tkinter.ttk import *


passwd = 3651
passwd_recording = ''

# file = open('lock_config.cfg', 'r')
# text = file.read()
# print(text)
# passwd = eval(text)
# # print(eval(text))
# # passwd = eval(text)

class Application_ui(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Application_lock')
        self.master.geometry('243x365')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Command1.TButton',font=('微软雅黑',24,'bold'))
        self.Command1 = Button(self.top, text='1', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.099, rely=0.219, relwidth=0.202, relheight=0.129)

        self.style.configure('Command1.TButton',font=('微软雅黑',24,'bold'))
        self.Command1 = Button(self.top, text='2', command=self.Command2_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.395, rely=0.219, relwidth=0.202, relheight=0.121)

        self.style.configure('Command1.TButton',font=('微软雅黑',24,'bold'))
        self.Command1 = Button(self.top, text='3', command=self.Command3_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.691, rely=0.219, relwidth=0.202, relheight=0.121)

        self.style.configure('Command1.TButton',font=('微软雅黑',24,'bold'))
        self.Command1 = Button(self.top, text='4', command=self.Command4_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.099, rely=0.416, relwidth=0.202, relheight=0.121)

        self.style.configure('Command1.TButton',font=('微软雅黑',24,'bold'))
        self.Command1 = Button(self.top, text='5', command=self.Command5_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.395, rely=0.416, relwidth=0.202, relheight=0.129)

        self.style.configure('Command1.TButton',font=('微软雅黑',24,'bold'))
        self.Command1 = Button(self.top, text='6', command=self.Command6_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.691, rely=0.416, relwidth=0.202, relheight=0.129)

        self.style.configure('Command1.TButton',font=('微软雅黑',24,'bold'))
        self.Command1 = Button(self.top, text='7', command=self.Command7_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.099, rely=0.614, relwidth=0.202, relheight=0.129)

        self.style.configure('Command1.TButton',font=('微软雅黑',24,'bold'))
        self.Command1 = Button(self.top, text='8', command=self.Command8_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.395, rely=0.614, relwidth=0.202, relheight=0.129)

        self.style.configure('Command1.TButton',font=('微软雅黑',24,'bold'))
        self.Command1 = Button(self.top, text='9', command=self.Command9_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.691, rely=0.614, relwidth=0.202, relheight=0.129)

        self.style.configure('Command1.TButton',font=('微软雅黑',24,'bold'))
        self.Command1 = Button(self.top, text='0', command=self.Command0_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.395, rely=0.811, relwidth=0.202, relheight=0.121)

        self.style.configure('Label1.TLabel',relief=SUNKEN, anchor='w', font=('宋体',25))
        self.Label1 = Label(self.top, style='Label1.TLabel')
        self.Label1.place(relx=0.066, rely=0.044, relwidth=0.169, relheight=0.112)

        self.style.configure('Label2.TLabel',relief=SUNKEN, anchor='w', font=('宋体',25))
        self.Label2 = Label(self.top, style='Label2.TLabel')
        self.Label2.place(relx=0.296, rely=0.044, relwidth=0.169, relheight=0.112)

        self.style.configure('Label3.TLabel',relief=SUNKEN, anchor='w', font=('宋体',25))
        self.Label3 = Label(self.top, style='Label3.TLabel')
        self.Label3.place(relx=0.527, rely=0.044, relwidth=0.169, relheight=0.112)

        self.style.configure('Label4.TLabel',relief=SUNKEN, anchor='w', font=('宋体',25))
        self.Label4 = Label(self.top, style='Label4.TLabel')
        self.Label4.place(relx=0.757, rely=0.044, relwidth=0.169, relheight=0.112)


class Application(Application_ui):

    def passwd_check(self, passwd_in):
        global passwd
        if int(passwd_in) != passwd:
            self.Label1.config(text='')
            self.Label2.config(text='')
            self.Label3.config(text='')
            self.Label4.config(text='')
            data = 'Fales'
            global passwd_recording
            passwd_recording = ''
            return data
        else:
            data = 'True'
            self.top.destroy()
            return data

    def show_pwd(self, pwd):
        global passwd_recording
        if self.Label1.cget('text') != '':
            if self.Label2.cget('text') != '':
                if self.Label3.cget('text') != '':
                    if self.Label4.cget('text') != '':
                        pass
                    else:
                        passwd_recording = passwd_recording + pwd
                        self.Label4.config(text='●')
                        self.passwd_check(passwd_recording)
                else:
                    passwd_recording = passwd_recording + pwd
                    self.Label3.config(text='●')
            else:
                passwd_recording = passwd_recording + pwd
                self.Label2.config(text='●')
        else:
            passwd_recording = passwd_recording + pwd
            self.Label1.config(text='●')

    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command0_Cmd(self):
        self.show_pwd('0')

    def Command1_Cmd(self):
        self.show_pwd('1')

    def Command2_Cmd(self):
        self.show_pwd('2')

    def Command3_Cmd(self):
        self.show_pwd('3')

    def Command4_Cmd(self):
        self.show_pwd('4')

    def Command5_Cmd(self):
        self.show_pwd('5')

    def Command6_Cmd(self):
        self.show_pwd('6')

    def Command7_Cmd(self):
        self.show_pwd('7')

    def Command8_Cmd(self):
        self.show_pwd('8')

    def Command9_Cmd(self):
        self.show_pwd('9')

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try:
        top.destroy()
    except:
        pass



if __name__ != "__main__":
    def up():
        top = Tk()
        Application(top).mainloop()
        try:
            top.destroy()
        except:
            pass