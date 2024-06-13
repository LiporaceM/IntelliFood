# Guia de Configuração do Projeto


## 1. Clonar o Repositório

Abra um terminal (ou prompt de comando) e clone o repositório do projeto:

```bash
git clone https://github.com/LiporaceM/barbieri.git
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
## 4. Mudar o Diretório
Mude para o Diretorio do Aplicativo
```
cd .\matheusliporace\
```
## 5. Fazer Migrações do Banco de Dados
Aplique as migrações do banco de dados para configurar o banco de dados inicial:
```
python manage.py migrate
```
## 6. Colocar as APIs
Substitua o valor das variaveis com o os IDs das APIs.
## 7. Rodar o Servidor de Desenvolvimento
Inicie o servidor de desenvolvimento para verificar se tudo está funcionando corretamente:
```
python manage.py runserver
```
