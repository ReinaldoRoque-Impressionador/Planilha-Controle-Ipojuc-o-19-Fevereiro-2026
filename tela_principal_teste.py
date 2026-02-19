import tkinter as tk
from tkinter import ttk

class MenuLateral(tk.Frame):
    def __init__(self, master, notebook):
        super().__init__(master, bg="lightblue", width=200)
        self.notebook = notebook
        self.grid_columnconfigure(0, weight=1)
        self._criar_botoes()

    def _criar_botoes(self):
        abas = ["cadastro", "clientes", "financeiro", "relatorios"]
        for i, nome in enumerate(abas):
            btn = tk.Button(
                self,
                text=f"• {nome.capitalize()}",
                command=lambda aba=nome: self._trocar_aba(aba),
                anchor="w",
                bg="#ffffff",
                relief="solid"
            )
            btn.grid(row=i, column=0, sticky="ew", padx=10, pady=5)

    def _trocar_aba(self, nome):
        nova_aba = ttk.Frame(self.notebook)
        label = tk.Label(nova_aba, text=f"Conteúdo da aba: {nome}", font=("Arial", 16))
        label.pack(padx=20, pady=20)
        self.notebook.add(nova_aba, text=nome.capitalize())
        self.notebook.select(nova_aba)

def iniciar_teste():
    janela = tk.Tk()
    janela.title("Teste Menu Lateral")
    janela.geometry("800x600")

    frame_principal = tk.Frame(janela)
    frame_principal.grid(row=0, column=0, sticky="nsew")
    frame_principal.grid_columnconfigure(0, minsize=200)  # largura do menu
    frame_principal.grid_columnconfigure(1, weight=1)
    frame_principal.grid_rowconfigure(0, weight=1)

    # Conteúdo principal
    conteudo = tk.Frame(frame_principal, bg="white")
    conteudo.grid(row=0, column=1, sticky="nsew")
    conteudo.grid_rowconfigure(0, weight=1)
    conteudo.grid_columnconfigure(0, weight=1)

    notebook = ttk.Notebook(conteudo)
    notebook.grid(row=0, column=0, sticky="nsew")

    # Menu lateral
    menu = MenuLateral(master=frame_principal, notebook=notebook)
    menu.grid(row=0, column=0, sticky="ns")

    janela.mainloop()

iniciar_teste()