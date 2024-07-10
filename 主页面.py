import wx
import sqlite3
from Users登录 import *
from DBM登录 import *

class Choice(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title = "登录选择", pos = (700, 300), size =(400, 300))
        panel = wx.Panel(self)
        text = wx.StaticText(panel, label = "请选择登录的方式", pos = (140, 70))
        text.SetForegroundColour("Black")
        self.bt1 = wx.Button(panel, label = "管理员", pos = (105, 130))
        self.bt2 = wx.Button(panel, label = "普通用户", pos = (195, 130))
        self.bt1.Bind(wx.EVT_BUTTON, self.bt1_f)
        self.bt2.Bind(wx.EVT_BUTTON, self.bt2_f)

    def bt1_f(self,event):
        self.Destroy()
        DBMmain()
    def bt2_f(self, event):
        self.Destroy()
        Loginmain()

if __name__ == "__main__":
    app = wx.App()
    frame = Choice(None, -1)
    frame.Show()
    frame.Centre()
    app.MainLoop()
