import pandas as pd
import numpy as np
from scipy.stats import norm
import os

#pequena verificação para garantir que o caminho do arquivo CSV está correto
print("Pasta atual:", os.getcwd())

# caminho do arquivo CSV
caminho = r"C:\Users\PC\Downloads\dados.csv"

#leitura da base de dados
df = pd.read_csv("04_resultados/dados_tratados.csv", sep=";")

#limpeza dos dados para evitar erros.
df = df.drop(columns=["Unnamed: 9", "Unnamed: 10", "Unnamed: 11"], errors='ignore')

# Converter para número
df["Valor"] = pd.to_numeric(df["Valor"], errors='coerce')

# Remover valores nulos
df = df.dropna(subset=["Valor"])

#definindo a variavel onde vai entroduzir todos os dados da coluna
dados = df["Valor"]

#aqui esta sendo feito o calculo da media, desvio e mediana para a variavel escolhida. Oque é importante para o resto dos calculos.
#aqui eu fiquei em duvida se deveria criar as contas ou se podia usar as funçoes dos pandas, caso seja do seu interesse eu posso criar as contas usando formulas na proxima sprint
media = dados.mean()
desvio = dados.std()
mediana = dados.median()

print("\n===== ESTATÍSTICAS =====")
print("Média:", media)
print("Desvio padrão:", desvio)
print("Mediana:", mediana)

#exercicio 1 (a)
prob_mediana = (dados > mediana).mean()

print("\n===== EXERCÍCIO 1 (a) =====")
print("P(X > mediana):", prob_mediana)

if abs(prob_mediana - 0.5) < 0.05:
    print("Classificação: Evento equiprovável")
else:
    print("Classificação: Evento não equiprovável")

#exercicio 1 (b)
lim_inf = media - 2 * desvio
lim_sup = media + 2 * desvio

prob_intervalo = ((dados >= lim_inf) & (dados <= lim_sup)).mean()

print("\n===== EXERCÍCIO 1 (b) =====")
print("Probabilidade (média ± 2 desvios):", prob_intervalo)

if prob_intervalo > 0.9:
    print("Classificação: Evento muito provável")
else:
    print("Classificação: Evento pouco provável")

#Teste Z para a média, isso serve para detectar se existe um outlier significativo, eu pensava que o objetivo era detectar se existia um outlier e excluir ele, 
#mas o real objetivo é apenas avisar que exite para quem que va analisar os dados ter essa noçao que ouve uma distorção significativa por conta de uma pessoa.
mu0 = 50

media_amostral = dados.mean()
sigma = dados.std()

#conta 1 Teste unilateral
n_a = 20

Z_a = (media_amostral - mu0) / (sigma / np.sqrt(n_a))
z_critico_a = norm.ppf(0.05)

print("\n===== EXERCÍCIO 2 (a) =====")
print("Z calculado:", Z_a)
print("Z crítico:", z_critico_a)

if Z_a < z_critico_a:
    print("Decisão: Rejeitar H0")
    print("Conclusão: A média é menor que a média populacional")
else:
    print("Decisão: Não rejeitar H0")
    print("Conclusão: Não há evidência suficiente")

#conta 2 Teste bilateral
n_b  = 15

Z_b = (media_amostral - mu0) / (sigma / np.sqrt(n_b))
z_critico_b = norm.ppf(0.995)

print("\n===== EXERCÍCIO 2 (b) =====")
print("Z calculado:", Z_b)
print("Z crítico:", z_critico_b)

if abs(Z_b) > z_critico_b:
    print("Decisão: Rejeitar H0")
    print("Conclusão: A média é diferente da média populacional")
else:
    print("Decisão: Não rejeitar H0")
    print("Conclusão: Não há evidência suficiente")

#essa parte abaixo salva os resultados em um arquivo csv para fazer outros tipos de leitura e analise

resultados = pd.DataFrame({
    "Estatística": [
        "Média",
        "Desvio padrão",
        "Mediana",
        "P(X > mediana)",
        "P(média ± 2σ)",
        "Z teste (a)",
        "Z teste (b)"
    ],
    "Valor": [
        media,
        desvio,
        mediana,
        prob_mediana,
        prob_intervalo,
        Z_a,  
        Z_b
    ]
})

# salvar arquivo
resultados.to_csv("resultados_estatisticos.csv", index=False, sep=";")

print("Arquivo de resultados salvo com sucesso!")