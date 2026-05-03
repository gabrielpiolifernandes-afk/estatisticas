import pandas as pd
import os

#aqui eu falo aonde esta o arquivo excel que esta o banco de dados no meu computador.
caminho_entrada = r"C:\Users\PC\Downloads\98bdb16c8e3fcba06b29a2edd2440aaa426b1c30ea7f9909f722e7f04bb8259c\Nova pasta\excel uber 1000.xlsx"
#aqui ele le o arquivo excel e tranforma em um dataframe no pandas
df = pd.read_excel(caminho_entrada)
#uma pequena verificação
print("Arquivo carregado com sucesso!")
print(df.head())
#aqui é onde eu falo aonde eu quero salvar este arquivo
pasta_saida = r"C:\Users\PC\estatistica_0.1\estatisticas\Sprint0.3\04_resultados"
os.makedirs(pasta_saida, exist_ok=True)
#aqui eu falo o nome que quero dar para o arquivo e para a pasta onde quero salvar
caminho_saida = os.path.join(pasta_saida, "dados_tratados.csv")
#isso é uma formatação para deixar o arquivo separa por ";" e sem o indice(0, 1, 2, ...) do pandas, para facilitar a leitura dos outros codigos
df.to_csv(caminho_saida, index=False, sep=';')
#mais uma pequena verificação para garantir que o arquivo foi salvo corretamente
print(f"CSV salvo com sucesso em: {caminho_saida}")