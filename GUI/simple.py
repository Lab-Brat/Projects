import tkinter as tk
from tkinter import ttk


class gui():
    def __init__(self, title, width=300, height=200):
        self.root = tk.Tk()
        self.title = self.root.title(title)
        self.width = width
        self.height = height

    def mid_screen(self, resize=True):
        screen_wid = self.root.winfo_screenwidth()
        screen_hei = self.root.winfo_screenheight()
        #find center
        center_x = int(screen_wid/2 - self.width/2)
        center_y = int(screen_hei/2 - self.height/2)
        self.root.geometry(f'{self.width}x{self.height}+{center_x}+{center_y}')
        if resize==False:
            self.root.resizable(False,False)

    def return_pressed(self, event):
        print('Return key pressed.')

    def log(self, event):
        print(event)

    def button(self):
        btn = ttk.Button(self.root, text='Save')
        btn.bind('<Return>', self.return_pressed)
        btn.bind('<Return>', self.log, add='+')
        btn.focus()
        btn.pack(expand=True)

    def show(self, m_text, position):
        if position == 'mid':
            self.mid_screen()
        else:
            self.root.geometry(self.width, self.height)

        #message = tk.Label(self.root, text=m_text).pack()
        self.button()
        self.root.mainloop()


if __name__ == "__main__":
    title = 'WINDOW'
    m_text = 'This is a window!'
    gui(title).show(m_text, 'mid')
