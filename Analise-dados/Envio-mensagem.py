import pandas as pd
from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "AC19ace56a0820a135a1d007e233ff57eb"
# Your Auth Token from twilio.com/console
auth_token = "b058ff273d8887fe0dc99dfca87a08f1"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5531971100890",
            from_="+12312254843",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)

