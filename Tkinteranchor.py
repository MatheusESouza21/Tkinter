from tkinter import *
i=Tk()
i.title('Programa financeiro')
i.geometry('980x720+250+30')

lb1 = Label(i,text='Label 1',bg='yellow')
lb1.place(x=230,y=200)

lb2 = Label(i,text='Label 2',bg='pink')
lb2.place(x=230,y=230)

lb3 = Label(i,text='Label 3',bg='LightGreen')
lb3.place(x=230,y=260)

lb4 = Label(i,text='Label 4',bg='red')
lb4.place(x=230,y=290)

#CODIGO ABAIXO POSICIONA CADA LABEL EM LUGARES DIFERENTES
# APÓS TESTAR COMENTE A LINHA DO LB1 ATE O LB4

lb1.pack(side=LEFT)
lb2.pack(side='left')
lb3.pack(anchor=W) # SEMPRE QUE NÃO UTILZO A OPÇÃO side, ELE SEMPRE SERÁ TOPO
lb4.pack(anchor='w') # SEMPRE QUE NÃO UTILZO A OPÇÃO side, ELE SEMPRE SERÁ TOPO


#lb4.pack(side=BOTTOM, anchor='sw')

lb4.pack(side=TOP, anchor='e')

i.mainloop()