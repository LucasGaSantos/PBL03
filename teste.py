import csv
dado = ['{"HOJE": 1,'
'         "AMANHA": 2,'
' }']
with open('ARQUIVOTESTE.CSV', 'w+', encoding="utf-8") as teste:
    escrever = csv.DictWriter(teste, fieldnames=["DIAS DA SEMANA"])
    escrever.writerows(dado)
    ler = csv.DictReader()
    for linha in ler:
        print(ler)