from tkinter import *

root = Tk()

LANGS = [
    ('python', 1),
    ('Per1', 2),
    ('Ruby', 3),
    ('Lua', 4)]
print(type(LANGS))
v = IntVar()
v.set(1)

for lang, num in LANGS:
    b = Radiobutton(root, text=lang, variable=v, value=num, indicatoron=False)  # indicatoron=False 设置单选不使用点的方式。
    # fill=X设置和其父窗口一样宽, 可以使用 fill=X 属性
    b.pack(fill=X)

mainloop()

