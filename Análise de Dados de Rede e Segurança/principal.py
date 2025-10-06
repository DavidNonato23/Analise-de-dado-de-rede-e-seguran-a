from lista import lista_ip_publicos 
from lista import lista_ip_privados
from lista import lista_clientes_ips
from lista import lista_adiministradores

import pandas as pd
import datetime 
import os 

# Função de Logging de Segurança
def registrar_log(acao, usuario="N/A"):
    """Registra uma ação crítica no log_seguranca.txt."""
    try:
        with open("log_seguranca.txt", "a", encoding='utf-8') as f: 
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] USUARIO: {usuario} | ACAO: {acao}\n")
    except IOError:
        print("AVISO DE SEGURANÇA: Não foi possível escrever no arquivo de log.")


# Criação de DataFrames Pandas
df_clientes_1 = pd.DataFrame(lista_ip_publicos)
df_clientes_2 = pd.DataFrame(lista_ip_privados)
df_clientes_3 = pd.DataFrame(lista_clientes_ips)

# DataSetMaster - Início do Programa

print("Bem vindo a DataSetMaster\n")

# Loop principal para retornar ao menu inicial
while True:
    
    nome = input("Qual é seu nome: ")
    print(f"Seja bem vindo {nome} ao banco nacional do Triplex\n")
    
    # Bloco para salvar o nome de acesso
    try:
        df_nome_acesso = pd.DataFrame({'Nome de Acesso': [nome], 'Data/Hora': [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]})
        incluir_header = not os.path.exists("nomes_acesso.csv")
        df_nome_acesso.to_csv("nomes_acesso.csv", index=False, mode='a', header=incluir_header, encoding='utf-8')
    except Exception as e:
        print(f"AVISO: Não foi possível salvar o nome de acesso no CSV. Erro: {e}")
        
    print(nome) 

    # Opções de usuario - Menu Inicial
    print("\nEscolha uma opção abaixo\n")
    opcao = input(" [1] Você é um funcionario [2] Ver Ips publicos, [3] Verfica ip privados, [4] para filtra ips, [5] para SAIR do sistema: ")

    # Opção 1: Autenticação com Senha e Logging
    if opcao == "1":
        print("\nVerificado de funcionarios\n")
        
        usuario_logado = None

        while True:
            respota_usuario = input("Qual seu nome: ")
            resposta_senha = input("Qual sua senha: ")

            if respota_usuario in lista_adiministradores:
                if lista_adiministradores[respota_usuario] == resposta_senha:
                    print("Acesso autorizado!")
                    usuario_logado = respota_usuario
                    
                    registrar_log("Login bem-sucedido", usuario_logado)
                    
                    try:
                        # CORREÇÃO 2: Adicionando encoding='latin-1' para ler o arquivo existente 
                        df_log = pd.read_csv('log_seguranca.txt', header=None, sep='|', names=['Timestamp', 'Usuario', 'Acao'], engine='python', encoding='latin-1') 
                        df_log.to_csv("Lista de logs.csv", index=False, encoding='utf-8')
                    except (FileNotFoundError, pd.errors.ParserError, UnicodeDecodeError) as e:
                        # A captura do erro foi aprimorada para incluir UnicodeDecodeError
                        print(f"AVISO: Problema ao exportar o log de segurança para CSV. Erro: {e}")
                        
                    break
                else:
                    print("Acesso negado: Senha incorreta.")
                    registrar_log("Tentativa de login FALHOU: Senha incorreta", respota_usuario)
            else:
                print("Acesso negado: Usuário não encontrado.")
                registrar_log("Tentativa de login FALHOU: Usuário não encontrado", respota_usuario)
                
            continue


        # Menu Principal do Administrador (em loop)
        while usuario_logado:
            print("\n--- MENU DE ADMINISTRADOR ---\n")
            print(f"Bem vindo, {usuario_logado}.")
            opcao_funcionario = input(
                "[1] Ver Administradores \n[2] Adicionar Administrador \n[3] Remover Administrador \n[4] Verificar Administrador \n[5] Verificar IPs Públicos \n[6] Verificar IPs Privados \n[7] Verificar IPs de Clientes \n[8] SAIR do Menu de Administrador \nSelecione uma opção: "
            )

            # Ver lista de administradores
            if opcao_funcionario == "1":
                print("\nVocê selecionou a opção de ver a lista de administradores\n")
                print(list(lista_adiministradores.keys())) 
            
            # Adicionar novo administrador
            elif opcao_funcionario == "2":
                print("\nVocê selecionou a opção de adicionar um novo administrador\n")
                while True:
                    nome_funcionario = input("Digite o nome do funcionario: ")
                    senha_funcionario = input("Digite a senha para o novo administrador: ")
                    
                    sobrenome_funcionario = input("Digite o sobrenome do funcionario: ")
                    data_nascimento_funcionario = input("Digite a data de nascimento do funcionario: ")
                    cpf_funcionario = input("Digite o cpf do funcionario: ")

                    if nome_funcionario in lista_adiministradores:
                        print("Cadastro se encontra na lista de administradores, Tente de novo")
                        continue
                    else:
                        lista_adiministradores[nome_funcionario] = senha_funcionario 
                        registrar_log(f"Administrador adicionado: {nome_funcionario}", usuario_logado)
                        print("Cadastro realizado com sucesso!")
                        break

            # Remove administrado
            elif opcao_funcionario == "3":
                print("\nVocê selecionou a opção de remover um administrador\n")

                resposta_funcionario = input("Digite o nome do funcionario que deseja remover: ")

                if resposta_funcionario in lista_adiministradores:
                    del lista_adiministradores[resposta_funcionario] 
                    registrar_log(f"Administrador removido: {resposta_funcionario}", usuario_logado)
                    print("Remoção realizado com sucesso!")
                else:
                    print("Administrador não encontrado.")

            # Verifica um administrador
            elif opcao_funcionario == "4":
                print("\nVocê selecionou a opção de verificar um administrador\n")

                while True:
                    resposta_funcionario_filta_administrado = input("Digite o nome do funcionario que deseja verificar: ")

                    if resposta_funcionario_filta_administrado in lista_adiministradores:
                        print("Administrado encontrado na lista!")
                        break
                    else:
                        print("Administrado não encontrado na lista")
                        continue

            # Verificar ips publicos
            elif opcao_funcionario == "5":
                print("\nVocê selecionou a opção de verificar ips publicos\n")
                print(df_clientes_1)

            # Verficar ips privados
            elif opcao_funcionario == "6":
                print("\nVocê selecionou a opção de verificar ips privados\n")
                print(df_clientes_2)

            # ver ips de cada cliente
            elif opcao_funcionario == "7":
                print("\nVocê selecionou a opção de verificar a lista de ip de cada clientes\n")
                print(df_clientes_3)

                #Criando um arquivo .csv
                df_ips = pd.DataFrame(lista_clientes_ips)
                df_ips.to_csv("clientes_com_ip.csv", index=False, encoding='utf-8')

            # Opção 8: SAIR DO MENU DE ADMINISTRADOR
            elif opcao_funcionario == "8":
                print("Saindo do Menu de Administrador. Voltando ao menu principal...")
                registrar_log("Logout de administrador", usuario_logado)
                usuario_logado = None
                break
                
            else:
                print("\nOpção inválida. Tente novamente.")

            input("\nPressione ENTER para voltar ao Menu de Administrador...")

        
    # Opção 2: Ver ips publicos
    elif opcao == "2":
        print("\nVocê selecionou a opção de ver ips publicos\n")
        print(df_clientes_1)


    # Opção 3: Ver ips privados
    elif opcao == "3":
        print("\nVocê selecionou a opção de ver ips privados\n")
        print(df_clientes_2)


    # Opção 4: Filtrar ips
    elif opcao == "4":
        print("\nVocê selecionou a opção de filtrar ips\n")

        print("Selecione uma opção abaixo: ")

        resposta_de_filtragem = input("Selecione uma opção [1] Para filtra os ips publicos [2] Para filtra os ips privados: ")   

        #Filtragem de ips publicos
        if resposta_de_filtragem == "1":
            print("\nVocê selecionou a opção de filtra pelos ips publicos\n")

            while True:
                resposta_de_filtragem_1 = input("Digite o ip que deseja filtrar:")
                if resposta_de_filtragem_1 in lista_ip_publicos:
                    print("Ip localizado com sucesso na lista!")
                    break
                else:
                    print("Ip não localizado na lista")
                    continue

         #Filtragem de ips privados
        elif resposta_de_filtragem == "2":
            print("\nVocê selecionou a opção de filtra pelos ips privados\n")

            while True:
                resposta_de_filtragem_2 = input("Digite o ip que deseja filtrar:")
                if resposta_de_filtragem_2 in lista_ip_privados:
                    print("ip localizado com sucesso na lista!")
                    break
                else:
                    print("Ip não localizado na lista")
                    continue
        else:
            print("\nOpção de filtragem inválida.")
            
    # Opção 5: SAIR DO SISTEMA
    elif opcao == "5":
        print("\nObrigado por usar o DataSetMaster. Encerrando o sistema...")
        break

    else:
        print("\nOpção inválida no menu inicial. Tente novamente.")

    # Pausa antes de retornar ao menu inicial
    if opcao in ["2", "3", "4"] or (opcao == "1" and usuario_logado is None):
        input("\nPressione ENTER para voltar ao Menu Inicial...")
        print("-" * 30)