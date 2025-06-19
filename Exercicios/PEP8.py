"""
x = int(input('Digite um número: '))
print(x)

y = float(input('Digite um número decimal: '))
print(y)

soma = 0
for i in range(3):
    i = int(input('Digite um número: '))
    soma = soma + i
print(soma)

a = float(input('Digite um número:'))
quadrado = a**2
quinta = a/5

print(quadrado)
print(quinta)
"""
"""
escala = input('Escolha a escala de temperatura de entrada(K/C/F): ')
entrada = float(input('Digite a temperatura: '))
conversao = input('Para qual escla deseja converter(K/C/F): ')
saida = 0
if escala == 'k' and conversao == 'c':
    saida = entrada - 273.15
elif escala == 'k' and conversao == 'f':
    saida = (entrada-273.15)*1.8+32
elif escala == 'k' and conversao == 'k':
    saida = entrada
elif escala == 'c' and conversao == 'k':
    saida = entrada+273.15
elif escala == 'c' and conversao == 'c':
    saida = entrada
elif escala == 'c' and conversao == 'f':
    saida = entrada*1.8+32
elif escala == 'f' and conversao == 'k':
    saida = (entrada-32)*(5/9)+273.15
elif escala == 'f' and conversao == 'c':
    saida = (entrada-32)/1.8
elif escala == 'f' and conversao == 'k':
    saida = entrada
else:
    print('Digite uma entrada válida')
conversao = conversao.upper()
print(f'Conversão: {saida:.2f}º{conversao}')
"""

soma1 = 0
for q in range(3):
    q = int(input('Digite um número: '))
    q = q**2
    soma1 = soma1 + q
print(soma1)

soma2 = 0
for w in range(4):
    w = float(input(f'Digite a nota {w+1}: '))
    soma2 = soma2 + w
print(soma2/4)

x = 1
while x != 0:
    x = int(input('Digite um número:'))
    print(x)

