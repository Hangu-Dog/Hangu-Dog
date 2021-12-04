#------ Class化　スクリプト ------
#------ 補助ツールテキストポップ君 Ver.1.15 ------

from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
import os
import configparser
from Font_My_Dialog import mains

#-----------------------------------------------------------------------------

class Text_pop_app(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.configs = configparser.ConfigParser()
        self.tp_config = 'tp_config.ini'
        self.text_log_f = 'text_log.txt'
        self.file = ''
        if os.path.exists(self.tp_config):
            self.configs.read(self.tp_config)
        if os.path.exists(self.text_log_f):
            pass
        else:
            f =open(self.text_log_f,'w',encoding='utf-8')
            f.write('')
            f.close()
        
        self.master.title('補助ツールテキストポップ君 Ver.1.15')
        self.master.attributes('-topmost', True)
        self.master.geometry('400x230+200+600')

        self.main_widget()
        self.main_s()
        self.config_load()

#-----------------------------------------------------------------------------

    def config_load(self):
        self.configs.read(self.tp_config)
        if self.configs.has_option('tp_file','file_pass'):
            self.file = self.configs.get('tp_file','file_pass')
            self.f_label['text'] = self.file

        if self.configs.has_option('Font_data','font'):
            self.font_f = self.configs.get('Font_data','font')

        if self.configs.has_option('Font_data','f_size'):
            self.font_s = self.configs.getint('Font_data','f_size')

        if self.configs.has_option('Font_color','f_color'):
            self.text_color = self.configs.get('Font_color','f_color')

        if self.configs.has_option('del_check','check'):
            self.Chk3 = self.configs.getboolean('del_check','check')
            self.chkvalue_3.set(self.Chk3)
            if self.Chk3:
                self.del_time_b['state'] = 'normal'
                if self.configs.has_option('del_time','times'):
                    self.time_set_int = self.configs.getint('del_time','times')
                    self.time_set = int(self.time_set_int/1000)
                    self.del_time_l['text'] = self.time_set,'秒'
                    self.messeage_label.after(self.time_set,lambda: self.del_label())
            else:
                self.Chk3 = self.configs.getboolean('del_check','check')       
                self.chkvalue_3.set(False)
                self.del_time_b['state'] = 'disabled'
                
        if self.configs.has_option('Font_data','font'):
            self.font_f = self.configs.get('Font_data','font')
            if self.configs.has_option('Font_size','f_size'):
                self.font_s = self.configs.get('Font_size','f_size')
                self.messeage_label['font'] = (self.font_f,self.font_s)
                self.font_label['text'] = f'[ {self.font_f} ] SIZE= {str(self.font_s)}'
            else:
                self.messeage_label['font'] = (self.font_f,14)
                self.font_label['text'] = f'[ {self.font_f} ]'

        if self.configs.has_option('Font_size','f_size'):
            self.font_s = self.configs.getint('Font_size','f_size')
            if self.configs.has_option('Font_data','font'):
                pass
            else:
                self.messeage_label['font'] = ('',self.font_s)
                self.font_label['text'] = f'[ default ]  SIZE= {str(self.font_s)}'

        if self.configs.has_option('Font_color','f_color'):
            self.text_color = self.configs.get('Font_color','f_color')
            self.messeage_label['foreground'] = self.text_color
            self.color_Button['foreground'] = self.text_color

#-----------------------------------------------------------------------------
            
    def file_dialog(self):
        self.typ = [('テキストファイル','*.txt')]
        self.dir = 'C:\\'
        self.file = filedialog.askopenfilenames(filetype = self.typ, initialdir = self.dir)
        if self.file:
            self.file = self.file[0]
            self.configs['tp_file'] = {'file_pass' : self.file}
            self.f_label['text'] = self.file
            with open(self.tp_config, 'w') as f:
                self.configs.write(f)

    def test_m(self,re_text='テストメッセージを表示させています。確認用メッセージです A test message is being displayed confirmation message.'):
        self.messeage_label['text'] = re_text
        if self.Chk3:
            if self.configs.has_option('del_time','times'):
                self.time_set_int = self.configs.getint('del_time','times')
                self.messeage_label.after(self.time_set_int,lambda:self.del_label())
            else:
                self.messeage_label.after(8000,lambda:self.del_label())
        else:
            pass


    def Che_comm1(self):
        self.Chk1 = self.chkvalue_1.get()
        if self.Chk1:
            self.messeage_win.overrideredirect(1)
        else:
            self.messeage_win.overrideredirect(0)

    def Che_comm2(self):
        self.Chk2 = self.chkvalue_2.get()
        if self.Chk2:
            self.messeage_win.configure(bg='snow')
            self.messeage_label['background'] = 'snow'
        else:
            self.messeage_win.configure(bg='black')
            self.messeage_label['background'] = 'black'

    def Che_comm3(self):
        self.Chk3 = self.chkvalue_3.get()
        self.configs['del_check'] = {'check' : self.Chk3}
        with open(self.tp_config, 'w') as f:
            self.configs.write(f)
        if self.Chk3:
            if self.configs.has_option('del_time','times'):
                self.time_set_int = self.configs.getint('del_time','times')
                self.messeage_label.after(self.time_set_int,lambda: self.del_label())
                self.time_set_int = int(self.time_set_int/1000)
                self.del_time_b['state'] = 'normal'
                self.del_time_l['text'] = self.time_set_int,'秒'
            else:
                self.messeage_label.after(8000,lambda: self.del_label())
                self.del_time_b['state'] = 'normal'
                self.del_time_l['text'] = '8 秒'
        else:
            self.del_time_b['state'] = 'disabled'
            self.del_time_l['text'] = '秒'

    def del_label(self):
        self.messeage_label['text'] = ''
    
    def del_time_set(self):
        self.time_set = self.del_time_e.get()
        self.del_time_l['text'] = self.time_set,' 秒'
        self.time_set_int = int(self.time_set)
        self.time_set_int = self.time_set_int*1000
        self.messeage_label.after(self.time_set_int,lambda: self.del_label())
        self.configs['del_time'] = {'times' : self.time_set_int}
        with open(self.tp_config,'w',) as f:
            self.configs.write(f)
        
    
    def font_d(self):
        self.font_f = mains()
        if self.font_f:
            self.configs['Font_data'] = {'font' : self.font_f}
            if self.configs.has_option('Font_size','f_size'):
                self.font_s = self.configs.get('Font_size','f_size')
                self.font_label['text'] = f'[ {self.font_f} ]  SIZE= {self.font_s}'
                self.messeage_label['font'] = (self.font_f,self.font_s)
            else:
                self.font_label['text'] = f'[ {self.font_f} ]'
                self.messeage_label['font'] = (self.font_f,14)
            self.color_Button['font'] = (self.font_f,14)
            with open(self.tp_config,'w') as f:
                self.configs.write(f)
        else:
            self.messeage_label['font'] = ('System',20)

    def font_ds(self,EVENT):
        self.font_s = int(self.f_size_combox.get())
        self.configs['Font_size'] = {'f_size' : self.font_s}
        with open(self.tp_config,'w') as f:
            self.configs.write(f)

        if self.configs.has_option('Font_data','font'):
            self.font_f = self.configs.get('Font_data','font')
            self.font_label['text'] = f'[ {self.font_f} ]  SIZE= {self.font_s}'
            self.messeage_label['font'] = (self.font_f,self.font_s)
        else:
            self.font_label['text'] = f'[ default ]  SIZE= {self.font_s}'

    def test(self):
        messagebox.showinfo('README', '[ 補助ツールテキストポップ君 Ver.1.15 ]\n\n2021年6月より、０からPythonを独学しました\nこのソフトを使用は「自己責任」でお願いします。\n追加機能と、不具合は気分とリアル仕事次第で！\n最後に「こんなアプリでも使ってくださいまして\nありがとうございます！(/・ω・)/」\n作者：はんぐぅ\nTwitter : @hangu_dog')

    def end(self):
        self.master.destroy()
        print('終了処理完了')
    
    def Re_text(self):
        with open(self.text_log_f,'r',encoding='UTF-8') as f:
            self.text_log2 = f.read()
        if self.text_log2:
            self.test_m(self.text_log2)

    def color_d(self):
        self.text_color = colorchooser.askcolor()
        if self.text_color[1]:
            self.text_color = self.text_color[1]
            self.messeage_label['foreground'] = self.text_color
            self.color_Button['foreground'] = self.text_color
            self.configs['Font_color'] = {'f_color' : self.text_color}
            with open(self.tp_config,'w') as f:
                self.configs.write(f)

    def main_s(self):
        self.w_size = self.messeage_win.winfo_width()
        self.messeage_label['wraplength'] = self.w_size-20
        if self.configs.has_option('tp_file','file_pass'):
            self.file = self.configs.get('tp_file','file_pass')
            with open(self.file, 'r+', encoding='UTF-8') as f:
                self.text_data = f.read()

            with open(self.text_log_f,'r',encoding='UTF-8') as f:
                self.text_log = f.read()
                
            if self.text_data != '':
                if self.text_data == self.text_log:
                    pass
                else:
                    self.messeage_label['text'] = self.text_data
                    self.text_log = self.text_data
                    with open(self.text_log_f,'w',encoding='UTF-8') as f:
                        f.write(self.text_log)
                    if self.configs.has_option('del_check','check'):
                        self.Chk3 = self.configs.getboolean('del_check','check')
                        if self.Chk3:
                            if self.configs.has_option('del_time','times'):
                                self.time_set_int = self.configs.getint('del_time','times')
                                self.messeage_label.after(self.time_set_int,lambda:self.del_label())
                            else:
                                self.messeage_label.after(8000,lambda:self.del_label())
                        else:
                            pass
                    else:
                        pass
            else:
                pass
        self.after(500, self.main_s)

#-----------------------------------------------------------------------------

    def main_widget(self):
        self.chkvalue_1 = tk.BooleanVar()
        self.chkvalue_1.set(False)
        self.chkvalue_2 = tk.BooleanVar()
        self.chkvalue_2.set(True)
        self.chkvalue_3 = tk.BooleanVar()
        
        self.check_button = ttk.Checkbutton(self.master,text = 'Window_Title_透明', command = self.Che_comm1, variable=self.chkvalue_1)
        self.check_button.place(x=10,y=125)
        self.check_button2 = ttk.Checkbutton(self.master, text = 'Window_background_透明', command = self.Che_comm2, variable=self.chkvalue_2)
        self.check_button2.place(x=10,y=145)
        self.check_button3 = ttk.Checkbutton(self.master, text = 'テキスト消去タイマー(default=8秒)', command = self.Che_comm3, variable=self.chkvalue_3)
        self.check_button3.place(x=10,y=165)

        self.f_frame = tk.LabelFrame(self.master, text = '参照ファイル', width=390, height=40)
        self.f_frame.place(x=5,y=5)
        self.f_frame2 = tk.LabelFrame(self.master, text='フォント', width=390,height=40)
        self.f_frame2.place(x=5,y=44)
        self.f_frame3 = tk.LabelFrame(self.master, text='フォントカラー', width=390, height=40)
        self.f_frame3.place(x=5,y=83)
        self.f_frame4 = tk.LabelFrame(self.master,text='消去タイマー',width=200,height=40)
        self.f_frame4.place(x=5,y=185)

        self.f_dialog = ttk.Button(self.f_frame, text='ファイル参照',command=self.file_dialog)
        self.f_dialog.place(x=305,y=-6)
        self.f_label = ttk.Label(self.f_frame, text='*.txt')
        self.f_label.place(x=5,y=-3)

        self.font_B = ttk.Button(self.f_frame2,text='Font',command=self.font_d)
        self.font_B.place(x=255,y=-6)
        self.font_label = ttk.Label(self.f_frame2)
        self.font_label.place(x=5,y=-3)
        self.module = (14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
        self.v = tk.StringVar()
        self.f_size_combox = ttk.Combobox(self.f_frame2,textvariable=self.v,values=self.module,width=4)
        self.f_size_combox.bind('<<ComboboxSelected>>',self.font_ds)
        self.f_size_combox.place(x=335,y=-4)

        self.color_B = ttk.Button(self.f_frame3, text='Font_Color', command=self.color_d)
        self.color_B.place(x=305,y=-6)
        self.color_Button = ttk.Label(self.f_frame3, text='あいうえ　　　ABCD', font=('',12),foreground='tomato')
        self.color_Button.place(x=70,y=-4)

        self.test_B = ttk.Button(self.master,text='Test_Messeage',command=self.test_m)
        self.test_B.place(x=220,y=125)
        self.clear_B = ttk.Button(self.master, text='clear',command=self.del_label)
        self.clear_B.place(x=315,y=125)

        self.del_time_l = ttk.Label(self.f_frame4, text='秒')
        self.del_time_l.place(x=5,y=0)
        self.del_time_e = tk.Entry(self.f_frame4,width=4)
        self.del_time_e.place(x=115,y=-3)
        self.del_time_b = ttk.Button(self.f_frame4,text='セット',width=6,command=self.del_time_set,state='disabled')
        self.del_time_b.place(x=149,y=-5)

        self.re_messe = ttk.Button(self.master,text='Re TEXT',command=self.Re_text)
        self.re_messe.place(x=315,y=155)

        self.end_B = ttk.Button(self.master,text='終了',command=self.end)
        self.end_B.place(x=315,y=200)

        #--------------------------------------------------------------

        self.messeage_win = Toplevel()
        self.messeage_win.title('MESSEAGE_Window')
        self.messeage_win.attributes('-topmost',True)
        self.messeage_win.geometry('900x400+700+20')
        self.messeage_win.wm_attributes('-transparentcolor','snow')
        self.messeage_win.configure(bg='snow')
        #------
        self.messeage_label = ttk.Label(self.messeage_win,font=('System',20),wraplength=800,foreground='tomato',anchor='w',background='snow')
        self.messeage_label.place(x=5,y=5)
        #------
        self.messeage_win.protocol('WM_DELETE_WINDOW', (lambda: 'pass'))

        #--------------------------------------------------------------

        self.menu_ber = tk.Menu(self)
        root.config(menu=self.menu_ber)

        self.test_menu = tk.Menu(self.menu_ber,tearoff=0)
        self.menu_ber.add_cascade(label='～メモ～',menu=self.test_menu)
        self.test_menu.add_command(label='READEM',command=self.test)
        
#--------------------------------------------------------------
def main():
    root = tk.Tk()
    app = Text_pop_app(master=root)
    app.mainloop()
#--------------------------------------------------------------

#--------------------------------------------------------------
if __name__ == '__main__':
    root = tk.Tk()
    app = Text_pop_app(master=root)
    app.mainloop()

#--------------------------------------------------------------
