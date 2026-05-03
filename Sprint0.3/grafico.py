import pandas as pd
import matplotlib.pyplot as plt

#pra eu conseguir usar esse codigo eu tive que baixar o matplotlib

#este codigo puxa o arquivo csv gerado le ele para os proximos codigos consigam gerar os graficos
df = pd.read_csv("resultados_estatisticos.csv", sep=";")

estat1 = df.iloc[:3]
estat2 = df.iloc[3:]

#codigo que gera os graficos juntos 
fig, axes = plt.subplots(1, 2, figsize=(14,5))

#grafico 1
axes[0].bar(estat1["Estatística"], estat1["Valor"], color="steelblue")
axes[0].set_title("Estatísticas Descritivas")
axes[0].tick_params(axis='x', rotation=45)

#grafico 2
axes[1].bar(estat2["Estatística"], estat2["Valor"], color="darkorange")
axes[1].set_title("Probabilidades e Testes Z")
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()