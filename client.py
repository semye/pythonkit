from tkinter import *
import json


class Application(Frame):
    result = {}
    layout = {}
    style = {}
    border = {}
    action = {}
    count = 0
    widgets = {}

    # 是新建还是编辑 false 为编辑  true为新建
    status = FALSE

    # 当前下标
    item_index = 0

    def __init__(self, master: NONE):
        super().__init__(master)
        self.master = master
        self.pack(anchor=W)

        # 左边布局
        self.leftFrame = Frame(self, width=500, height=760, relief="solid", borderwidth=1)
        self.leftFrame.pack(side=LEFT, anchor=W)
        self.leftFrame.pack_propagate(0)

        self.rightFrame = Frame(self, width=500, height=760, relief="solid", borderwidth=1, padx=10)
        self.rightFrame.pack(side=RIGHT, anchor=E)
        self.rightFrame.pack_propagate(0)
        self.rightFrame.pack_forget()

        self.centerFrame = Frame(self, width=200, height=760, relief="solid", borderwidth=1, bg="#efefef")
        self.centerFrame.pack(side=LEFT, anchor=W)
        self.centerFrame.pack_propagate(0)

        listboxV = StringVar()
        self.listbox = Listbox(self.centerFrame, selectmode=SINGLE, listvariable=listboxV)
        self.listbox.pack(expand=FALSE)
        self.listbox.bind("<<ListboxSelect>>", self.on_listbox_selected)

        self.toolFrame = Frame(self.centerFrame, relief="solid")
        self.toolFrame.pack(expand=FALSE, pady=10, fill=X)

        self.new = Button(self.toolFrame, text="新建", width=6)
        self.new['command'] = self.create_type
        self.new.pack()
        self.delete = Button(self.toolFrame, text="删除", width=6)
        self.delete['command'] = self.delete_type
        self.delete.pack()
        self.imt = Button(self.toolFrame, text="导入", width=6)
        self.imt['command'] = self.impt
        self.imt.pack()
        self.button2 = Button(self.toolFrame, text="预览", width=6)
        self.button2['command'] = self.draw
        self.button2.pack()

        self.canvas = Canvas(self.leftFrame, width=375, height=667, bg="#00ff00", relief="solid", borderwidth=1)
        self.canvas.pack(expand=FALSE)
        self.canvas.pack_propagate(0)

        self.content = Entry(self.rightFrame)
        self.content_text = Label(self.rightFrame, text="content")
        self.value_frame = Frame(self.rightFrame)
        self.title_frame = Frame(self.rightFrame)
        self.style_frame = Frame(self.rightFrame)
        self.button1 = Button(self.rightFrame, text="保存")
        self.button1.pack(side=BOTTOM)
        self.button1['command'] = self.save

        self.frame_type = Frame(self.rightFrame)
        self.label_type = Label(self.rightFrame)
        self.layout1 = Frame(self.rightFrame)

        self.bg_color_frame = Frame(self.style_frame)
        self.bg_text_frame = Frame(self.style_frame)
        self.font2_value_frame = Frame(self.style_frame)
        self.padding_frame = Frame(self.style_frame)
        self.border_frame = Frame(self.style_frame)
        self.corner_radius_frame = Frame(self.style_frame)
        self.border_value_frame = Frame(self.style_frame)
        self.font1_value_frame = Frame(self.style_frame)
        self.font1_text_frame = Frame(self.style_frame)
        self.fg_text_frame = Frame(self.style_frame)
        self.font2_text_frame = Frame(self.style_frame)
        self.fg_color_frame = Frame(self.style_frame)

        self.fg_color_night = Entry(self.fg_color_frame)
        self.fg_color = Entry(self.fg_color_frame)

        self.bg_color_night = Entry(self.bg_color_frame)
        self.bg_color = Entry(self.bg_color_frame)

        self.italic = Entry(self.font1_value_frame)
        self.font = Entry(self.font1_value_frame)
        self.v_align = Entry(self.font2_value_frame, width=7)
        self.h_align = Entry(self.font2_value_frame, width=7)
        self.bold = Entry(self.font2_value_frame)

        self.number = IntVar()

        self.v = StringVar()
        self.v.set("text")
        self.radio_video = Radiobutton(self.frame_type, text="视频", variable=self.v, value="video")
        self.radio_gif = Radiobutton(self.frame_type, text="动图", variable=self.v, value="gif")
        self.radio_image = Radiobutton(self.frame_type, text="图片", variable=self.v, value="image")
        self.radio_text = Radiobutton(self.frame_type, text="文字", variable=self.v, value="text")

        self.divide_frame = Frame(self.layout1)
        self.divide_x = Entry(self.divide_frame, width=6)
        self.divide_y = Entry(self.divide_frame, width=6)

        self.frame_frame = Frame(self.layout1)
        self.frame_x = Entry(self.frame_frame, width=6)
        self.frame_y = Entry(self.frame_frame, width=6)
        self.frame_width = Entry(self.frame_frame, width=6)
        self.frame_height = Entry(self.frame_frame, width=6)

        self.frame_margin = Frame(self.layout1)
        self.margin_left = Entry(self.frame_margin, width=6)
        self.margin_top = Entry(self.frame_margin, width=6)
        self.margin_right = Entry(self.frame_margin, width=6)
        self.margin_bottom = Entry(self.frame_margin, width=6)

        self.corner_radius_topLeft = Entry(self.corner_radius_frame, width=6)
        self.corner_radius_topRight = Entry(self.corner_radius_frame, width=6)
        self.corner_radius_bottomRight = Entry(self.corner_radius_frame, width=6)
        self.corner_radius_bottomLeft = Entry(self.corner_radius_frame, width=6)

        self.padding_left = Entry(self.padding_frame, width=6)
        self.padding_top = Entry(self.padding_frame, width=6)
        self.padding_right = Entry(self.padding_frame, width=6)
        self.padding_bottom = Entry(self.padding_frame, width=6)

        self.border_color_night = Entry(self.border_value_frame, width=7)
        self.border_color = Entry(self.border_value_frame, width=7)
        self.border_width = Entry(self.border_value_frame, width=7)

        self.show = Entry(self.value_frame, width=7)
        self.report_urls = Entry(self.value_frame, width=7)
        self.click = Entry(self.value_frame, width=7)
        self.create_right_frame()
        pass

    def create_fg_layout(self):
        self.fg_text_frame.pack(anchor=W)
        Label(self.fg_text_frame, text="foreground_color").pack(side=LEFT)
        Label(self.fg_text_frame, text="foreground_color_night").pack(side=LEFT, padx=70)
        self.fg_color_frame.pack(anchor=W)
        self.fg_color.pack(side=LEFT)
        self.fg_color_night.pack(side=LEFT)
        pass

    def create_bg_layout(self):
        self.bg_text_frame.pack(anchor=W)
        Label(self.bg_text_frame, text="background_color").pack(side=LEFT)
        Label(self.bg_text_frame, text="background_color_night").pack(side=LEFT, padx=70)

        self.bg_color_frame.pack(anchor=W)
        self.bg_color.pack(side=LEFT)
        self.bg_color_night.pack(side=LEFT)
        pass

    def on_listbox_selected(self, evt):
        w = evt.widget
        cur = self.listbox.curselection()
        if len(cur) < 1:
            return
        self.item_index = cur[0]
        self.status = FALSE
        r = w.get(cur[0])
        print("选中的元素名" + r)
        json_file = open("./build/" + self.widgets.get(r), "r")
        json_dict = json_file.read()
        json_data = json.loads(json_dict)

        self.rightFrame.pack()

        self.v.set(json_data['type'])
        self.content.delete(0, END)
        self.content.insert(0, json_data['content'])
        pass

    def on_click(self):
        pass

    '''创建新元素'''

    def create_type(self):
        self.status = True

        self.rightFrame.pack()

        # 重置控件状态
        self.radio_text.select()

        self.content.delete(0, END)
        self.content.insert(0, "标题")

        self.divide_x.delete(0, END)
        self.divide_x.insert(0, 1)
        self.divide_y.delete(0, END)
        self.divide_y.insert(0, 1)

        self.frame_x.delete(0, END)
        self.frame_x.insert(0, 0)
        self.frame_y.delete(0, END)
        self.frame_y.insert(0, 0)
        self.frame_width.delete(0, END)
        self.frame_width.insert(0, 0)
        self.frame_height.delete(0, END)
        self.frame_height.insert(0, 0)

        # 左 上 右 下
        self.margin_left.delete(0, END)
        self.margin_left.insert(0, 0)
        self.margin_top.delete(0, END)
        self.margin_top.insert(0, 0)
        self.margin_right.delete(0, END)
        self.margin_right.insert(0, 0)
        self.margin_bottom.delete(0, END)
        self.margin_bottom.insert(0, 0)

        self.corner_radius_topLeft.delete(0, END)
        self.corner_radius_topLeft.insert(0, 0)
        self.corner_radius_topRight.delete(0, END)
        self.corner_radius_topRight.insert(0, 0)
        self.corner_radius_bottomRight.delete(0, END)
        self.corner_radius_bottomRight.insert(0, 0)
        self.corner_radius_bottomLeft.delete(0, END)
        self.corner_radius_bottomLeft.insert(0, 0)

        self.padding_left.delete(0, END)
        self.padding_left.insert(0, 0)
        self.padding_top.delete(0, END)
        self.padding_top.insert(0, 0)
        self.padding_right.delete(0, END)
        self.padding_right.insert(0, 0)
        self.padding_bottom.delete(0, END)
        self.padding_bottom.insert(0, 0)
        pass

    def delete_type(self):
        pass

    def impt(self):
        pass

    # 保存或修改元素
    def save(self):
        self.rightFrame.pack_forget()

        self.result['type'] = self.v.get()
        self.result['content'] = self.content.get()
        self.result['layer_level'] = 1
        divide = [int(self.divide_x.get()), int(self.divide_y.get())]
        frame = [int(self.frame_x.get()), int(self.frame_y.get()), int(self.frame_width.get()),
                 int(self.frame_height.get())]
        margin = [int(self.margin_left.get()), int(self.margin_top.get()), int(self.margin_right.get()),
                  int(self.margin_bottom.get())]

        self.layout['divide'] = divide
        self.layout['frame'] = frame
        self.layout['margin'] = margin
        self.result['layout'] = self.layout

        self.style['foreground'] = self.fg_color.get()
        self.style['foreground_night'] = self.fg_color_night.get()
        self.style['background'] = self.bg_color.get()
        self.style['background_night'] = self.bg_color_night.get()
        self.style['font'] = self.font.get()
        self.style['italic'] = self.italic.get()
        self.style['bold'] = self.bold.get()
        align = [self.h_align.get(), self.v_align.get()]
        self.style['align'] = align

        top_left = self.corner_radius_topLeft.get()
        top_right = self.corner_radius_topRight.get()
        bottom_right = self.corner_radius_bottomRight.get()
        bottom_left = self.corner_radius_bottomLeft.get()
        corner_radius = [int(top_left), int(top_right), int(bottom_right), int(bottom_left)]
        self.style['corner_radius'] = corner_radius

        padding_left = self.padding_left.get()
        padding_top = self.padding_top.get()
        padding_right = self.padding_right.get()
        padding_bottom = self.padding_bottom.get()
        padding = [int(padding_left), int(padding_top), int(padding_right), int(padding_bottom)]
        self.style['padding'] = padding

        width = self.border_width.get()
        color = self.border_color.get()
        color_night = self.border_color_night.get()

        self.border['width'] = width
        self.border['color'] = color
        self.border['color_night'] = color_night
        self.style['border'] = self.border
        self.style['max_lines'] = 1

        self.result['style'] = self.style

        show = {}
        click = {}
        show['uri'] = self.show.get()
        click['uri'] = self.show.get()
        click['report_urls'] = []
        click['callup_url'] = ''

        self.action['show'] = show
        self.action['click'] = click
        self.result['action'] = self.action

        jon = json.dumps(self.result)

        # 如果是新建
        if self.status:
            print("新建")
            self.count = self.count + 1
            self.listbox.insert(END, str(self.count))
            a = open("./build/" + str(self.count) + ".json", "w")
            a.write(jon)
            a.close()
            self.widgets[str(self.count)] = str(self.count) + '.json'
        else:
            # 修改
            print("修改")
            print(self.widgets[str(self.item_index + 1)])
            a = open("./build/" + self.widgets[str(self.item_index + 1)], "w")
            a.write(jon)
            a.close()
        pass

    def create_font_style1(self):
        self.font1_text_frame.pack(anchor=W)
        Label(self.font1_text_frame, text="font").pack(side=LEFT)
        Label(self.font1_text_frame, text="italic").pack(side=LEFT, padx=155)

        self.font1_value_frame.pack(anchor=W)
        self.font.pack(side=LEFT)
        self.italic.pack(side=LEFT)
        pass

    def create_font_style2(self):
        self.font2_text_frame.pack(anchor=W)
        Label(self.font2_text_frame, text="bold").pack(side=LEFT)
        Label(self.font2_text_frame, text="align").pack(side=LEFT, padx=155)

        self.font2_value_frame.pack(anchor=W)
        self.bold.pack(side=LEFT)
        self.h_align.pack(side=LEFT)
        self.v_align.pack(side=LEFT)
        pass

    def create_right_frame(self):
        # type
        self.label_type["text"] = "type"
        self.label_type.pack(anchor=W)
        self.frame_type.pack(anchor=W)
        self.radio_text.pack(side=LEFT, anchor=W)
        self.radio_image.pack(side=LEFT, anchor=W)
        self.radio_gif.pack(side=LEFT, anchor=W)
        self.radio_video.pack(side=LEFT, anchor=W)
        self.content_text.pack(anchor=W)
        self.content.pack(anchor=W, fill=X)
        self.layout1.pack(fill=X)
        Label(self.layout1, text="divide").pack(anchor=W)
        self.divide_frame.pack(anchor=W)
        self.divide_x.pack(side=LEFT)
        self.divide_y.pack(side=LEFT)

        Label(self.layout1, text="frame").pack(anchor=W)
        self.frame_frame.pack(anchor=W)
        self.frame_x.pack(side=LEFT)
        self.frame_y.pack(side=LEFT)
        self.frame_width.pack(side=LEFT)
        self.frame_height.pack(side=LEFT)

        Label(self.layout1, text="margin").pack(anchor=W)
        self.frame_margin.pack(anchor=W)
        self.margin_left.pack(side=LEFT)
        self.margin_top.pack(side=LEFT)
        self.margin_right.pack(side=LEFT)
        self.margin_bottom.pack(side=LEFT)

        self.style_frame.pack(anchor=W)

        self.create_bg_layout()
        self.create_font_style1()
        self.create_fg_layout()
        self.create_font_style2()

        Label(self.style_frame, text="corner_radius").pack(anchor=W)
        self.corner_radius_frame.pack(anchor=W)
        self.corner_radius_topLeft.pack(side=LEFT)
        self.corner_radius_topRight.pack(side=LEFT)
        self.corner_radius_bottomRight.pack(side=LEFT)
        self.corner_radius_bottomLeft.pack(side=LEFT)

        Label(self.style_frame, text="padding").pack(anchor=W)
        self.padding_frame.pack(anchor=W)
        self.padding_left.pack(side=LEFT)
        self.padding_top.pack(side=LEFT)
        self.padding_right.pack(side=LEFT)
        self.padding_bottom.pack(side=LEFT)

        self.border_frame.pack(anchor=W)
        Label(self.border_frame, text="border width").pack(side=LEFT)
        Label(self.border_frame, text="border color").pack(side=LEFT)
        Label(self.border_frame, text="border color_night").pack(side=LEFT)

        self.border_value_frame.pack(anchor=W)
        self.border_width.pack(side=LEFT)
        self.border_color.pack(side=LEFT)
        self.border_color_night.pack(side=LEFT)

        self.title_frame.pack(anchor=W)
        Label(self.title_frame, text="show").pack(side=LEFT)
        Label(self.title_frame, text="click").pack(side=LEFT)
        Label(self.title_frame, text="report_urls").pack(side=LEFT)

        self.value_frame.pack(anchor=W)
        self.show.pack(side=LEFT)
        self.click.pack(side=LEFT)
        self.report_urls.pack(side=LEFT)

        pass

    '''绘制'''

    def draw(self):

        json_file = open("./build/1.json", "r")
        json_dict = json_file.read()
        json_data = json.loads(json_dict)

        if json_data['type'] == "text":
            self.canvas.create_text(100, 100, text=json_data['content'])
        pass


if __name__ == '__main__':
    root = Tk()
    window = Application(master=root)
    root.title("动态布局生成工具")
    root.maxsize(1200, 760)
    root.minsize(1200, 760)
    window.mainloop()
