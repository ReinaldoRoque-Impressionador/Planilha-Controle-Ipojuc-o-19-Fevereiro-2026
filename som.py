# som.py
import pygame
import threading
import os
import pygame
pygame.mixer.init()


som_ativo = True  # Estado global do som

####

from tkinter import StringVar, ttk
#from modulos.recursos.som import tocar_som, pausar_som, continuar_som, parar_som

# def criar_barra_som(frame_pai):
#     frame = ttk.Frame(frame_pai)
#     frame.grid(row=0, column=0, sticky="nsew")
#
#     ttk.Label(frame, text="🔊 Controle de Som", font=("Arial", 16)).grid(row=0, column=0, pady=10)
#
#     botao_som = ttk.Button(frame, text="🔈 Som Ativado", command=lambda: alternar_som(botao_som))
#     botao_som.grid(row=1, column=0, pady=5)
#
#     faixas = [
#         "musica_abertura.mp3", "musica_fundo.mp3", "acesso_concedido.mp3", "acesso_negado.mp3",
#         "bouncy_pet_intro.mp3", "breaking_news_intro_378273.mp3", "clair_de_lune_prelude.mp3",
#         "confirmacao.mp3", "dramatic_delete.mp3", "end_of_day.mp3", "musica_consulta.mp3",
#         "relatorio.mp3", "salvando.mp3", "search_ping.mp3", "soft_edit_tune.mp3",
#         "usuario_adicionado.mp3", "usuario_removido.mp3", "efeito_click.mp3"
#     ]
#
#     faixa_var = StringVar(value=faixas[0])
#     combo_faixas = ttk.Combobox(frame, textvariable=faixa_var, values=faixas, state="readonly")
#     combo_faixas.grid(row=2, column=0, pady=5)
#
#     ttk.Button(frame, text="▶️ Play", command=lambda: tocar_som(f"sons/{faixa_var.get()}")).grid(row=3, column=0, pady=5)
#     ttk.Button(frame, text="⏸️ Pausar", command=pausar_som).grid(row=4, column=0, pady=5)
#     ttk.Button(frame, text="⏯️ Continuar", command=continuar_som).grid(row=5, column=0, pady=5)
#     ttk.Button(frame, text="⏹️ Parar", command=parar_som).grid(row=6, column=0, pady=5)
#
#     return frame

####


def inicializar_audio():
    if not pygame.mixer.get_init():
        pygame.mixer.init()

def ativar_som():
    global som_ativo
    som_ativo = True

def desativar_som():

    global som_ativo
    som_ativo = False

def alternar_som(botao=None):
    global som_ativo
    som_ativo = not som_ativo
    if botao:
        texto = "🔈 Som Ativado" if som_ativo else "🔇 Som Desativado"
        botao.config(text=texto)

def alternar_som_estado(botao=None):
    global som_ativo
    som_ativo = not som_ativo
    if botao:
        texto = "🔈 Som Ativado" if som_ativo else "🔇 Som Desativado"
        botao.config(text=texto)

# def tocar_som(caminho, duracao=None):
#     if not som_ativo or not os.path.exists(caminho):
#         print(f"Tocando: {caminho}")
#         print(f"🔇 Som desativado ou caminho inválido: {caminho}")
#         return

def tocar_som(caminho, duracao=None):
    if not som_ativo:
        print("🔇 Som está desativado.")
        return

    if not os.path.exists(caminho):
        print(f"❌ Caminho inválido: {caminho}")
        return

    # def reproduzir():
    #     try:
    #         inicializar_audio()
    #         pygame.mixer.music.load(caminho)
    #         pygame.mixer.music.play()
    #         if duracao:
    #             pygame.time.delay(duracao * 1000)
    #             pygame.mixer.music.stop()
    #     except Exception as e:
    #         print(f"Erro ao tocar som: {e}")
    #
    # threading.Thread(target=reproduzir, daemon=True).start()


    # def reproduzir():
    #     try:
    #         inicializar_audio()
    #         pygame.mixer.music.load(caminho)
    #         pygame.mixer.music.play()
    #         if duracao:
    #             pygame.time.delay(duracao * 1000)
    #             pygame.mixer.music.stop()
    #     except Exception as e:
    #         print(f"Erro ao tocar som: {e}")
    #
    # threading.Thread(target=reproduzir, daemon=True).start()

    # def reproduzir():
    #     try:
    #         inicializar_audio()
    #         pygame.mixer.music.stop()  # ← ESSENCIAL: para qualquer faixa anterior
    #         pygame.mixer.music.unload()  # ← limpa faixa anterior (opcional, mas recomendado)
    #         pygame.mixer.music.load(caminho)
    #         pygame.mixer.music.play()
    #         if duracao:
    #             pygame.time.delay(duracao * 1000)
    #             pygame.mixer.music.stop()
    #     except Exception as e:
    #         print(f"Erro ao tocar som: {e}")
    #
    # threading.Thread(target=reproduzir, daemon=True).start()
    def reproduzir():
        try:
            inicializar_audio()
            pygame.mixer.music.stop()  # Para qualquer faixa anterior
            pygame.mixer.music.load(caminho)
            pygame.mixer.music.play()
            if duracao:
                pygame.time.delay(duracao * 1000)
                pygame.mixer.music.stop()
        except Exception as e:
            print(f"Erro ao tocar som: {e}")

    threading.Thread(target=reproduzir, daemon=True).start()


def parar_som():
    if pygame.mixer.get_init():
        pygame.mixer.music.stop()

# def tocar_som_bloqueante(caminho):
#     if som_ativo and os.path.exists(caminho):
#         inicializar_audio()
#         pygame.mixer.music.load(caminho)
#         pygame.mixer.music.play()
#         while pygame.mixer.music.get_busy():
#             pygame.time.Clock().tick(10)

def som_evento(tipo):
    sons = {
        "login_sucesso": "sons/acesso_concedido.mp3",
        "login_falha": "sons/acesso_negado.mp3",
        "usuario_adicionado": "sons/usuario_adicionado.mp3",
        "usuario_removido": "sons/usuario_removido.mp3",
        "consulta": "sons/musica_consulta_pet.mp3",
        "relatorio": "sons/relatorio.mp3",
        "abertura": "sons/musica_abertura.mp3",
        "fechamento": "sons/musica_end_of_day.mp3",
        "mascote": "sons/bouncy_pet_intro.mp3",
        "salvando": "sons/salvando.mp3"
    }
    caminho = sons.get(tipo)
    if caminho:
        tocar_som(caminho)





def tocar_som_curto(path):
    if som_ativo and os.path.exists(path):
        try:
            som = pygame.mixer.Sound(path)
            som.play()
        except Exception as e:
            print(f"Erro ao tocar som curto: {e}")

def pausar_som():
    if pygame.mixer.get_init():
        pygame.mixer.music.pause()

def som_e_expressao_acao():
    som_evento("consulta")

def continuar_som():
    if pygame.mixer.get_init():
        pygame.mixer.music.unpause()




















# # som.py
# import tkinter as tk
#
# import pygame
# import threading
# import os
#
#
#
# from abas.ferramentas.barra_som import criar_barra_som
#
# def criar_aba_barra_som(notebook):
#     frame = ttk.Frame(notebook)
#     frame.pack(fill="both", expand=True)
#
#     # Chama a barra de som dentro do frame
#     criar_barra_som(frame)
#
#     ttk.Label(frame, text="🎛️ Controle de trilhas e som global", font=("Arial", 10)).pack(pady=10)
#
#     return frame
#
#
# from tkinter import ttk
# som_ativo = True  # isso pode ser movido para o módulo som.py
#
#
# # ✅ Inicializa mixer uma única vez
# def inicializar_audio():
#     if not pygame.mixer.get_init():
#         pygame.mixer.init()
#
# # 🎵 Controlador de som global
# som_ativo = True
#
# def ativar_som():
#     global som_ativo
#     som_ativo = True
#
# def desativar_som():
#     global som_ativo
#     som_ativo = False
#
# def alternar_som(botao=None):
#     global som_ativo
#     som_ativo = not som_ativo
#     if botao:
#         texto = "🔈 Som Ativado" if som_ativo else "🔇 Som Desativado"
#         botao.config(text=texto)
#
# # 🔊 Toca trilha de forma assíncrona
# def tocar_som(caminho, duracao=None):
#     if not som_ativo:
#         print("🔇 Som desativado. Trilha ignorada.")
#         return
#     #if os.path.exists(caminho):
#
#     if som_ativo and os.path.exists(caminho):
#         def reproduzir():
#             try:
#                 inicializar_audio()
#                 pygame.mixer.music.load(caminho)
#                 pygame.mixer.music.play()
#                 if duracao:
#                     pygame.time.delay(duracao * 1000)
#                     pygame.mixer.music.stop()
#             except Exception as e:
#                 print(f"Erro ao tocar som: {e}")
#         threading.Thread(target=reproduzir, daemon=True).start()
#     else:
#         print(f"🔇 Caminho inválido ou som desativado: {caminho}")
#
# # ⏹️ Parar trilha
# def parar_som():
#     if pygame.mixer.get_init():
#         pygame.mixer.music.stop()
#
#
# # 🔒 Modo bloqueante (espera terminar)
# def tocar_som_bloqueante(caminho):
#     if som_ativo and os.path.exists(caminho):
#         inicializar_audio()
#         pygame.mixer.music.load(caminho)
#         pygame.mixer.music.play()
#         while pygame.mixer.music.get_busy():
#             pygame.time.Clock().tick(10)
#
# # 🎯 Som por evento
# def som_evento(tipo):
#     sons = {
#         "login_sucesso": "sons/acesso_concedido.mp3",
#         "login_falha": "sons/acesso_negado.mp3",
#         "usuario_adicionado": "sons/usuario_adicionado.mp3",
#         "usuario_removido": "sons/usuario_removido.mp3",
#         "consulta": "sons/musica_consulta_pet.mp3",
#         "relatorio": "sons/relatorio.mp3",
#         "abertura": "sons/musica_abertura.mp3",
#         "fechamento": "sons/musica_end_of_day.mp3",
#         "mascote": "sons/bouncy_pet_intro.mp3"
#     }
#     caminho = sons.get(tipo)
#     if caminho:
#         tocar_som(caminho)
#
# # ✨ Animação visual: fade de mensagem
# def fade_label(label, janela, cor_base="#444", tempo=1000):
#     def fade(passo=0):
#         alpha = max(0, 1 - passo / 20)
#         cinza = int(68 * alpha)
#         nova_cor = f"#{cinza:02x}{cinza:02x}{cinza:02x}"
#         label.config(fg=nova_cor)
#         if passo < 20:
#             janela.after(50, fade, passo + 1)
#     janela.after(tempo, fade)
#
# # 🐶 Mascote piscando
# from PIL import Image, ImageTk, ImageEnhance
#
# def animar_mascote(janela, caminho_img="imagens/mascote.png", x=870, y=540):
#     if not os.path.exists(caminho_img):
#         return
#     base = Image.open(caminho_img).resize((130,130))
#     img_normal = ImageTk.PhotoImage(base)
#     escurecida = ImageTk.PhotoImage(ImageEnhance.Brightness(base).enhance(0.6))
#     label = tk.Label(janela, image=img_normal, bg="#fff")
#     label.image = img_normal
#     label.place(x=x, y=y)
#
#     def piscar(on=True):
#         label.config(image=escurecida if on else img_normal)
#         label.image = escurecida if on else img_normal
#         janela.after(300 if on else 2400, piscar, not on)
#
#     piscar()