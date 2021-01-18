import win32gui 
import win32con 
import win32clipboard as w 
import random


sen = ['我知道，你一定是生气了。因为我看到：你的头发炸起来了。','今夜我是一点没睡，因为我要闭门思过，见你我一定低头认错，请你做好准备接受!','没有你阳光不再灿烂!今天太阳好大，但比不上我心里下的雨大!再不原谅我，我的心开始发霉了!','在这我真诚地请你原谅，别生气了好吗?', '我知道你很生气。而且你每次生气我都好害怕。理解我，好么?原谅我，好么?','我没有停止爱你，我只是不再表现出来，因为无论我多么努力，你都不会明了。','爱着你，跟着你的志向一起飞翔，无论走了多久，永远微笑着在你怀里。','不要因为努力变成别人喜欢的样子，却到头来连自己都忘了真实的自己。','我真的不能没有你','求你回来吧，我有怎样不好的你直接说，我改！']

class QQMessageSend: 
    def send_message(self,msg): 
        # 窗口名字，就是备注名 
        name = "Clown" 
        # 将测试消息复制到剪切板中 
        w.OpenClipboard() 
        w.EmptyClipboard() 
        w.SetClipboardData(win32con.CF_UNICODETEXT, msg) 
        w.CloseClipboard() 
        # 获取窗口句柄 
        handle = win32gui.FindWindow(None, name) 
        # 填充消息 
        win32gui.SendMessage(handle, 770, 0, 0) 
        # 回车发送消息 
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0) 

    def main(self): 
        # 消息内容 
        # 循环发送 
        for i in range(30): 
          msg = sen[random.randint(0,9)]
          self.send_message(msg) 


if __name__ == '__main__': 
    qq_message_send = QQMessageSend() 
    qq_message_send.main() 