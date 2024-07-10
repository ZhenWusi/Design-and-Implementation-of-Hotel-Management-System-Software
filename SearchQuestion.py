import wx
import sqlite3

path = "酒店管理系统.db"

class SearchRoomorder(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title = "查询客户反馈", size =(800, 500))
        panel = wx.Panel(self)
        wx.StaticText(panel, label = "客户ID：", pos = (50,50))
        wx.StaticText(panel, label = "酒店ID：", pos = (50,90))
        wx.StaticText(panel, label = "房间ID：", pos = (50,130))
        self.Customer_ID =  wx.TextCtrl(panel, pos = (175, 50), size = (235, 25),style =  wx.TE_LEFT)
        self.Hotel_ID =  wx.TextCtrl(panel, pos = (175, 90), size = (235, 25),style =  wx.TE_LEFT)
        self.Room_ID =  wx.TextCtrl(panel, pos = (175, 130), size = (235, 25),style =  wx.TE_LEFT)

        self.bt1 = wx.Button(panel, label = "查询所有问题", pos = (50,160))
        self.bt2 = wx.Button(panel, label = "删除", pos = (210,160))
        self.bt1.Bind(wx.EVT_BUTTON, self.bt1_f)
        self.bt2.Bind(wx.EVT_BUTTON, self.bt2_f)

        wx.StaticText(panel, label = "客户ID", pos = (50,200))
        wx.StaticText(panel, label = "名字", pos = (165,200))
        wx.StaticText(panel, label = "电话", pos = (220,200))
        wx.StaticText(panel, label = "酒店ID", pos = (280,200))
        wx.StaticText(panel, label = "房间ID", pos = (340,200))
        wx.StaticText(panel, label = "问题内容", pos = (440,200))

        self.Text = wx.TextCtrl(panel, pos = (50,220), size = (600, 200),style =  wx.TE_MULTILINE)
    
    def bt1_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("SELECT * FROM Question")
        inf = cur.fetchall() 
        string = ""
        for i in inf:
            string = string+ i[0] +"\t" + i[1] +"\t"+ i[2] +"\t" +i[3]+"\t"+i[4]+"\t"+i[5]+"\t\n"
        self.Text.SetValue(string)
        cur.close()

    def bt2_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        C_ID = self.Customer_ID.GetValue()
        H_ID = self.Hotel_ID.GetValue()
        R_ID = self.Room_ID.GetValue()
        if C_ID == "" or H_ID == "" or R_ID == "":
            message = "信息不完整！"
            wx.MessageBox(message)
        else:
            cur.execute("DELETE * FROM Question WHERE 房间ID = ? AND 酒店ID = ? AND 客户ID = ?",(R_ID,H_ID,C_ID))
            con.commit()
        cur.close()

def SearchQusetion():
    app = wx.App()
    frame = SearchRoomorder(None, -1)
    frame.Centre()
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    app = wx.App()
    frame = SearchRoomorder(None, -1)
    frame.Centre()
    frame.Show()
    app.MainLoop()