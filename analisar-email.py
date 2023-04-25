emails = []
while True:
    # caso queira mostrar a lista de emails cadastrados
    '''print("-=-=-=-= Emails registrados; -=-=-=-=")
    for emailss in emails:
        print(emailss)          
    print("-="*20)'''
    email = input('Insira seu email: ')
    # se o email estiver na lista, mostre a mensagem informando e peça novamente o email.
    if email in emails:
        print('Este e-mail já está cadastrado, Tente outro')
        continue
    # Senão, adicione o email ao banco e mostre a mensagem de confirmação.
    else:
        emails.append(email)
        # evita que emails sejam duplicados na lista
        emails = list(set(emails))
        print("E-mail cadastrado com sucesso")
        while True:
            # Pergunte ao usuário se ele deseja adicionar outro email ou encerrar o programa.
            op = int(input("Deseja adicionar outro email? [1] Sim   [2] Não\n>>> "))
            if op == 1:
                break 
            # Identifique caso a opção seja inválida.
            if op != 1 and op != 2:
                print("opção inválida")
            if op == 2:
                break
        if op == 2:
            break
        