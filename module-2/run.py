import os

import requests

pasta_feedbacks = "/data/feedback"
arquivos_feedback: list[str] = os.listdir(pasta_feedbacks)

for nome_arquivo in arquivos_feedback:
    feedback: dict = {}

    with open(f"{pasta_feedbacks}/{nome_arquivo}") as arquivo:
        conteudo_arquivo: list[str] = [linha.strip() for linha in arquivo.readlines()]

        titulo: str = conteudo_arquivo[0]
        nome: str = conteudo_arquivo[1]
        data: str = conteudo_arquivo[2]
        texto_feedback: str = conteudo_arquivo[3]

        feedback["title"] = titulo
        feedback["name"] = nome
        feedback["date"] = data
        feedback["feedback"] = texto_feedback

    ip_externo: str = "<IP da API externa>"
    resposta: requests.Response = requests.post(
        f"http://{ip_externo}/feedback/",
        data=feedback,
    )

    resposta.raise_for_status()
