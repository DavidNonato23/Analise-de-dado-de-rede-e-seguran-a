import json
import os

ARQUIVO_ADMINS = "administradores.json"
ARQUIVO_IPS_PUBLICOS = "ips_publicos.json"
ARQUIVO_IPS_PRIVADOS = "ips_privados.json"
ARQUIVO_CLIENTES = "clientes.json"

def carregar_dados_json(nome_arquivo, dados_padrao):
    if not os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados_padrao, f, indent=4)
    
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_dados_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4)

dados_padrao_admins = {}

dados_padrao_ips_publicos = ["192.169.0.1", "192.169.0.2", "192.169.0.3", "192.169.0.4"]

dados_padrao_ips_privados = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4"]

dados_padrao_clientes = [
    {"id": 1, "nome": "Ana Carolina", "ip": "192.168.0.1", "cidade": "São Paulo"},
    {"id": 2, "nome": "Bruno Melo", "ip": "192.168.0.2", "cidade": "Brasilia"},
    {"id": 3, "nome": "Matheus Silva", "ip": "192.168.1.3", "cidade": "Rio de Janeiro"},
    {"id": 4, "nome": "Thiago Santos", "ip": "192.168.0.4", "cidade": "Salvador"},
    {"id": 5, "nome": "Willian Andrade", "ip": "192.168.1.5", "cidade": "Curitiba"},
    {"id": 6, "nome": "Bruno Santos", "ip": "192.168.0.6", "cidade": "São Paulo"},
    {"id": 7, "nome": "David Souza", "ip": "192.168.0.6", "cidade": "São Paulo"}
]

lista_adiministradores = carregar_dados_json(ARQUIVO_ADMINS, dados_padrao_admins)
lista_ip_publicos = carregar_dados_json(ARQUIVO_IPS_PUBLICOS, dados_padrao_ips_publicos)
lista_ip_privados = carregar_dados_json(ARQUIVO_IPS_PRIVADOS, dados_padrao_ips_privados)
lista_clientes_ips = carregar_dados_json(ARQUIVO_CLIENTES, dados_padrao_clientes)