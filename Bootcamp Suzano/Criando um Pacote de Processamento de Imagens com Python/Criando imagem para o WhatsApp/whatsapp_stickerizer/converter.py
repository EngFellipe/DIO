from PIL import Image
import os

def imagem_para_sticker(caminho_imagem: str, caminho_saida: str = "sticker.webp"):
    """
    Converte uma imagem para o formato de figurinha do WhatsApp (WebP, 512x512 px, ≤100 KB).
    
    :param caminho_imagem: Caminho da imagem de entrada
    :param caminho_saida: Caminho para salvar a figurinha (default: sticker.webp)
    """
    with Image.open(caminho_imagem) as img:
        img = img.convert("RGBA")
        img.thumbnail((512, 512), Image.LANCZOS)
        img.save(caminho_saida, format="WEBP", optimize=True, quality=80)
