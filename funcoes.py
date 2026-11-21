# ESTE ARQUIVO CONTEM TODAS AS FUNÇÕES UTILIZADAS NO PROGRAMA PRINCIPAL

def menu(): # MENU INICIAL + COLETAR OPÇÃO DO USUÁRIO
    print("Bem vindo ao Sistema de Transferência da Gamecon Bahia Pocket")
    print("O que deseja realizar hoje?")
    print('1 - Registrar Usuário\n' \
    '2 - Acessar sistema de busca\n' \
    '3 - Transação\n' \
    '0 - Fechar Programa')
    try:
        while True:
            opcao = int(input("Opção selecionada: "))
            if opcao >= 0:
                if opcao <=3:
                    return opcao
                else:
                    print("Opção inválida. Opções disponíveis entre 0 e 3")
            else:
                print("Opção inválida. Opções disponíveis entre 0 e 3")
    except ValueError:
        print("Opção inválida. Insira apenas números.")

def menu_busca(): # MENU DE BUSCA + COLETAR OPÇÃO DO USUÁRIO
    print("Qual tipo de busca deseja realizar?")
    print("1 - Histórico Geral\n" \
    "2 - Histórico do usuário\n" \
    "3 - Histórico com limite")
    try:
        while True:
            opcao = int(input("Opção selecionada: "))
            if opcao == 1 or opcao == 2 or opcao == 3:
                return opcao
            else:
                print("Erro. Insira um das opções listadas acima.")       
    except ValueError:
        print("Opção inválida. Insira apenas números")



def transacao(idsUsados):
    r = 0
    while r == 0:
        try:
            emissor = int(input("Emissor: "))
            if str(emissor) in idsUsados:
                receptor = int(input("Receptor: "))
                if str(receptor) in idsUsados:
                    r+= 1
                else:
                    print("Receptor não está cadastrado.")
            else:
                    print("Emissor não está cadastrado.")
        except ValueError:
            print("Erro no ID. ID's são números.")

    r = 0
    while r == 0:
        try: 
            valor = float(input("Informe o valor da transferência: "))
            if valor == 0:
                print("Valor inválido. Zero não é transferível.")
            elif valor < 0:
                print("Não é possível transferir valor negativo.")
            else:
                r+=1
                return emissor, receptor, valor
        except ValueError:
            print("Erro na transferencia. Valor inserido não é numerico.")