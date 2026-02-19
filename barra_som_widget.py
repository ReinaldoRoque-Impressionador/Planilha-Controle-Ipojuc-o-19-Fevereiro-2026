# barra_som_widget.py

import tkinter as tk
from tkinter import ttk
import pygame
pygame.mixer.init()

from modulos.recursos.som import tocar_som, alternar_som
from tkinter import StringVar

import os

from tkinter import ttk, StringVar

from modulos.recursos.som import tocar_som, tocar_som_curto, pausar_som, continuar_som, parar_som, alternar_som


som_ativo = True

# def criar_barra_som(frame_pai):
#     frame = ttk.Frame(frame_pai)
#     frame.grid(row=0, column=1, sticky="nsew")
#
#     ttk.Label(frame, text="🔊 Controle de Som", font=("Arial", 16)).pack(pady=10)
#
#     botao_som = ttk.Button(frame, text="🔈 Som Ativado", command=lambda: alternar_som(botao_som))
#     botao_som.grid(row=0, column=2, sticky='nsew')
#
#     ttk.Button(frame, text="Testar Som", command=lambda: tocar_som("sons/musica_abertura.mp3")).pack(pady=5)

#    return frame

# def criar_barra_som(frame_pai):
#     frame = ttk.Frame(frame_pai)_#     frame.grid(row=0, column=0, sticky="nsew")
#
#     ttk.Label(frame, text="🔊 Controle de Som", font=("Arial", 16)).grid(row=0, column=0, pady=10)
#
#     botao_som = ttk.Button(frame, text="🔈 Som Ativado", command=lambda: alternar_som(botao_som))
#     botao_som.grid(row=1, column=0, pady=5)
#
#     faixas = ["musica_abertura.mp3", "musica_fundo.mp3", "acesso_concedido.mp3", "acesso_negado.mp3", "bouncy_pet_intro.mp3", "breaking_news_intro_378273.mp3",
#               "clair_de_lune_prelude.mp3","confirmacao.mp3", "dramatic_delete.mp3", "end_of_day.mp3", "musica_consulta.mp3", "relatorio.mp3", "salvando.mp3", "search_ping.mp3",
#               "soft_edit_tune.mp3", "usuario_adicionado.mp3", "usuario_removido.mp3", "efeito_click.mp3"]
#     faixa_var = StringVar(value=faixas[0])
#     combo_faixas = ttk.Combobox(frame, textvariable=faixa_var, values=faixas, state="readonly")
#     combo_faixas.grid(row=2, column=0, pady=5)
#
#     ttk.Button(frame, text="Testar Som", command=lambda: tocar_som(f"sons/{faixa_var.get()}")).grid(row=3, column=0, pady=5)
#
#     return frame




# def criar_barra_som(frame_pai):
#     frame = ttk.Frame(frame_pai)
#     frame.grid(row=0, column=0, sticky="nsew")
#
#     ttk.Label(frame, text="🔊 Controle de Som", font=("Arial", 16)).grid(row=0, column=0, pady=10)
#
#     botao_som = ttk.Button(frame, text="🔈 Som Ativado", command=lambda: alternar_som(botao_som))
#     botao_som.grid(row=1, column=0, pady=5)
#
#     def ao_selecionar(event):
#         faixa_selecionada = faixa_var.get()
#         print(f"Faixa selecionada: {faixa_selecionada}")  # Para depuração
#
#     def tocar_faixa_selecionada():
#         faixa = faixa_var.get()
#         print(f"Tocando faixa: {faixa}")
#         tocar_som(f"sons/{faixa}")
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
#     combo_faixas.grid(row=2, column=0, pady=(10, 5))
#     combo_faixas.bind("<<ComboboxSelected>>", ao_selecionar)
#
#     # ttk.Button(frame, text="▶️ Play", command=lambda: tocar_som(f"sons/{faixa_var.get()}")).grid(row=3, column=0, pady=5)
#     ttk.Button(frame, text="▶️ Play", command=tocar_faixa_selecionada).grid(row=3, column=0, pady=5)
#     ttk.Button(frame, text="⏸️ Pausar", command=pausar_som).grid(row=4, column=0, pady=5)
#     ttk.Button(frame, text="⏯️ Continuar", command=continuar_som).grid(row=5, column=0, pady=5)
#     ttk.Button(frame, text="⏹️ Parar", command=parar_som).grid(row=6, column=0, pady=5)
#     ttk.Button(frame, text="🔔 Efeito Curto", command=lambda: tocar_som_curto("sons/sucesso.mp3")).grid(row=7, column=0, pady=5)
#
#     return frame


# def criar_barra_som(frame_pai):
#     frame = ttk.Frame(frame_pai)
#     frame.grid(row=0, column=0, sticky="nsew")
#
#     # 🎛️ Título
#     ttk.Label(frame, text="🔊 Controle de Som", font=("Arial", 16)).grid(row=0, column=0, pady=(10, 5))
#
#     # 🔈 Botão para ativar/desativar som
#     botao_som = ttk.Button(frame, text="🔈 Som Ativado", command=lambda: alternar_som(botao_som))
#     botao_som.grid(row=1, column=0, pady=5)
#
#     # 🎵 Lista de faixas disponíveis
#     faixas = [
#         "musica_abertura.mp3", "musica_fundo.mp3", "acesso_concedido.mp3", "acesso_negado.mp3",
#         "bouncy_pet_intro.mp3", "breaking_news_intro_378273.mp3", "clair_de_lune_prelude.mp3",
#         "confirmacao.mp3", "dramatic_delete.mp3", "end_of_day.mp3", "musica_consulta.mp3",
#         "relatorio.mp3", "salvando.mp3", "search_ping.mp3", "soft_edit_tune.mp3",
#         "usuario_adicionado.mp3", "usuario_removido.mp3", "efeito_click.mp3"
#     ]
#
#     faixa_var = StringVar()
#     faixa_var.set(faixas[0])  # Valor inicial
#
#     combo_faixas = ttk.Combobox(frame, textvariable=faixa_var, values=faixas, state="readonly")
#     combo_faixas.grid(row=2, column=0, pady=(10, 5))
#
#     # 🔁 Atualiza faixa selecionada (opcional para depuração)
#     def ao_selecionar(event):
#         print(f"Faixa selecionada: {faixa_var.get()}")
#
#     combo_faixas.bind("<<ComboboxSelected>>", ao_selecionar)
#
#     # ▶️ Botão para tocar faixa selecionada
#     def tocar_faixa_selecionada():
#         faixa = faixa_var.get()
#         print(f"Tocando faixa: {faixa}")
#         tocar_som(f"sons/{faixa}")
#
#     ttk.Button(frame, text="▶️ Play", command=tocar_faixa_selecionada).grid(row=3, column=0, pady=5)
#
#     # ⏸️ Pausar, ⏯️ Continuar, ⏹️ Parar
#     ttk.Button(frame, text="⏸️ Pausar", command=pausar_som).grid(row=4, column=0, pady=5)
#     ttk.Button(frame, text="⏯️ Continuar", command=continuar_som).grid(row=5, column=0, pady=5)
#     ttk.Button(frame, text="⏹️ Parar", command=parar_som).grid(row=6, column=0, pady=5)
#
#     # 🔔 Efeito sonoro curto
#     ttk.Button(frame, text="🔔 Efeito Curto", command=lambda: tocar_som_curto("sons/sucesso.mp3")).grid(row=7, column=0, pady=(5, 10))
#
#     return frame

from tkinter import ttk, StringVar
import tkinter as tk
from modulos.recursos.som import tocar_som, tocar_som_curto, pausar_som, continuar_som, parar_som, alternar_som

def criar_barra_som(frame_pai):
    frame = ttk.Frame(frame_pai)
    frame.grid(row=0, column=2, sticky="w")


    # 🔊 Título
    ttk.Label(frame, text="🔊 Controle de Som", font=("Arial", 16)).grid(row=0, column=0, sticky="e", pady=(10, 5))

    # 🔈 Botão de ativar/desativar som
    botao_som = ttk.Button(frame, text="🔈 Som Ativado", command=lambda: alternar_som(botao_som))
    botao_som.grid(row=1, column=0, pady=5)

    # 🎵 Lista de faixas
    faixas = [
        "acesso_concedido.mp3", "acesso_negado.mp3",
        "bouncy_pet_intro.mp3", "breaking_news_intro_378273.mp3", "clair_de_lune_prelude.mp3",
        "confirmacao.mp3", "dramatic_delete.mp3", "end_of_day.mp3", "musica_abertura.mp3","musica_consulta.mp3",
        "relatorio.mp3", "salvando.mp3", "search_ping.mp3", "soft_edit_tune.mp3",
        "usuario_adicionado.mp3", "usuario_removido.mp3", "efeito_click.mp3"
    ]

    faixa_var = StringVar()
    faixa_var.set(faixas[0])  # Define valor inicial


    combo_faixas = ttk.Combobox(frame, textvariable=faixa_var, values=faixas, state="readonly")
    combo_faixas.grid(row=2, column=0, sticky="e", pady=(10, 5))

    # ▶️ Botão para tocar faixa selecionada
    # def tocar_faixa_selecionada():
    #     faixa = faixa_var.get()
    #     # caminho = f"sons/{faixa}"
    #     caminho = os.path.join("sons", faixa)
    #     print(f"Tocando faixa: {caminho}")
    #     tocar_som(caminho)

    def tocar_faixa_selecionada():
        faixa = combo_faixas.get()
        #base_dir = os.path.dirname(os.path.abspath(__file__))
        # base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # caminho = os.path.join(base_dir, "sons", faixa)
        projeto_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        caminho = os.path.join(projeto_raiz, "sons", faixa)
        print(f"Tocando faixa: {caminho}")
        tocar_som(caminho)

    ttk.Button(frame, text="▶️ Play", command=tocar_faixa_selecionada).grid(row=3, column=0, pady=5, sticky="w")

    # ⏸️ Pausar, ⏯️ Continuar, ⏹️ Parar
    ttk.Button(frame, text="⏸️ Pausar", command=pausar_som).grid(row=3, column=1, sticky="e", pady=5)
    ttk.Button(frame, text="⏯️ Continuar", command=continuar_som).grid(row=4, column=0, sticky="w", pady=5)
    ttk.Button(frame, text="⏹️ Parar", command=parar_som).grid(row=4, column=1, sticky="e", pady=5)

    # 🔔 Efeito sonoro curto
    ttk.Button(frame, text="🔔 Efeito Curto", command=lambda: tocar_som_curto("sons/sucesso.mp3")).grid(row=5, column=0, sticky="w", pady=(5, 10))
    ttk.Button(frame, text="🎧 Testar faixa atual", command=lambda: print(f"Atual: {faixa_var.get()}")).grid(row=5, column=1, sticky="e", pady=(5, 10))
    return frame