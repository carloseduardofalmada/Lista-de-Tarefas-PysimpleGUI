import PySimpleGUI as sg
#Criando o layout
def criar_janela (): #Função onde cria a janela
    sg.theme('DarkGrey11') #Tema dentro da janela, ou seja, as cores dentro da janela
    linha = [
        [sg.Checkbox(''), sg.Input('')] #Cria a caixa de marcação onde o usuário confirma que a tarefa foi feita e Pede ao usuário para digitar a sua tarefa

    ]
    layout = [
        [sg.Frame('Tarefas',layout=linha,key='container')], #Estiliza com o nome tarefa colocando uma linha em volta das tarefas
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')] #Cria os botões que o usuário aperta para criar e excluir as tarefas
    ]
    return sg.Window('Checklist', layout=layout,finalize=True) #Usa-se o (finalize=True) apenas quando se define uma função para a janela

janela = criar_janela()
while True: #condição de loop para por exemplo encerrar o programa se o usuário fechar a janela
    evento, valores = janela.read() #é usado para capturar eventos que ocorrem na janela
    if evento == sg.WIN_CLOSED: #Se o usuário fechar a janela o código termina
        break
    elif evento == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]]) #Puxa a key (container) e extende a janela do código caso o usuário aperte em nova tarefa
    elif evento == 'Resetar':
        janela.close()
        janela = criar_janela()