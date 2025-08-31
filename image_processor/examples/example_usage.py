# Importa as funções diretamente do seu pacote instalado
from simple_image_processor import (
    carregar_imagem,
    salvar_imagem,
    converter_para_escala_de_cinza,
    redimensionar_imagem,
    rotacionar_imagem,
    ajustar_brilho_contraste
)


def main():
    # Caminho da imagem de entrada e dos arquivos de saída
    caminho_entrada = 'examples/sample.jpg'

    # Carrega a imagem original
    imagem_original = carregar_imagem(caminho_entrada)

    if imagem_original:
        # 1. Converte para escala de cinza
        img_cinza = converter_para_escala_de_cinza(imagem_original)
        salvar_imagem(img_cinza, 'examples/resultado_cinza.jpg')

        # 2. Redimensiona a imagem
        img_redimensionada = redimensionar_imagem(imagem_original, (400, 400))
        salvar_imagem(img_redimensionada,
                      'examples/resultado_redimensionada.jpg')

        # 3. Rotaciona a imagem em 45 graus
        img_rotacionada = rotacionar_imagem(imagem_original, 45)
        # Salva em PNG para fundo transparente
        salvar_imagem(img_rotacionada, 'examples/resultado_rotacionada.png')

        # 4. Aumenta o contraste e um pouco o brilho
        img_contraste = ajustar_brilho_contraste(
            imagem_original, brilho=1.1, contraste=1.5)
        salvar_imagem(img_contraste, 'examples/resultado_contraste.jpg')


if __name__ == "__main__":
    main()
