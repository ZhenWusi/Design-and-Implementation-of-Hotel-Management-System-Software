import wx
import sqlite3

path = "酒店管理系统.db"

class Function(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title = "Order", size =(800, 600))
        panel = wx.Panel(self)
        wx.StaticText(panel, label = "*住房订单ID", pos = (100,40))
        wx.StaticText(panel, label = "日期", pos = (100,90))
        wx.StaticText(panel, label = "房间ID", pos = (100,140))
        wx.StaticText(panel, label = "酒店ID", pos = (100,190))
        wx.StaticText(panel, label = "客户ID", pos = (100,240))
        wx.StaticText(panel, label = "总消费", pos = (100,290))

        wx.StaticText(panel, label = "*住房订单ID", pos = (100,375))
        wx.StaticText(panel, label = "房间ID", pos = (215,375))
        wx.StaticText(panel, label = "酒店ID", pos = (270,375))
        wx.StaticText(panel, label = "客户ID", pos = (330,375))
        wx.StaticText(panel, label = "日期", pos = (400,375))
        wx.StaticText(panel, label = "总消费", pos = (490,375))

        self.Ord_ID =  wx.TextCtrl(panel, pos = (200, 40), size = (235, 25),style =  wx.TE_LEFT)
        self.Ord_date =  wx.TextCtrl(panel, pos = (200, 90), size = (235, 25),style =  wx.TE_LEFT)
        self.Ord_roomID =  wx.TextCtrl(panel, pos = (200,140), size = (235, 25),style =  wx.TE_LEFT)
        self.Ord_hotelID = wx.TextCtrl(panel, pos = (200,190), size = (235, 25),style =  wx.TE_LEFT)
        self.Ord_customerID =  wx.TextCtrl(panel, pos = (200,240), size = (235, 25),style =  wx.TE_LEFT)
        self.Ord_consume =  wx.TextCtrl(panel, pos = (200,290), size = (235, 25),style =  wx.TE_LEFT)
        self.bt1 = wx.Button(panel, label = "查询所有信息", pos = (100,325))
        self.bt2 = wx.Button(panel, label = "查询", pos = (210,325))
        self.bt3 = wx.Button(panel, label = "录入", pos = (300,325))
        self.bt4 = wx.Button(panel, label = "删除", pos = (400,325))
        self.bt5 = wx.Button(panel, label = "修改", pos = (500,325))
        self.bt1.Bind(wx.EVT_BUTTON, self.bt1_f)
        self.bt2.Bind(wx.EVT_BUTTON, self.bt2_f)
        self.bt3.Bind(wx.EVT_BUTTON, self.bt3_f)
        self.bt4.Bind(wx.EVT_BUTTON, self.bt4_f)
        self.bt5.Bind(wx.EVT_BUTTON, self.bt5_f)
        self.Text = wx.TextCtrl(panel, pos = (100,400), size = (550, 150),style =  wx.TE_MULTILINE)

    def bt1_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("SELECT * FROM HOrder")
        inf = cur.fetchall() 
        string = ""
        for i in inf:
            string = string+ i[0] +"\t" + i[1] +"\t"+ i[2] +"\t" +i[3]+"\t"+i[4]+"\t"+str(i[5])+"\t\n"
        self.Text.SetValue(string)
        cur.close()

    def bt2_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        ID = self.Ord_ID.GetValue()
        Date = self.Ord_date.GetValue()
        RoomID = self.Ord_roomID.GetValue()
        HotelID = self.Ord_hotelID.GetValue()
        CustomerID = self.Ord_customerID.GetValue()
        Consume = self.Ord_consume.GetValue()
        if ID == "":
            message = "请输入包间订单ID"
            wx.MessageBox(message)
        else:
            cur.execute("SELECT * FROM HOrder WHERE 住房订单ID = ?",(ID,))
            inf = cur.fetchall()
            if inf == []:
                message = "信息不存在"
                wx.MessageBox(message)
            else :
                string = ""
                string =inf[0][0] +"\t"+ inf[0][1] +"\t"+ inf[0][2] +"\t" +inf[0][3] +"\t"+inf[0][4]+"\t"+str(inf[0][5])+"\t"
                self.Text.SetValue(string)
        cur.close()

    def bt3_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        ID = self.Ord_ID.GetValue()
        Date = self.Ord_date.GetValue()
        RoomID = self.Ord_roomID.GetValue()
        HotelID = self.Ord_hotelID.GetValue()
        CustomerID = self.Ord_customerID.GetValue()
        Consume = self.Ord_consume.GetValue()
        if ID == "" or Date == "" or RoomID == "" or CustomerID == "" or Consume == "" or HotelID == "":
            message = "信息不完整"
            wx.MessageBox(message)
        else:
            message = "信息录入成功"
            cur.execute("INSERT INTO HOrder(住房订单ID,房间ID,酒店ID,客户ID,日期,总消费) VALUES(?,?,?,?,?,?)",(ID,RoomID,HotelID,CustomerID,Date,int(Consume)))
            wx.MessageBox(message)
        con.commit()
        cur.close()

    def bt4_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        ID = self.Ord_ID.GetValue()
        Date = self.Ord_date.GetValue()
        RoomID = self.Ord_roomID.GetValue()
        HotelID = self.Ord_hotelID.GetValue()
        CustomerID = self.Ord_customerID.GetValue()
        Consume = self.Ord_consume.GetValue()
        if ID == "":
            message = "所需删除的数据不明确"
            wx.MessageBox(message)
        else:
            cur.execute("SELECT * FROM HOrder WHERE 住房订单ID = ?",(ID,))
            inf = cur.fetchall()
            if inf == []:
                message = "信息不存在"
                wx.MessageBox(message)
            else:
                message = "信息删除成功"
                cur.execute("DELETE FROM HOrder WHERE 住房订单ID = ?",(ID,))
                wx.MessageBox(message)
            con.commit()
        cur.close()

    def bt5_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        ID = self.Ord_ID.GetValue()
        Date = self.Ord_date.GetValue()
        RoomID = self.Ord_roomID.GetValue()
        HotelID = self.Ord_hotelID.GetValue()
        CustomerID = self.Ord_customerID.GetValue()
        Consume = self.Ord_consume.GetValue()
        if ID == "":
            message = "所需更改的数据不明确"
            wx.MessageBox(message)
        else:
            cur.execute("SELECT * FROM HOrder WHERE 住房订单ID = ?",(ID,))
            inf = cur.fetchall()
            if inf == []:
                message = "信息不存在"
                wx.MessageBox(message)
            else:
                message = "请输入需要修改的信息"
                if Date != "":
                    message = "信息修改成功"
                    cur.execute("UPDATE HOrder SET 日期 = ? WHERE 住房订单ID = ?",(Date,ID))
                if RoomID != "":
                    message = "信息修改成功"
                    cur.execute("UPDATE HOrder SET 房间ID = ? WHERE 住房订单ID = ?",(RoomID,ID))
                if CustomerID != "":
                    message = "信息修改成功"
                    cur.execute("UPDATE HOrder SET 客户ID = ? WHERE 住房订单ID = ?",(CustomerID,ID))
                if Consume != "":
                    message = "信息修改成功"
                    cur.execute("UPDATE HOrder SET 总消费 = ? WHERE 住房订单ID = ?",(int(Consume),ID))
                if HotelID != "":
                    message = "信息修改成功"
                    cur.execute("UPDATE HOrder SET 酒店ID = ? WHERE 住房订单ID = ?",(HotelID,ID))
                wx.MessageBox(message)
            con.commit()
        cur.close()

def housingorder():
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