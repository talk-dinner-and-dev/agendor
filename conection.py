import requests
import pandas as pd
import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

base_url = 'https://api.agendor.com.br/v3/'

# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': f'Bearer {api_key}',
# }

# def get_organizations():
#     endpoint = 'organizacoes'
    
#     response = requests.get(f'{base_url}{endpoint}', headers=headers)

#     if response.status_code == 200:
#         organizations = response.json()
#         print('Organizações:')
#         for organization in organizations:
#             print(f"{organization['nome']} - {organization['id']}")
#     else:
#         print(f'Erro ao obter organizações. Status Code: {response.status_code}')
#         print(response.text)

# def get_people():
#     endpoint = 'pessoas'
    
#     response = requests.get(f'{base_url}{endpoint}', headers=headers)

#     if response.status_code == 200:
#         people = response.json()
#         print('Pessoas:')
#         for person in people:
#             print(f"{person['nome']} - {person['id']}")
#     else:
#         print(f'Erro ao obter pessoas. Status Code: {response.status_code}')
#         print(response.text)

# def get_funnels():
#     endpoint = 'funil_vendas'
    
#     response = requests.get(f'{base_url}{endpoint}', headers=headers)

#     if response.status_code == 200:
#         funnels = response.json()
#         print('Funis de Vendas:')
#         for funnel in funnels:
#             print(f"{funnel['nome']} - {funnel['id']}")
#     else:
#         print(f'Erro ao obter funis de vendas. Status Code: {response.status_code}')
#         print(response.text)

# # Chame as funções para obter os dados
# get_organizations()
# get_people()
# get_funnels()

response = requests.get(f'{base_url}organizations',headers={'Authorization': f'Token {api_key}'})
test = json.loads(response.text)

# for i in test.get('data'):
#     for chave, valor in i.items():
#         if chave == 'products':
#             for j in i.get('products'):
#                 for subchave, subvalor in j.items():
#                     print(subchave,subvalor)        
#     print('-'*100)

print(test.get('data')[0].get('products')[0].get('id'))

#lista acessa .get('data')
#dict acessa .items()