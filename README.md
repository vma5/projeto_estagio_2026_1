<img src="logo.png" alt="Mupi Systems Logo" width="200"/>

🚀 Mupi Systems - Desafio Full Stack
Este projeto é um teste de estágio da Mupi Systems. Consiste em uma Landpage para uma agência de tecnologia, um sistema de captura de mensagens e um Painel Administrativo customizado e protegido para gestão de leads.

📋 Funcionalidades
Landpage: Página moderna e responsiva com informações sobre serviços.

Captação de Leads: Formulário de contato que valida e salva dados no SQLite.

Autenticação: Sistema de login seguro para administradores.

Painel de Gestão: Área restrita para visualizar, listar e gerenciar mensagens recebidas.

🛠️ Tecnologias Utilizadas
Framework: Django 4.2+

Linguagem: Python 3.10+

Estilização: TailwindCSS (Interface responsiva e moderna)

Banco de Dados: SQLite

🚀 Passo a Passo para Rodar o Projeto
Siga estas etapas para configurar o ambiente localmente:

1. Clonar o Repositório
Bash

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
2. Configurar Ambiente Virtual (Recomendado)
Bash

# Criar o ambiente
python -m venv venv

# Ativar (Windows)
.\venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate
3. Instalar Dependências
Bash

pip install -r requirements.txt
4. Preparar o Banco de Dados
Execute as migrações para criar as tabelas necessárias:

Bash

python manage.py migrate
5. Criar Usuário Administrador
Para acessar o painel restrito, você precisa criar um superusuário:

Bash

python manage.py createsuperuser
Siga as instruções no terminal para definir nome de usuário, e-mail e senha.

6. Iniciar o Servidor
Bash

python manage.py runserver
Agora, acesse:

Site Público: http://127.0.0.1:8000/

Painel Admin: http://127.0.0.1:8000/login/

📂 Estrutura do Projeto
Plaintext

├── core/              # Configurações globais do Django
├── contato/           # App principal (Models, Views, Forms)
│   ├── templates/     # Arquivos HTML (Landpage, Login, Painel)
│   └── models.py      # Definição da tabela de Mensagens
├── manage.py          # Utilitário de comando do Django
└── requirements.txt   # Lista de dependências do projeto