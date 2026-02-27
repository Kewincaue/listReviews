usuarios = ['Marcos', 'João', 'José', 'Maurício', 'Junior', 'Rafael']
senhas = [1010, 2020, 3030, 4040, 5050, 6060]


while usuarios:
    user = input('Digíte seu usuário: ')

    if user in usuarios:
        password = int(input('Digíte sua senha: '))
        indice = usuarios.index(user)
        
        if password == senhas[indice]:
            print(f'\nLogin Realizado com Sucesso! Seja muito bem vindo ' +user+'.')
            break
            
        else:
            print('Senha incorreta.\n')
    
    else:
        print('Usuário não encontrado.\n')
        
# --- O código abaixo só aparece após o BREAK ---

print("-" * 30)
print(f"PAINEL DE CONTROLE: {user.upper()}")
print("-" * 30)
print("1. Ver perfil")
print("2. Editar configurações")
print("3. Log de atividades")
print("4. Sair do sistema")
print("-" * 30)

opcao = input("Escolha uma opção: ")
print(f"Você selecionou a opção {opcao}. Carregando...")
