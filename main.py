import tkinter as tk
import template

class Show_app(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        width = 830
        height = 585
        self.attributes('-alpha', 0.0)
        self.title('TEMPLATE_')
        self.geometry(f'{width}x{height}')
        self.resizable(width=0, height=0)
        self.iconbitmap(template.image_app + 'icon.ico')
        template.center(self)
        self.attributes('-alpha', 1.0)

        self.frames = {}

        for f in (template.Frame_page_,
                  template.Frame_login):
            name_page = f.__name__
            frame = f(ancestor=self)
            frame.place(x=0, y=0, width=width, height=height)
            self.frames[name_page] = frame


    def show_frame(self, name_page):
        frame = self.frames[name_page]
        frame.tkraise()

if __name__ == "__main__":
    app = Show_app()
    app.mainloop()