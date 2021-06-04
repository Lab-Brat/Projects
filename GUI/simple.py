import tkinter as tk

root = tk.Tk()
root.title('WINDOW')
# root.geometry('600x400')

win_wid = 300
win_hei = 200
# screen dimensions
screen_wid = root.winfo_screenwidth()
screen_hei = root.winfo_screenheight()
#find center
center_x = int(screen_wid/2 - win_wid/2)
center_y = int(screen_hei/2 - win_hei/2)
root.geometry(f'{win_wid}x{win_hei}+{center_x}+{center_y}')


message = tk.Label(root, text='This is a window!')
message.pack()

# display the window
root.mainloop()
