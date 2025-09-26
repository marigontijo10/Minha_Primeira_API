🎬 API de Filmes
API desenvolvida com FastAPI para servir dados de filmes. Permite listar todos os filmes, buscar por ID e filtrar por nome ou categoria.
🚀 Tecnologias

Python
FastAPI
Pandas
Uvicorn

📁 Como rodar
Instalar dependências:
bashpip install -r requirements.txt
Executar a API:
bashpython main.py
🔗 Endpoints
1. GET / (Básico)
Retorna informações sobre a API
json{
  "projeto": "API de Filmes",
  "autor": "Seu Nome",
  "descricao": "API para servir dados de filmes",
  "total_registros": 50
}
2. GET /dados (Básico)
Lista TODOS os filmes do dataset
json[
  {
    "id": 1,
    "nome": "Avatar",
    "ano": 2009,
    "categoria": "Ficção",
    "nota": 7.8
  },
  ...
]
3. GET /dados/{id} (Intermediário)
Busca um filme específico pelo ID

Exemplo: /dados/1 - retorna o filme com ID 1

4. GET /buscar (Intermediário - Opcional)
Busca filmes com filtros

Parâmetros: nome, categoria, limite
Exemplo: /buscar?nome=avatar&limite=5

📊 Dataset

Fonte: Dataset criado manualmente
Total: 50 filmes
Formato: CSV
Campos: id, nome, ano, categoria, nota

🧪 Testando
Acesse http://localhost:8000/docs para testar os endpoints na documentação automática do FastAPI.
📝 Estrutura do Projeto
Minha_Primeira_API/
├── dados/
│   ├── dataset.csv
│   └── fonte.txt
├── main.py
├── README.md

└── requirements.txt
