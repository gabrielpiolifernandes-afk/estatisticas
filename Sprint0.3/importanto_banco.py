import pandas as pd
import os

# =========================
# 1. Caminho do arquivo de entrada (Excel)
# =========================
caminho_entrada = r"C:\Users\PC\Downloads\98bdb16c8e3fcba06b29a2edd2440aaa426b1c30ea7f9909f722e7f04bb8259c\Nova pasta\excel uber 1000.xlsx"

# =========================
# 2. Ler o Excel
# =========================
df = pd.read_excel(caminho_entrada)

print("Arquivo carregado com sucesso!")
print(df.head())

# =========================
# 3. Criar pasta de saída (CSV)
# =========================
pasta_saida = r"C:\Users\PC\estatistica_0.1\estatisticas\Sprint0.3\04_resultados"
os.makedirs(pasta_saida, exist_ok=True)

# =========================
# 4. Caminho do arquivo CSV de saída
# =========================
caminho_saida = os.path.join(pasta_saida, "dados_tratados.csv")

# =========================
# 5. Salvar CSV
# =========================
df.to_csv(caminho_saida, index=False, sep=';')

print(f"CSV salvo com sucesso em: {caminho_saida}")