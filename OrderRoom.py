import wx
import sqlite3


path = "酒店管理系统.db"

class OrderRoom(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title = "OrderRoom", size =(700, 600))
        panel = wx.Panel(self)
        wx.StaticText(panel, label = "客户ID", pos = (100,25))
        wx.StaticText(panel, label = "名字", pos = (100,75))
        wx.StaticText(panel, label = "电话", pos = (100,125))
        wx.StaticText(panel, label = "房间ID", pos = (100,175))
        wx.StaticText(panel, label = "酒店ID", pos = (100,225))
        wx.StaticText(panel, label = "日期", pos = (100,275))

        wx.StaticText(panel, label = "房间ID", pos = (100,350))
        wx.StaticText(panel, label = "酒店ID", pos = (150,350))
        wx.StaticText(panel, label = "类型", pos = (215,350))
        wx.StaticText(panel, label = "等级", pos = (275,350))
        wx.StaticText(panel, label = "价格", pos = (325,350))
        wx.StaticText(panel, label = "状态", pos = (385,350))

        self.Cus_ID =  wx.TextCtrl(panel, pos = (200, 25), size = (235, 25),style =  wx.TE_LEFT)
        self.name =  wx.TextCtrl(panel, pos = (200, 75), size = (235, 25),style =  wx.TE_LEFT)
        self.Tel =  wx.TextCtrl(panel, pos = (200,125), size = (235, 25),style =  wx.TE_LEFT)
        self.Room_ID =  wx.TextCtrl(panel, pos = (200,175), size = (235, 25),style =  wx.TE_LEFT)
        self.Hotle_ID =  wx.TextCtrl(panel, pos = (200,225), size = (235, 25),style =  wx.TE_LEFT)
        self.State =  wx.TextCtrl(panel, pos = (200,275), size = (235, 25),style =  wx.TE_LEFT)

        self.bt1 = wx.Button(panel, label = "查询空闲房间", pos = (100,320))
        self.bt2 = wx.Button(panel, label = "预定房间", pos = (220,320))
        self.bt3 = wx.Button(panel, label = "返回主界面", pos = (320,320))
        self.bt1.Bind(wx.EVT_BUTTON, self.bt1_f)
        self.bt2.Bind(wx.EVT_BUTTON, self.bt2_f)
        self.bt3.Bind(wx.EVT_BUTTON, self.bt3_f)

        self.Text = wx.TextCtrl(panel, pos = (100,370), size = (400, 150),style =  wx.TE_MULTILINE)

    def bt1_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("SELECT * FROM Room WHERE 状态 = ?", ("空闲",))
        inf = cur.fetchall() 
        string = ""
        for i in inf:
            string = string+i[0] + "\t" + i[1] + "\t" + i[2] +"\t"+i[3]+"\t"+i[4]+"\t"+i[5]+"\t\n"
        self.Text.SetValue(string)
        cur.close()
        con.close()

    def bt2_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        Cus_ID = self.Cus_ID.GetValue()
        name = self.name.GetValue()
        Tel = self.Tel.GetValue()
        Room_ID = self.Room_ID.GetValue()
        Hotle_ID = self.Hotle_ID.GetValue()
        State = self.State.GetValue()
        if Cus_ID == "" or name == "" or Tel == "" or Room_ID == "" or Hotle_ID == "":
            message = "输入信息不全" + "\n"
            wx.MessageBox(message)
        else:
            cur.execute("SELECT * FROM Customer WHERE 客户ID = ?",(Cus_ID,))
            inf = cur.fetchall()
            cur.execute("SELECT * FROM Room WHERE (状态, 房间ID, 酒店ID) = (?, ? ,?)", ("空闲", Room_ID, Hotle_ID))
            inf2 = cur.fetchall()
            cur.execute("SELECT 住房订单ID FROM Order")
            inf3 = cur.fetchall()
            Sum = 0
            for i in inf3:
                Sum = Sum+1
            Sum = Sum+1
            Sum = str(Sum) #sum为订单号
            if len(Sum) == 1:
                Sum = "ho00"+Sum
            elif len(Sum) == 2:
                Sum = "ho0" + Sum
            elif len(Sum) == 3:
                Sum = "ho" + Sum
            
            if len(inf2) != 0:
                if len(inf) == 0:
                    cur.execute("INSERT INTO CUSTOMER(客户ID, 名字, 电话) VALUES(?, ?, ?)", (Cus_ID, name, Tel))
                cur.execute("INSERT INTO Order(住房订单ID, 房间ID, 酒店ID, 客户ID, 日期, 总消费) VALUES(?, ?, ?, ?, ?, ?)", (Sum, Room_ID, Hotle_ID, Cus_ID, State, random.randint(1000, 10000)))
                cur.execute("UPDATE Room SET 状态 = ? WHERE (房间ID, 酒店ID) = (?, ?)", ("已满", Room_ID, Hotle_ID))
                con.commit()
                message = "预定成功"
                wx.MessageBox(message)
            elif len(inf2) == 0:
                message = "输入信息有误"
                wx.MessageBox(message)
        cur.close()
        con.close()
    def bt3_f(self, event):
        self.Destroy()

def orderRoom():
    app = wx.App()
    frame = OrderRoom(None, -1)
    frame.Centre()
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    orderRoom()

