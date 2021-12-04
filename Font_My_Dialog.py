import tkinter as tk
import tkinter.font


class Font_dialog(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        master.geometry('390x320')
        master.title('Font_My_Dialog')
        master.attributes('-topmost',True)
        
        self.var = tk.StringVar(master)
        self.main_pro()


    def get_res(self):
        return self.var_s

    def ok(self):
        self.master.destroy()

    def main_pro(self):
        def show_selected(EVENT):
            n = self.listbox.curselection()
            self.var.set(self.listbox.get(n))
            self.var_s = self.listbox.get(n)
            self.label['font']=(self.var_s,20)

        self.font = tk.font.families(self)
        self.font_list = list(self.font)
        self.font_lost_not = [self.s for self.s in self.font_list if '@' not in self.s]
        self.scroll = tk.Scrollbar(self)
        self.scroll.pack(side=tk.RIGHT,fill='y')

        self.listbox = tk.Listbox(self,width=30,font=('',18),yscrollcommand=self.scroll.set)
        for self.v in self.font_lost_not:
            self.listbox.insert(tk.END,self.v)
        self.listbox.bind('<<ListboxSelect>>',show_selected)
        self.listbox.pack()
        self.scroll['command']=self.listbox.yview

        self.label = tk.Label(self,textvariable=self.var,font=('',20),width=30)
        self.label.pack()

        self.lb = tk.Button(self,text=' O K ',command=self.ok)
        self.lb.pack()

def mains():
    win = tk.Tk()
    app = Font_dialog(master=win)
    app.wait_window(app)
    return app.get_res()

if __name__ == '__main__':
    font = mains()
    print('mains_out==',font)
