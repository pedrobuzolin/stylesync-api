# StyleSync API

API REST desenvolvida em **Python** para gerenciamento de usuários, produtos e vendas.

O projeto simula o backend de um sistema de gestão para comércio, incluindo autenticação com **JWT** e upload de vendas via **arquivo CSV**.

Este projeto foi desenvolvido com foco em **boas práticas de desenvolvimento backend**, incluindo:

* arquitetura organizada
* testes automatizados
* integração contínua (CI)
* separação de responsabilidades
* preparação para deploy

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
* Pytest
* Mongomock (mock de banco para testes)
* GitHub Actions (CI)
* Gunicorn (servidor WSGI para produção)

---

# Funcionalidades

* Autenticação de usuários com token JWT
* Cadastro de usuários
* Listagem de usuários (rota protegida)
* Cadastro de produtos
* Listagem de produtos
* Upload de vendas via arquivo CSV
* Testes automatizados da API
* Mock de banco de dados para ambiente de testes
* Integração contínua (CI)

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

```bash
gunicorn run:app
```

O servidor **Gunicorn** é utilizado para executar a aplicação Flask em ambiente de produção.

---

# Segurança

* Autenticação via JWT
* Variáveis sensíveis protegidas por `.env`
* Banco de testes isolado com Mongomock

---

# Roadmap do Projeto

Melhorias planejadas:

* Containerização com Docker
