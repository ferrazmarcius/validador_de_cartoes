# A função de apoio que você criou com o Copilot
def validar_bandeira_cartao(numero_cartao):
    """
    Valida e retorna a bandeira de um cartão de crédito com base em suas regras de número e prefixo.
    """
    # [cite_start]Regras Bandeira Visa: 16 digitos, comecando com 4 [cite: 1]
    # [cite_start]Regras Bandeira Mastercard: 16 digitos, comecando com 51, 52, 53, 54 ou 55 [cite: 1]
    # [cite_start]Regras Bandeira American Express: 15 digitos, comecando com 34 [cite: 1]
    # [cite_start]Regras Bandeira Elo: 16 digitos, comecando com 4011, 4312, 4389, 4514, 4576, 5041, 5067, 5067, 5090, 5091, 5092, 5093, 5094, 5095, 5096 ou 5097 [cite: 1]
    # [cite_start]Regras Bandeira Hipercard: 16 digitos, comecando com 60, 61, 62, 63, 64 ou 65 [cite: 1]
    # [cite_start]Regras Bandeira Discover: 16 digitos, comecando com 6011, 622126 a 622925, 644, 645, 646, 647, 648, 649 ou 65 [cite: 1]
    
    numero_cartao = str(numero_cartao).replace(" ", "")
    
    if len(numero_cartao) == 16 and numero_cartao.startswith('4'):
        return 'Visa'
    elif len(numero_cartao) == 16 and numero_cartao[:2] in ['51', '52', '53', '54', '55']:
        return 'Mastercard'
    elif len(numero_cartao) == 15 and numero_cartao.startswith('34'):
        return 'American Express'
    elif len(numero_cartao) == 16 and any(numero_cartao.startswith(prefix) for prefix in ['4011', '4312', '4389', '4514', '4576', 
                                                                                        '5041', '5067', '5090', '5091', 
                                                                                        '5092', '5093', '5094', 
                                                                                        '5095', '5096', '5097']):
        return 'Elo'
    elif len(numero_cartao) == 16 and any(numero_cartao.startswith(prefix) for prefix in ['60', '61', '62', '63', '64', '65']):
        return 'Hipercard'
    elif len(numero_cartao) == 16 and any(numero_cartao.startswith(prefix) for prefix in ['6011'] + [f'622{i}' for i in range(126, 926)] + 
                                                                                        ['644', '645', '646', '647', '648', '649'] + ['65']):
        return 'Discover'
    
    return None

if __name__ == "__main__":
    # Pede ao usuário para digitar o número do cartão
    numero_digitado = input("Digite o número do cartão de crédito para validação: ")
    
    # Chama a sua função para obter a bandeira
    bandeira = validar_bandeira_cartao(numero_digitado)
    
    # Exibe o resultado para o usuário
    if bandeira:
        print(f"✅ A bandeira do cartão é: {bandeira}")
    else:
        print("❌ Bandeira do cartão não identificada ou número inválido.")