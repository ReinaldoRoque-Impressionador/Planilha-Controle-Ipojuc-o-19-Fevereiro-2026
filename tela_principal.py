
# tela_principal.py

import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk



from modulos.controladores.gerenciador_abas import gerenciador
from componentes.menu_lateral_widget import MenuAdmin
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
import pygame



def criar_player():
   pass

from modulos.banco.database import testar_conexao
from modulos.recursos.conexao_utils import conexao_valida  # aqui conexao_valida  grifado em vermelho
from modulos.componentes.barra_som_widget import criar_barra_som


from modulos.recursos import dados_compartilhados as dc


#from modulos.abas.aba_inativos import montar_aba_inativos
from modulos.recursos.dados_compartilhados import UsuarioLogado



gerenciador.registrar_aba("cadastro", montar_aba_cadastro)
gerenciador.registrar_aba("financeiro", montar_aba_financeiro)
gerenciador.registrar_aba("clientes", montar_aba_clientes)
gerenciador.registrar_aba("editor_codigo", AbaEditorCodigo)
gerenciador.registrar_aba("clima", montar_aba_clima)
gerenciador.registrar_aba("config", montar_aba_config)
gerenciador.registrar_aba("relatorios", montar_aba_relatorios)
gerenciador.registrar_aba("itau", criar_aba_itau)
gerenciador.registrar_aba("dados_compartilhados", montar_dados_compartilhados)
gerenciador.registrar_aba("inativos", montar_aba_inativos)
gerenciador.registrar_aba("consulta", montar_aba_consulta)
#gerenciador.registrar_aba("teste", montar_aba_teste)


def iniciar_janela_principal(usuario_logado):
    print("Perfil do usuário:", usuario_logado.perfil)
    janela = tk.Toplevel()
    dc.inicializar_variaveis(janela)
    janela.title("Sistema Principal")
    janela.geometry("1960x968")

    # Frame principal
    frame_principal = tk.Frame(janela)
    frame_principal.grid(row=1, column=0, sticky="nsew")
    frame_principal.grid_rowconfigure(0, weight=1)
    frame_principal.grid_columnconfigure(0, weight=0)  # menu
    frame_principal.grid_columnconfigure(1, weight=1)  # contaúdo
    frame_principal.grid_columnconfigure(0, minsize=200)

    # Notebook na coluna 1 (conteúdo)
    notebook = ttk.Notebook(frame_principal)
    notebook.grid(row=0, column=1, sticky="nsew")

    print("Perfil do usuário:", usuario_logado.perfil)

    perfil = usuario_logado.perfil.lower()  # normaliza para minúsculo
    if perfil in ("admin", "funcionario", "usuario", "administrador"):
        menu_lateral = MenuAdmin(
            master=frame_principal,
            perfil_usuario=perfil,
            gerenciador_abas=gerenciador,
            notebook=notebook
        )
        menu_lateral.config(width=200, bg="lightblue")
        menu_lateral.grid(row=0, column=0, sticky="ns")
        print(f"✅ MenuLateral criado para perfil: {perfil}")

        # Barra superior
        frame_topo = tk.Frame(janela)
        frame_topo.grid(row=0, column=0, sticky="ew")
        barra_som = criar_barra_som(frame_topo)
        barra_som.grid(row=0, column=0, sticky="ew", padx=10, pady=5)

        label = tk.Label(frame_topo, text=f"Bem-vindo, Ao Sistema de Controle Ipojucão, {usuario_logado.nome}!", font=("Segoe UI", 30, "bold"))
        label.grid(row=0, column=1, sticky="e", padx=10)

        # Rodape
        rodape_imagem(janela)

        # Música ao abrir
        caminho_som = os.path.join("sons", "PET_SHOP_IPOJUCÃO.mp3")  # ou WAV
        if os.path.exists(caminho_som):
            pygame.mixer.init()
            pygame.mixer.music.load(caminho_som)
            pygame.mixer.music.play()
        else:
            print("⚠️ Música não encontrada:", caminho_som)

        # Só retorna depois de montar tudo
        return janela

    # toca música ao abrir
    # caminho_som = os.path.join("sons", "PET_SHOP_IPOJUCÃO.mp3")
    # if os.path.exists(caminho_som):
    #     pygame.mixer.init()
    #     pygame.mixer.music.load(caminho_som)
    #     pygame.mixer.music.play()
    # else:
    #     print("⚠️ Música não encontrada:", caminho_som)
    # return janela



    # Layout da janela
    # janela.grid_rowconfigure(1, weight=1)
    # janela.grid_columnconfigure(0, weight=0)








    # if usuario_logado.perfil in ("admin", "funcionario", "usuario", "administrador"):
    #     menu_lateral = MenuAdmin(
    #         master=frame_principal,
    #         perfil_usuario=usuario_logado.perfil,
    #         gerenciador_abas=gerenciador,
    #         notebook=notebook
    #     )
    #     menu_lateral.config(width=200, bg="lightblue")
    #     menu_lateral.grid(row=0, column=0, sticky="ns")
    #     #frame_principal.grid_columnconfigure(0, minsize=200)
    #     print(f"✅ MenuLateral criado para perfil: {usuario_logado.perfil}")

    # Topo com barra de som
    frame_topo = tk.Frame(janela)
    frame_topo.grid(row=0, column=0, sticky="ew")
    frame_topo.grid_columnconfigure(0, weight=1)
    barra_som = criar_barra_som(frame_topo)
    barra_som.grid(row=0, column=0, sticky="ew", padx=10, pady=5)

    label = tk.Label(frame_topo, text=f"Bem-vindo, ao Sistema de Controle Ipojucão, {usuario_logado.nome}!", font=("Segoe UI", 30, "bold"))
    label.grid(row=0, column=1, sticky="e", padx=10)

    # Ajustes visuais
    frame_principal.config(borderwidth=2, relief="solid")

    # Área de conteúdo

    # conteudo = tk.Frame(frame_principal, bg="white")
    # conteudo.grid(row=0, column=1, sticky="nsew")
    # conteudo.grid_rowconfigure(0, weight=1)
    # conteudo.grid_columnconfigure(0, weight=1)

    # Ajustes visuais
    # frame_principal.config(borderwidth=2, relief="solid")
    # conteudo.config(borderwidth=2, relief="solid")

    # def rodape_imagem(frame_pai):
    #     caminho_img = os.path.join("imagensipojucao", "rodape", "footer.png")
    #     if os.path.exists(caminho_img):
    #         img = Image.open(caminho_img).resize((1000, 80))
    #         img_tk = ImageTk.PhotoImage(img)
    #         rodape = tk.Label(frame_pai, image=img_tk)
    #         rodape.image = img_tk  # mantém referência da imagem
    #
    #         # Posiciona no final da grid
    #         rodape.grid(row=10, column=0, columnspan=5, sticky="ew")  # usa row "alta" para evitar conflito
    #     else:
    #         print(" ⚠️ Imagem do rodapé não encontrada.")
    #
    # return janela


def rodape_imagem(frame_pai):
    caminho_img = os.path.join("imagensipojucao", "footer.png")
    if os.path.exists(caminho_img):
        img = Image.open(caminho_img).resize((500, 200))
        img_tk = ImageTk.PhotoImage(img)
        rodape = tk.Label(frame_pai, image=img_tk)
        rodape.image = img_tk  # mantém referência
        rodape.grid(row=10, column=0, columnspan=5, sticky="ew")
    else:
        print("⚠️ Imagem do rodapé não encontrada:", caminho_img)

    # Menu lateral (se for admin)


# Classes auxiliares fora da função

# class GerenciadorAbas:
#     def __init__(self):
#         self.abas_registradas = {}
#
#     def registrar_aba(self, nome, funcao_montagem):
#         self.abas_registradas[nome] = funcao_montagem
#
#     def trocar_aba(self, nome_aba, notebook):
#         if nome_aba in self.abas_registradas:
#             nova_aba = ttk.Frame(notebook)
#             self.abas_registradas[nome_aba](notebook, nova_aba)
#             notebook.add(nova_aba, text=nome_aba.capitalize())
#             notebook.select(nova_aba)
#             notebook.update_idletasks()
#
#         print(f"Trocando para a aba: {nome_aba}")
#
# class MenuLateral(tk.Frame):
#     def __init__(self, master, perfil_usuario, gerenciador_abas, notebook):
#         super().__init__(master, bg="lightblue", width=200)
#         self.gerenciador = gerenciador_abas
#         self.perfil = perfil_usuario
#         self.notebook = notebook

        # Teste visual: borda do menu

        #self.config(borderwidth=2, relief="solid", bg="lightblue")

       # print(f"✅ MenuLateral criado para perfil: {self.perfil}")

        # Garante que o menu ocupe espaço vertical

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        #
        # self.montar_menu()
        # self.config(borderwidth=1, relief="solid")

# def montar_aba_teste(notebook, frame):
#     label = tk.Label(frame, text="Conteúdo da aba de teste", font=("Arial", 16))
#     label.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
#     frame.grid_rowconfigure(0, weight=1)
#     frame.grid_columnconfigure(0, weight=1)




# frame_principal.grid_columnconfigure(0, minsize=200)
# print(f"Perfil logado: {usuario_logado.perfil}")








    def montar_menu(self):
        # Agrupamento por categorias com ícones
        grupos = {
            "📋 Cadastro": ["cadastro", "clientes"],
            "🔍 Consultas": ["consulta", "relatorios", "dados_compartilhados"],
            "⚙️ Configurações": ["config", "clima", "itau"],
            "💻 Ferramentas": ["financeiro"]  # editor_codigo será adicionado abaixo se for admin
        }

        if self.perfil == "admin":
            grupos["💻 Ferramentas"].append("editor_codigo")
        print(f"Montando menu para o perfil: {self.perfil}")

        linha = 0
        for titulo, abas in grupos.items():
            # Separador visual
            separador = tk.Label(
                self,
                text=titulo,
                font=("Segoe UI", 30, "bold"),
                bg="#dcdcdc",
                anchor="w"
            )
            separador.grid(row=linha, column=0, sticky="ew", padx=5, pady=(10, 2))
            linha += 1

            for nome_aba in abas:
                print(f"Criando botão para aba: {nome_aba}")
                btn = tk.Button(
                    self,
                    text=f"• {nome_aba.capitalize()}",
                    command=lambda aba=nome_aba: self.gerenciador.trocar_aba(aba, self.notebook),
                    anchor="w",
                    bg="#ffffff",
                    relief="solid",
                    borderwidth=1
                )
                btn.grid(row=linha, column=0, sticky="ew", padx=15, pady=2)
                linha += 1
        # Expande a coluna para ocupar toda a largura disponível
        self.grid_columnconfigure(0, weight=1)




def verificar_conexao():
    testar_conexao()
    if conexao_valida():
        print("✅ Conexão OK")
    else:
        print("❌ Erro na conexão")

verificar_conexao()





def caminho_imagem(nome):
    base = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base, "imagensipojucao", "imagens", nome)

def criar_player_som(janela):
        #from modulos.componentes.barra_som_widget import criar_barra_som  # exemplo
        player = criar_player(janela)
        return player



