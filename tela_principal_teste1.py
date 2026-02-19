import tkinter as tk
from tkinter import ttk
import os

from reportlab.lib.colors import lightblue

from abas.aba_inativos import montar_aba_inativos
from dados_compartilhados import montar_dados_compartilhados
from interface.aba_cadastro import montar_aba_cadastro
from modulos.abas.aba_clientes import montar_aba_clientes
from modulos.abas.aba_financeiro import montar_aba_financeiro
from modulos.abas.aba_relatorios import montar_aba_relatorios
from modulos.abas.aba_clima import montar_aba_clima
from modulos.recursos.aba_itau import criar_aba_itau
from modulos.abas.aba_config import montar_aba_config
from modulos.abas.editor_codigo import AbaEditorCodigo
#from modulos.abas.ferramentas.barra_som import criar_barra_som
from modulos.abas.aba_consulta import montar_aba_consulta




def iniciar_janela_principal(usuario_logado):
    janela = tk.Tk()
    dc.inicializar_variaveis(janela)
    janela.title("Sistema Principal")
    janela.geometry("1024x768")

    # Layout da janela
    janela.grid_rowconfigure(1, weight=1)
    janela.grid_columnconfigure(0, weight=0)

    # Frame principal
    frame_principal = tk.Frame(janela)
    frame_principal.grid(row=1, column=0, sticky="nsew")
    frame_principal.grid_rowconfigure(0, weight=1)
    frame_principal.grid_columnconfigure(0, weight=0)  # menu
    frame_principal.grid_columnconfigure(1, weight=1)  # conteúdo

    # Topo com barra de som
    frame_topo = tk.Frame(janela)
    frame_topo.grid(row=0, column=0, sticky="ew")
    frame_topo.grid_columnconfigure(0, weight=1)

    barra_som = criar_barra_som(frame_topo)
    barra_som.grid(row=0, column=0, sticky="ew", padx=10, pady=5)

    label = tk.Label(
        frame_topo,
        text=f"Bem-vindo ao Sistema de Controle Ipojucão, {usuario_logado.nome}!",
        font=("Arial", 14)
    )
    label.grid(row=0, column=1, sticky="e", padx=10)

    # Área de conteúdo
    conteudo = tk.Frame(frame_principal, bg="white")
    conteudo.grid(row=0, column=1, sticky="nsew")
    conteudo.grid_rowconfigure(0, weight=1)
    conteudo.grid_columnconfigure(0, weight=1)
    conteudo.config(borderwidth=2, relief="solid")

    # Notebook com abas
    notebook = ttk.Notebook(conteudo)
    notebook.grid(row=0, column=0, sticky="nsew")

    # Gerenciador de abas
    gerenciador = GerenciadorAbas()
    gerenciador.registrar_aba("cadastro", montar_aba_cadastro)
    gerenciador.registrar_aba("financeiro", montar_aba_financeiro)
    gerenciador.registrar_aba("clientes", montar_aba_clientes)
    gerenciador.registrar_aba("editor_codigo", AbaEditorCodigo)
    gerenciador.registrar_aba("clima", montar_aba_clima)
    gerenciador.registrar_aba("config", montar_aba_config)
    gerenciador.registrar_aba("relatorios", montar_aba_relatorios)
    gerenciador.registrar_aba("itau", criar_aba_itau)
    gerenciador.registrar_aba("dados_compartilhados", montar_dados_compartilhados)
    gerenciador.registrar_aba("montar_aba_inativos", montar_aba_inativos)
    gerenciador.registrar_aba("consulta", montar_aba_consulta)

    # Exibe menu lateral para perfis autorizados
    if usuario_logado.perfil in ("admin", "funcionario"):
        frame_principal.grid_columnconfigure(0, minsize=200)

        menu_lateral = MenuLateral(
            master=frame_principal,
            perfil_usuario=usuario_logado.perfil,
            gerenciador_abas=gerenciador,
            notebook=notebook
        )
        menu_lateral.config(width=200, bg="lightblue")
        menu_lateral.grid(row=0, column=0, sticky="ns")

        print(f"✅ MenuLateral criado para perfil: {usuario_logado.perfil}")

    frame_principal.config(borderwidth=2, relief="solid")
    janela.mainloop()