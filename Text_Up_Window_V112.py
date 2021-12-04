# 補助ツールテキストポップ君 Ver.1.12

from tkinter import ttk
from tkinter import *
import tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
import os
import configparser
from Font_My_Dialog import mains
#
#
config = configparser.ConfigParser()
if os.path.exists('tp_config.ini'):
    config.read('tp_config.ini')
if os.path.exists('text_log.txt'):
    pass
else:
    fl=open('text_log.txt','w',encoding='utf-8')
    fl.write('')
    fl.close

def test_m():
    Test_messe = 'テストメッセージを表示させています。確認用メッセージです A test message is being displayed confirmation message.'
    messeage_label['text'] = Test_messe
    if os.path.exists('tp_config.ini'):
        config.read('tp_config.ini')
    if config.has_option('del_check','check'):
        check = config.getboolean('del_check','check')
        if check:
            if config.has_option('del_time','times'):
                times=config.getint('del_time','times')
                messeage_label.after(times,lambda:del_label())
            else:
                messeage_label.after(8000,lambda:del_label())
    config.read('tp_config.ini')
    if config.has_option('Font_data','font'):
        font_f = config.get('Font_data','font')
        if config.has_option('Font_size','f_size'):
            font_s = config.getint('Font_size','f_size')
            messeage_label['font'] = (font_f,font_s)
        else:
            font_s = int(14)
            messeage_label['font'] = (font_f,font_s)
    else:
        if config.has_option('Font_size','f_size'):
            font_s = config.getint('Font_size','f_size')
            messeage_label['font'] = ('',font_s)
        else:
            messeage_label['font'] = ('',16)

def del_label():
    messeage_label['text'] = ''

def Che_comm1():
    Chk1 = chkValue_1.get()
    if Chk1:
        messege_win.overrideredirect(1)
    else:
        messege_win.overrideredirect(0)

def Che_comm2():
    Chk2 = chkValue_2.get()
    if Chk2:
        messege_win.configure(bg='snow')
        messeage_label['background'] = 'snow'
    else:
        messege_win.configure(bg='black')
        messeage_label['background'] = 'black'

def Che_comm3():
    Chk3 = chkValue_3.get()
    config['del_check'] = {'check' : Chk3}
    with open('tp_config.ini', 'w') as files:
        config.write(files)
    if Chk3:
        del_time_b['state'] = 'normal'
        if 'del_time' in config:
            times = config.getint('del_time','times')/1000
            times = int(times)
            del_time_l['text'] = times,'秒'
        else:
            del_time_l['text'] = '8','秒'
    else:
        del_time_b['state'] = 'disabled'
        del_time_l['text'] = '秒'
    if os.path.exists('tp_config.ini'):
        config.read('tp_config.ini')
        if config.has_option('del_check','check'):
            check = config.getboolean('del_check','check')
            if check:
                if config.has_option('del_time','times'):
                    times=config.getint('del_time','times')
                    messeage_label.after(times,lambda:del_label())
                else:
                    messeage_label.after(8000,lambda:del_label())
            else:
                pass        

def file_dialog():
    typ = [('テキストファイル','*.txt')]
    dir = 'C:\\'
    file = filedialog.askopenfilenames(filetypes = typ, initialdir = dir)
    if file:
        file = file[0]
        config['tp_faile'] = {'file_pass': file}
        f_label['text'] = file
        with open('tp_config.ini', 'w') as files:
            config.write(files)
    
def color_d():
    text_color = colorchooser.askcolor()
    if text_color[1]:
        text_color = text_color[1]
        messeage_label['foreground'] = text_color
        color_Button['foreground'] = text_color
        config['Font_color'] = {'f_color' : text_color}
        with open('tp_config.ini', 'w') as files:
            config.write(files)

def font_d():
    font_data = mains()
    config['Font_data'] = {'font' : font_data}
    if font_data:
        with open('tp_config.ini', 'w') as files:
            config.write(files)
        if config.has_option('Font_size','f_size'):
            font_s = config.getint('Font_size','f_size')
            messeage_label['font'] = (font_data,font_s)
            font_label['text'] = '[ '+font_data+' ]'+'  SIZE= '+str(font_s)
        else:
            messeage_label['font'] = (font_data,14)
        color_Button['font'] = (font_data,12)
        font_label['text'] = '[ '+font_data+' ]'+'  SIZE= '+'14'
        config['Font_data'] = {'Font' : font_data}

    else:
        messeage_label['font'] = ('System',14)

def font_ds(EVENT):
    f_size = int(f_size_combox.get())
    config['Font_size'] = {'f_size' : f_size}
    if config.has_option('Font_data','font'):
        font_data = config.get('Font_data','font')
        messeage_label['font'] = (font_data,f_size)
        font_label['text'] = '[ '+font_data+' ]'+'  SIZE= '+str(f_size)
    else:
        messeage_label['font'] = ('',f_size)
    with open('tp_config.ini','w') as f:
        config.write(f)
    

def del_time_set():
    time_set = del_time_e.get()
    time_set = int(time_set)*1000
    config['del_time'] = {'times' : time_set}
    with open('tp_config.ini', 'w') as files:
        config.write(files)
    time_set = config.getint('del_time','times')/1000
    time_set = int(time_set)
    del_time_l['text'] = time_set,'秒'
#
def Re_text():
    with open('text_log.txt','r',encoding='utf-8') as f3:
        text_log2 = f3.read()
        messeage_label['text'] = text_log2
        f3.close()
    if os.path.exists('tp_config.ini'):
        config.read('tp_config.ini')
        if config.has_option('del_check','check'):
            check = config.getboolean('del_check','check')
            if check:
                if config.has_option('del_time','times'):
                    times=config.getint('del_time','times')
                    messeage_label.after(times,lambda:del_label())
                else:
                    messeage_label.after(8000,lambda:del_label())
            else:
                pass
#
def end():
    op_win.destroy()
#
def maim_s():
    w_size = messege_win.winfo_width() 
    messeage_label['wraplength'] = w_size-20
    if config.has_option('tp_faile','file_pass'):
        file = config.get('tp_faile','file_pass')
        with open(file, 'r', encoding='UTF-8') as f:
            text_data = f.read()
            text_data = text_data.replace('。', '。\n')
            f.close()
        with open('text_log.txt','r',encoding='utf-8') as f2:
            text_log = f2.read()
            f2.close()
        if text_data != '':
            if text_data == text_log:
                pass
            else:
                messeage_label['text'] = text_data
                text_log = text_data
                with open('text_log.txt','w',encoding='utf-8') as f:
                    f.write(text_log)
                if os.path.exists('tp_config.ini'):
                    config.read('tp_config.ini')
                    if config.has_option('del_check','check'):
                        check = config.getboolean('del_check','check')
                        if check:
                            if config.has_option('del_time','times'):
                                times=config.getint('del_time','times')
                                messeage_label.after(times,lambda:del_label())
                            else:
                                messeage_label.after(8000,lambda:del_label())
                        else:
                            pass

    op_win.after(500, maim_s)
#
#
config.read('tp_config.ini')
#
op_win = Tk()
op_win.title('補助ツールテキストポップ君 Ver.1.12') # バージョン
op_win.attributes('-topmost',True)
op_win.geometry('400x230+200+600')
#

chkValue_1 = tk.BooleanVar()
chkValue_1.set(False)
chkValue_2 = tk.BooleanVar()
chkValue_2.set(True)
chkValue_3 = tk.BooleanVar()
if os.path.exists('tp_config.ini'):
    if 'del_check' in config:
        if 'check' in config['del_check']:
            chkValue_3.set(config.getboolean('del_check','check'))
        else:
            chkValue_3.set(False)

check_button = ttk.Checkbutton(op_win, text='Window_Title_透明', command=Che_comm1,variable=chkValue_1)
check_button.place(x=10,y=125)
check_button2 = ttk.Checkbutton(op_win, text='Window_background_透明',command=Che_comm2,variable=chkValue_2)
check_button2.place(x=10,y=145)
check_button3 = ttk.Checkbutton(op_win, text='テキスト消去タイマー(default=8秒)',command=Che_comm3,variable=chkValue_3)
check_button3.place(x=10,y=165)

f_frame = tk.LabelFrame(op_win, text='参照ファイル', width=390, height=40)
f_frame.place(x=5,y=5)
f_frame2 = tk.LabelFrame(op_win, text='フォント', width=390, height=40)
f_frame2.place(x=5,y=44)
f_frame3 = tk.LabelFrame(op_win, text='フォントカラー', width=390, height=40)
f_frame3.place(x=5,y=83)
f_frame4 = tk.LabelFrame(op_win, text='消去タイマー',width=200, height=40)
f_frame4.place(x=5,y=185)

f_dialog = ttk.Button(f_frame, text='ファイル参照', command=file_dialog)
f_dialog.place(x=305,y=-6)
f_label = ttk.Label(f_frame, text='*.txt')
f_label.place(x=10,y=0)

font_B = ttk.Button(f_frame2, text='Font', command=font_d)
font_B.place(x=255,y=-6)
font_label = ttk.Label(f_frame2)
font_label.place(x=5,y=-3)
module = (14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
v = tk.StringVar()
f_size_combox = ttk.Combobox(f_frame2,textvariable=v,values=module,width=4)
f_size_combox.bind('<<ComboboxSelected>>',font_ds)
f_size_combox.place(x=335,y=-4)

color_B = ttk.Button(f_frame3, text='Font_Color', command=color_d)
color_B.place(x=305,y=-6)
color_Button = ttk.Label(f_frame3,text='あいうえ      ABCD', font=(12),foreground='tomato')
color_Button.place(x=70,y=-4)

test_B = ttk.Button(op_win, text='Test_Messeage', command=test_m)
test_B.place(x=220,y=125)
clear_B = ttk.Button(op_win, text='clear', command=del_label)
clear_B.place(x=315,y=125)
re_messe = ttk.Button(op_win, text='Re TEXT',command=Re_text)
re_messe.place(x=315,y=155)

del_time_l = ttk.Label(f_frame4, text='秒')
del_time_l.place(x=5,y=0)
del_time_e = tk.Entry(f_frame4,width=4)
del_time_e.place(x=115,y=-3)
del_time_b = ttk.Button(f_frame4,text='セット',width=6,command=del_time_set, state='disabled')
del_time_b.place(x=149,y=-5)

end_B = ttk.Button(op_win, text='終了', command=end)
end_B.place(x=315,y=200)

#
#

messege_win = Toplevel(op_win)
messege_win.title('MESSAGE_Window')
messege_win.attributes('-topmost',True)
messege_win.geometry('900x400+700+20')
messege_win.wm_attributes("-transparentcolor", "snow")
messege_win.configure(bg='snow')
messege_win.protocol('WM_DELETE_WINDOW', (lambda: 'pass'))

#
#

messeage_label = ttk.Label(messege_win,wraplength=880,foreground='tomato',anchor='w',background='snow')
messeage_label.place(x=5,y=5)

#
def test():                                                     # バージョン
    messagebox.showinfo('README', '[ 補助ツールテキストポップ君 Ver.1.12 ]\n\n2021年6月より、０からPythonを独学しました\nこのソフトを使用は「自己責任」でお願いします。\n追加機能と、不具合は気分とリアル仕事次第で！\n最後に「こんなアプリでも使ってくださいまして\nありがとうございます！(/・ω・)/」\n作者：はんぐぅ\nTwitter : @hangu_dog')

#
menuber = tkinter.Menu(op_win)
test_menu = tkinter.Menu(menuber, tearoff=0)

menuber.add_cascade(label='～メモ～', menu=test_menu)
test_menu.add_command(label='README', command=test)

op_win.config(menu=menuber)

# iniファイル系でtxtファイルをSAVE

if os.path.exists('tp_config.ini'):
    if config.has_option('tp_faile','file_pass'):
        file = config.get('tp_faile','file_pass')
        f_label['text'] = file
    else:
        file =''
        f_label['text'] = '*.txt'

    if config.has_section('Font_color'):
        if config.has_option('Font_color','f_color'):
            text_color = config.get('Font_color','f_color')
            messeage_label['foreground'] = text_color
            color_Button['foreground'] = text_color

    if config.has_option('Font_data','font'):
        font_f = config.get('Font_data','font')
        font_label['text'] = '[ '+font_f+' ]'
        color_Button['font'] = (font_f,14)
        if config.has_option('Font_size','f_size'):
            font_s = config.getint('Font_size','f_size')
            font_label['text'] = '[ '+font_f+' ]'+'  SIZE= '+str(font_s)
            messeage_label['font'] = (font_f,font_s)
        else:
            messeage_label['font'] = (font_f,20)
    else:
        if config.has_option('Font_size','f_size'):
            font_s = config.getint('Font_size','f_size')
            messeage_label['font'] = ('',font_s)

    if config.has_section('del_check'):
        Chk3 = config.getboolean('del_check','check')
        if Chk3:            
            del_time_b['state'] = 'normal'
            if 'del_time' in config:
                times = config.getint('del_time','times')/1000
                times = int(times)
                del_time_l['text'] = times,'秒'
            else:
                del_time_l['text'] = '8','秒'
        else:
            del_time_b['state'] = 'disabled'
else:
    file =''
    f_label['text'] = '*.txt'

#
#

if __name__ == "__main__":

    maim_s()
    op_win.mainloop()
