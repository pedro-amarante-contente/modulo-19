import seaborn as sns
import pandas as pd

gasolina_df = pd.read_csv('gasolina.csv', sep=',')
with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda')
  grafico.set(ylabel='preço médio')
  grafico.figure.set_size_inches(w=30/2.54, h=15/2.54)
  grafico.get_figure().savefig(f'gasolina.png')