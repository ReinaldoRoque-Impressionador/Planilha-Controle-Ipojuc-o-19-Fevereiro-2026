import os
from PIL import Image
import pygame

# Caminhos base
CAMINHO_IMAGENS = r"C:\Users\VEIRANO\PycharmProjects\ModuloTkinter\PlanilhaControleIpojucão\imagensipojucao"
CAMINHO_SONS = r"C:\Users\VEIRANO\PycharmProjects\ModuloTkinter\PlanilhaControleIpojucão\sonsipojucao"

# Lista de arquivos esperados
arquivos_imagem = [
    "logo_ipojucao.png",
    "mascote_coracao.png",
    "mascote_beijo.png"
]

arquivos_som = [
    "splash.mp3"
]

def diagnosticar_imagens():
    print("🖼️ Diagnóstico de Imagens:")
    for nome in arquivos_imagem:
        caminho = os.path.join(CAMINHO_IMAGENS, nome)
        if os.path.exists(caminho):
            try:
                Image.open(caminho)
                print(f"✅ {nome} carregado com sucesso.")
            except Exception as e:
                print(f"❌ {nome} encontrado, mas falha ao abrir: {e}")
        else:
            print(f"❌ {nome} não encontrado no caminho: {caminho}")

def diagnosticar_sons():
    print("\n🔊 Diagnóstico de Sons:")
    pygame.mixer.init()
    for nome in arquivos_som:
        caminho = os.path.join(CAMINHO_SONS, nome)
        if os.path.exists(caminho):
            try:
                pygame.mixer.music.load(caminho)
                print(f"✅ {nome} carregado com sucesso.")
            except Exception as e:
                print(f"❌ {nome} encontrado, mas falha ao carregar: {e}")
        else:
            print(f"❌ {nome} não encontrado no caminho: {caminho}")

# Executar diagnóstico
if __name__ == "__main__":
    diagnosticar_imagens()
    diagnosticar_sons()diadia