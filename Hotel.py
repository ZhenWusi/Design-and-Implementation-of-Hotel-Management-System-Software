import wx
import sqlite3

path = "酒店管理系统.db"

class Function(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title = "酒店", size =(750, 550))
        panel = wx.Panel(self)
        wx.StaticText(panel, label = "*酒店ID", pos = (100,50))
        wx.StaticText(panel, label = "名字", pos = (100,100))
        wx.StaticText(panel, label = "地址", pos = (100,150))
        wx.StaticText(panel, label = "房间数量", pos = (100,200))

        wx.StaticText(panel, label = "*酒店ID", pos = (100,285))
        wx.StaticText(panel, label = "名字", pos = (170,285))
        wx.StaticText(panel, label = "地址", pos = (300,285))
        wx.StaticText(panel, label = "房间数量", pos = (430,285))


        self.Hot_ID =  wx.TextCtrl(panel, pos = (200, 40), size = (235, 25),style =  wx.TE_LEFT)
        self.Hot_name =  wx.TextCtrl(panel, pos = (200, 90), size = (235, 25),style =  wx.TE_LEFT)
        self.Hot_location =  wx.TextCtrl(panel, pos = (200,140), size = (235, 25),style =  wx.TE_LEFT)
        self.Hot_num_room =  wx.TextCtrl(panel, pos = (200,190), size = (235, 25),style =  wx.TE_LEFT)
        self.bt1 = wx.Button(panel, label = "查询所有信息", pos = (100,235))
        self.bt2 = wx.Button(panel, label = "查询", pos = (210,235))
        self.bt3 = wx.Button(panel, label = "录入", pos = (300,235))
        self.bt4 = wx.Button(panel, label = "删除", pos = (400,235))
        self.bt5 = wx.Button(panel, label = "修改", pos = (500,235))
        self.bt1.Bind(wx.EVT_BUTTON, self.bt1_f)
        self.bt2.Bind(wx.EVT_BUTTON, self.bt2_f)
        self.bt3.Bind(wx.EVT_BUTTON, self.bt3_f)
        self.bt4.Bind(wx.EVT_BUTTON, self.bt4_f)
        self.bt5.Bind(wx.EVT_BUTTON, self.bt5_f)
        self.Text = wx.TextCtrl(panel, pos = (100,320), size = (550, 150),style =  wx.TE_MULTILINE)

    def bt1_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("SELECT * FROM Hotel")
        inf = cur.fetchall() 
        string = ""
        for i in inf:
            string = string+ i[0] + "\t" + i[1] + "\t" + i[2] + "\t" + str(i[3]) + "\t\n"
        self.Text.SetValue(string)
        cur.close()

    def bt2_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        ID = self.Hot_ID.GetValue()
        Name = self.Hot_name.GetValue()
        Location = self.Hot_location.GetValue()
        Num_room = self.Hot_num_room.GetValue()
        if ID == "":
            message = "请输入酒店ID"
            wx.MessageBox(message)
        else:
            cur.execute("SELECT * FROM Hotel WHERE 酒店ID = ? ",(ID,))
            inf = cur.fetchall()
            if inf == []:
                message = "信息不存在"
                wx.MessageBox(message)
            else :
                string = ""
                string = inf[0][0] + "\t" + inf[0][1] + "\t" + inf[0][2] + "\t" + str(inf[0][3]) + "\t"
                self.Text.SetValue(string)
        cur.close()

    def bt3_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        ID = self.Hot_ID.GetValue()
        Name = self.Hot_name.GetValue()
        Location = self.Hot_location.GetValue()
        Num_room = self.Hot_num_room.GetValue()
        if ID == ""  or Name == "" or Location == "" or Num_room == "":
            message = "信息不完整"
            wx.MessageBox(message)
        else:
            message = "信息录入成功"
            cur.execute("INSERT INTO Hotel(酒店ID,名字,地址,房间数量) VALUES(?,?,?,?)",(ID,Name,Location,int(Num_room)))
            wx.MessageBox(message)
        con.commit()
        cur.close()

    def bt4_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        ID = self.Hot_ID.GetValue()
        Name = self.Hot_name.GetValue()
        Location = self.Hot_location.GetValue()
        Num_room = self.Hot_num_room.GetValue()
        if ID == "":
            message = "所需删除的数据不明确"
            wx.MessageBox(message)
        else:
            cur.execute("SELECT * FROM Hotel WHERE 酒店ID = ?",(ID,))
            inf = cur.fetchall()
            if inf == []:
                message = "信息不存在"
                wx.MessageBox(message)
            else:
                message = "信息删除成功"
                cur.execute("DELETE FROM Hotel WHERE 酒店ID = ?",(ID,))
                wx.MessageBox(message)
            con.commit()
        cur.close()

    def bt5_f(self, event):
        con = sqlite3.connect(path)
        cur = con.cursor()
        ID = self.Hot_ID.GetValue()
        Name = self.Hot_name.GetValue()
        Location = self.Hot_location.GetValue()
        Num_room = self.Hot_num_room.GetValue()
        if ID == "":
            message = "所需更改的数据不明确"
            wx.MessageBox(message)
        else:
            cur.execute("SELECT * FROM Hotel WHERE 酒店ID = ?",(ID,))
            inf = cur.fetchall()
            if inf == []:
                message = "信息不存在"
                wx.MessageBox(message)
            else:
                message = "请输入需要修改的信息"
                if Name != "":
                    message = "信息修改成功"
                    cur.execute("UPDATE Hotel SET 名字 = ? WHERE 酒店ID = ?",(Name,ID))
                if Location != "":
                    message = "信息修改成功"
                    cur.execute("UPDATE Hotel SET 地址 = ? WHERE 酒店ID = ?",(Location,ID))
                if Num_room != "":
                    message = "信息修改成功"
                    cur.execute("UPDATE Hotel SET 房间数量 = ? WHERE 酒店ID = ?",(Num_room,ID))
                wx.MessageBox(message)
            con.commit()
        cur.close()

def hotel():
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