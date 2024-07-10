import wx
import sqlite3

path = "酒店管理系统.db"

class Function(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title = "问题提交", size =(700, 600))
        panel = wx.Panel(self)
        wx.StaticText(panel, label = "房间ID", pos = (100,40))
        wx.StaticText(panel, label = "酒店ID", pos = (100,90))
        wx.StaticText(panel, label = "客户ID", pos = (100,140))
        wx.StaticText(panel, label = "姓名", pos = (100,190))
        wx.StaticText(panel, label = "电话", pos = (100,240))
        wx.StaticText(panel, label = "问题内容", pos = (100,290))
        
        self.Roo_ID =  wx.TextCtrl(panel, pos = (200, 40), size = (235, 25),style =  wx.TE_LEFT)
        self.Roo_hotelID =  wx.TextCtrl(panel, pos = (200, 90), size = (235, 25),style =  wx.TE_LEFT)
        self.C_ID =  wx.TextCtrl(panel, pos = (200,140), size = (235, 25),style =  wx.TE_LEFT)
        self.C_Name =  wx.TextCtrl(panel, pos = (200,190), size = (235, 25),style =  wx.TE_LEFT)
        self.C_Telephone =  wx.TextCtrl(panel, pos = (200,240), size = (235, 25),style =  wx.TE_LEFT)
        self.question =  wx.TextCtrl(panel, pos = (200,290), size = (235, 25),style =  wx.TE_LEFT)

        self.bt = wx.Button(panel, label = "提交", pos = (280,350))
        self.bt.Bind(wx.EVT_BUTTON, self.bt_f)

    def bt_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        RoomID = self.Roo_ID.GetValue()
        HotelID = self.Roo_hotelID.GetValue()
        CustomerID = self.C_ID.GetValue()
        CustomerTelephone = self.C_Telephone.GetValue()
        Name = self.C_Name.GetValue()
        Question = self.question.GetValue()
        flag = 1
        if RoomID == "" or HotelID == "" or CustomerID== "" or CustomerTelephone == "" or Name == "" or Question == "":
            message = "填入信息不完整"
            wx.MessageBox(message)
        else:
            cur.execute("SELECT * FROM Hotel WHERE 酒店ID = ?",(HotelID,))
            inf = cur.fetchall()
            if inf == []:
                message = "酒店不存在！"
                wx.MessageBox(message)
                flag = 0
            cur.execute("SELECT * FROM Room WHERE 房间ID = ?",(RoomID,))
            inf = cur.fetchall()
            if inf == []:
                message = "房间不存在！"
                wx.MessageBox(message)
                flag = 0
            cur.execute("SELECT * FROM Customer WHERE 客户ID = ?",(CustomerID,))
            inf = cur.fetchall()
            if inf == []:
                message = "客户不存在！"
                wx.MessageBox(message)
                flag = 0
            if flag == 1:
                message = "提交成功！"
                cur.execute("INSERT INTO Question(房间ID,酒店ID,客户ID,名字,电话,问题内容) VALUES(?,?,?,?,?,?)",(RoomID,HotelID,CustomerID,Name,CustomerTelephone,Question))
                wx.MessageBox(message)
                con.commit()
        cur.close()

def submitQuestion():
    app = wx.App()
    frame = Function(None, -1)
    frame.Centre()
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    app = wx.App()
    frame = Function(None, -1)
    frame.Centre()
    frame.Show()
    app.MainLoop()