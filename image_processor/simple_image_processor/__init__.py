# Importa as funções para que possam ser acessadas diretamente do pacote
# Ex: from simple_image_processor import carregar_imagem

from .utils import carregar_imagem, salvar_imagem
from .processing import (
    redimensionar_imagem,
    converter_para_escala_de_cinza,
    aplicar_blur,
    rotacionar_imagem,
    ajustar_brilho_contraste,
)

# Opcional: define o que é exportado quando se usa 'from simple_image_processor import *'
__all__ = [
    'carregar_imagem',
    'salvar_imagem',
    'redimensionar_imagem',
    'converter_para_escala_de_cinza',
    'aplicar_blur',
    'rotacionar_imagem',
    'ajustar_brilho_contraste',
]
