import wx
import sqlite3

from Room import *
from Hotel import *
from Housingorder import *

class Function(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title = "酒店管理系统", size =(300,300))
        panel = wx.Panel(self)

        self.bt1 = wx.Button(panel, label="酒店", pos=(100, 40))
        self.bt2 = wx.Button(panel, label="订单", pos=(100, 80))
        self.bt3 = wx.Button(panel, label="房间", pos=(100, 120))
        self.bt4 = wx.Button(panel, label="退出", pos=(100, 160))

        self.bt1.Bind(wx.EVT_BUTTON, self.ManangeHotel)
        self.bt2.Bind(wx.EVT_BUTTON, self.ManageOrder)
        self.bt3.Bind(wx.EVT_BUTTON, self.ManageRoom)
        self.bt4.Bind(wx.EVT_BUTTON, self.Exit)

    def ManageRoom(self, event):
        room()
    def ManageOrder(self, event):
        housingorder()
    def ManangeHotel(self, event):
        hotel()
    def Exit(self, event):
        self.Destroy()

def ManageInformation():
    app = wx.App()
    frame = Function(None,-1)
    frame.Centre()
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    app = wx.App()
    frame = Function(None, -1)
    frame.Centre()
    frame.Show()
    app.MainLoop()