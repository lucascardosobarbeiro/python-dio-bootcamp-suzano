from PIL import Image
from typing import Optional


def carregar_imagem(caminho: str) -> Optional[Image.Image]:
    """
    Carrega uma imagem a partir de um caminho de arquivo.

    Args:
        caminho (str): O caminho para o arquivo de imagem.

    Returns:
        Optional[Image.Image]: Um objeto de imagem do Pillow, ou None se ocorrer um erro.
    """
    try:
        imagem = Image.open(caminho)
        return imagem
    except FileNotFoundError:
        print(f"Erro: O arquivo não foi encontrado em '{caminho}'")
        return None
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")
        return None


def salvar_imagem(imagem: Image.Image, caminho_saida: str):
    """
    Salva uma imagem em um caminho de arquivo.

    Args:
        imagem (Image.Image): O objeto de imagem do Pillow a ser salvo.
        caminho_saida (str): O caminho onde a imagem será salva.
    """
    try:
        imagem.save(caminho_saida)
        print(f"Imagem salva com sucesso em '{caminho_saida}'")
    except Exception as e:
        print(f"Erro ao salvar a imagem: {e}")
