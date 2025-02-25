#comando abaixo importa tudo da biblioteca que é necessaria para a criação de telas. (ASTERISCO significa tudo)
from tkinter import *

# i (intanciar) recebe o objeto tk
i = Tk()
#gerar tiulo da janela
i.title('Programa financeiro')

#propriedade que altera o tamanho da janela(980x720) 
# e distancia da direita e topo da tela(250x30)
i.geometry('980x720+250+30')

#propriedades graficas, cor de fundo da tela (bg) ou (background)
#Não pode passar o i com ponto! DEVE SER I[]
i['bg']= "yellow"

#CRIA O ICONE NA JANELA, VOCE DEVE TER A IMAGEM NO MESMO LOCAL DO CODIGO.
#i.wm_iconbitmap('icone.ico')

#cria um label e posiciona (place) ele em relação a tela.

lb = Label(i,text='Nome do usuário')
lb.place(x=100,y=100)

#cria um botão que posicina (place) ele em relação a label.

bt = Button(i, width='20',text='OK')
bt.place(x=230,y=100)

#gera a janela gráfica 
i.mainloop()
