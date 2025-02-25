from tkinter import *
i=Tk()
i.title('Programa financeiro')
i.geometry('980x720+250+30')

lb1 = Label(i,text='Label 1',bg='yellow')
lb1.place(x=230,y=200)

lb2 = Label(i,text='Label 1',bg='pink')
lb2.place(x=230,y=230)

lb3 = Label(i,text='Label 1',bg='LightGreen')
lb3.place(x=230,y=260)

lb4 = Label(i,text='Label 1',bg='red')
lb4.place(x=230,y=290)

'''lb1.pack()
lb2.pack()
lb3.pack()
lb4.pack()'''


#O codigo abaixo é responável para posicionar o label no topo da interface
#lb1.pack(side='top')

#O codigo abaixo é responável para posicionar o label a esquerda da interface
#lb2.pack(side='left')

#O codigo abaixo é responável para posicionar o label a direita da interface
#lb3.pack(side='right')

#O codigo abaixo é responável para posicionar o label para baixo na interface
#lb4.pack(side='bottom')

lb1.pack(side='left')
lb2.pack(side='left')
lb3.pack()
lb4.pack()

i.mainloop()