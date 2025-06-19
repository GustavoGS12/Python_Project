# Função para calcular o custo de um anúncio
def valor_de_sobra(valor_total, porcentagem):
    return (valor_total/100) * porcentagem

def calcular_custo_anuncio(preco_produto, porcentagem_comissao, lucro_desejado):
    comissao = (preco_produto * porcentagem_comissao) / 100
    custo_total = preco_produto + comissao + lucro_desejado
    return custo_total


# Parâmetros
preco_produto = float(input("Digite o preço do produto: R$ "))
lucro_desejado = float(input("Digite o lucro desejado: R$ "))

# Comissões Mercado Livre
comissao_classico = 12.0  # Porcentagem de comissão para anúncio Clássico
comissao_premium = 17.0  # Porcentagem de comissão para anúncio Premium

# Calculando os custos
custo_classico = calcular_custo_anuncio(preco_produto, comissao_classico, lucro_desejado)
custo_premium = calcular_custo_anuncio(preco_produto, comissao_premium, lucro_desejado)

# Exibindo os resultados
print(f"O custo total do anúncio Clássico será: R$ {custo_classico:.2f}")
print(f"O custo total do anúncio Premium será: R$ {custo_premium:.2f}")


# Função para calcular o custo total de um anúncio na Shopee
def calcular_custo_anuncio_shopee(preco_produto, porcentagem_comissao, lucro_desejado, custo_frete):
    comissao = (preco_produto * porcentagem_comissao) / 100
    custo_total = preco_produto + comissao + lucro_desejado + custo_frete
    return custo_total

# Parâmetros
preco_produto = float(input("Digite o preço do produto: R$ "))
porcentagem_comissao = float(input("Digite a porcentagem de comissão da Shopee: "))
lucro_desejado = float(input("Digite o lucro desejado: R$ "))
custo_frete = float(input("Digite o custo do frete: R$ "))

# Calculando o custo total
custo_total = calcular_custo_anuncio_shopee(preco_produto, porcentagem_comissao, lucro_desejado, custo_frete)

# Exibindo o resultado
print(f"O custo total do anúncio na Shopee será: R$ {custo_total:.2f}")

