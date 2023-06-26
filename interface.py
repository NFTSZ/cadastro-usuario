import PySimpleGUI as sg
from email_validator import validate_email, EmailNotValidError

usuarios = {}  # Dicionário para armazenar os usuários cadastrados
exibir_senha = False  # Variável de controle para o estado do campo de senha

# Layout da janela
sg.theme('Default1')  # Define o tema da interface gráfica
layout = [
    [sg.Text('E-mail'), sg.Input(key='email', size=(25, 1))],  # Campo de entrada para o e-mail
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(25, 1))],  # Campo de entrada para a senha
    [sg.Button('Mostrar senha', key='mostrar', size=(12, 1)),  # Botão para mostrar/ocultar a senha
     sg.Button('Cadastrar', size=(12, 1), button_color=('white', 'green'))],  # Botão para cadastrar o usuário
    [sg.Text(size=(50, 1), key='mensagem')]  # Elemento para exibir mensagens na janela
]

# Criação da janela
janela = sg.Window('Tela de Cadastro', layout)  # Cria uma nova janela com o título "Tela de Cadastro" e o layout definido

# Loop de eventos
while True:
    eventos, valores = janela.read()  # Lê os eventos da janela
    if eventos == sg.WINDOW_CLOSED:  # Verifica se a janela foi fechada
        break  # Encerra o loop

    if eventos == 'Cadastrar':  # Evento para cadastrar o usuário
        email = valores['email']  # Obtém o valor do campo de entrada de e-mail
        senha = valores['senha']  # Obtém o valor do campo de entrada de senha

        if not email:  # Verifica se o campo de e-mail está vazio
            janela['mensagem'].update("Insira um e-mail.", text_color='red')  # Atualiza a mensagem exibida na cor vermelha
            continue  # Volta para o início do loop

        try:
            validate_email(email)  # Valida o formato do e-mail
        except EmailNotValidError:
            janela['mensagem'].update('E-mail inválido. Por favor, verifique o formato do e-mail.')
            continue

        if not senha:  # Verifica se o campo de senha está vazio
            janela['mensagem'].update("Insira uma senha.", text_color='red')  # Atualiza a mensagem exibida na cor vermelha
            continue  # Volta para o início do loop

        if email in usuarios:  # Verifica se o e-mail já está cadastrado
            janela['mensagem'].update('Esse e-mail já está cadastrado, tente outro.')
            continue  # Volta para o início do loop

        # Se todas as condições forem atendidas, cadastra o usuário no dicionário de usuários
        usuarios[email] = senha
        janela['mensagem'].update("E-mail cadastrado com sucesso")
        

    if eventos == 'mostrar':  # Evento para mostrar/ocultar a senha
        exibir_senha = not exibir_senha  # Alterna o estado do campo de senha

        # Atualiza o campo de senha para exibir ou ocultar os caracteres, dependendo do estado atual
        janela['senha'].update(password_char='' if exibir_senha else '*')

        # Atualiza o texto do botão para 'Ocultar senha' se a senha estiver sendo exibida, caso contrário, 'Mostrar senha'
        janela['mostrar'].update('Ocultar senha' if exibir_senha else 'Mostrar senha')

janela.close()  # Fecha a janela quando o loop de eventos é encerrado
