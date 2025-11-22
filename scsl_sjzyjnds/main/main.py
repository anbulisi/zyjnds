# 主界面

import tkinter as tk
import os
from importlib.resources import contents

from PIL import Image, ImageTk
from scsl_sjzyjnds import image

# 按钮位置
button_X = 80
button_Y = 200

# 标题位置
title_X = 200
title_Y = 100

contents_list = ['日志分析','防火墙策略','系统报警']

# 点击按钮，标题对应改变
title_change = 0

class app():
    # 创建窗口
    def create_window(self):
        self.root = tk.Tk()  # 创建窗口
        self.root.geometry("780x600")  # 设置窗口大小
        self.root.title("设备控制界面")  # 设置窗口标题
        self.button_index = 0
        self.root.resizable(False, False)  # 设置窗口不可调整大小
        self.title_change = 0  # 将title_change作为实例变量


    # 设置窗口属性
    def window_create(self):
        image_path = os.path.join(os.path.dirname(__file__), "..", "image", "1.jpeg")
        image = Image.open(image_path)
        image = image.resize((780, 600), Image.LANCZOS)
        self.photo_image = ImageTk.PhotoImage(image)
        self.label = tk.Label(self.root, image=self.photo_image)
        self.label.place(x=0, y=0, relwidth=1, relheight=1)

    # 设置界面框架



    # 设置按钮
    def create_button(self):
        # 日志分析
        button_1 = tk.Button(self.root, width=10,height=2 , text=contents_list[0],command=lambda: self.button_command(0),bg='#215E21', fg='white')
        button_1.place(x=button_X, y=button_Y)

        # 防火墙策略
        button_2 = tk.Button(self.root, width=10,height=2 ,text=contents_list[1],command=lambda: self.button_command(1) ,bg='#215E21', fg='white')
        button_2.place(x=button_X, y=button_Y + 55)

        # 系统报警
        button_3 = tk.Button(self.root, width=10,height=2 ,text=contents_list[2],command=lambda:self.button_command(2) ,bg='#215E21', fg='white')
        button_3.place(x=button_X, y=button_Y + 110)

    #设置标题
    def title(self):
        self.title_label = tk.Label(self.root, text=contents_list[self.title_change], width=10, height=2, bg='#215E21',font=("微软雅黑", 20), fg='white')
        self.title_label.place(x=title_X, y=title_Y)

        # 处理按钮点击事件
    def update_title(self, index):
        self.title_change = index
        self.title_label.config(text=contents_list[index])
        # 处理按钮点击事件
    def button_command(self, button_index):
        # 更新标题
        if button_index == 0:
            print('进入日志分析页面')
            # 改变标题
            self.update_title(0)
        elif button_index == 1:
            print('进入防火墙策略页面')
            # 改变标题
            self.update_title(1)
        elif button_index == 2:
            print('进入系统报警页面')
            # 改变标题
            self.update_title(2)

while True:
    app = app()
    app.create_window()
    app.window_create()
    app.window_create()
    app.create_button()
    app.title()
    app.root.mainloop()

