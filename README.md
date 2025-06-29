# Validador de Cartões de Crédito 💳 (API com FastAPI)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3.x-blue.svg?style=for-the-badge&logo=python)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Uma aplicação web completa para validar e identificar a bandeira de um número de cartão de crédito. O projeto utiliza um back-end construído com **FastAPI** e um front-end interativo com **HTML, CSS e JavaScript**, que consome a API de forma assíncrona.

## ✨ Funcionalidades

* **Interface Web Interativa:** Uma página simples e limpa para que o usuário possa inserir o número do cartão e ver o resultado em tempo real, sem recarregar a página.
* **API RESTful:** Um endpoint `POST` que recebe os dados do cartão em formato JSON e retorna a bandeira identificada.
* **Validação no Back-end:** Toda a lógica de verificação de prefixos e comprimentos é executada no lado do servidor, em Python.
* **Suporte às Principais Bandeiras:** O sistema reconhece as bandeiras mais comuns do mercado.

## 🚀 Como Executar o Projeto

Este projeto utiliza um ambiente virtual Python e FastAPI. Para executá-lo, siga os passos abaixo.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/ferrazmarcius/validador_de_cartoes.git](https://github.com/ferrazmarcius/validador_de_cartoes.git)
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd validador_de_cartoes
    ```

3.  **Crie e ative o ambiente virtual:**
    ```bash
    # Criar o ambiente
    python -m venv .venv
    
    # Ativar no Windows (Git Bash)
    source .venv/Scripts/activate
    
    # Ativar no Linux/macOS
    # source .venv/bin/activate
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Inicie o servidor da API:**
    ```bash
    uvicorn main:app --reload
    ```

6.  **Acesse a aplicação:**
    * Abra o seu navegador e acesse: **http://127.0.0.1:8000**

## Endpoints da API

A API possui os seguintes endpoints:

* `GET /`: Retorna a página principal da aplicação (`index.html`).
* `POST /validar-cartao`: Recebe um corpo JSON com o número do cartão e retorna a bandeira.
    * **Request Body:** `{"numero_cartao": "..."}`
    * **Response Body:** `{"bandeira": "Nome da Bandeira"}
