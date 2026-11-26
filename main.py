# Autor: LUCAS GABRIEL OLIVEIRA DOS SANTOS
# Componente Curricular: MI - Algoritmos
# Concluído em: 
# Declaro que este código foi elaborado por mim de forma individual e não contém 
# nenhum trecho de código de colega ou de outro autor, tais como provindos de livros e 
# apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código 
# de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
# código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

# IMPORTAÇÃO DAS BIBLIOTECAS
import csv 
from classes import pessoa
from funcoes import *

# DECLARAÇÃO DA LISTA PARA COLETAR OS DADOS DO ARQUIVO PARA QUE NÃO O ABRA A TODO INSTANTE
idUsados = []
pessoa = pessoa()
# TENTANDO COLETAR OS DADOS DO ARQUIVO. SE NÃO HOUVER, CRIA UM ARQUIVO DO ZERO
try:
    with open('Pessoas.csv', 'r', newline='', encoding="utf-8") as arquivoPessoas: # COLETANDO OS DADOS DO ARQUIVO
        conteudo = csv.reader(arquivoPessoas)
        next(conteudo) # FUNÇÃO PARA PULAR UMA LINHA DO ARQUIVO 
        for linhas in conteudo:
            idUsados.append(linhas[0])
except FileNotFoundError: # CAPTANDO ERRO POR NÃO EXISTIR ARQUIVO (PRIMEIRA VEZ QUE O CÓDIGO RODA)
    with open('Pessoas.csv', 'w',newline='', encoding="utf-8") as arquivoPessoas:
        escrever = csv.writer(arquivoPessoas)
        escrever.writerow(['ID', 'NOME']) # LINHA DE INFORMAÇÃO PARA CADA UMA DAS COLUNAS

# TENTANDO COLETAR OS DADOS DO ARQUIVO. SE NÃO HOUVER, CRIA UM ARQUIVO DO ZERO
try:
    with open('Transacoes.csv', 'r', newline='') as arquivoTransacoes:
        arquivoTransacoes.close()
except FileNotFoundError: # CAPTANDO ERRO POR NÃO EXISTIR ARQUIVO (PRIMEIRA VEZ QUE O CÓDIGO RODA)
    with open('Transacoes.csv', 'a', newline='') as arquivoTransacoes:
        escrever = csv.writer(arquivoTransacoes)
        escrever.writerow(['QUEM TRANSFERIU', 'QUEM RECEBEU', 'VALOR DA TRANSFERENCIA'])

# INICIANDO O PROGRAMA
chave_Programa = 1
while chave_Programa == 1:
    opcao_menu = menu() # COLETANDO A SELEÇÃO DO MENU

    if opcao_menu == 0: # CASO QUEIRA ENCERRAR O PROGRAMA
        chave_Programa -= 1
        print("Programa Encerrado.")

    elif opcao_menu == 1: # CASO QUEIRA REGISTRAR UMA PESSOA
        registro(idUsados)
        
    elif opcao_menu == 2: # CASO QUEIRA CONSULTAR O HISTÓRICO
        resultadoBusca = menu_busca() # COLETANDO A SELEÇÃO DO MENU DE BUSCA     
        if resultadoBusca == 1: # CASO QUEIRA VER O HISTÓRICO COMPLETO
                busca_completa()

        elif resultadoBusca == 2: # CASO QUEIRA VER O HISTÓRICO DE UM USUÁRIO EM ESPECÍFICO
            busca_id(idUsados)

        elif resultadoBusca == 3: # CASO QUEIRA VER O HISTÓRICO GERAL COM PARÂMETRO
            busca_parametro()

    elif opcao_menu == 3: # CASO QUEIRA TRANSFERIR
        transferencia(idUsados)
