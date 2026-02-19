import pygame
import os


def criar_player_som():
    print("🔊 Player de som criado com sucesso!")
    # Aqui você pode iniciar o mixer, carregar sons, etc.




def tocar_som(caminho):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"[ERRO] Não foi possível tocar o som: {e}")


def alternar_som(botao=None):
    global som_ativo
    som_ativo = not som_ativo
    if botao:
        texto = "🔈 Som Ativado" if som_ativo else "🔇 Som Desativado"
        botao.config(text=texto)