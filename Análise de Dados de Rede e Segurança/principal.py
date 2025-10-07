import pandas as pd
import datetime
import os
import getpass
import bcrypt
import logging

from lista import (
    lista_adiministradores, lista_ip_publicos, lista_ip_privados, lista_clientes_ips,
    salvar_dados_json, ARQUIVO_ADMINS
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | USUARIO: %(user)s | ACAO: %(message)s',
    filename='log_sistema.txt',
    encoding='utf-8'
)

def gerar_hash_senha(senha):
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

def verificar_senha(senha_digitada, hash_armazenado):
    return bcrypt.checkpw(senha_digitada.encode('utf-8'), hash_armazenado.encode('utf-8'))

def adicionar_administrador(usuario_logado):
    print("\n--- Adicionar Novo Administrador ---")
    
    nome_admin = input("Digite o nome do novo administrador: ")
    if nome_admin in lista_adiministradores:
        print("Erro: Administrador já existe.")
        return

    senha = getpass.getpass("Digite a senha para o novo administrador: ")
    senha_confirm = getpass.getpass("Confirme a senha: ")

    if senha != senha_confirm:
        print("Erro: As senhas não coincidem.")
        return
    
    hash_senha = gerar_hash_senha(senha).decode('utf-8')
    lista_adiministradores[nome_admin] = hash_senha
    salvar_dados_json(ARQUIVO_ADMINS, lista_adiministradores)
    
    print(f"Administrador '{nome_admin}' adicionado com sucesso!")
    logging.info(f"Administrador adicionado: {nome_admin}", extra={'user': usuario_logado})

def remover_administrador(usuario_logado):
    print("\n--- Remover Administrador ---")
    nome_admin = input("Digite o nome do administrador a ser removido: ")

    if nome_admin not in lista_adiministradores:
        print("Erro: Administrador não encontrado.")
        return
    
    if nome_admin == usuario_logado:
        print("Erro: Você não pode remover a si mesmo.")
        return

    del lista_adiministradores[nome_admin]
    salvar_dados_json(ARQUIVO_ADMINS, lista_adiministradores)
    
    print(f"Administrador '{nome_admin}' removido com sucesso!")
    logging.info(f"Administrador removido: {nome_admin}", extra={'user': usuario_logado})

def menu_administrador(usuario_logado):
    while True:
        print("\n--- MENU DE ADMINISTRADOR ---")
        print(f"Bem-vindo, {usuario_logado}.")
        opcao = input(
            "[1] Ver Administradores\n"
            "[2] Adicionar Administrador\n"
            "[3] Remover Administrador\n"
            "[4] Verificar IPs de Clientes\n"
            "[5] SAIR do Menu de Administrador\n"
            "Selecione uma opção: "
        )

        if opcao == "1":
            print("\n--- Lista de Administradores ---")
            print(list(lista_adiministradores.keys()))
        elif opcao == "2":
            adicionar_administrador(usuario_logado)
        elif opcao == "3":
            remover_administrador(usuario_logado)
        elif opcao == "4":
            print("\n--- Lista de IPs de Clientes ---")
            df_clientes = pd.DataFrame(lista_clientes_ips)
            print(df_clientes)
        elif opcao == "5":
            print("Saindo do Menu de Administrador...")
            logging.info("Logout", extra={'user': usuario_logado})
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        input("\nPressione ENTER para continuar...")

def autenticar_e_iniciar_menu_admin():
    print("\n--- Verificação de Funcionários ---")
    
    usuario = input("Qual seu nome de usuário: ")
    senha = getpass.getpass("Qual sua senha: ")

    if usuario in lista_adiministradores and verificar_senha(senha, lista_adiministradores[usuario]):
        print("Acesso autorizado!")
        logging.info("Login bem-sucedido", extra={'user': usuario})
        menu_administrador(usuario)
    else:
        print("Acesso negado: Usuário ou senha incorreta.")
        logging.warning("Tentativa de login FALHOU", extra={'user': usuario})

def filtrar_ips(lista_ips, tipo_ip):
    print(f"\n--- Filtrar IPs {tipo_ip} ---")
    while True:
        ip_filtrar = input(f"Digite o IP {tipo_ip} que deseja filtrar (ou 'sair' para voltar): ")
        if ip_filtrar.lower() == 'sair':
            break
        if ip_filtrar in lista_ips:
            print("IP localizado com sucesso na lista!")
            break
        else:
            print("IP não localizado na lista. Tente novamente.")

def main():
    if not lista_adiministradores:
        print("Nenhum administrador encontrado. Por favor, crie o primeiro administrador.")
        nome = input("Digite o nome para o primeiro admin: ")
        senha = getpass.getpass(f"Digite a senha para '{nome}': ")
        hash_senha = gerar_hash_senha(senha).decode('utf-8')
        lista_adiministradores[nome] = hash_senha
        salvar_dados_json(ARQUIVO_ADMINS, lista_adiministradores)
        print(f"Administrador '{nome}' criado com sucesso! Por favor, reinicie o programa e faça login.")
        return

    print("Bem-vindo à DataSetMaster\n")

    while True:
        print("\n--- MENU PRINCIPAL ---")
        opcao = input(
            "[1] Sou funcionário\n"
            "[2] Ver IPs Públicos\n"
            "[3] Ver IPs Privados\n"
            "[4] Filtrar IPs\n"
            "[5] SAIR do sistema\n"
            "Escolha uma opção: "
        )

        if opcao == "1":
            autenticar_e_iniciar_menu_admin()
        elif opcao == "2":
            print("\n--- IPs Públicos ---")
            print(pd.DataFrame(lista_ip_publicos, columns=["IP Público"]))
        elif opcao == "3":
            print("\n--- IPs Privados ---")
            print(pd.DataFrame(lista_ip_privados, columns=["IP Privado"]))
        elif opcao == "4":
            resposta_filtragem = input("Deseja filtrar IPs [1] Públicos ou [2] Privados? ")
            if resposta_filtragem == "1":
                filtrar_ips(lista_ip_publicos, "Público")
            elif resposta_filtragem == "2":
                filtrar_ips(lista_ip_privados, "Privado")
            else:
                print("Opção de filtragem inválida.")
        elif opcao == "5":
            print("\nObrigado por usar o DataSetMaster. Encerrando o sistema...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")
        
        if opcao in ["2", "3", "4"]:
            input("\nPressione ENTER para voltar ao Menu Principal...")

if __name__ == "__main__":
    main()