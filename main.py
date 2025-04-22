from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()

@app.post("/api/dados")
async def receber_dados(request: Request):
    dados = await request.json()
    print(f"[{datetime.now().isoformat()}] Dados recebidos: {dados}")
    return {"status": "ok", "mensagem": "Dados recebidos com sucesso"}
