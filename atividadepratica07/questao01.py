import pandas as pd

def processar_logs_treinamento(arquivo_Log):
    try:
        leitor = pd.read_csv(arquivo_Log)
        media = leitor['tempo_execucao'].mean()
        desvio_Padrao = leitor['tempo_execucao'].std()
        return f"Média: {media}, Desvio padrão: {desvio_Padrao}"



    except: FileNotFoundError
    return "Arquivo não encontrado"

arquivo = input("Digite o nome do arquivo de log: ")
print(processar_logs_treinamento(arquivo))