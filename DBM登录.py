import wx
import sqlite3
from DBM功能选择界面 import *
from 注册新用户 import *

class DBM(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title = "管理者登录", pos = (700, 300), size =(500, 350))
        panel = wx.Panel(self)
        wx.StaticText(panel, label = "请输入用户名和密码", pos = (160, 40))
        self.label_User = wx.StaticText(panel, label = "用户名:", pos = (50, 90))
        self.label_Password = wx.StaticText(panel, label = "密码:", pos = (50, 130))
        self.User = wx.TextCtrl(panel, pos = (100, 90), size = (235, 25),style =  wx.TE_LEFT)
        self.Password = wx.TextCtrl(panel, pos = (100, 130), size = (235, 25), style = wx.TE_PASSWORD)
        self.bt1 = wx.Button(panel, label = "确定", pos = (110, 170))
        self.bt2 = wx.Button(panel, label = "清空", pos = (235, 170))
        self.bt3 = wx.Button(panel, label = "退出", pos = (360, 170))
        self.bt1.Bind(wx.EVT_BUTTON, self.bt1_f)
        self.bt2.Bind(wx.EVT_BUTTON, self.bt2_f)
        self.bt3.Bind(wx.EVT_BUTTON, self.bt3_f)

    def bt1_f(self,event):
        con = sqlite3.connect("酒店管理系统.db")
        cur = con.cursor()
        UserName = self.User.GetValue()
        Password = self.Password.GetValue()
        cur.execute("SELECT * FROM DBM where 用户名 = '%s'" % UserName)
        l_info = cur.fetchall()
        cur.close()
        con.close()
        flag = 0
        if UserName == "" or Password == "":
            message = "用户名或密码不能为空"
        elif len(l_info) == 0:
            message = "用户名或密码不正确"
        elif str(l_info[0][1]) != str(Password) :
            message = "用户名或密码不正确"
        else :
            flag = 1
            message = "登录成功"
            self.Destroy()
        wx.MessageBox(message)
        if flag == 1:
            main1()
    def bt2_f(self, event):
        self.User.SetValue("")
        self.Password.SetValue("")

    def bt3_f(self, event):
        self.Destroy()
        exit()             

def DBMmain():
    app = wx.App()
    frame = DBM(None, -1)
    frame.Centre()
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    DBMmain()