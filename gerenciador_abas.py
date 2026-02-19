# modulos/controladores/gerenciador_abas.py
import tkinter as tk
from tkinter import ttk
from modulos.interface.aba_cadastro import montar_aba_cadastro
from modulos.abas.aba_clientes import montar_aba_clientes


# class GerenciadorAbas:
#     def __init__(self):
#         self.abas = {}
#
#     def registrar_aba(self, nome, funcao):
#         self.abas[nome] = funcao
#
#     def trocar_aba(self, nome_aba, master):
#         print(f"🔄 Trocando para aba: {nome_aba}")
#         if nome_aba in self.abas:
#             frame = ttk.Frame(master)
#             try:
#                 self.abas[nome_aba](master, frame)
#                 frame.grid(row=0, column=2, sticky="nsew")
#                 return frame
#             except Exception as e:
#                 print(f"❌ Erro ao abrir aba '{nome_aba}': {e}")
#                 return None
#         else:
#             print(f"❌ Aba '{nome_aba}' não reconhecida.")
#             return None

import tkinter as tk
from tkinter import ttk

class GerenciadorAbas:
    def __init__(self):
        # dicionário que guarda as abas registradas
        # gerenciador = GerenciadorAbas()

        self.abas = {}

    def registrar_aba(self, nome, funcao_montagem):
        """Registra uma aba no gerenciador"""
        self.abas[nome] = funcao_montagem
        print(f"✅ Aba registrada: {nome}")

    # def trocar_aba(self, nome_aba, notebook):
    #     """Troca para a aba especificada"""
    #     if nome_aba in self.abas:
    #         print(f"🔄 Trocando para a aba: {nome_aba}")
    #         nova_aba = ttk.Frame(notebook)
    #         # chama a função de montagem passando notebook e frame
    #         self.abas[nome_aba](notebook, nova_aba)
    #         notebook.add(nova_aba, text=nome_aba.capitalize())
    #         notebook.select(nova_aba)
    #         notebook.update_idletasks()
    #         return nova_aba
    #     else:
    #         print(f"⚠️ Aba '{nome_aba}' não encontrada no gerenciador.")
    #         return None



    # def trocar_aba(self, nome, notebook):
    #     if nome in self.abas:
    #         conteudo = self.abas[nome](notebook)  # chama função registrada
    #         notebook.add(conteudo, text=nome.capitalize())
    #         notebook.select(notebook.index("end") - 1)
    #         return conteudo
    #     else:
    #         print(f"Aba {nome} não encontrada")
    #         return None

    def trocar_aba(self, nome_aba, notebook):
        print(f"🔄 Trocando para a aba: {nome_aba}")
        if nome_aba in self.abas:
            frame = self.abas[nome_aba](notebook)  # chama função com 1 argumento
            notebook.add(frame, text=nome_aba.capitalize())
            notebook.select(notebook.index("end") - 1)
            return frame
        else:
            print(f"Aba {nome_aba} não encontrada")
            return None

# Instância global do gerenciador
gerenciador = GerenciadorAbas()

gerenciador.registrar_aba("cadastro", montar_aba_cadastro)
gerenciador.registrar_aba("clientes", montar_aba_clientes)

    # def trocar_aba(self, nome_aba, master):
    #     try:
    #         return self.abas[nome_aba](master, inner_frame)
    #     except KeyError:
    #         print(f"❌ Aba '{nome_aba}' não reconhecida.")
    #         return None
    # def trocar_aba(self, nome_aba, master):
    #     if nome_aba in self .abas:
    #         frame = ttk.Frame(master)
    #         self.abas[nome_aba](master, frame)
    #         frame.grid(row=0, column=2, sticky="nsew")
    #     else
    #         print(print(f"❌ Aba '{nome_aba}' não reconhecida."))
    #
    #     print(f"🔄 Trocando para aba: {nome_aba}")
    #     try:
    #         return self.abas[nome_aba](master)  # ✅ passa apenas master
    #     except KeyError:
    #         print(f"❌ Aba '{nome_aba}' não reconhecida.")
    #         return None
    #     except Exception as e:
    #         print(f"❌ Erro ao abrir aba '{nome_aba}': {e}")
    #         return None



# Instância global (opcional)
#gerenciador = GerenciadorAbas()

# def trocar_aba(nome_aba, master):
#     return gerenciador.trocar_aba(nome_aba, master)

# def trocar_aba(self, nome_aba, master):
#     print(f"🔄 Trocando para aba: {nome_aba}")
#     try:
#         return self.abas[nome_aba](master)
#     except KeyError:
#         print(f"❌ Aba '{nome_aba}' não reconhecida.")
#         return None
#     except Exception as e:
#         print(f"❌ Erro ao abrir aba '{nome_aba}': {e}")
#         return None