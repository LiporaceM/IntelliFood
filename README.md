# Guia de Configuração do Projeto

Este guia descreve como configurar e rodar o projeto em um novo computador, assumindo que o projeto será importado pelo Git.

## 1. Clonar o Repositório

Abra um terminal (ou prompt de comando) e clone o repositório do projeto:

```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/LiporaceM/barbieri)
cd barbieri
```
## 2. Crie o ambiente virtual
```
Crie um ambiente virtual e ative-o:
python -m venv venv
```
```
# Ative o ambiente virtual
# No Windows
venv\Scripts\activate
# No macOS/Linux
source venv/bin/activate
```
## 3. Instalar Dependências
Instale as dependências necessárias usando o pip:
```
pip install django googletrans==4.0.0-rc1 requests
```
## 4. Fazer Migrações do Banco de Dados
Aplique as migrações do banco de dados para configurar o banco de dados inicial:
```
python manage.py migrate
```
## 5. Rodar o Servidor de Desenvolvimento
Inicie o servidor de desenvolvimento para verificar se tudo está funcionando corretamente:
```
python manage.py runserver
```
