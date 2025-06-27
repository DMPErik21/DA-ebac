#gerando o grafico
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

#trasnformando e um dataframe.
df = pd.read_csv('gasolina.csv')
df.head()

#grafico de linha.
plt.figure(figsize=(10,6))
grafico = sns.lineplot(data=df, x="dia", y="venda")
grafico.set(title="Vendas de Gasolina", xlabel="Dia", ylabel="Preço")

#salvando
plt.savefig('gasolina.png')
plt.show()
