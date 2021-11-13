# テキストポップしてくれる君 Ver.1.05

from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter import colorchooser
from tkinter import filedialog
import configparser

#
#

def test_m():
    Test_messe = 'テストメッセージを表示させています。確認用メッセージです A test message is being displayed confirmation message.'
    messeage_label['text'] = Test_messe
    messege_win.after(8000, lambda : del_label())

def Che_comm1():
    Chk1 = chkValue_1.get()
    if Chk1:
        messege_win.overrideredirect(1)
    else:
        messege_win.overrideredirect(0)

def Che_comm2():
    Chk2 = chkValue_2.get()
    print(Chk2)
    if Chk2:
        messege_win.configure(bg='snow')
        messeage_label['background'] = 'snow'
    else:
        messege_win.configure(bg='black')
        messeage_label['background'] = 'black'

def file_dialog():
    typ = [('テキストファイル','*.txt')]
    dir = 'C:\\'
    file = filedialog.askopenfilenames(filetypes = typ, initialdir = dir)
    f_label['text'] = file
    file = file[0]
    config['tp_faile'] = {'file_pass': file}
    with open('tp_config.ini', 'w') as files:
        config.write(files)

def del_label():
    messeage_label['text'] = ''
    
def color_d():
    text_color = colorchooser.askcolor()
    text_color = text_color[1]
    messeage_label['foreground'] = text_color
    config['Font_color'] = {'f_color' : text_color}
    with open('tp_config.ini', 'w') as files:
        config.write(files)

#

#
def maim_s():
    if file:
        with open(file, 'r+', encoding='UTF-8') as f:
            text_data = f.read()
            f.truncate(0)
        if text_data != '':
            messeage_label['text'] = text_data
            messege_win.after(10000, lambda : del_label())
    op_win.after(1000, maim_s)
#
#

op_win = Tk()
op_win.title('テキストポップしてくれる君 Ver.0.03')
op_win.attributes('-topmost',True)
op_win.geometry('400x120')
op_win.attributes('-topmost',True)
#

chkValue_1 = tk.BooleanVar()
chkValue_1.set(False)
chkValue_2 = tk.BooleanVar()
chkValue_2.set(True)
check_button = ttk.Checkbutton(op_win, text='Window_Title_透明', command=Che_comm1,variable=chkValue_1)
check_button.place(x=10,y=50)
check_button2 = ttk.Checkbutton(op_win, text='Window_background_透明',command=Che_comm2,variable=chkValue_2)
check_button2.place(x=10,y=70)
f_frame = tk.LabelFrame(op_win, text='参照ファイル', width=390, height=40)
f_frame.place(x=5,y=5)

f_dialog = ttk.Button(f_frame, text='ファイル参照', command=file_dialog)
f_dialog.place(x=305,y=-6)
f_label = ttk.Label(f_frame, text='*.txt')
f_label.place(x=10,y=0)

test_B = ttk.Button(op_win, text='Test_Messeage', command=test_m)
test_B.place(x=230,y=50)
color_B = ttk.Button(op_win, text='Font_Color', command=color_d)
color_B.place(x=320,y=50)

Ver_Label = ttk.Label(op_win, text='Prototype_テキストポップしてくれる君 Ver.1.05')
Ver_Label.place(x=5,y=100)
end_B = ttk.Button(op_win, text='終了', command=exit)
end_B.place(x=320,y=90)

#
#

messege_win = Toplevel()
messege_win.title('MESSAGE_Window')
messege_win.attributes('-topmost',True)
messege_win.geometry('900x300+700+20')
messege_win.wm_attributes("-transparentcolor", "snow")
messege_win.configure(bg='snow')

#
#

messeage_label = ttk.Label(messege_win,font=('System',20),wraplength=880,foreground='tomato',anchor='w',background='snow')
messeage_label.place(x=5,y=5)

#
# iniファイル系でtxtファイルをSAVE
config = configparser.ConfigParser()

if config.read('tp_config.ini'):
    #print(config)
    if 'tp_faile' in config:
        file = config['tp_faile']['file_pass']
        f_label['text'] = file
    else:
        file =''
        f_label['text'] = '*.txt'
    if 'Font_color' in config:
        text_color = config['Font_color']['f_color']
        messeage_label['foreground'] = text_color
else:
    file =''
    f_label['text'] = '*.txt'

#
#

if __name__ == "__main__":

    maim_s()
    op_win.mainloop()
