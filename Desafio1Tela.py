from tkinter import *
i=Tk()
i.title('Programa financeiro')
i.geometry('980x720+250+30')


lb1=Label(i,text='Login',bg='yellow')
#componente.grid serve tambem para posicionar
# utilizando indicativo de linha(row) e coluna
#(column).
lb1.place(x=743,y=160)

lb2 = Label(i,text='Senha',bg='red')
lb2.place(x=743,y=120)

ed1 = Entry(i)
ed1.place(x=700,y=100)

ed2 = Entry(i)
ed2.place(x=700,y=140)

bt1 = Button(i,text='Login')
bt1.place(x=450,y=500)

i.mainloop()