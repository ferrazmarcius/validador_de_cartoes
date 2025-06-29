from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles  # 1. Importe StaticFiles
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Validador de Cartões de Crédito")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

def validar_bandeira_cartao(numero_cartao):
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

# --- Lógica da API ---

class CartaoRequest(BaseModel):
    numero_cartao: str

# --- 2. Correção da Rota Principal ---
@app.get("/", response_class=FileResponse)
async def get_home():
    # 3. Retorne diretamente o nome do arquivo HTML
    return "index.html"

@app.post("/validar-cartao")
async def validar(request: CartaoRequest):
    bandeira = validar_bandeira_cartao(request.numero_cartao)
    return {"bandeira": bandeira}