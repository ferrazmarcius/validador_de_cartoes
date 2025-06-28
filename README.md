# Validador de Bandeira de Cartão de Crédito 💳

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Um script simples em Python para validar e identificar a bandeira de um número de cartão de crédito. Este projeto foi desenvolvido como um desafio de código para praticar lógica condicional e manipulação de strings em Python.

## ✨ Funcionalidades

* Validação baseada no número de dígitos e nos prefixos oficiais de cada bandeira.
* Interface de linha de comando interativa e de fácil utilização.
* Código limpo, comentado e de fácil entendimento.
* Suporte para as principais bandeiras utilizadas no mercado.

## 🚀 Como Usar

Este projeto não requer a instalação de nenhuma biblioteca externa. Basta ter o Python 3 instalado no seu sistema.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd seu-repositorio
    ```

3.  **Execute o script:**
    ```bash
    python validacao.py
    ```

4.  O programa irá solicitar que você digite o número do cartão de crédito. Após inserir e pressionar Enter, ele exibirá a bandeira correspondente ou uma mensagem de erro.

**Exemplo de uso:**
```
$ python validacao.py
Digite o número do cartão de crédito para validação: 4111222233334444
✅ A bandeira do cartão é: Visa
```

## 💳 Bandeiras Suportadas

O validador utiliza as seguintes regras para identificar as bandeiras:

| Bandeira | Dígitos | Prefixos |
| :--- | :---: | :--- |
| **Visa** | 16 | [cite_start]Começa com `4`[cite: 1]. |
| **Mastercard** | 16 | [cite_start]Começa com `51`, `52`, `53`, `54` ou `55`[cite: 1]. |
| **American Express**| 15 | [cite_start]Começa com `34`[cite: 1]. |
| **Elo** | 16 | [cite_start]`4011`, `4312`, `4389`, `4514`, `4576`, `5041`, `5067`, `5090` e outros[cite: 1]. |
| **Hipercard** | 16 | [cite_start]Começa com `60` a `65`[cite: 1]. |
| **Discover** | 16 | [cite_start]`6011`, `65`, e intervalos como `622126` a `622925` ou `644` a `649`[cite:1]. |

## 🤝 Contribuição

Contribuições são muito bem-vindas! Se você tiver sugestões para adicionar novas bandeiras ou melhorar a lógica de validação, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## 📝 Licença

Este projeto está licenciado sob a Licença MIT.