from PIL import Image, ImageFilter, ImageEnhance
import numpy as np


def redimensionar_imagem(imagem: Image.Image, tamanho: tuple[int, int]) -> Image.Image:
    """Redimensiona a imagem para um novo tamanho."""
    return imagem.resize(tamanho)


def converter_para_escala_de_cinza(imagem: Image.Image) -> Image.Image:
    """Converte a imagem para escala de cinza."""
    return imagem.convert("L")


def aplicar_blur(imagem: Image.Image, raio: int = 2) -> Image.Image:
    """Aplica um filtro de desfoque (blur) gaussiano."""
    return imagem.filter(ImageFilter.GaussianBlur(radius=raio))


def rotacionar_imagem(imagem: Image.Image, angulo: float) -> Image.Image:
    """Rotaciona a imagem em um determinado ângulo."""
    # 'expand=True' garante que a imagem inteira apareça após a rotação
    return imagem.rotate(angulo, expand=True)


def ajustar_brilho_contraste(imagem: Image.Image, brilho: float = 1.0, contraste: float = 1.0) -> Image.Image:
    """
    Ajusta o brilho e o contraste da imagem.
    Valores: brilho=1.0 e contraste=1.0 mantêm a imagem original.
    """
    # Ajusta o brilho
    enhancer_brilho = ImageEnhance.Brightness(imagem)
    imagem_brilho = enhancer_brilho.enhance(brilho)

    # Ajusta o contraste
    enhancer_contraste = ImageEnhance.Contrast(imagem_brilho)
    imagem_final = enhancer_contraste.enhance(contraste)

    return imagem_final
