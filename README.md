# StyleSync API

## 🔥 API de Gestão Comercial com Processamento de Vendas

API backend desenvolvida para simular um sistema real de gestão comercial, permitindo autenticação de usuários, controle de produtos e processamento de vendas, incluindo ingestão de dados via arquivos CSV.

👉 O objetivo é resolver o problema de centralização e processamento de dados comerciais, preparando o sistema para cenários reais de uso.

### ⚙️ Principais Funcionalidades

* Autenticação segura com JWT

* Cadastro e gerenciamento de usuários e produtos

* Processamento de vendas

* Upload e ingestão de dados via CSV

* Testes automatizados com banco mock (Mongomock)

* Integração contínua com GitHub Actions

* Containerização com Docker

* Deploy em ambiente de produção

---

# Arquitetura da Aplicação

```
Client
   ↓
Flask API
   ↓
MongoDB
```

A API é responsável por autenticação, gerenciamento de dados e processamento de uploads de vendas.

---

# Tecnologias Utilizadas

* Python
* Flask
* MongoDB
* PyMongo
* JWT Authentication
* Pydantic
* Bcrypt (hash seguro de senhas)
* Pytest
* Mongomock (mock de banco para testes)
* GitHub Actions (CI)
* Gunicorn (servidor WSGI para produção)
* Docker

---

# Funcionalidades

* Autenticação de usuários com token JWT
* Cadastro de usuários com **hash seguro de senha**
* Listagem de usuários (rota protegida)
* Cadastro de produtos
* Listagem de produtos
* Upload de vendas via arquivo CSV
* Testes automatizados da API
* Mock de banco de dados para ambiente de testes
* Integração contínua (CI)
* Containerização da aplicação com Docker

---

# API Online

A API está disponível publicamente em:

```
https://stylesync-api.onrender.com
```

Endpoint de teste:

```
GET /
```

Resposta esperada:

```json
{
  "message": "Bem vindo ao StyleSync!"
}
```

---

# Documentação da API

A API possui documentação interativa utilizando Swagger (Flasgger).

A documentação permite:

visualizar todos os endpoints

testar requisições diretamente pelo navegador

visualizar parâmetros e respostas esperadas

Acesse em:

https://stylesync-api.onrender.com/apidocs

---

# Instalação

Clone o repositório:

```bash
git clone https://github.com/seuusuario/stylesync-api.git
cd stylesync-api
```

Crie um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual.

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# Variáveis de Ambiente

Crie um arquivo `.env` baseado no `.env.example`.

Exemplo:

```
MONGO_URI=your_mongodb_connection_string
SECRET_KEY=your_secret_key
```

Essas variáveis são utilizadas para conectar ao banco de dados e gerar os tokens de autenticação.

---

# Executando a Aplicação Localmente

Execute o arquivo principal:

```bash
python run.py
```

A API ficará disponível em:

```
http://localhost:5000
```

---

# Executando com Docker

A aplicação também pode ser executada utilizando **Docker**, garantindo um ambiente isolado e reproduzível.

Primeiro construa a imagem:

```bash
docker build -t stylesync-api .
```

Depois execute o container:

```bash
docker run -p 5000:5000 \
-e MONGO_URI="your_mongodb_connection_string" \
-e SECRET_KEY="your_secret_key" \
stylesync-api
```

A aplicação ficará disponível em:

```
http://localhost:5000
```

---

# Executando os Testes

Para rodar os testes automatizados:

```bash
pytest
```

Os testes utilizam **mongomock**, permitindo simular o banco de dados sem necessidade de um MongoDB real.

---

# Integração Contínua (CI)

Este projeto utiliza **GitHub Actions** para executar testes automaticamente.

A pipeline roda sempre que ocorre:

* push na branch `main`
* abertura de pull request

Etapas executadas:

1. Checkout do repositório
2. Configuração do ambiente Python
3. Instalação das dependências
4. Execução dos testes automatizados com Pytest

Isso garante que novas alterações não quebrem funcionalidades existentes da API.

---

# Principais Endpoints

## Health Check

```
GET /
```

Resposta:

```json
{
  "message": "Bem vindo ao StyleSync!"
}
```

---

## Autenticação

```
POST /login
```

Exemplo de requisição:

```json
{
  "username": "admin",
  "password": "123"
}
```

Resposta:

```json
{
  "access_token": "jwt_token"
}
```

---

## Usuários

```
GET /users
POST /user
```

---

## Produtos

```
GET /products
POST /products
```

---

## Upload de Vendas

```
POST /sales/upload
```

Exemplo de CSV aceito:

```
date,product,quantity,price
2025-01-01,produto a,2,10.50
2025-01-02,produto b,4,5.40
```

---

# Testes Automatizados

A aplicação possui testes automatizados para garantir o funcionamento das principais funcionalidades.

Os testes cobrem:

* autenticação
* rotas protegidas
* criação de usuários
* criação de produtos
* upload de vendas via CSV

Ferramentas utilizadas:

* Pytest
* Mongomock

Execução:

```bash
pytest
```

---

# Deploy

O deploy da aplicação pode ser realizado em plataformas de hospedagem como **Render**.

Comando utilizado para iniciar a aplicação em produção:

```
gunicorn run:app
```

O servidor **Gunicorn** é utilizado para executar a aplicação Flask em ambiente de produção.

---

# Segurança

* Autenticação via JWT
* Senhas armazenadas utilizando **hash seguro com Bcrypt**
* Variáveis sensíveis protegidas por `.env`
* Banco de testes isolado com Mongomock

---

# Roadmap do Projeto

Melhorias planejadas:

* Paginação em endpoints de listagem
* Melhor tratamento global de erros
* Controle de permissões de usuário (roles)
