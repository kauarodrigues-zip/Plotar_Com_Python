import pandas as pd
import matplotlib.pyplot as plt

#Função para gerar os graficos

def gerarGraficos():
    g = int(input("Quantos Graficos deseja Gerar? (Número): "))
    graficos = []

    for i in range(g):
        print(f"\n--- Preenchendo dados para o Gráfico {i+1} ---")
        dados = lerDados()
        graficos.append(dados)

    for i, dados in enumerate(graficos):
        plotar(*dados)

#Função para ler os dados do usuário

def lerDados():
    print("===============================================================================")
    print("Calcular Orçamento X Realizado")
    print("Como Usar: Defina categorias, gastos orçados e por ultimo gastos realizados")
    print("===============================================================================")
    c = int(input("Quantas Categorias deseja adicionar? (Número): "))
    print("===============================================================================")
    categorias = []
    orcado = []
    realizado = []
    for cat in range(0,c):
        categorias.append(input(f"Qual o nome da {cat+1}° categoria? "))
        orcado.append(float(input(f"Qual o valor orçado para a categoria: {categorias[cat]} ? ")))
        realizado.append(float(input(f"Qual o valor Gasto para a categoria: {categorias[cat]} ? ")))
        print("===============================================================================")
    data = [categorias,orcado,realizado]
    return data

#Função para Plotar dados em um Grafico

def plotar(cat, orc, rea):
  dados = {
    "Categoria": cat,
    "Gasto Orcado": orc,
    "Gasto Real": rea
    }

  df = pd.DataFrame(dados)

  ax = df.plot(
    x="Categoria",
    y=["Gasto Orcado", "Gasto Real"],
    kind="bar",
    figsize=(9,5),
    color=["#0F35DF","#E21616"]
  )

  plt.title("Comparativo: Orçado Vs Realizado (R$)", fontsize=13, fontweight="bold")
  plt.xlabel("Categoria da Despesa", fontsize=11)
  plt.ylabel("Valor gasto (R$)", fontsize=11)
  plt.xticks(rotation=0)
  plt.grid(axis="y", linestyle="--", alpha=0.5)
  plt.legend(["Orçado", "Realizado"])

  plt.tight_layout()
  return plt.show()