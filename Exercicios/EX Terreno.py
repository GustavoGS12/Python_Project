largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
valorMetro = float(input("Digite o valor do metro quadrado: "))
area = largura * comprimento
preco = area * valorMetro

print(f"Area do terreno = {area:.2f}")
print(f"Preço do terreno = {preco}")