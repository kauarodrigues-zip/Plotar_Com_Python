import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Categoria": ["Alimentação","Transporte","Lazer","Moradia","Saúde"],
    "Gasto Orcado": [800,300,200,1200,150],
    "Gasto Real": [920,280,350,1200,100]
    }

df = pd.DataFrame(dados)

ax = df.plot(
  x="Categoria",
  y=["Gasto Orcado", "Gasto Real"],
  kind="bar",
  figsize=(9,5),
  color=["#4C72B0","#DD8452"]
)

plt.title("Comprativo: Orçado Vs Realizado (R$)", fontsize=13, fontweight="bold")
plt.xlabel("Categora de Despesa", fontsize=11)
plt.ylabel("Valor em R$", fontsize=11)
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.legend(["Orçado", "Realizado"])

plt.tight_layout()
plt.show()