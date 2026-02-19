from PIL import Image, ImageTk

def carregar_imagem_mascote(nome_arquivo, tamanho=(150, 150)):
    from modulos.recursos.dados_compartilhados import caminho_arquivo
    caminho = caminho_arquivo(nome_arquivo, "imagens")
    imagem = Image.open(caminho).resize(tamanho)
    return ImageTk.PhotoImage(imagem)