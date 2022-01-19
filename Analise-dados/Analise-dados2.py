import pandas as pd
from twilio.rest import Client

account_sid = "AC19ace56a0820a135a1d007e233ff57eb"
auth_token = "0c4ee1fccff2f3b220365506a1b52d0e"

client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[(tabela_vendas['Vendas'] > 55000), 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[(tabela_vendas['Vendas'] > 55000), 'Vendas'].values[0]
        print(f'No mês de {mes}, alguém bateu a meta! Vendedor(a): {vendedor}, Vendas: {vendas}.')
        message = client.messages.create(
            to="+5531971100890",
            from_="+12312254843",
            body=f'No mês de {mes}, alguém bateu a meta! Vendedor(a): {vendedor}, Vendas: {vendas}.')

        print(message.sid)
