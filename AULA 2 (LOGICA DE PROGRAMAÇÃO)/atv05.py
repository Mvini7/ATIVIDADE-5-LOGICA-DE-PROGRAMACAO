preco = float(input("Digite o preço do produto: "))

desconto = preco * 0.05

preco -= desconto

print(f"O preço após o desconto de 5% é: R${preco:.2f}")