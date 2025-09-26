from fastapi import FastAPI
import pandas as pd

# Carregar dados
try:
    dados = pd.read_csv("dados/dataset.csv")
    dados_dict = dados.to_dict("records")
except Exception as e:
    print(f"Erro ao carregar dados:", e)
    dados_dict = []

# Criar app FastAPI
app = FastAPI(title="API de Filmes")

# Endpoint básico
@app.get("/")
def home():
    return {
        "projeto": "API de Filmes",
        "autor": "Seu Nome",
        "descricao": "API para servir dados de filmes",
        "total_registros": len(dados_dict)
    }

@app.get("/dados")
def listar_todos():
    return dados_dict

# Endpoint intermediário: busca por ID
@app.get("/dados/{item_id}")
def buscar_por_id(item_id: int):
    resultado = next((item for item in dados_dict if item["id"] == item_id), None)
    if resultado:
        return resultado
    return {"erro": "ID não encontrado"}

# Endpoint intermediário opcional: query parameters
@app.get("/buscar")
def buscar_com_filtros(nome: str = None, categoria: str = None, limite: int = 10):
    resultados = dados_dict
    
    if nome:
        resultados = [item for item in resultados if nome.lower() in str(item.get("nome", "")).lower()]
    
    if categoria:
        resultados = [item for item in resultados if categoria.lower() in str(item.get("categoria", "")).lower()]
    
    return {
        "filtros": {"nome": nome, "categoria": categoria, "limite": limite},
        "resultados": resultados[:limite],
        "total": len(resultados)
    }

# Executar servidor (adicione essa parte no final)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)