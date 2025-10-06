# 🛡️ DataSetMaster: Sistema de Administração e Análise de Risco de Redes (IPs)

## 1\. Visão Geral do Projeto

O **DataSetMaster** é uma ferramenta de linha de comando (**CLI**) desenvolvida em **Python** para administração de dados de rede e segurança. O projeto simula um sistema de gestão centralizada de IPs (Públicos e Privados) e informações de clientes, integrando recursos essenciais de **auditoria de segurança**, **análise de risco** e **visualização profissional** de dados.

### 🎯 Foco Principal

O valor central do DataSetMaster reside na sua capacidade de transformar dados estáticos em *insights* de segurança, permitindo aos administradores **identificar e mitigar riscos** de configuração de rede (IPs Duplicados) rapidamente.

-----

## 2\. Destaques das Funcionalidades

### 🔒 Cibersegurança e Auditoria

| Funcionalidade | Detalhes e Risco Mitigado |
| :--- | :--- |
| **Autenticação e Acesso Restrito** | Implementação de um sistema de login com validação de usuário (Administrador) para garantir que apenas pessoal autorizado acesse as funções críticas do sistema. |
| **Análise de IPs Duplicados (Risco)** | Utiliza **Pandas** para uma varredura eficiente nos conjuntos de dados de IPs. **Alerta imediato** sobre IPs repetidos, indicando potenciais **conflitos de rede** ou tentativas de acesso não autorizadas. |
| **Registro de Logs de Segurança** | Todas as ações administrativas (Login, Logout, Execução de Análise de Risco) são registradas em `log_seguranca.txt`, criando uma trilha de auditoria completa (com *timestamp* e usuário). |

### 📊 Administração e Análise de Dados

| Funcionalidade | Descrição |
| :--- | :--- |
| **Visualização Aprimorada** | Uso da biblioteca **`tabulate`** para exibir DataFrames e conjuntos de dados em **tabelas formatadas e limpas** no console. |
| **Gestão de Usuários** | Funções completas de CRUD (Criação, Remoção, Verificação) de usuários administradores. |
| **Usabilidade (UX)** | Implementação de limpeza de tela para garantir que os menus e os resultados sejam exibidos de forma organizada. |
| **Exportação de Dados para BI** | Exporta **conjuntos de dados** de clientes e logs em formato **CSV**, servindo como fonte de dados limpa para *dashboards* avançados (ex: Power BI). |

-----

## 3\. Tecnologias Utilizadas

| Categoria | Ferramenta | Propósito no Projeto |
| :--- | :--- | :--- |
| **Linguagem** | Python 3.x | Base do sistema CLI e lógica de segurança. |
| **Análise de Dados** | Pandas | Manipulação de DataFrames, contagem de valores e checagem de IPs duplicados. |
| **Visualização (CLI)**| Tabulate | Formatação profissional e legível das tabelas no console. |
| **Formato de Dados** | **CSV File Format** | Interface padrão de exportação (`clientes_com_ip.csv`) para interoperabilidade com ferramentas de BI. |
| **Reporting** | Power BI (Offline) | Utilizado para criar *dashboards* a partir dos arquivos CSV gerados pelo sistema. |

-----

## 4\. Instalação e Configuração

### Pré-requisitos

  * Python 3.x instalado.

### 4.1. Instalação das Dependências

Abra seu terminal ou prompt de comando e instale as bibliotecas necessárias:

```bash
pip install pandas tabulate
```

### 4.2. Estrutura de Arquivos

O projeto depende dos seguintes arquivos principais:

1.  `principal.py`: Contém a lógica de todo o sistema.
2.  `lista.py`: Contém os conjuntos de dados estáticos (IPs, clientes e o set/dicionário de administradores).

**⚠️ Configuração de Segurança:** Para que o login funcione corretamente com senhas, o seu arquivo `lista.py` deve definir `lista_adiministradores` como um **dicionário**, e não como um conjunto (`set`), como no exemplo:

```python
# Exemplo de lista.py CORRETO para senhas
lista_adiministradores = {
    "David": "senha_david_aqui",
    "Ronald": "senha_ronald_aqui"
}
```

-----

## 5\. Instruções de Uso

1.  **Executar o Sistema:**
    Inicie o sistema a partir do diretório raiz:

    ```bash
    python principal.py
    ```

2.  **Acesso Admin:**
    No menu inicial, selecione `[1] Você é um funcionario` e insira as credenciais definidas em `lista.py`.

3.  **Análise de Risco (Opção [9]):**
    Dentro do Painel de Administrador, selecione a opção `[9] **ANÁLISE DE IPs DUPLICADOS**` para executar a checagem de segurança e visualizar os IPs em conflito.

4.  **Geração de Relatório CSV:**
    A opção `[7] Verificar IPs de Clientes` garante que o arquivo `clientes_com_ip.csv` seja atualizado para uso no Power BI.

-----
