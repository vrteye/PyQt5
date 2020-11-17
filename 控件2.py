


monty2 = ttk.LabelFrame(tab2, text='方案②')
monty2.grid(column=0, row=0, padx=8, pady=4)
chVarDis = tk.IntVar()

values = ["富强民主", "文明和谐"]


# Radiobutton callback function
def radCall():
    radSel = radVar.get()
    print(radSel)
    if radSel == 0:
        monty2.configure(text='富强民主')
    elif radSel == 1:
        monty2.configure(text='文明和谐')


radVar = tk.IntVar()
radVar.set(99)
for col in range(2):
    # curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(monty2, text=values[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W, columnspan=4)
labelsFrame = ttk.LabelFrame(monty2, text=' 嵌套区域 ')
labelsFrame.grid(column=0, row=8, columnspan=4)
ttk.Label(labelsFrame, text="你才25岁，你可以成为任何你想成为的人。").grid(column=0, row=0)
# Add some space around each label