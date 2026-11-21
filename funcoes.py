# ESTE ARQUIVO CONTEM TODAS AS FUNÇÕES UTILIZADAS NO PROGRAMA PRINCIPAL
import csv

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

def busca_id(id): # BUSCANDO HISTÓRICO E DADOS POR ID
    transacoes = qtdEnvio = envio = qtdRecebido = recebido = paraSi = envioParaSi = 0
    with open('Transacoes.csv', 'r') as arquivoTransacoes:
        conteudo = csv.reader(arquivoTransacoes)
        next(conteudo)
        print("Valores enviados:")
        for linhas in conteudo:
            if linhas[0] == str(id):
                envio += float(linhas[2])
                transacoes+=1
                qtdEnvio+=1
                print(f"O ID {id} transferiu para {linhas[1]} o valor de R${linhas[2]}")
    with open('Transacoes.csv', 'r') as arquivoTransacoes:                   
        conteudo = csv.reader(arquivoTransacoes)
        next(conteudo)
        print("Valores recebidos:")
        for linhas in conteudo:
            if linhas[1] == str(id):
                print(f"O ID {id} recebeu de {linhas[0]} o valor de R${linhas[2]}") 
                recebido += float(linhas[2])
                if linhas[0] != str(id):
                    transacoes+=1
                    qtdRecebido+=1
                else:
                    paraSi += 1
                    envioParaSi += float(linhas[2])
    print(f"Dados estatísticos do ID: {id}\n"\
            f"Nome cadastrado no ID {id}: {linhas[1]}\n"\
            f"Participação em transferências: {transacoes}\n"\
            f"Volume financeiro movimentado: {envio+recebido}\n"\
            f"Transferências enviadas: {qtdEnvio}\n"\
            f"Valor total das transferências enviadas: {envio}\n"\
            f"Transferências recebidas: {qtdRecebido}\n"\
            f"Valor total das transferências recebidas: {recebido}\n"\
            f"Transferências para si: {paraSi}\n"\
            f"Valor total transferido para si: {envioParaSi}")

def busca_parametro(): # BUSCA DO HISTÓRICO DE TRANSFERÊNCIA A PARTIR DE UM PARAMETRO
    idsListados = []
    def parametro(): # COLETANDO PARAMETRO
        while True:
            try:
                valor_minimo = int(input("Insira o valor mínimo como parâmetro: "))
                if valor_minimo < 0:
                    print("Valor inválido. Insira valores negativos.")
                else:
                    return valor_minimo
            except ValueError:
                print("Erro de valor. Insira apenas números.")
    
    valor = parametro()
    with open('Transacoes.csv', 'r') as arquivoTransacoes: # PERCORRENDO O BANCO DE DADOS E ADICIONANDO TODAS AS TRANSAÇÕES
        conteudo = csv.reader(arquivoTransacoes)
        next(conteudo)
        for linhas in conteudo:
            if linhas[0] != linhas[1]:
                idsListados.append(linhas[0])
                idsListados.append(linhas[1])
            else:
                idsListados.append(linhas[0])
    if len(idsListados) > 0: # SE HOUVER TRANSAÇÕES
        idsListadosOrdenados = ordenacao(idsListados)
        auxiliar = []
        soma = 0
        for i in range(len(idsListadosOrdenados) - 1):
            try:
                if idsListadosOrdenados.count(idsListadosOrdenados[i]) >= valor:
                    auxiliar.append(idsListadosOrdenados[i])
                    for i in range(len(auxiliar)-1):
                        if auxiliar[i] == auxiliar[i+1]:
                            auxiliar.pop(i)
            except IndexError:
                None
        for i in range(len(auxiliar) -1, -1 , -1):
            print(f"O ID {auxiliar[i]} participou de {idsListadosOrdenados.count(auxiliar[i])}")
                
    else: # SE NÃO HOUVER TRANSAÇÕES
        print("Não há transferências.")
        print("\n\n\n")

def transacao(idsUsados): # REALIZANDO TRANSACOES
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
                print("Transferência realizada.")
                print("\n\n\n")
        except ValueError:
            print("Erro na transferencia. Valor inserido não é numerico.")
    with open('Transacoes.csv', 'a', newline='') as arquivoTransacoes:
        escrever = csv.writer(arquivoTransacoes)
        escrever.writerow([f'{emissor}', f'{receptor}', f'{valor}'])

def ordenacao(lista):
    lista2 = []
    for i in range(len(lista)- 1):
        lista2.append(int(lista[i]))
    tamanho = len(lista2)
    for i in range(1, tamanho):
        aux = lista2[i]
        j = i - 1
        while j >= 0 and aux < lista2[j]:
            lista2[j+1] = lista2[j]
            j -= 1
        lista2[j+1] = aux
    return lista2