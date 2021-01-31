import re
import tkinter as tk
from urllib import parse
import tkinter.messagebox as msgbox
import webbrowser

class APP:
    def __init__(self, width=500, height=300):
        self.w = width
        self.h = height
        self.title = 'N-V-W'
        self.root = tk.Tk(className=self.title)
        self.url = tk.StringVar

        self.v = tk.IntVar()
        self.v.set(1)

        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)

        group = tk.Label(frame_1, text='播放通道', padx=10, pady=10)
        tb = tk.Radiobutton(frame_1, text='通道_1')

        label = tk.Label(frame_2, text='请输入视频播放地址: ')
        entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=30)
        play = tk.Button(frame_2, text='播放', font=('楷体', 12), fg='Purple', width=2, height=1, command=self.video_play)

        frame_1.pack()
        frame_2.pack()

        group.grid(row=0, column=0)
        tb.grid(row=0, column=1)
        label.grid(row=0, column=2)
        entry.grid(row=0, column=3)
        play.grid(row=0, column=4, ipadx=10, ipady=10)

    def video_play(self):
        port = 'http://www.wmxz.wang/video.php?url='
        # if re.match(r'https?:/{2}\w.+$', self.url().get()):
        ip = self.url().get()
        ip = parse.quote_plus(ip)

        webbrowser.open(port + ip)
        # else:
        #     msgbox.showinfo(title='错误', message='')
    def loop(self):
            self.root.mainloop()

if __name__ == '__main__':
    app = APP()
    app.loop()