import matplotlib.pyplot as plt

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]
gastos = [45.50, 30.00, 85.20, 20.00, 110.00, 65.00, 40.00]

plt.figure(figsize=(9, 5))
barras = plt.bar(dias,gastos, color="royalblue", edgecolor="black")

plt.title("Gastos Diários da Semana (R$)", fontsize=14, fontweight="bold")

plt.xlabel("Dias da Semana", fontsize=11)

plt.ylabel("Valor gasto (R$)", fontsize=11)

for barra in barras:
  altura = barra.get_height()
  plt.text(
      barra.get_x() + barra.get_width() / 2,
      altura + 2,
      f"R$ {altura:.2f}",
      ha="center", fontsize=9
  )

plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.ylim(0, max(gastos) + 20)
plt.show()

