# ESTE ARQUIVO CONTEM TODAS AS FUNÇÕES UTILIZADAS NO PROGRAMA PRINCIPAL
import csv
from classes import *

def registro(lista): # REGISTRO DOS USUÁRIOS
    with open('Pessoas.csv', 'a',newline='', encoding="utf-8") as arquivoPessoas:
        pessoa.id = len(lista) + 1 # GERANDO ID CONFORME A QUANTIDADE DE PESSOAS PRESENTES NO ARQUIVO
        lista.append(str(pessoa.id)) 
        pessoa.nome = input("Nome: ") # COLETANDO O NOME
        escritor = csv.writer(arquivoPessoas)
        escritor.writerow([f'{pessoa.id}', f'{pessoa.nome}']) # INSERINDO NO ARQUIVO

def menu(): # MENU INICIAL + COLETAR OPÇÃO DO USUÁRIO
    print("\n\n\n\n\nBem vindo ao Sistema de Transferência da Gamecon Bahia Pocket")
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
                print("\n\n\n\n")
                return opcao
            else:
                print("Erro. Insira um das opções listadas acima.")       
    except ValueError:
        print("Opção inválida. Insira apenas números")

def busca_completa(): # BUSCA COMPLETA DO HISTÓRICO DE TRANSFERÊNCIA
    quantidade_linhas = 0
    with open('Transacoes.csv', 'r') as arquivoTransacoes: # VERIFICANDO SE O ARQUIVO ESTÁ VAZIO
        conteudo = csv.reader(arquivoTransacoes)
        next(conteudo)
        for linhas in conteudo:
            quantidade_linhas+= 1
    if quantidade_linhas > 1: # CASO O ARQUIVO NÃO ESTEJA VAZIO
        with open('Transacoes.csv', 'r') as arquivoTransacoes:
            conteudo = csv.reader(arquivoTransacoes)
            next(conteudo)
            for linhas in conteudo:
                print(f'ID {linhas[0]} transferiu para o ID {linhas[1]} a quantia de R$ {linhas[2]}')
    else: # CASO O ARQUIVO ESTEJA VAZIO
        print("Não há transações registradas.")


def busca_id(lista): # BUSCANDO HISTÓRICO E DADOS POR ID

    def coletar_id(lista): # COLETANDO ID DO USUÁRIO
        chave_ConsultaId = 1
        while chave_ConsultaId == 1:
            try:
                id = int(input("Informe o ID a ser consultado: "))
                if str(id) in lista:
                    chave_ConsultaId += 1
                    return id # RETORNANDO ID PARA A FUNÇÃO PRINCIPAL
                else:
                    print("ID informado não consta no sistema.")
                    chave_ConsultaId += 1
                    return False
            except ValueError:
                print("Erro de ID. ID são numéricos.")

    with open('Transacoes.csv', 'r') as arquivoTransacoes: # CONFERINDO SE O ARQUIVO ESTÁ VAZIO 
        conteudo = csv.reader(arquivoTransacoes)
        quantidade_linhas = 0
        for linha in conteudo:
            quantidade_linhas +=1  
    if quantidade_linhas > 1: # CASO O ARQUIVO CONTENHA DADOS
        idPesquisa = coletar_id(lista)
        if idPesquisa == False: # CASO O ID PESQUISADO NÃO CONSTE, O CÓDIGO NÃO RODARÁ
            None
        else: # CASO O ID PESQUISADO CONSTE, O CÓDIGO RODARÁ
            transacoes = qtdEnvio = envio = qtdRecebido = recebido = paraSi = envioParaSi = 0
            with open('Transacoes.csv', 'r') as arquivoTransacoes: # ABRE O ARQUIVO TRANSFERENCIA PARA COLETAR DADOS DE ENVIO
                conteudo = csv.reader(arquivoTransacoes)
                next(conteudo)
                print("Valores enviados:")
                for linhas in conteudo:
                    if linhas[0] == str(idPesquisa):
                        envio += float(linhas[2])
                        transacoes+=1
                        qtdEnvio+=1
                        print(f"O ID {idPesquisa} transferiu para {linhas[1]} o valor de R${linhas[2]}")
            with open('Transacoes.csv', 'r') as arquivoTransacoes: # ABRE O ARQUIVO TRANSFERENCIA PARA COLETAR DADOS DE RECEBIMENTO                    
                conteudo = csv.reader(arquivoTransacoes)
                next(conteudo)
                print("Valores recebidos:")
                for linhas in conteudo:
                    if linhas[1] == str(idPesquisa):
                        print(f"O ID {idPesquisa} recebeu de {linhas[0]} o valor de R${linhas[2]}") 
                        recebido += float(linhas[2])
                        if linhas[0] != str(idPesquisa):
                            transacoes+=1
                            qtdRecebido+=1
                        else:
                            paraSi += 1
                            envioParaSi += float(linhas[2])
            with open('Pessoas.csv', 'r') as arquivoPessoas: # ABRE O ARQUIVO DE PESSOAS PARA COLETAR O NOME 
                conteudo = csv.reader(arquivoPessoas)
                next(conteudo)
                for linhas in conteudo:
                    if linhas[0] == str(idPesquisa):
                        nome_ID = linhas[1]
            # IMPRESSÃO DAS ESTATÍSTICAS COLETADAS
            print(f"Dados estatísticos do ID: {idPesquisa}\n"\
                    f"Nome cadastrado no ID {idPesquisa}: {nome_ID}\n"\
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
    
    valor = parametro() # TRAZENDO O RETORNO DO PARAMETRO PARA FUNÇÃO PRINCIPAL
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
        idsListadosOrdenados = ordenacao(idsListados) # ORDENANDO A LISTA DE IDS QUE PARTICIPARAM DE TRANSAÇÕES
        idsDentroLimite = []
        for i in range(len(idsListadosOrdenados) - 1): # ENCONTRANDO OS IDS DENTRO DO LIMITE
            try:
                if idsListadosOrdenados.count(idsListadosOrdenados[i]) >= valor:
                    idsDentroLimite.append(idsListadosOrdenados[i])
                    for i in range(0, len(idsDentroLimite)-1):
                        if idsDentroLimite[i] == idsDentroLimite[i+1]:
                            idsDentroLimite.pop(i)
            except IndexError:
                None
        maiores = []
        if len(idsDentroLimite) == 0:
            print("Não há IDS com transferências dentro do parâmetro informado.")
        else:
            maior = 0
            for i in range(0, len(idsListadosOrdenados) -1):
                if idsListadosOrdenados.count(idsListadosOrdenados[i]) >= idsListadosOrdenados.count(maior):
                    maior = idsListadosOrdenados[i]
                    maiores.append(maior)
                    if maiores.count(maior) > 1:
                        maiores.remove(maior)
        # TRATAMENTO DA IMPRESSÃO DOS DADOS ESTATÍSTICOS DE QUEM MAIS PARTICIPOU DE TRANSFERÊNCIAS       
        if len(maiores) == 1:
            print(f"O ID que mais participou de transações foi o ID {maior}")
        elif len(maiores) > 1:
            print("Os ID's que mais participaram de transações:")
            for i in maiores:
                print(f"ID: {i}")
        # IMPRESSÃO DOS DADOS ESTATÍSTICOS DE QUEM ESTÁ DENTRO DO PARÂMETRO ESTABELECIDO
        for i in range(0, len(idsDentroLimite) -1):
            print(f"O ID {idsDentroLimite[i]} participou de {idsListadosOrdenados.count(idsDentroLimite[i])}")
                
    else: # SE NÃO HOUVER TRANSAÇÕES
        print("Não há transferências.")
        print("\n\n\n")

def transacao(idsUsados): # REALIZANDO TRANSACOES
    chave_coletaID = 0
    while chave_coletaID == 0:
        try: # COLETAR ID DO EMISSOR E DO RECEPTOR
            emissor = int(input("Emissor: "))
            if str(emissor) in idsUsados:
                receptor = int(input("Receptor: "))
                if str(receptor) in idsUsados:
                    chave_coletaID += 1
                    dadosColetados = True
                else:
                    print("Receptor não está cadastrado.")
                    chave_coletaID += 1
            else:
                    print("Emissor não está cadastrado.")
                    chave_coletaID += 1
        except ValueError:
            print("Erro no ID. ID's são números.")
    if dadosColetados == True:
        chave_Transacao = 0
        while chave_Transacao == 0:
            try: 
                valor = float(input("Informe o valor da transferência: "))
                if valor == 0:
                    print("Valor inválido. Zero não é transferível.")
                elif valor < 0:
                    print("Não é possível transferir valor negativo.")
                else:
                    chave_Transacao=1
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