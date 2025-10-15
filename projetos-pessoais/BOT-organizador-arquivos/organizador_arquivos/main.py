import os
import shutil

# Pasta que você quer organizar
pasta_origem = r"C:\Users\caio.diniz\Desktop\teste"

# Pastas por tipo de arquivo
tipos = {
    "Imagens": [".jpg", ".png", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Outros": []
}

# Criar pastas se não existirem
for pasta in tipos.keys():
    caminho = os.path.join(pasta_origem, pasta)
    if not os.path.exists(caminho):
        os.makedirs(caminho)

# Mover arquivos para pastas correspondentes
for arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, arquivo)
    if os.path.isfile(caminho_arquivo):
        movido = False
        for pasta, extensoes in tipos.items():
            if any(arquivo.lower().endswith(ext) for ext in extensoes):
                shutil.move(caminho_arquivo, os.path.join(pasta_origem, pasta, arquivo))
                movido = True
                break
        if not movido:
            shutil.move(caminho_arquivo, os.path.join(pasta_origem, "Outros", arquivo))

print("Arquivos organizados com sucesso!")
