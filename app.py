import os

restaurantes = [{'nome':'praça', 'categoria':'japonesa', 'ativo':False},
                {'nome':'pizza', 'categoria':'piza', 'ativo': True},
                {'nome':'cantina','categoria':'Italiano', 'ativo': False}]
    
def exibir_nome_do_programa():
    '''Exibie o nome do programa na tela'''

    print("""
    ╔═══╦═══╦══╗╔═══╦═══╗╔═══╦═╗╔═╦═══╦═══╦═══╦═══╦═══╗
    ║╔═╗║╔═╗║╔╗║║╔═╗║╔═╗║║╔══╩╗╚╝╔╣╔═╗║╔═╗║╔══╣╔═╗║╔═╗║
    ║╚══╣║─║║╚╝╚╣║─║║╚═╝║║╚══╗╚╗╔╝║╚═╝║╚═╝║╚══╣╚══╣╚══╗
    ╚══╗║╚═╝║╔═╗║║─║║╔╗╔╝║╔══╝╔╝╚╗║╔══╣╔╗╔╣╔══╩══╗╠══╗║
    ║╚═╝║╔═╗║╚═╝║╚═╝║║║╚╗║╚══╦╝╔╗╚╣║──║║║╚╣╚══╣╚═╝║╚═╝║
    ╚═══╩╝─╚╩═══╩═══╩╝╚═╝╚═══╩═╝╚═╩╝──╚╝╚═╩═══╩═══╩═══╝""")

             #FUNÇÔES
def exibir_opcoes():
    '''Exibe as pções disponíveis no menu'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n' )

def finalizar_app():
    '''Exibe a mensagem de finalização do aplicativo'''
    exibir_subtitulo('Finalizar App')

def voltar_ao_menu_principal():
    '''Solicita que aperte uma tecla para voltar ao menu principal
    
    - Outputs: (Saída que a função gera)
    Retorna ao menu principal '''
    
    input('\nDigite uma tecla para voltar ao menu')
    main()

def opcao_invalida():
    '''Informa que a opção escolhida não existe no aplicativo e volta ao menu principal
    
    - Outputs: (Saída que a função gera)
    Retorna ao menu principal '''

    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto) :
    '''Exibe um subtitulo estilizado na tela
    Inputs:
     - Texto: str - o texto do subtítulo'''

    os.system ('cls')
    linha = '*' * (len(texto))
    print (linha)
    print (texto)
    print (linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante com validações de segurança
    
    Inputs: 
    - Nome do restaurante (com validação de tamanho, caracteres e duplicidade)
    - Categoria 
    
    Outputs:
    - Adiciona um novo restaurante seguro à lista de restaurantes'''

    exibir_subtitulo('Cadastro de novos restaurantes')

        #----- INÍCIO DA BLINDAGEM (LOOP DE SEGURANÇA) ---
    while True :
        nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ').strip()
       
        #DEFESA 1: TAMANHO DO NOME DOS RESTAURANTES
        if len(nome_do_restaurante) <2 or len(nome_do_restaurante) > 30:
                print('❌ ERRO: O nome do restaurante deve ter entre 2 e 30 letras. Tente novamente.\n')
                continue

        #DEFESA 2: APENAS LETRAS E ESPAÇOS
        if not nome_do_restaurante.replace(' ','').isalpha():
            print('❌ ERRO DE SEGURANÇA: Use apenas letras. Símbolos e números não são permitidos.\n')
            continue

         #DEFESA 3: RESTAURANTE REPETIDO 
        ja_existe = False
        for rest in restaurantes:
            if rest['nome'].upper() == nome_do_restaurante.upper():
                ja_existe = True
                break
             
        if ja_existe:
                print(f'❌ ERRO: O restaurante "{nome_do_restaurante}" já existe no sistema!\n ')
                continue
        
             # SE PASSOU POR TODAS AS ETAPAS PODE PROSEGUIR
        break
         #--- FIM DA BLINDAGEM ---
          
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante ={'nome':nome_do_restaurante, 'categoria': categoria, 'ativo' :False }
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Lista os restaurantes cadastrados
    
    Input:
     - Filtra a categoria escolhida pelo usuário ou deixe em branco para mostrar todas

    Outputs:
     - Exibe a lista de restaurantes na tela'''
    
    exibir_subtitulo('Listando restaurantes')

    filtro = input('Digite a categoria que deseja filtrar (ou deixe em branco para mostrar todas as categorias): ')
 
    print(f"{'nome do restaurante'.ljust(22)} | {'categoria'. ljust(20)} | Status")

    for restaurante in restaurantes:
        if not filtro or filtro.upper() ==restaurante['categoria'].upper():
            nome_restaurante = restaurante ['nome']
            categoria = restaurante['categoria']
            ativo = 'ativo' if restaurante ['ativo'] else 'desativado'
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal ()       

def alternar_estado_restaurante():
    '''Informa se o restaurante está ativo ou inativo
    
    Outputs:
     - Exibe uma mensagem indicando o sucesso da operação'''
    
    exibir_subtitulo ('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante ['ativo'] = not restaurante ['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f' O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()       

def escolher_opcao():
   ''' Solicita e executa a opção escolhida pelo usúario
   Outputs:
    - Executa a opção escolhida pelo usúario'''
   
   try:
     opcao_escolhida = int(input('Escolha uma opcao: ')) 

     if opcao_escolhida == 1:
       cadastrar_novo_restaurante()

     elif opcao_escolhida ==2:
        listar_restaurantes()
    
     elif opcao_escolhida ==3:
        alternar_estado_restaurante()
    
     elif opcao_escolhida ==4:
        finalizar_app()
     else:
      opcao_invalida()    
   except:
       opcao_invalida()


def main():
    '''Funcção principal que inicia o programa'''
    
    os.system ('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__=='__main__':
    main()
