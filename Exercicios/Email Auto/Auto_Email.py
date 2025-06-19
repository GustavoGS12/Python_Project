import pandas as pd
import win32com.client as win32

tabelaVendas = pd.read_excel('Vendas.xlsx')


pd.set_option('display.max_columns', None)
#print(tabelaVendas)

faturamento = tabelaVendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()

#print(faturamento)

produtosVendido = tabelaVendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

#print(produtosVendido)

ticketMedio = (faturamento['Valor Final'] / produtosVendido['Quantidade']).to_frame()
ticketMedio = ticketMedio.rename(columns={0: 'Ticket Médio'})

newEmail = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'benjamim13@gmail.com'
mail.Subject = 'Teste aula'
mail.HTMLBody = f'''
Prezados, 
Segue os relatorios de vendas dos shoppings no mes de referencia 01/Janeiro;

Faturamento:
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

Quantidade de produtos vendidos:
{produtosVendido.to_html()}

Ticket Médio por loja:
{ticketMedio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

At.te, Gustavo
'''
mail.send()