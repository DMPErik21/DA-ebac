# código de geração do gráfico 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gasolina_df = pd.read_csv("gasolina.csv")
gasolina_df.head()

#ajustando o tamanho.
plt.figure(figsize=(10, 6))

#gerando o grafico
sns.lineplot(data=gasolina_df, x="dia", y="venda")

#botando titulos, nomes de cada eixo.
plt.title("Preço médio da gasolina na cidade de São Paulo nos 10 primeiros dias de Julho de 2021.")
plt.xlabel("Dias.")
plt.ylabel("Preço.")
plt.savefig("gasolina.png")