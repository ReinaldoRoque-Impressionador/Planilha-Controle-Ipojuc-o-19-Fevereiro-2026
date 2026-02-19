import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os


from modulos.abas.editor_codigo import AbaEditorCodigo  # Certifique-se de que esse caminho está correto


from modulos.recursos.utilitarios import caminho_arquivo
from modulos.recursos.dados_compartilhados import usuarios, som_global_ativo
from modulos.recursos.som import tocar_som, tocar_som_curto, parar_som
#importações após reestruturação do projeto abaixo
#específicamente para a aba_login_fusion

#from modulos.banco.db_models import Usuario
from modulos.banco.database import Cliente, Tutor, Usuario, Pagamento, Pets
from modulos.banco.database import SessionLocal, Base, inicializar_banco
from modulos.banco.database import engine
from modulos.recursos.utils_gerais import validar_email
from modulos.abas.login_config import verificar_credenciais
from modulos.recursos.som import tocar_som, tocar_som_curto, parar_som
#from abas.ferramentas.audio import tocar_som, tocar_som_curto, parar_som

from modulos.recursos.aba_itau import criar_aba_itau
from modulos.abas.editor_codigo import AbaEditorCodigo
from modulos.recursos import dados_compartilhados as dc
#>>>>>>>>>>

def alterar_senha(email, senha_atual, nova_senha):
    db = SessionLocal()
    usuario = db.query(Usuario).filter_by(email=email, senha=senha_atual).first()
    if usuario:
        usuario.senha = nova_senha
        db.commit()
        db.close()
        return True
    else:
        db.close()
        return False
#XXXXXXXXXXXXX
# def abrir_tela_alterar_senha(janela_pai):
#     janela_senha = tk.Toplevel(janela_pai)
#     janela_senha.title("Alterar Senha")
#     janela_senha.geometry("400x300")

#XXXXXXXXXXXXXXX

def abrir_tela_alterar_senha(janela_pai):
    janela_senha = tk.Toplevel(janela_pai)
    janela_senha.title("Alterar Senha")
    janela_senha.geometry("400x300")

        # Configuração de layout
    for i in range(4):
        janela_senha.grid_rowconfigure(i, weight=1)
    janela_senha.grid_columnconfigure(0, weight=1)

        # Email
    tk.Label(janela_senha, text="Email:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    entrada_email = tk.Entry(janela_senha, width=40)
    entrada_email.grid(row=0, column=1, padx=10, pady=5)

        # Senha atual
    tk.Label(janela_senha, text="Senha atual:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    entrada_senha_atual = tk.Entry(janela_senha, show="*", width=40)
    entrada_senha_atual.grid(row=1, column=1, padx=10, pady=5)

        # Nova senha
    tk.Label(janela_senha, text="Nova senha:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    entrada_nova_senha = tk.Entry(janela_senha, show="*", width=40)
    entrada_nova_senha.grid(row=2, column=1, padx=10, pady=5)

        # Botão de confirmação
    def confirmar_alteracao():
        email = entrada_email.get().strip()
        senha_atual = entrada_senha_atual.get().strip()
        nova_senha = entrada_nova_senha.get().strip()

        if alterar_senha(email, senha_atual, nova_senha):
            messagebox.showinfo("Sucesso", "Senha alterada com sucesso!")
            janela_senha.destroy()
        else:
            messagebox.showerror("Erro", "Email ou senha atual incorretos.")

    btn_confirmar = tk.Button(janela_senha, text="Confirmar", command=confirmar_alteracao)
    btn_confirmar.grid(row=3, column=0, columnspan=2, pady=10)

#XXXXXXXXXXXX
    # tk.Label(janela_senha, text="Email:").pack(pady=5)
    # entrada_email = tk.Entry(janela_senha, width=40)
    # entrada_email.pack()
    #
    # tk.Label(janela_senha, text="Senha atual:").pack(pady=5)
    # entrada_senha_atual = tk.Entry(janela_senha, show="*", width=40)
    # entrada_senha_atual.pack()
    #
    # tk.Label(janela_senha, text="Nova senha:").pack(pady=5)
    # entrada_nova_senha = tk.Entry(janela_senha, show="*", width=40)
    # entrada_nova_senha.pack()

    def confirmar_alteracao():
        email = entrada_email.get().strip()
        senha_atual = entrada_senha_atual.get().strip()
        nova_senha = entrada_nova_senha.get().strip()

        if alterar_senha(email, senha_atual, nova_senha):
            messagebox.showinfo("Sucesso", "Senha alterada com sucesso!")
            janela_senha.destroy()
        else:
            messagebox.showerror("Erro", "Email ou senha atual incorretos.")

    tk.Button(janela_senha, text="Confirmar", command=confirmar_alteracao).grid(row=3, column=0, columnspan=2, pady=5, sticky="ew")

#<<<<<<<<<



# def menu_lateral(container):
#     from modulos.controladores.fluxo_abas import fluxo_abas
#     fluxo_abas(container)
#importações após reestruturação do projeto acima
#específicamente para a aba_login_fusion

try:
    from mascote import mostrar_mascote_expressivo
except ImportError:
    mostrar_mascote_expressivo = lambda *args: None  # Fallback

# No início do arquivo, após as importações
def chamar_mascote_login(janela, erro_senha=False):
    expressao = "triste" if erro_senha else "feliz"
def mostrar_mascote_expressivo(janela, expressao=None):
    print(f"Expressão recebida: {expressao}")


# def caminho_arquivo(nome, subpasta=None):
#     raiz = os.path.dirname(os.path.dirname(__file__))  # volta para raiz do projeto
#     return os.path.join(raiz, subpasta if subpasta else "", nome)

def caminho_arquivo(nome, subpasta=None):
    raiz = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    # sobe 3 níveis em vez de 2
    return os.path.join(raiz, subpasta if subpasta else "", nome)

print(caminho_arquivo("olho_aberto.png", subpasta="imagensipojucao/imagensipojucao"))

# def caminho_expressao(expressao):
#     raiz = os.path.dirname(os.path.dirname(__file__))  # raiz do projeto
#     caminho = os.path.join(raiz, "imagensipojucao", "imagens", f"mascote_{expressao}.png")
#     return caminho if os.path.exists(caminho) else None

def caminho_expressao(expressao):
    base = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base, "imagensipojucao", "expressoes", f"mascote_{expressao}.png")

    caminho_img = caminho_expressao("feliz")
    print(caminho_img, os.path.exists(caminho_img))



# Lista de usuários desenvolvedores
desenvolvedores = {
    "cebous@hotmail.com.br": {"senha": "1234", "nome": "Raphael"},
    "roquereinaldo@gmail.com": {"senha": "975624asa", "nome": "Reinaldo"}
}

def autenticar_usuario(email, senha):
    if email in desenvolvedores and desenvolvedores[email]["senha"] == senha:
        return desenvolvedores[email]["nome"], desenvolvedores[email]["perfil"]


    return None, None



def tentar_login():
    global entrada_email, entrada_senha
    email = entrada_email.get().strip()
    senha = entrada_senha.get().strip()

    if not email or not senha:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")
        return

        nome = autenticar_usuario(email, senha)
        if nome:
            messagebox.showinfo("Bem-vindo", f"Acesso liberado para {nome}")
            janela.destroy()
            if ao_logar_callback:
                ao_logar_callback(email, nome)

            # Acesso exclusivo para desenvolvedores
            if email in desenvolvedores:
                AbaEditorCodigo(janela).grid(row=2, column=0, columnspan=2, sticky="nsew")
                criar_aba_itau(janela)
        else:
            messagebox.showerror("Erro", "Credenciais inválidas ou acesso não autorizado.")

# Exemplo de uso: abrir editor apenas para desenvolvedores
def iniciar_editor(email, nome):
    root = tk.Tk()
    root.title(f"Editor de Código - {nome}")
    root.geometry("800x600")

    editor = AbaEditorCodigo(root)
    editor.grid(row=0, column=0, sticky="nsew")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()




def criar_login(ao_logar_callback):
    janela_login = tk.Toplevel()
    janela_login.title("Login Ipojucão")
    janela_login.geometry("800x500")
    janela_login.resizable(False, False)

    chamar_mascote_login(janela_login, erro_senha=True)
    chamar_mascote_login(janela_login, erro_senha=False)

    tk.Button(janela_login, text="Alterar Senha", command=lambda: abrir_tela_alterar_senha(janela_login)).grid(row=5, column=0, columnspan=2, pady=5, sticky="ew")

    # 🔊 Som de fundo
    intro_path = caminho_arquivo("bouncy_pet_intro.mp3", subpasta="sons")
    if som_global_ativo and os.path.exists(intro_path):
        #tocar_musica("sons/intro_path")
        tocar_som(intro_path)
        tocar_som_curto(caminho_arquivo("clique.mp3", subpasta="sons"))
    print("Login carregado")
#    🖼️ Fundo com imagem
    fundo_path = caminho_arquivo("login_fundo.png", subpasta="imagens")
    if os.path.exists(fundo_path):
        fundo_img = Image.open(fundo_path).resize((800, 500))
        bg = ImageTk.PhotoImage(fundo_img)
        fundo = tk.Label(janela_login, image=bg)
        fundo.image = bg
        fundo.place(relwidth=1, relheight=1)

    # 📦 Container central
    frame = tk.Frame(janela_login, bg="#ffffff", bd=2)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # 📧 Email
    tk.Label(frame, text="Email:", bg="white").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    email_entry = tk.Entry(frame, width=30)
    email_entry.grid(row=0, column=1, pady=10)

    # 🔒 Senha
    tk.Label(frame, text="Senha:", bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    senha_entry = tk.Entry(frame, width=30, show="*")
    senha_entry.grid(row=1, column=1, pady=10)

    # 👁️ Alternância de senha
    mostrar_senha = tk.BooleanVar(value=False)

    def alternar_senha():
        senha_entry.config(show="" if mostrar_senha.get() else "*")
        novo_icone = olho_aberto_img if mostrar_senha.get() else olho_fechado_img
        mostrar_checkbox.config(image=novo_icone)
        mostrar_checkbox.image = novo_icone
        if som_global_ativo:
            tocar_som_curto(caminho_arquivo("clique.mp3", subpasta="sons"))
            #tocar_som_curto("sons/clique.mp3")

    olho_aberto_path = caminho_arquivo("olho_aberto.png", subpasta="imagensipojucao/imagensipojucao")
    olho_fechado_path = caminho_arquivo("olho_fechado.png", subpasta="imagensipojucao/imagensipojucao")
    print("Caminho olho aberto:", olho_aberto_path, os.path.exists(olho_aberto_path))
    print("Caminho olho fechado:", olho_fechado_path, os.path.exists(olho_fechado_path))
    olho_aberto_img = ImageTk.PhotoImage(Image.open(olho_aberto_path).resize((30, 30))) if os.path.exists(olho_aberto_path) else None
    olho_fechado_img = ImageTk.PhotoImage(Image.open(olho_fechado_path).resize((30, 30))) if os.path.exists(olho_fechado_path) else None

    mostrar_checkbox = tk.Checkbutton(frame, variable=mostrar_senha, command=alternar_senha,
                                      image=olho_fechado_img, bg="white")
    mostrar_checkbox.grid(row=2, column=1, sticky="w")

    # 🔐 Autenticação
    def autenticar():
        try:
            email = email_entry.get().strip()
            senha = senha_entry.get().strip()
            user = usuarios.get(email)
            if user and user["senha"] == senha:
                parar_som()
                global usuario_atual
                usuario_atual = email
                mostrar_mascote_expressivo(janela_login, "feliz")
                # messagebox.showinfo("Bem-vindo", f"Olá, {user['nome']}!\nPerfil: {user['perfil']}")
                janela_login.destroy()
                ao_logar_callback(user["nome"], user["perfil"])
            else:
                mostrar_mascote_expressivo(janela_login, "negativo")
                messagebox.showerror("Acesso negado", "Email ou senha inválidos.")

        except Exception as e:
            print(f"Erro na autenticação: {e}")
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")


    tk.Button(frame, text="Entrar", command=autenticar, bg="#4CAF50", fg="white").grid(row=3, columnspan=2, pady=20)

#🧩 Parte 2 – Cadastro e exclusão de usuários
def cadastro_usuario(janela_principal):
    janela_cadastro = tk.Toplevel(janela_principal)
    janela_cadastro.title("Novo Usuário")
    janela_cadastro.geometry("400x300")

    labels = ["Nome:", "Email:", "Senha:", "Perfil:"]
    entries = {}
    for i, texto in enumerate(labels[:3]):
        tk.Label(janela_cadastro, text=texto).grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entry = tk.Entry(janela_cadastro, show="*" if texto == "Senha:" else "")
        entry.grid(row=i, column=1, padx=10)
        entries[texto] = entry

    perfil_var = tk.StringVar(value="Funcionário")
    tk.Label(janela_cadastro, text="Perfil:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    perfil_menu = tk.OptionMenu(janela_cadastro, perfil_var, "Administrador", "Funcionário")
    perfil_menu.grid(row=3, column=1)

    def salvar():
        nome = entries["Nome:"].get().strip()
        email = entries["Email:"].get().strip()
        senha = entries["Senha:"].get().strip()
        perfil = perfil_var.get()
        if not nome or not email or not senha:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")
            return
        if email in usuarios:
            messagebox.showerror("Duplicado", "Este email já está cadastrado.")
            return
        usuarios[email] = {"nome": nome, "senha": senha, "perfil": perfil}
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        janela_cadastro.destroy()

    tk.Button(janela_cadastro, text="Salvar", command=salvar, bg="#4CAF50", fg="white").grid(row=4, columnspan=2, pady=20)


def excluir_usuario(janela_principal):
    janela_excluir = tk.Toplevel(janela_principal)
    janela_excluir.title("Excluir Usuário")
    janela_excluir.geometry("400x200")

    tk.Label(janela_excluir, text="Email do usuário a excluir:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    email_entry = tk.Entry(janela_excluir)
    email_entry.grid(row=0, column=1)

    def excluir():
        email = email_entry.get().strip()
        if email in usuarios:
            confirmacao = messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir {email}?")
            if confirmacao:
                del usuarios[email]
                messagebox.showinfo("Excluído", "Usuário removido com sucesso.")
                janela_excluir.destroy()
        else:
            messagebox.showerror("Não encontrado", "Usuário não localizado.")

    tk.Button(janela_excluir, text="Excluir", command=excluir, bg="#f44336", fg="white").grid(row=1, columnspan=2, pady=20)

#🧩 Parte 3 – Tela de boas-vindas e acesso ao painel
def abrir_boas_vindas():
    janela_boas_vindas = tk.Toplevel()
    janela_boas_vindas.title("Ipojucão • Bem-vindo!")
    janela_boas_vindas.geometry("500x300")

    frame = tk.Frame(janela_boas_vindas)
    frame.grid(row=0, column=0, padx=30, pady=30)

    tk.Label(frame, text="Menu principal", font=("Segoe UI", 16)).grid(row=0, column=0, columnspan=2, pady=10)

    btn_acessar = tk.Button(
        frame,
        text="📊 Acessar painel de administração",
        bg="#4CAF50",
        fg="white",
        font=("Segoe UI", 12),
        command=lambda: [janela_boas_vindas.destroy(), abrir_janela_principal("Reinaldo", "Administrador")]
    )
    btn_acessar.grid(row=1, column=0, columnspan=2, pady=10)

    btn_sair = tk.Button(
        frame,
        text="❌ Sair do sistema",
        bg="#f44336",
        fg="white",
        font=("Segoe UI", 12),
        command=janela_boas_vindas.destroy
    )
    btn_sair.grid(row=2, column=0, columnspan=2, pady=10)

def rodape_imagem(frame_pai):
    caminho_img = os.path.join("imagensipojucao", "rodape", "footer.png")
    if os.path.exists(caminho_img):
        img = Image.open(caminho_img).resize((1000, 80))
        img_tk = ImageTk.PhotoImage(img)
        rodape = tk.Label(frame_pai, image=img_tk)
        rodape.image = img_tk  # mantém referência da imagem

        # Posiciona no final da grid
        rodape.grid(row=2, column=0, columnspan=0, sticky="ew")  # usa row "alta" para evitar conflito
    else:
        print("Imagem do rodapé não encontrada.")



print("✅ Usando aba_login_fusion da pasta MODULOS")

# def barra_audio(frame_pai):
#     barra = tk.Frame(frame_pai)
#     barra.grid(row=999, column=0, columnspan=999, pady=10)

def montar_aba_login_fusion(master):
    from modulos.componentes.barra_som_widget import criar_barra_som

    frame_login_fusion = tk.Frame(master)
    frame_login_fusion.grid(row=0, column=0, sticky="nsew")

    master.grid_rowconfigure(0, weight=1)
    master.grid_columnconfigure(0, weight=1)

    barra_audio(frame_login_fusion)


    # ▶️ Botão para tocar trilha sonora longa
    # btn_trilha = ttk.Button(barra_audio, text="🎶 Tocar Trilha", command=lambda: tocar_som("sons/abertura.mp3"))
    # btn_trilha.grid(row=0, column=0, padx=5)

    # 🔈 Botão para tocar som curto (efeito)
    btn_efeito = ttk.Button(barra_audio, text="🔔 Efeito Curto", command=lambda: tocar_som_curto("sons/sucesso.mp3"))
    btn_efeito.grid(row=0, column=1, padx=5)

    # ⏹️ Botão para parar a trilha sonora
    btn_parar = ttk.Button(barra_audio, text="🛑 Parar Música", command=parar_som)
    btn_parar.grid(row=0, column=2, padx=5)


# def iniciar_interface_login(frame_aba_login_fusion):
#     barra_audio(frame_aba_login_fusion)
























