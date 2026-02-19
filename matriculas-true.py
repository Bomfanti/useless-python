import json

ARQUIVO = "response.json"

with open(ARQUIVO, "r", encoding="utf-8") as f:
    data = json.load(f)

if isinstance(data, dict):
    for valor in data.values():
        if isinstance(valor, list):
            data = valor
            break
    else:
        raise ValueError("Lista?.")

if not isinstance(data, list):
    raise TypeError("JSON?.")

total_bruto = 0
alunos_true = 0
alunos_false = 0
responsaveis_ignorados = 0

for pessoa in data:
    total_bruto += 1  

    matricula = pessoa.get("matriculaConfirmada") is True

    if matricula:
        alunos_true += 1
        qtd_resp = len(pessoa.get("responsaveis", []))
        alunos_true += qtd_resp
        total_bruto += qtd_resp  
    else:
        alunos_false += 1
        qtd_resp = len(pessoa.get("responsaveis", []))
        responsaveis_ignorados += qtd_resp
        total_bruto += qtd_resp  


print("Total bruto de registros:", total_bruto)
print("Matricula TRUE (inclui responsáveis):", alunos_true)
print("Matricula FALSE (somente alunos):", alunos_false)
print("Responsáveis ignorados:", responsaveis_ignorados)

