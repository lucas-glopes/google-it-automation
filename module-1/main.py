from pathlib import Path

from PIL import Image


def obter_imagens(diretorio: str) -> list[Image.Image]:
    nomes_imagens: list[str] = [
        diretorio + "/" + imagem.name
        for imagem in Path.iterdir(Path.cwd() / diretorio)
        if imagem.is_file()
    ]

    return nomes_imagens, [Image.open(nome_imagem) for nome_imagem in nomes_imagens]


def rotacionar_imagem_90_graus_horario(imagem: Image) -> Image.Image:
    return imagem.rotate(-90)


def redimensionar_imagem_128x128(imagem: Image) -> Image.Image:
    return imagem.resize((128, 128))


def salvar_imagem(imagem: Image, nome_imagem, destino: str) -> None:
    if imagem.mode != "RGB":
        imagem = imagem.convert("RGB")
    imagem.save(destino + "/" + Path(nome_imagem).stem + ".jpeg")


def main() -> None:
    # obter nome e objeto Image das imagens
    nomes_imagens, imagens = obter_imagens("images")

    # rotacionar imagens
    imagens_rotacionadas: list[Image.Image] = [
        rotacionar_imagem_90_graus_horario(imagem) for imagem in imagens
    ]

    # redimensionar imagens rotacionadas
    imagens_rotacionadas_redimensionadas: list[Image.Image] = [
        redimensionar_imagem_128x128(imagem) for imagem in imagens_rotacionadas
    ]

    # salvar imagens editadas
    for indice in range(len(imagens_rotacionadas_redimensionadas)):
        salvar_imagem(
            imagens_rotacionadas_redimensionadas[indice],
            nomes_imagens[indice],
            "/opt/icons",
        )


if __name__ == "__main__":
    main()
