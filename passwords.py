import shelve

# armazenar senhas;
# sem utilização de criptografia;

login = input("> Insira a senha: ")
login = login.lower()
print('\n')

while True:

    with shelve.open('senhas') as db:
        if 'passwords' in db:
            passwords = db['passwords']
        else:
            passwords = {}

    if login == "senha":   #coloque sua senha principal
        question = input("> Você deseja ver, alterar, incluir ou excluir uma senha? ")
        print('\n')
    else:
        print("> Senha incorreta, desligando...")
        quit()
        
    if question == "ver":
        senha = input("> Qual senha você deseja ver? ").lower()
        if senha in passwords:
            print('\n', passwords[senha], '\n')
        else:
            print("> Senha não registrada.", '\n')

    elif question == "alterar":
        alt1 = input("> Qual senha você deseja alterar? ").lower()
        alt2 = input("> Digite nova senha: ")
        passwords[alt1] = alt2
        with shelve.open('senhas', 'w') as db:
            db['passwords'] = passwords
            print('\n')

    elif question == "incluir":
        sistema = input("> A senha será de qual sistema/etc.? ")
        nova_senha = input("> Digite a nova senha: ")
        nova_senha = nova_senha.lower()
        passwords[sistema] = nova_senha
        with shelve.open('senhas', 'w') as db:
            db['passwords'] = passwords
            print('\n')

    elif question == "excluir":
        excl = input("> A senha de qual sistema você deseja apagar? ")
        if excl in passwords:
            del passwords[excl]
            with shelve.open('senhas', 'w') as db:
                db['passwords'] = passwords
                print('\n')
        else:
            print("> Senha não registrada.", '\n')

    elif question == "ver tudo":
        print('\n')
        for sis, sen in passwords.items():
            print(sis.upper() + ':', sen)
        print('\n')

    elif question == "sair":
        print("> Desligando...")
        quit()

    else:
        print("> Opção inválida.", '\n')

db.sync()