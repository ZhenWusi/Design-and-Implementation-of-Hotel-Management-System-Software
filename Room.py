import wx
import sqlite3

path = "酒店管理系统.db"

class Function(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title = "Room", size =(800, 600))
        panel = wx.Panel(self)
        wx.StaticText(panel, label = "*房间ID", pos = (100,40))
        wx.StaticText(panel, label = "*酒店ID", pos = (100,90))
        wx.StaticText(panel, label = "类型", pos = (100,140))
        wx.StaticText(panel, label = "等级", pos = (100,190))
        wx.StaticText(panel, label = "价格", pos = (100,240))
        wx.StaticText(panel, label = "状态", pos = (100,290))

        wx.StaticText(panel, label = "*房间ID", pos = (100,375))
        wx.StaticText(panel, label = "*酒店ID", pos = (150,375))
        wx.StaticText(panel, label = "类型", pos = (215,375))
        wx.StaticText(panel, label = "等级", pos = (275,375))
        wx.StaticText(panel, label = "价格", pos = (325,375))
        wx.StaticText(panel, label = "状态", pos = (385,375))

        self.Roo_ID =  wx.TextCtrl(panel, pos = (200, 40), size = (235, 25),style =  wx.TE_LEFT)
        self.Roo_hotelID =  wx.TextCtrl(panel, pos = (200, 90), size = (235, 25),style =  wx.TE_LEFT)
        self.Roo_kind =  wx.TextCtrl(panel, pos = (200,140), size = (235, 25),style =  wx.TE_LEFT)
        self.Roo_level =  wx.TextCtrl(panel, pos = (200,190), size = (235, 25),style =  wx.TE_LEFT)
        self.Roo_price =  wx.TextCtrl(panel, pos = (200,240), size = (235, 25),style =  wx.TE_LEFT)
        self.Roo_state =  wx.TextCtrl(panel, pos = (200,290), size = (235, 25),style =  wx.TE_LEFT)
        self.bt1 = wx.Button(panel, label = "查询所有信息", pos = (100,325))
        self.bt2 = wx.Button(panel, label = "查询", pos = (200,325))
        self.bt3 = wx.Button(panel, label = "录入", pos = (300,325))
        self.bt4 = wx.Button(panel, label = "删除", pos = (400,325))
        self.bt5 = wx.Button(panel, label = "修改", pos = (500,325))
        self.bt1.Bind(wx.EVT_BUTTON, self.bt1_f)
        self.bt2.Bind(wx.EVT_BUTTON, self.bt2_f)
        self.bt3.Bind(wx.EVT_BUTTON, self.bt3_f)
        self.bt4.Bind(wx.EVT_BUTTON, self.bt4_f)
        self.bt5.Bind(wx.EVT_BUTTON, self.bt5_f)
        self.Text = wx.TextCtrl(panel, pos = (100,400), size = (500, 150),style =  wx.TE_MULTILINE)

    def bt1_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("SELECT * FROM Room")
        inf = cur.fetchall() 
        string = ""
        for i in inf:
            string = string+ i[0] +"\t" + i[1] +"\t"+ i[2] +"\t" +i[3]+"\t"+str(i[4])+"\t"+i[5]+"\t\n"
        self.Text.SetValue(string)
        cur.close()

    def bt2_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        ID = self.Roo_ID.GetValue()
        HotelID = self.Roo_hotelID.GetValue()
        Kind = self.Roo_kind.GetValue()
        Level = self.Roo_level.GetValue()
        Price = self.Roo_price.GetValue()
        State = self.Roo_state.GetValue()
        if ID == "" or HotelID == "":
            message = "请输入房间ID和酒店ID"
            wx.MessageBox(message)
        else:
            cur.execute("SELECT * FROM Room WHERE 房间ID = ? AND 酒店ID = ?",(ID,HotelID))
            inf = cur.fetchall()
            if inf == []:
                message = "信息不存在"
                wx.MessageBox(message)
            else :
                string = ""
                string =inf[0][0] +"\t"+ inf[0][1] +"\t"+ inf[0][2] +"\t"+inf[0][3] +"\t"+str(inf[0][4])+"\t"+inf[0][5]+"\t"
                self.Text.SetValue(string)
        cur.close()

    def bt3_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        ID = self.Roo_ID.GetValue()
        HotelID = self.Roo_hotelID.GetValue()
        Kind = self.Roo_kind.GetValue()
        Level = self.Roo_level.GetValue()
        Price = self.Roo_price.GetValue()
        State = self.Roo_state.GetValue()
        if ID == "" or HotelID == "" or Kind == "" or Level == "" or Price == "" or State == "":
            message = "信息不完整"
            wx.MessageBox(message)
        else:
            message = "信息录入成功"
            cur.execute("INSERT INTO Room(房间ID,酒店ID,类型,等级,价格,状态) VALUES(?,?,?,?,?,?)",(ID,HotelID,Kind,Level,int(Price),State))
            wx.MessageBox(message)
        con.commit()
        cur.close()

    def bt4_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        ID = self.Roo_ID.GetValue()
        HotelID = self.Roo_hotelID.GetValue()
        Kind = self.Roo_kind.GetValue()
        Level = self.Roo_level.GetValue()
        Price = self.Roo_price.GetValue()
        State = self.Roo_state.GetValue()
        if ID == "" or HotelID == "":
            message = "所需删除的数据不明确"
            wx.MessageBox(message)
        else:
            cur.execute("SELECT * FROM Room WHERE 房间ID = ? AND 酒店ID = ?",(ID,HotelID))
            inf = cur.fetchall()
            if inf == []:
                message = "信息不存在"
                wx.MessageBox(message)
            else:
                message = "信息删除成功"
                cur.execute("DELETE FROM Room WHERE 房间ID = ? AND 酒店ID == ?",(ID,HotelID))
                wx.MessageBox(message)
            con.commit()
        cur.close()

    def bt5_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        ID = self.Roo_ID.GetValue()
        HotelID = self.Roo_hotelID.GetValue()
        Kind = self.Roo_kind.GetValue()
        Level = self.Roo_level.GetValue()
        Price = self.Roo_price.GetValue()
        State = self.Roo_state.GetValue()
        if ID == "" or HotelID == "":
            message = "所需更改的数据不明确"
            wx.MessageBox(message)
        else:
            cur.execute("SELECT * FROM Room WHERE 房间ID = ? AND 酒店ID = ?",(ID,HotelID))
            inf = cur.fetchall()
            if inf == []:
                message = "信息不存在"
                wx.MessageBox(message)
            else:
                message = "请输入需要修改的信息"
                if Level != "":
                    message = "信息修改成功"
                    cur.execute("UPDATE Room SET 等级 = ? WHERE 房间ID = ? AND 酒店ID = ?",(Level,ID,HotelID))
                if Price != "":
                    message = "信息修改成功"
                    cur.execute("UPDATE Room SET 价格 = ? WHERE 房间ID = ? AND 酒店ID = ?",(int(Price),ID,HotelID))
                if State != "":
                    message = "信息修改成功"
                    cur.execute("UPDATE Room SET 状态 = ? WHERE 房间ID = ? AND 酒店ID = ?",(State,ID,HotelID))
                if Kind != "":
                    message = "信息修改成功"
                    cur.execute("UPDATE Room SET 类型 = ? WHERE 房间ID = ? AND 酒店ID = ?",(Kind,ID,HotelID))
                wx.MessageBox(message)
            con.commit()
        cur.close()

def room():
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
