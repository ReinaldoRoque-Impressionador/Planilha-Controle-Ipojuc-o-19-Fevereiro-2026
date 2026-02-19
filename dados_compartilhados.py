import tkinter as tk
from tkinter import ttk

from modulos.banco.database import SessionLocal
#from modulos.banco.db_models import DadosCompartilhados
from modulos.banco.database import Cliente, Tutor, Usuario, Pagamento, Pets
from modulos.banco.database import DadosCompartilhados

from modulos.banco.database import Pets

from tkinter import messagebox
from modulos.recursos.player_som import tocar_som
import json
import os
from openpyxl import Workbook


# Lista global de pets cadastrados
todos_os_pets_cadastrados = []

def buscar_dados_compartilhados():
    session = SessionLocal()
    try:
        return session.query(DadosCompartilhados).all()
    finally:
        session.close()

pacotes_servicos = {}
print(json.dumps(pacotes_servicos, indent=2, ensure_ascii=False))
# modulos/abas/dados_compartilhados.py

usuarios = []
config_global = {}

def carregar_dados():
    # Exemplo de função
    print("Dados carregados")


som_global_ativo = {
    "ativo": True
}
usuario_atual = None

variaveis = {}  # ✅ Agora está no escopo global
servicos_disponiveis = []
variaveis_servicos = {}
labels_valores = {}
entrys_desconto_individual = {}
descontos_por_servico = {}
desconto_total = {"tipo": None, "valor": 0.0}
calendario_servico = None
label_resultado = None
entry_desconto_fixo = None
entry_desconto_percentual = None
pacotes_servicos = {}  # se existir
dados_pet = {}         # se existir

# 🗓️ Elementos de interface (inicializados depois)
calendario_servico = None
label_resultado = None
entry_desconto_fixo = None
entry_desconto_percentual = None



def inicializar_variaveis(master):
    variaveis["var_pagamento"] = tk.StringVar(master=master)
    variaveis["var_status_pagamento"] = tk.StringVar(master)
    variaveis["var_porte"] = tk.StringVar(master=master)
    variaveis["var_raca"] = tk.StringVar(master=master)
    variaveis["var_tipo_pacote"] = tk.StringVar(master=master, value="Avulso")

def get_variaveis():
    return variaveis

def get_contexto_financeiro():
    return {
        "servicos_disponiveis": servicos_disponiveis,
        "variaveis_servicos": variaveis_servicos,
        "labels_valores": labels_valores,
        "entrys_desconto_individual": entrys_desconto_individual,
        "descontos_por_servico": descontos_por_servico,
        "desconto_total": desconto_total,
        "calendario_servico": calendario_servico,
        "label_resultado": label_resultado,
        "entry_desconto_fixo": entry_desconto_fixo,
    }

# Dicionário global de variáveis
variaveis = {}



def inicializar_variaveis(master):
    variaveis["var_nome"] = tk.StringVar(master)
    variaveis["var_cpf_tutor"] = tk.StringVar(master)
    variaveis["var_porte"] = tk.StringVar(master)
    variaveis["var_raca"] = tk.StringVar(master)
    variaveis["var_idade_anos"] = tk.StringVar(master)
    variaveis["var_idade_meses"] = tk.StringVar(master)
    variaveis["var_data_cadastro"] = tk.StringVar(master)
    variaveis["var_tutor1"] = tk.StringVar(master)
    variaveis["var_tutor2"] = tk.StringVar(master)
    variaveis["var_logradouro"] = tk.StringVar(master)
    variaveis["var_numero"] = tk.StringVar(master)
    variaveis["var_complemento"] = tk.StringVar(master)
    variaveis["var_tipopelo"] = tk.StringVar(master)
    variaveis["var_pelagem"] = tk.StringVar(master)
    variaveis["var_descricao"] = tk.StringVar(master)

def get_variaveis():
    return variaveis

# def cadastrar_pet():
#     cpf = variaveis["var_cpf_tutor"].get().strip().replace(".", "").replace("-", "")
#     nome = variaveis["var_nome"].get().strip()
#
#     if cpf_ja_cadastrado(cpf):
#         return None  # ou lançar uma exceção, ou retornar uma mensagem
#
#     novo_pet = {
#         "id_pet": len(todos_os_pets_cadastrados) + 1,
#         "cpf_tutor": cpf,
#         "nome": nome
#     }
#
#     todos_os_pets_cadastrados.append(novo_pet)
#     return novo_pet


def salvar_em_arquivo_json():
    caminho = os.path.join("dados", "pets_cadastrados.json")
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(todos_os_pets_cadastrados, f, ensure_ascii=False, indent=4)


from openpyxl import Workbook

def exportar_para_planilha():
    wb = Workbook()
    ws = wb.active
    ws.title = "Pets Cadastrados"

    # Cabeçalhos
    ws.append(["ID", "Nome", "CPF Tutor", "Raça", "Porte", "Idade (anos)", "Idade (meses)"])

    for pet in todos_os_pets_cadastrados:
        dados = pet.get("dados_completos", {})
        ws.append([
            pet["id_pet"],
            pet["nome"],
            pet["cpf_tutor"],
            dados.get("raca", ""),
            dados.get("porte", ""),
            dados.get("idade_anos", ""),
            dados.get("idade_meses", "")
        ])

    caminho = os.path.join("dados", "pets_cadastrados.xlsx")
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    wb.save(caminho)
    #ttk.Button(frame, text="📤 Exportar para Planilha", command=dc.exportar_para_planilha).grid(row=99, column=0, pady=10)

def registrar_pet_completo(dados):
    cpf = dados.get("cpf_tutor", "").strip().replace(".", "").replace("-", "")
    nome = dados.get("nome", "").strip()

    if not cpf or not nome:
        return {"erro": "CPF e nome são obrigatórios."}

    if any(pet["cpf_tutor"] == cpf for pet in todos_os_pets_cadastrados):
        return {"erro": "CPF já cadastrado."}

    novo_pet = {
        "id_pet": len(todos_os_pets_cadastrados) + 1,
        "cpf_tutor": cpf,
        "nome": nome,
        "dados_completos": dados
    }

    todos_os_pets_cadastrados.append(novo_pet)
    salvar_em_arquivo_json()
    exportar_para_planilha()
    return {"sucesso": novo_pet}



def cpf_ja_cadastrado(cpf_digitado):
    #global todos_os_pets_cadastrados
    cpf_digitado = cpf_digitado.strip().replace(".", "").replace("-", "")
    return any(pet["cpf_tutor"] == cpf_digitado for pet in todos_os_pets_cadastrados)


def cadastrar_pet():
    #global todos_os_pets_cadastrados

    cpf = variaveis["var_cpf_tutor"].get().strip().replace(".", "").replace("-", "")
    nome = variaveis["var_nome"].get().strip()

    if not cpf or not nome:
        return {"erro": "CPF e nome são obrigatórios."}

    if cpf_ja_cadastrado(cpf):
        return {"erro": "CPF já cadastrado."}

    novo_pet = {
        "id_pet": len(todos_os_pets_cadastrados) + 1,
        "cpf_tutor": cpf,
        "nome": nome
    }

    todos_os_pets_cadastrados.append(novo_pet)
    return {"sucesso": novo_pet}



# def cpf_ja_cadastrado(cpf_digitado):
#     global todos_os_pets_cadastrados
#     cpf_digitado = cpf_digitado.strip().replace(".", "").replace("-", "")
#     return any(pet["cpf_tutor"] == cpf_digitado for pet in todos_os_pets_cadastrados)

def buscar_por_cpf(cpf_digitado):
    #global todos_os_pets_cadastrados
    cpf_digitado = cpf_digitado.strip().replace(".", "").replace("-", "")
    for pet in todos_os_pets_cadastrados:
        if pet["cpf_tutor"] == cpf_digitado:
            return pet  # retorna o pet completo
    return None

class UsuarioLogado:
    def __init__(self, nome, perfil):
        self.nome = nome
        self.perfil = perfil

def salvar_dados_pet(entradas_tempo, campo_obs, inner_frame):
    from modulos.recursos.som import som_evento, alternar_som

    dados = {
        "nome": dc.variaveis["var_nome"].get(),
        "cpf_tutor": dc.variaveis["var_cpf_tutor"].get(),
        "porte": dc.variaveis["var_porte"].get(),
        "raca": dc.variaveis["var_raca"].get(),
        "idade_anos": dc.variaveis["var_idade_anos"].get(),
        "idade_meses": dc.variaveis["var_idade_meses"].get(),
        "data_cadastro": dc.variaveis["var_data_cadastro"].get(),
        "tutor1": dc.variaveis["var_tutor1"].get(),
        "tutor2": dc.variaveis["var_tutor2"].get(),
        "logradouro": dc.variaveis["var_logradouro"].get(),
        "numero": dc.variaveis["var_numero"].get(),
        "complemento": dc.variaveis["var_complemento"].get(),
        "obs": campo_obs.get("1.0", "end").strip(),
        "tipopelo": dc.variaveis["var_tipopelo"].get(),
        "pelagem": dc.variaveis["var_pelagem"].get(),
        "tempos": {et: entradas_tempo[et].get() for et in entradas_tempo}
    }

    resultado = dc.registrar_pet_completo(dados)

    if "erro" in resultado:
        tk.messagebox.showwarning("Erro", resultado["erro"])
        return

    pet = resultado["sucesso"]
    print("🐾 Pet cadastrado com sucesso:", pet)

    som_evento("cadastro")
    som_evento("salvando.mp3")

    btn_audio = tk.Button(inner_frame, text="🔊 Áudio")
    btn_audio.grid(row=10, column=0, padx=10, pady=5)
    btn_audio.config(command=lambda: alternar_som(btn_audio))

    tk.messagebox.showinfo("Cadastro", f"Pet cadastrado: {pet['nome']} (ID: {pet['id_pet']})")



    # variaveis["var_tipopelo"] = tk.StringVar(master=master)
    #
    # variaveis["var_descricao"] = tk.StringVar(master=master)
    # variaveis["var_data_cadastro"] = tk.StringVar(master)
    # variaveis["var_pelagem"] = tk.StringVar(master)
    # variaveis["var_caracteristicas"] = tk.StringVar(master)
    #

    # Exporta o dicionário


    # dc.var_pagamento
    # dc.var_status_pagamento
    # dc.radiobutton_pix
    # etc.
    # ... outras variáveis



# 📇 BASE DE USUÁRIOS SIMULADA (pode ser salva em JSON depois)
usuarios = {
    "roquereinaldo@gmail.com": {"senha": "975624asa", "nome": "Reinaldo", "perfil": "Administrador"},
    "araujolindi@yahoo.com.br": {"senha": "1234", "nome": "Lindinalva", "perfil": "Administrador"},
    "cebous@hotmail.com.br": {"senha": "1234", "nome": "Raphael", "perfil": "Administrador"},
    "admin@ipojucao.com": {"senha": "1234", "nome": "Marlene", "perfil": "Administrador"},
    "anna_paula@ipojucao.com": {"senha": "1234", "nome": "Anna Paula", "perfil": "Administrador"},
    "wander@ipojucao.com": {"senha": "petpet", "nome": "Wander", "perfil": "Funcionário"},
}



# dados_compartilhados.py

# Aqui você declara suas variáveis e dicionários globais



# 📦 Pacotes de serviços
pacotes_servicos = {
    "Banho": {
        "incluidos": ["Banho", "Secagem", "Corte de Unhas", "Limpeza Ouvido"],
        "bonus_opcoes": ["Laço", "Perfume"]
    },
    "Banho e Tosa": {
        "incluidos": ["Banho", "Tosa", "Secagem", "Corte de Unhas", "Limpeza Ouvido"],
        "bonus_opcoes": ["Laço", "Perfume"]
    },
    "Banho Terapêutico": {
        "incluidos": ["Banho", "Shampoo Terapêutico-Linha Completa Pet-Societ", "Secagem", "Corte de Unhas", "Limpeza Ouvido"],
        "bonus_opcoes": ["Laço", "Perfume"]
    },
    "Banho Terapêutico + Tosa": {
        "incluidos": ["Banho", "Shampoo Terapêutico-Linha Completa Pet-Societ", "Secagem", "Tosa", "Corte de Unhas", "Limpeza Ouvido"],
        "bonus_opcoes": ["Laço", "Perfume"]
    }
}


# 📇
# # 🧮 Variáveis de controle financeiro
# variaveis_servicos = {}
# labels_valores = {}
# entrys_desconto_individual = {}
# descontos_por_servico = {}
# desconto_total = {"tipo": None, "valor": 0.0}
#
# # 🧪 Variáveis dinâmicas (ex: campos de entrada, filtros)
# variaveis = {}
#
# # 📁 Dados exportáveis
# dados_exportados = []
#
# # 🔧 Configurações temporárias
# configuracoes_gerais = {
#     "modo_debug": False,
#     "tema": "claro",
#     "versao": "1.0.0"



# Outras variáveis...

# 🔣 Serviços disponíveis


servicos_disponiveis = [
    "Banho", "Hidratação", "Desembolo", "Remoção de Pelos",
    "Corte de Unhas", "Tosa Higiênica", "Tosa na Máquina",
    "Tosa na Tesoura", "Escovação de Dentes", "Leva e Trás"
]


# 🧮 Estrutura auxiliar para controle financeiro

class DadosCompartilhados:
    def __init__(self):
        self.variaveis_servicos = {}
        self.labels_valores = {}
        self.entrys_desconto_individual = {}
        self.descontos_por_servico = {}
        self.desconto_total = {"tipo": None, "valor": 0.0}

dc = DadosCompartilhados()

# variaveis_servicos = {}
# labels_valores = {}
# entrys_desconto_individual = {}
# descontos_por_servico = {}
# desconto_total = {"tipo": None, "valor": 0.0}



# 🎁 Pacotes contratados

pacotes_servicos = {
    "Quinzenal": {
        "incluidos": ["Banho", "Banho"],
        "bonus_opcoes": ["Hidratação", "Tosa Higiênica"]
    },
    "Mensal": {
        "incluidos": ["Banho"] * 4,
        "bonus_opcoes": ["Hidratação", "Tosa Higiênica"]
    }
}


def editar_pacote(nome_pacote):
    janela = tk.Toplevel()
    janela.title(f"Editar Pacote: {nome_pacote}")

    dados = pacotes_servicos[nome_pacote]["incluidos"]

    ttk.Label(janela, text="Serviços incluídos:").grid(row=0, column=0, sticky="w")

    var_incluidos = tk.StringVar(value=", ".join(dados["incluidos"]))
    ttk.Entry(janela, textvariable=var_incluidos, width=50).pack(pady=5)

    ttk.Label(janela, text="Bônus:").pack()
    var_bonus = tk.StringVar(value=", ".join(dados["bonus_opcoes"]))
    ttk.Entry(janela, textvariable=var_bonus, width=50).pack(pady=5)

    def salvar(dc):
        dc.pacotes_servicos[nome_pacote]["incluidos"] = [s.strip() for s in var_incluidos.get().split(",")]
        dc.pacotes_servicos[nome_pacote]["bonus_opcoes"] = [s.strip() for s in var_bonus.get().split(",")]
        messagebox.showinfo("Atualizado", f"Pacote '{nome_pacote}' atualizado com sucesso!")
        janela.destroy()

    ttk.Button(janela, text="Salvar", command=salvar).pack(pady=10)


# Dados estáticos de raças por porte e preços
# 🐕 Dados estáticos por porte

dados_pet = {
    "pequeno": {
        "raças": ['Schitzu', 'Lhasa Apso', 'Maltes', 'Yorkshire', 'Dachshund', 'Cavalier King Charles Spaniel',
                  'Biewer Terrier', 'Bulldog Francês', 'Pug', 'Chihuahua', 'Cocker Spaniel', 'Papillon',
                  'Spitz Alemao', 'Pinscher', 'Poodle', 'Jack Russell Terrier', 'Galgo Italiano', 'Pequinês',
                  'Bichon Frise', 'Boston Terrier', 'Fox Paulistinha', 'Petit Basset Griffon Vendéen'],
        "preços": {"Banho": 55, "Hidratação": 20, "Desembolo": 20, "Remoção de Pelos": 20, "Corte de Unhas": 15,
                   "Escovação de Dentes": 15, "Tosa Higiênica": 20, "Tosa na Máquina": 115,
                   "Tosa na Tesoura": 125, "Leva e Trás": 10},
    },
    "médio": {
        "raças": ['American Bully', 'Australian Cattle Dog', 'Basset Hound',
                  'Bulldog Campeiro', 'Bulldog', 'Bulldog Ingles', 'Bull Terrier', 'Basset Fulvo',
                  'Boxer', 'Clumber Spaniel', 'Cocker Americano', 'Cocker Ingles', 'Flat Coated Retriever',
                  'Pastor de Shetland', 'Pumi', 'Schnauzer Standard', 'Shar Pei', 'Spaniel Bretao', 'Spaniel Frances',
                  'Spitz Japones', 'Spriger Spaniel Ingles', 'Terrier Tibetano', 'S.R.D. Médio'],
        "preços": {"Banho": 65, "Hidratação": 20, "Desembolo": 20, "Remoção de Pelos": 20, "Corte de Unhas": 15,
                   "Escovação de Dentes": 15, "Tosa Higiênica": 20, "Tosa na Máquina": 115,
              "Tosa na Tesoura": 125, "Leva e Trás": 10},
    },
    "grande": {
        "raças": ['Pastor Alemao', 'Dogue Alemao', 'Terra Nova', 'Rottweiler', 'Sao-Bernardo', 'Labrador Retriever',
                  'Golden Retriever', 'Fila brasileiro', 'Cane corso', 'Border collie', 'Boiadeiro de Berna',
                  'Akita Inu', 'Mastim Ingles', 'Husky Siberiano', 'Dogo argentino', 'Dalmata', 'Weimaraner',
                  'Bull terrier', 'Mastim tibetano', 'Leonberger', 'Pastor australiano', 'Setter irlandes',
                  'Bulmastife', 'Mastim napolitano', 'Dogue de bordeus', 'Bulmastife', 'cao de Santo Humberto',
                  'Rhodesian ridgeback', 'Boiadeiro da Flandres', 'Bearded collie', 'Bichon bolonhes', 'Basenji',
                  'Boerboel', 'Pastor do caucaso', 'Veadeiro Pampeano', 'Buhund noruegues',
                  'Basset artesiano normando', 'Braco de Auvernia', 'Galgo Ingles', 'Pastor Belga', 'Mastiff',
                  'Bernese', 'Akita', 'Bloodhound', 'Australian Shepherd'],
        "preços": {"Banho": 70, "Hidratação": 20, "Desembolo": 20, "Remoção de Pelos": 20, "Corte de Unhas": 15,
                   "Escovação de Dentes": 15, "Tosa Higiênica": 20, "Tosa na Máquina": 115,
                "Tosa na Tesoura": 125, "Leva e Trás": 10},
    },
    "maior": {
        "raças": ['American Pit Bull Terrier', 'Fila Brasileiro', 'Chow Chow', 'Doberman', 'Chip-dog', 'American Pit Bul terrier',
                  'Chow-chow'],
        "preços": {"Banho": 120, "Hidratação": 20, "Desembolo": 20, "Remoção de Pelos": 80, "Corte de Unhas": 50,
               "Escovação de Dentes": 55, "Tosa Higiênica": 75, "Tosa na Máquina": 85,
               "Tosa na Tesoura": 100, "Leva e Trás": 10},
    },
}

# Imagens dos portes e das raças
# 🖼️ Imagens dos portes

imagens_portes = {
    "pequeno": "pequeno.jpg",
    "médio": "medio.jpg",
    "grande": "grande.jpg",
    "maior": "maior.jpg"
}

# Dicionário para armazenar imagens das raças
# 🐶 Imagens específicas por raça

imagens_racas = {
    'Schitzu':'schitzu.jpg','Lhasa Apso':'lhasa_apso.jpg','Maltês':'maltes.jpg','Yorkshire':'yorkshire.jpg','Dachshund':'dachshund.jpg',
    'Cavalier King Charles Spaniel':'cavalier_king_charles_spaniel.jpg','Biewer Terrier':'biewer_terrier.jpg','Bulldog Francês':'bulldog_frances.jpg',
    'Pug':'pug.jpg','Chihuahua':'chihuahua.jpg','Cocker Spaniel':'cocker_spaniel.jpg','Papillon':'papillon.jpg','Spitz Alemao':'spitz_alemao.jpg',
    'Pinscher':'pinscher.jpg','Poodle':'poodle.jpg','Jack Russell Terrier':'jack_russell_terrier.jpg','Galgo Italiano':'galgo_italiano.jpg',
    'Pequinês':'pequines.jpg','Bichon Frise':'bichon_frise.jpg','Boston Terrier':'boston_terrier.jpg','Fox Paulistinha':'fox_paulistinha.jpg',
    'American Pit Bull Terrier':'american_pit_bull_terrier.jpg','Australian Cattle Dog':'australian_cattle.jpg','Australian Shepherd':'australian_shepherd.jpg',
    'Petit Basset Griffon Vendéen':'petit_basset_griffon_vendéen.jpg','Basset Hound':'basset_hound.jpg','Bulldog Campeiro':'bulldog_campeiro.jpg','Bulldog':'bulldog.jpg',
    'Bulldog Inglês':'bulldog_ingles.jpg','Bull Terrier':'bull_terrier.jpg','Basset Fulvo':'basset_fulvo.jpg','Boxer':'boxer.jpg',
    'Clumber Spaniel':'clumber_spaniel.jpg','Cocker Americano':'cocker_americano.jpg','Cocker Inglês':'cocker_ingles.jpg',
    'Flat Coated Retriever':'flat_coated_retriever.jpg','Pastor de Shetland':'pastor_de_shetland.jpg','Pumi':'pumi.jpg',
    'Schnauzer Standard':'schnauzer_standard.jpg','Shar Pei':'shar_pei.jpg','Spaniel Bretão':'spaniel_bretao.jpg','Spaniel Francês':'spaniel_frances.jpg',
    'Spitz Japonês':'spitz_japones.jpg','Springer Spaniel':'springer_spaniel.jpg','Springer Spaniel Inglês':'springer_spaniel_ingles.jpg',
    'Terrier Tibetano':'terrier_tibetano.jpg','American Bully':'american_bully.jpg','SRD Médio':'s_r_d_medio.jpg','Dogo Argentino':'dogo_argentino.jpg',
    'Dálmata':'dalmatian.jpg','Weimaraner':'weimaraner.jpg','Mastim Tibetano':'mastim_tibetano.jpg','Leonberger':'leonberger.jpg',
    'Pastor Australiano':'pastor_australiano.jpg','Setter Irlandês':'setter_irlandes.jpg','Bulmastife':'bulmastife.jpg','Mastim Napolitano':'mastim_napolitano.jpg',
    'Dogue de Bordeaux':'dogue_de_bordeaux.jpg','Cão de Santo Humberto':'cao_de_santo_humberto.jpg','Rhodesian Ridgeback':'rhodesian_ridgeback.jpg',
    'Boiadeiro da Flandres':'boiadeiro_da_flandres.jpg','Bearded Collie':'bearded_collie.jpg','Bichon Bolonhês':'bichon_bolonhes.jpg','Basenji':'basenji.jpg',
    'Boerboel':'boerboel.jpg','Pastor do Cáucaso':'pastor_do_caucaso.jpg','Veadeiro Pampeano':'veadeiro_pampeano.jpg','Buhund Norueguês':'buhund_noruegues.jpg',
    'Basset Artesiano Normando':'basset_artesiano_normando.jpg','Braco de Auvernia':'braco_de_auvernia.jpg','Galgo Inglês':'galgo_ingles.jpg',
    'Pastor Belga':'pastor_belga.jpg','Mastiff':'mastiff.jpg','Bernese':'bernese.jpg','Akita':'akita.jpg','Bloodhound':'bloodhound.jpg','Pit Bull':'pit_bull.jpg',
    'Fila Brasileiro':'fila_brasileiro.jpg','Chow Chow':'chow_chow.jpg','Doberman':'doberman.jpg','Chip Dog':'chip_dog.jpg',
}



# Dicionário de características
# 📋 Características por raça (para relatórios ou sugestões visuais)

caracteristicas_racas = {
    "Chihuahua": {"peso": "2kg", "tamanho": "Pequeno", "temperamento": "Ativo"},
    "Labrador": {"peso": "30kg", "tamanho": "Grande", "temperamento": "Amigável"},
    "Bulldog": {"peso": "20kg", "tamanho": "Médio", "temperamento": "Calmo"},
    "Dogue Alemão": {"peso": "50kg", "tamanho": "Gigante", "temperamento": "Gentil"},
    # ... complemente com mais raças
}


def atualizar_exemplo():
    porte = dc.variaveis["var_porte"].get()
    print(f"Porte selecionado: {porte}")

    dc.variaveis["var_porte"].trace_add("write", lambda *args: atualizar_exemplo())



# Referência aos widgets (serão inicializados em aba_config)
# 🧩 Referência aos widgets que serão preenchidos em tempo real

combobox_porte = None
combobox_raca = None
label_imagem = None
texto_caracteristicas = None

# 💳 Forma de pagamento widgets
radiobutton_pix = None
radiobutton_debito = None
radiobutton_credito = None
radiobutton_dinheiro = None


# Faixa de preços atual (atualizada ao selecionar porte)
precos_atuais = {}

widgets_pagamento = {
    "pix": None,
    "debito": None,
    "credito": None,
    "dinheiro": None,
}

# Forma de pagamento
# var_pagamento = None
# radiobutton_pix = None
# radiobutton_debito = None
# radiobutton_credito = None
# radiobutton_dinheiro = None

def salvar_variaveis():
    print("🔒 Salvando variáveis...")
    for nome, var in variaveis.items():
        valor = var.get()
        print(f"{nome}: {valor}")
        # Aqui você pode salvar em JSON, banco ou arquivo
    messagebox.showinfo("Sucesso", "Variáveis salvas com sucesso!")
    tocar_som("sons/confirmacao.mp3")  # se quiser som de feedback




import os

def caminho_arquivo(nome_arquivo, subpasta=None):
    # sobe dois níveis: de modulos/recursos até a raiz do projeto
    raiz = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    if subpasta:
        caminho_completo = os.path.join(raiz, subpasta, nome_arquivo)
    else:
        caminho_completo = os.path.join(raiz, nome_arquivo)
    return os.path.abspath(caminho_completo)

    # pasta_base = os.path.dirname(__file__)  # pega o caminho da pasta atual (dados_compartilhados.py)
    # caminho_completo = os.path.join(pasta_base, "..", subpasta, nome_arquivo)
    # return os.path.abspath(caminho_completo)


def exportar_dados(dc):
    with open("backup_dados.txt", "w", encoding="utf-8") as f:
        f.write("=== Variáveis ===\n")
        for nome, var in dc.variaveis.items():
            f.write(f"{nome}: {var.get()}\n")

        f.write("\n=== Pacotes ===\n")
        for nome, dados in dc.pacotes_servicos.items():
            f.write(f"{nome}: Incluídos={dados['incluidos']}, Bônus={dados['bonus_opcoes']}\n")

        f.write("\n=== Usuários ===\n")
        for email, info in dc.usuarios.items():
            f.write(f"{info['nome']} ({email}) - {info['perfil']}\n")

    messagebox.showinfo("Exportado", "Dados exportados para 'backup_dados.txt'")


def montar_dados_compartilhados(master):
    frame = ttk.LabelFrame(master, text="📦 Dados Compartilhados")
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Filtros
    filtro_frame = ttk.Frame(frame)
    filtro_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=5)

    ttk.Label(filtro_frame, text="Nome:").grid(row=0, column=0)
    entry_nome = ttk.Entry(filtro_frame)
    entry_nome.grid(row=0, column=1, padx=5)

    ttk.Label(filtro_frame, text="Tipo:").grid(row=0, column=2)
    entry_tipo = ttk.Entry(filtro_frame)
    entry_tipo.grid(row=0, column=3, padx=5)


    # Tabela

    colunas = ("id", "nome", "tipo", "data")
    tabela = ttk.Treeview(frame, columns=colunas, show="headings")
    for col in colunas:
        tabela.heading(col, text=col.capitalize())
        tabela.column(col, width=120)

    tabela.grid(row=1, column=0, padx=10, pady=10)

    # Botões
    botoes_frame = ttk.Frame(frame)
    botoes_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

    def aplicar_filtro():
        nome = entry_nome.get()
        tipo = entry_tipo.get()
        atualizar_tabela(tabela, nome, tipo)

    def exportar_para_txt():
        nome = entry_nome.get()
        tipo = entry_tipo.get()
        dados = buscar_filtrados(nome, tipo)
        with open("dados_exportados.txt", "w", encoding="utf-8") as f:
            for item in dados:
                linha = f"{item.id}\t{item.nome}\t{item.tipo}\t{item.data}\n"
                f.write(linha)
        print("✅ Exportado para dados_exportados.txt")

    ttk.Button(botoes_frame, text="Filtrar", command=aplicar_filtro).grid(row=0, column=0, padx=5)
    ttk.Button(botoes_frame, text="Exportar TXT", command=exportar_para_txt).grid(row=0, column=1, padx=5)

    # Inicializa com todos os dados
    atualizar_tabela(tabela)

    # Preencher com dados reais

    dados = buscar_dados_compartilhados()
    for item in dados:
        tabela.insert("", "end", values=(item.id, item.nome, item.tipo, item.data))

    entry_nome = ttk.Entry(frame)
    entry_nome.grid(row=1, column=0, padx=10, pady=5)

    btn_filtrar = ttk.Button(frame, text="Filtrar", command=lambda: filtrar_por_nome(entry_nome.get(), tabela))
    btn_filtrar.grid(row=1, column=1, padx=10, pady=5)

    return frame





def filtrar_por_nome(nome, tabela):
    for item in tabela.get_children():
        tabela.delete(item)

    session = SessionLocal()
    try:
        resultados = session.query(DadosCompartilhados).filter(DadosCompartilhados.nome.ilike(f"%{nome}%")).all()
        for item in resultados:
            tabela.insert("", "end", values=(item.id, item.nome, item.tipo, item.data))
    finally:
        session.close()

# def exportar_dados():
#     dados = buscar_dados_compartilhados()
#     for item in dados:
#         print(item.id, item.nome, item.tipo, item.data)


def buscar_filtrados(nome="", tipo=""):
    session = SessionLocal()
    try:
        query = session.query(DadosCompartilhados)
        if nome:
            query = query.filter(DadosCompartilhados.nome.ilike(f"%{nome}%"))
        if tipo:
            query = query.filter(DadosCompartilhados.tipo.ilike(f"%{tipo}%"))
        return query.all()
    finally:
        session.close()

def atualizar_tabela(tabela, nome="", tipo=""):
    for item in tabela.get_children():
        tabela.delete(item)
    dados = buscar_filtrados(nome, tipo)
    for item in dados:
        tabela.insert("", "end", values=(item.id, item.nome, item.tipo, item.data))

def exportar_dados():
    dados = buscar_dados_compartilhados()
    with open("backup_dados.txt", "w", encoding="utf-8") as f:
        for item in dados:
            f.write(f"{item.id}\t{item.nome}\t{item.tipo}\t{item.data}\n")
    messagebox.showinfo("Exportado", "Dados exportados para 'backup_dados.txt'")


def atualizar_exemplo(inner_frame):
    porte = dc.variaveis["var_porte"].get()
    print(f"Porte selecionado: {porte}")

    # Exemplo de atualização visual (opcional)
    # Você pode atualizar um label, recomputar valores, etc.
    # Exemplo:
    # dc.label_resultado.config(text=f"Porte atual: {porte}")

# def inicializar_variaveis(master):
#     variaveis["var_tipo_pacote"] = tk.StringVar(master=master, value="Avulso")
#     # (e demais variáveis...)


# def inicializar_variaveis(master):
#     variaveis["var_porte"] = tk.StringVar(master)
#     variaveis["var_raca"] = tk.StringVar(master)
#     variaveis["var_tipopelo"] = tk.StringVar(master)
#     variaveis["var_pagamento"] = tk.StringVar(master)
#     variaveis["var_descricao"] = tk.StringVar(master)
#     variaveis["var_data_cadastro"] = tk.StringVar(master)
#     variaveis["var_pelagem"] = tk.StringVar(master)
#     variaveis["var_caracteristicas"] = tk.StringVar(master)


    #global var_porte, var_raca, var_tipopelo, var_pagamento, var_descricao
    # var_porte = tk.StringVar(master, value="")
    # var_raca = tk.StringVar(master, value="")
    # var_tipopelo = tk.StringVar(master, value="")
    # var_pagamento = tk.StringVar(master, value="")
    # var_descricao = tk.StringVar(master, value="")

# def inicializar_variaveis(master):
#     global var_porte, var_raca, var_tipopelo, var_pagamento, var_descricao
#     var_porte = tk.StringVar(master, value="")
#     var_raca = tk.StringVar(master, value="")
#     var_tipopelo = tk.StringVar(master, value="")
#     var_pagamento = tk.StringVar(master, value="")
#     var_descricao = tk.StringVar(master, value="")  # ✅ Aqui está no momento certo!

# var_porte = tk.StringVar()
# var_raca = tk.StringVar()
# var_tipopelo = tk.StringVar()


# Variáveis globais ligadas aos Combobox
# var_porte = tk.StringVar(value="pequeno")
# var_raca = tk.StringVar()

