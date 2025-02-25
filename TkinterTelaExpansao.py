from tkinter import *
i=Tk()
i.title('Programa financeiro')
i.geometry('980x720+250+30')

lb1 = Label(i,text='Label 1',bg='yellow')
lb1.place(x=230,y=200)

lb2 = Label(i,text='Label 2',bg='pink')
lb2.place(x=230,y=200)

lb3 = Label(i,text='Label 3',bg='LightGreen')
lb3.place(x=230,y=200)

lb4 = Label(i,text='Label 4',bg='red')
lb4.place(x=230,y=200)


#lb1.pack(side=TOP,fill=X) # COMANDO fill É RESPONSÁVEL DO PREENCHIMENTO 100%
# DEVE USAR X PARA HORIZONTAL E DEVE SER MAIÚSCULO

#lb2.pack(side=RIGHT,fill=Y) # COMANDO fill É RESPONSÁVEL DO PREENCHIMENTO 100%
# DEVE USAR y PARA VERTCAL E DEVE SER MAIÚSCULO

#lb3.pack(side=LEFT,fill=Y) # COMANDO fill É RESPONSÁVEL DO PREENCHIMENTO 100%
# DEVE USAR y PARA VERTICAL E DEVE SER MAIÚSCULO

#lb4.pack(side=BOTTOM,fill=X) # COMANDO fill É RESPONSÁVEL DO PREENCHIMENTO 100%
# DEVE USAR x PARA HORIZONTAL E DEVE SER MAIÚSCULO

lb1.pack(side=TOP,fill=BOTH,expand=1.5) 
lb2.pack(side=TOP,fill=BOTH,expand=3) 
lb3.pack(side=TOP,fill=BOTH,expand=1)
lb4.pack(side=TOP,fill=BOTH,expand=1) 

i.mainloop()