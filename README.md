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
python -m venv ianesteves
```
```
# Ative o ambiente virtual
# No Windows
ianesteves\Scripts\activate
# No macOS/Linux
source ianesteves/bin/activate
```
## 3. Instalar Dependências
Instale as dependências necessárias usando o pip:
```
pip install django googletrans==4.0.0-rc1 requests python-dotenv
```
## 4. Mudar o Diretório
Mude para o Diretorio do Aplicativo
```
cd .\matheusliporace\
```
## 5. Fazer Migrações do Banco de Dados
Aplique as migrações do banco de dados para configurar o banco de dados inicial:
```
python manage.py makemigrations
python manage.py migrate
```
## 6. Configurar Variáveis de Ambiente
Crie um arquivo .env no diretório raiz do projeto (barbieri/) com o seguinte conteúdo:
```
GEMINI_API_KEY= seu_api_key_do_gemini
SEARCH_ENGINE_ID=sua_search_engine_id
GOOGLE_CUSTOM_SEARCH_API_KEY=seu_google_custom_search_api_key
```
## 8. Rodar o Servidor de Desenvolvimento
Inicie o servidor de desenvolvimento para verificar se tudo está funcionando corretamente:
```
python manage.py runserver
```
## 9. Acessar o Aplicativo
Abra seu navegador e acesse http://127.0.0.1:8000/ para usar o aplicativo.
```
Com essas instruções, suas chaves de API estarão protegidas no arquivo `.env`, e você garantirá que todas as dependências necessárias estejam instaladas, incluindo o `python-dotenv` para carregar as variáveis de ambiente corretamente.
```