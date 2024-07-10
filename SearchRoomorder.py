import wx
import sqlite3

path = "酒店管理系统.db"

class SearchRoomorder(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title = "查询房间订单", size =(600, 500))
        panel = wx.Panel(self)
        wx.StaticText(panel, label = "请输入客户ID：", pos = (50,50))
        self.Customer_ID =  wx.TextCtrl(panel, pos = (175, 50), size = (235, 25),style =  wx.TE_LEFT)

        self.bt1 = wx.Button(panel, label = "查询信息", pos = (100,100))
        self.bt2 = wx.Button(panel, label = "返回主界面", pos = (250,100))
        self.bt1.Bind(wx.EVT_BUTTON, self.bt1_f)
        self.bt2.Bind(wx.EVT_BUTTON, self.bt2_f)

        wx.StaticText(panel, label = "住房订单ID", pos = (50,180))
        wx.StaticText(panel, label = "房间ID", pos = (165,180))
        wx.StaticText(panel, label = "酒店ID", pos = (220,180))
        wx.StaticText(panel, label = "客户", pos = (280,180))
        wx.StaticText(panel, label = "日期", pos = (340,180))
        wx.StaticText(panel, label = "总消费", pos = (440,180))

        self.Text = wx.TextCtrl(panel, pos = (50,200), size = (500, 200),style =  wx.TE_MULTILINE)

    def bt1_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        ID = self.Customer_ID.GetValue()
        cur.execute("SELECT * FROM HOrder WHERE 客户ID = ?", (ID,))
        inf = cur.fetchall() 
        string = ""
        if inf == []:
            message = "未查到该客户信息"
            wx.MessageBox(message)
        else:
            for i in inf:
                string = string+ i[0] +"\t" + i[1] +"\t" + i[2] + "\t" +i[3]+"\t" +i[4]+"\t"+str(i[5])+"\t\n"
            if len(string) == 0:
                if len(ID) != 0:
                    message = "您还未订购房间"
                else :
                    message = "您还未输入客户ID"
                wx.MessageBox(message)
            self.Text.SetValue(string)
        cur.close()
        con.close()

    def bt2_f(self, event):
        self.Destroy()

def searchRoomorder():
    app = wx.App()
    frame = SearchRoomorder(None, -1)
    frame.Centre()
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    searchRoomorder()