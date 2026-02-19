import os

def caminho_arquivo(nome_arquivo, subpasta=None):
    base_dir = os.path.dirname(os.path.dirname(__file__))  # sobe da pasta modulos para raiz

    if subpasta:
        return os.path.join(base_dir, "imagensipojucao", subpasta, nome_arquivo)
    return os.path.join(base_dir, "imagensipojucao", "imagens", nome_arquivo)


if __name__ == "__main__":
    print(caminho_arquivo("teste.txt"))
    print(caminho_arquivo("teste.txt", "subpasta"))

    caminho = caminho_arquivo("dados.txt", "arquivos")
    print("Caminho:", caminho)
    print("Existe?", os.path.exists(caminho))


def arquivo_existe(nome_arquivo, subpasta=None):
    caminho = caminho_arquivo(nome_arquivo, subpasta)
    if not os.path.exists(caminho):
        print(f"[AVISO] Arquivo '{nome_arquivo}' não encontrado em '{caminho}'")
    return caminho

# dentro de utilitarios.py

def preencher_combobox_arquivos(combobox, subpasta, extensoes=None):
    from abas.recurso import listar_arquivos

    arquivos = listar_arquivos(subpasta, extensoes)
    combobox["values"] = arquivos
    if arquivos:
        combobox.set(arquivos[0])
    else:
        combobox.set("Nenhum arquivo encontrado")