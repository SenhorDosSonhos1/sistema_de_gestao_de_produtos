from controller import CreateUser
import getpass

#Quando logar na conta e o sistema seja tipo 'Minha conta' que vai ser onde da pra atualizar senha apagar conta?
def main():
    print('''
          |||-BEM VINDO A PLATAFORMA-|||
          [1] Já possui conta?
          [2] Criar conta
          [3] Acessar plataforma
          |||------------------------|||
          ''')

def register():
    username = input('Username: ') 
    password = getpass.getpass('Password: ')

    user = CreateUser(username, password)

    # O loop deve continuar até o usuario ser valido
    if user.is_authenticated:
        print()
        print('Usuario Criado com sucesso!!!')
        quit()
    else:
        # Mensagens de error
        print(f'Ops: {user.message}')
        print()
    
def login():
    ...

def front_end():
    while True:
        main()
        
        options = int(input('Opção: '))
        if  options == 1:
            login()
        elif options == 2:
            register()
                
if __name__ == '__main__':
    front_end()