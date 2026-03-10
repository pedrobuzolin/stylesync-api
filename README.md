# StyleSync API

API REST desenvolvida em Python para gerenciamento de usuários, produtos e vendas.
O projeto simula o backend de um sistema de gestão para comércio, incluindo autenticação com JWT e upload de vendas via arquivo CSV.

Este projeto foi desenvolvido com foco em **boas práticas de desenvolvimento backend**, incluindo testes automatizados, separação de responsabilidades e preparação para deploy.

---

# Arquitetura da Aplicação

```id="s3s3qk"
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

---

# Funcionalidades

* Autenticação de usuários com token JWT
* Cadastro de usuários
* Listagem de usuários (rota protegida)
* Cadastro e listagem de produtos
* Upload de vendas via arquivo CSV
* Testes automatizados da API
* Mock de banco de dados para ambiente de testes

---

# Instalação

Clone o repositório:

```id="snm9k0"
git clone https://github.com/seuusuario/stylesync-api.git
cd stylesync-api
```

Crie um ambiente virtual:

```id="t57rk1"
python -m venv venv
```

Ative o ambiente virtual:

Windows

```id="u3bn7c"
venv\Scripts\activate
```

Linux / Mac

```id="yj2e5b"
source venv/bin/activate
```

Instale as dependências:

```id="o7h7wk"
pip install -r requirements.txt
```

---

# Variáveis de Ambiente

Crie um arquivo `.env` baseado no `.env.example`.

Exemplo:

```id="62xag4"
MONGO_URI=your_mongodb_connection_string
SECRET_KEY=your_secret_key
```

Essas variáveis são utilizadas para conectar ao banco de dados e gerar os tokens de autenticação.

---

# Executando a Aplicação

Execute o arquivo principal:

```id="q3ezpc"
python run.py
```

A API ficará disponível em:

```id="3gyzz4"
http://localhost:5000
```

---

# Executando os Testes

Para rodar os testes automatizados:

```id="5kr2r1"
pytest --cov
```

Isso executará todos os testes do projeto e exibirá a cobertura de código.

---

# Principais Endpoints

### Health Check

```id="i3d0ud"
GET /
```

Resposta:

```id="9b40g9"
{
  "message": "Bem vindo ao StyleSync!"
}
```

---

### Autenticação

```id="t4pdfe"
POST /login
```

Exemplo de requisição:

```id="w4k3ya"
{
  "username": "admin",
  "password": "123"
}
```

Resposta:

```id="28p81j"
{
  "access_token": "jwt_token"
}
```

---

### Usuários

```id="tgj3s8"
GET /users
POST /user
```

---

### Produtos

```id="3jpm6d"
GET /products
POST /products
```

---

### Upload de Vendas

```id="v9byrn"
POST /sales/upload
```

Exemplo de CSV aceito:

```id="xq4x4y"
date,product,quantity,price
2025-01-01,produto a,2,10.50
2025-01-02,produto b,4,5.40
```

---

# Testes Automatizados

Os testes da aplicação utilizam:

* Pytest
* Mongomock para simulação do MongoDB
* Testes de autenticação
* Testes de rotas protegidas
* Testes de upload de arquivo CSV

Exemplo de execução:

```id="ttxfpr"
pytest
```

---

# Segurança

* Tokens JWT para autenticação
* Variáveis sensíveis via ambiente (.env)
* Banco de dados isolado para testes

---

# Roadmap do Projeto

Próximas melhorias planejadas:

* Integração contínua (CI)
* Deploy da API
* Containerização com Docker
* Documentação da API

---