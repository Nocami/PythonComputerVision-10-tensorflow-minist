import tensorflow as tf
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import filedialog
import time


def creat_windows():
    win = tk.Tk() # 创建窗口
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    ww, wh = 400, 450
    x, y = (sw-ww)/2, (sh-wh)/2
    win.geometry("%dx%d+%d+%d"%(ww, wh, x, y-40)) # 居中放置窗口

    win.title('手写体识别') # 窗口命名

    bg1_open = Image.open("timg.jpg").resize((300, 300))
    bg1 = ImageTk.PhotoImage(bg1_open)
    canvas = tk.Label(win, image=bg1)
    canvas.pack()


    var = tk.StringVar() # 创建变量文字
    var.set('')
    tk.Label(win, textvariable=var, bg='#C1FFC1', font=('宋体', 21), width=20, height=2).pack()

    tk.Button(win, text='选择图片', width=20, height=2, bg='#FF8C00', command=lambda:main(var, canvas), font=('圆体', 10)).pack()
    
    win.mainloop()

def main(var, canvas):
    file_path = filedialog.askopenfilename()
    bg1_open = Image.open(file_path).resize((28, 28))
    pic = np.array(bg1_open).reshape(784,)
    bg1_resize = bg1_open.resize((300, 300))
    bg1 = ImageTk.PhotoImage(bg1_resize)
    canvas.configure(image=bg1)
    canvas.image = bg1

    init = tf.global_variables_initializer()

    with tf.Session() as sess:
            sess.run(init)
            saver = tf.train.import_meta_graph('save/model.meta')  # 载入模型结构
            saver.restore(sess, 'save/model')  # 载入模型参数
            graph = tf.get_default_graph()       # 加载计算图
            x = graph.get_tensor_by_name("x-input:0")  # 从模型中读取占位符变量
            keep_prob = graph.get_tensor_by_name("keep_prob:0")
            y_conv = graph.get_tensor_by_name("y-pred:0")  # 关键的一句  从模型中读取占位符变量
            prediction = tf.argmax(y_conv, 1)
            predint = prediction.eval(feed_dict={x: [pic], keep_prob: 1.0}, session=sess)  # feed_dict输入数据给placeholder占位符
            answer = str(predint[0])
    var.set("预测的结果是：" + answer)

if __name__ == "__main__":
    creat_windows()
