import wx
import sqlite3
from SearchRoomorder import *
from OrderRoom import *
from SubmitQuestion import *


class UsersFunction(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="酒店管理系统", size=(300, 260))  # 设置窗口标题为"酒店管理系统"
        panel = wx.Panel(self)
        self.bt1 = wx.Button(panel, label="查询订单", pos=(100, 20))  # 将按钮1标签改为"查询订单"
        self.bt2 = wx.Button(panel, label="预定房间", pos=(100, 60))  # 将按钮2标签改为"预定房间"
        self.bt3 = wx.Button(panel, label="提交问题", pos=(100, 100))  # 将按钮3标签改为"提交问题"
        self.bt4 = wx.Button(panel, label="退出", pos=(100, 140))  # 将按钮4标签改为"退出"
        self.bt1.Bind(wx.EVT_BUTTON, self.SearchRoomorder)
        self.bt2.Bind(wx.EVT_BUTTON, self.Orderroom)
        self.bt3.Bind(wx.EVT_BUTTON, self.Question)
        self.bt4.Bind(wx.EVT_BUTTON, self.Exit)

    def SearchRoomorder(self, event):
        searchRoomorder()

    def Orderroom(self, event):
        orderRoom()

    def Question(self, event):
        submitQuestion()

    def Exit(self, event):
        self.Destroy()
        exit()


def usersFunction():
    app = wx.App()
    frame = UsersFunction(None, -1)
    frame.Centre()
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    usersFunction()
