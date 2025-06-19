x = list(input("Digite o número binário:"))
y = len(x) - 1
result = []

for i in x:
    result.append(int((int(i)*(2**y))))
    y -= 1


print(sum(result))
