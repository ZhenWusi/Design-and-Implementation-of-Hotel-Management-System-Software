import wx
import sqlite3
import os

from 管理酒店信息 import *
from Customer import *
from 注册新用户 import *
from SearchQuestion import *

class Function(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title = "酒店管理系统", size =(320,300))
        panel = wx.Panel(self)

        self.bt1 = wx.Button(panel, label = "管理酒店信息", pos = (100, 20))
        self.bt2 = wx.Button(panel, label = "管理客户信息", pos = (100, 60))
        self.bt3 = wx.Button(panel, label = "查看客户问题", pos = (100, 100))
        self.bt4 = wx.Button(panel, label = "注册DBM账号", pos = (100, 140))
        self.bt5 = wx.Button(panel, label = "注册User账号", pos = (100, 180))
        self.bt6 = wx.Button(panel, label = "Exit", pos = (105, 220))

        self.bt1.Bind(wx.EVT_BUTTON, self.ManageInformation)
        self.bt2.Bind(wx.EVT_BUTTON, self.Customer)
        self.bt3.Bind(wx.EVT_BUTTON, self.Question)
        self.bt4.Bind(wx.EVT_BUTTON, self.Register_DBM)
        self.bt5.Bind(wx.EVT_BUTTON, self.Register_User)
        self.bt6.Bind(wx.EVT_BUTTON, self.Exit)

        #self.Show(True)
    def ManageInformation(self,event):
        ManageInformation()
    def Register_DBM(self, event):
        Registered(1)
    def Register_User(self ,event):
        Registered(2)
    def Customer(self, event):
        customer()
    def Question(self, event):
        SearchQusetion()
    def Exit(self, event):
        self.Destroy()
        exit()

def main1():
    app = wx.App()
    frame = Function(None, -1)
    frame.Centre()
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main1()

