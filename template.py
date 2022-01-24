import tkinter as tk
import os
from datetime import datetime
 
image_app = os.path.dirname(__file__) + '\\images\\'

background = '#0d1117'
foreground = '#dcf0f9'
container = '#161b22'
container_error = '#301a1f'
select_text = '#2c98ff'
button = '#238636'


class Frame_login(tk.Frame):

    def __init__(self, ancestor, **kwargs):
        tk.Frame.__init__(self)
        self.ancestor = ancestor
        self.configure(background=background)

        self.logo = tk.PhotoImage(file=image_app + 'logo.png')
        self.lbl_logo = tk.Label(self,
                                 image=self.logo,
                                 background=background)
        self.lbl_logo.place(relx=.5, rely=.15, anchor='center')

        self.lbl_signin = tk.Label(self,
                                   text='Faça seu login',
                                   foreground=foreground,
                                   background=background,
                                   font='Verdana 23')
        self.lbl_signin.place(relx=.5, rely=.3, anchor='center')

        self.container = tk.PhotoImage(file=image_app + 'container.png')
        self.lbl_container = tk.Label(self,
                                      image=self.container,
                                      background=background)
        self.lbl_container.place(relx=.5, rely=.55, anchor='center')

        self.lbl_username = tk.Label(self,
                                     text='Nome de usuário',
                                     foreground=foreground,
                                     background=container,
                                     font='Verdana 12')
        self.lbl_username.place(relx=.53, rely=.41, anchor='e')

        self.txt_user_var = tk.StringVar()
        self.txt_user_var.trace('w', self.on_write)

        self.txt_user = tk.Entry(self,
                                 background=background,
                                 foreground=foreground,
                                 textvariable=self.txt_user_var,
                                 font=('Verdana', 12),
                                 borderwidth=0,
                                 highlightcolor=select_text,
                                 highlightbackground='#535d68',
                                 highlightthickness=1,
                                 insertofftime=800,
                                 insertbackground=select_text,
                                 insertwidth=2)
        self.txt_user.place(relx=.5,
                            rely=.47,
                            anchor='center',
                            height=33,
                            width=235)
        self.txt_user.bind('<Key>', self.key_enter)

        self.lbl_password = tk.Label(self,
                                     text='Senha',
                                     foreground=foreground,
                                     background=container,
                                     font='Verdana 12')
        self.lbl_password.place(relx=.422, rely=.54, anchor='e')

        self.txt_password_var = tk.StringVar()
        self.txt_password_var.trace('w', self.on_write)

        self.txt_password = tk.Entry(self,
                                     textvariable=self.txt_password_var,
                                     show='*',
                                     background=background,
                                     foreground=foreground,
                                     font=('Verdana', 12),
                                     borderwidth=0,
                                     highlightcolor=select_text,
                                     highlightbackground='#535d68',
                                     highlightthickness=1,
                                     insertofftime=800,
                                     insertbackground=select_text,
                                     insertwidth=2)
        self.txt_password.place(relx=.5,
                                rely=.6,
                                anchor='center',
                                height=33,
                                width=235)
        self.txt_password.bind('<Key>', self.key_enter)

        self.btn_signin = tk.Button(self,
                                    text='Entrar',
                                    width=25,
                                    command=self.validate,
                                    font='corbel 13',
                                    background=button,
                                    activebackground=select_text,
                                    foreground=foreground,
                                    activeforeground=foreground,
                                    borderwidth=0,
                                    highlightthickness=3)
        self.btn_signin.place(relx=.5, rely=.69, anchor='center')

        self.container_error = tk.PhotoImage(
            file=image_app + 'container_error.png')
        self.lbl_container_error = tk.Label(self,
                                            background=background)
        self.lbl_container_error.place(relx=.5, rely=.81, anchor='center')

        self.txt_container_error = tk.Label(self,
                                            background=background,
                                            foreground=foreground)
        self.txt_container_error.place(relx=.47, rely=.81, anchor='center')

        self.img_error = tk.PhotoImage(file=image_app + 'error.png')
        self.btn_error = tk.Button(self,
                                   command=self.exit_error,
                                   background=background,
                                   activebackground=background,
                                   borderwidth=0,
                                   foreground=foreground,
                                   activeforeground=foreground)
        self.btn_error.place(relx=.6, rely=.795, width=20, height=20)

        # baseboard

        self.img_info = tk.PhotoImage(file=image_app + 'info.png')
        self.btn_info = tk.Button(self,
                                  image=self.img_info,
                                  command=lambda:self.ancestor.show_frame('Frame_page_'),
                                  background=background,
                                  activebackground=background,
                                  borderwidth=0,
                                  foreground=foreground,
                                  activeforeground=foreground)
        self.btn_info.place(relx=.02, rely=.87, width=50, height=50)
        self.btn_info.bind('<Key>', self.key_enter)

    def on_write(self, *args):
        if args[0] == 'PY_VAR0':
            txt_ = self.txt_user_var
        else:
            txt_ = self.txt_password_var
        s = txt_.get()
        if len(s):
            if not s[-1]:
                txt_.set(s[:-1])
            else:
                txt_.set(s[:15])

    def validate(self):
        user = os.getlogin().upper()
        password = datetime.today().strftime('%d%m%Y')
        if user == self.txt_user.get().upper() and password == self.txt_password.get():
            self.btn_signin.configure(text='Entrando...')
            self.update()
            self.exit_error()
            self.after(1000, self.ancestor.show_frame('Frame_page_'))
            self.btn_signin.configure(text='Entrar')
            self.txt_user.focus_set()
        else:
            self.lbl_container_error.config(image=self.container_error)
            self.txt_container_error.config(
                text='Usuário ou senha incorretos.', background=container_error)
            self.btn_error.config(
                image=self.img_error, background=container_error, activebackground=container_error)
        self.txt_user.delete(0, "end")
        self.txt_password.delete(0, "end")

    def key_enter(self, event=None):
        key = event.keysym.upper()
        if key == 'RETURN':
            if str(self.focus_get()) == '.!frame_login.!entry':
                self.txt_password.focus_set()
            elif str(self.focus_get()) == '.!frame_login.!entry2':
                self.validate()
        if key == 'TAB':
            if str(self.focus_get()) == '.!frame_login.!entry':
                self.txt_password.focus_set()
            else:
                self.txt_user.focus_set()
            return "break"

    def exit_error(self):
        self.lbl_container_error.config(image='')
        self.txt_container_error.config(text='', background=background)
        self.btn_error.config(
            image='', background=background, activebackground=background)


class Frame_page_(tk.Frame):

    def __init__(self, ancestor, **kwargs):
        tk.Frame.__init__(self)
        self.ancestor = ancestor
        self.configure(background=background)

        self.lbl_title = tk.Label(self,
                                   text='RPA',
                                   foreground=foreground,
                                   background=background,
                                   font='Verdana 50')
        self.lbl_title.place(relx=.29, rely=.15, anchor='center')

        self.lbl_body = tk.Label(self,
                                   text=self.text_info('info.txt'),
                                   foreground=foreground,
                                   background=background,
                                   font='Verdana 16')
        self.lbl_body.place(relx=.29, rely=.5, anchor='center')

        self.page_info = tk.PhotoImage(file=image_app + 'page_info.png')
        self.lbl_page_info = tk.Label(self, 
                                      image=self.page_info,
                                      background=background)
        self.lbl_page_info.place(relx=.75, rely=.44, anchor='center')

        # baseboard

        self.img_return = tk.PhotoImage(file=image_app + 'return.png')
        self.btn_return = tk.Button(self,
                                  image=self.img_return,
                                  command=lambda:self.ancestor.show_frame('Frame_login'),
                                  background=background,
                                  activebackground=background,
                                  borderwidth=0,
                                  foreground=foreground,
                                  activeforeground=foreground)
        self.btn_return.place(relx=.02, rely=.87, width=50, height=50)


    def text_info(self, filename):
        return """
Os bots de software 
Robotic Process Automation 
podem interagir com qualquer 
aplicativo ou sistema da 
mesma forma que as pessoas,
os bots podem se adaptar a 
qualquer interface ou fluxo 
de trabalho.
        """


def center(win):
    win.update_idletasks()

    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    win.geometry(f'{width}x{height}+{x}+{y}')
    win.deiconify()
