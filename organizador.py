import os
import shutil

#1 Definir o caminho da pasta a ser organizada
PASTA_ALVO = os.path.expanduser("~/Downloader")

#2 Mapeamento de extensões para o nome da pasta de destino
REGRAS_ORGANIZAÇÃO ={
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Instaladores": [".exe", ".msi", ".dmg", ".deb"],
    "Audios": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"]
} 

def organizar_pasta(caminho):
    # Verificar se a pasta informada realmente existe
    if not os.path.exists(caminho):
        print(f"A pasta '{caminho}' não foi encontrada.")
        return

    # Listar todos os itens da pasta
    itens = os.listdir(caminho)

    for item in itens:
        caminho_item = os.path.join(caminho, item)

        # ignorar se for um diretório/pasta (só queremos mover os arquivos)
        if os.path.isdir(caminho_item):
            continue

        # Extrai a extensão do arquivo (ex: '.pdf) em minúsculo
        _, extensao = os.path.splitext(item)
        extensao = extensao.lower()

        moved = False

        # Procura em qual categoria a extensão se encaixa
        for categoria, extensoes in REGRAS_ORGANIZAÇÃO.items():
            if extensao in extensoes:
                pasta_destino = os.path.join(caminho, categoria)

                # Cria a pasta da categoria se ela ainda não existir
                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)

                # Mover o arquivo para a pasta correspondente
                shutil.move(caminho_item, os.path.join(pasta_destino, item))
                print(f"MOvido: '{item}' > '{categoria}/'")
                moved = True
                break

            # Se for uma extensão desconhecida, envia para a pasta 'Outros'
            if not moved and extensao != "":
                pasta_outros = os.path.join(caminho, "Outros")
                if not os.path.exists(pasta_outros):
                    os.makedirs(pasta_outros)
                    shutil.move(caminho_item, os.path.join(pasta_outros, item))
                    print(f"Movido: '{item}' > 'Outros/'")

        print("\nOrganização concluída com sucesso!")

        # Executar o script
        if __name__ == "__main__":
            organizar_pasta(PASTA_ALVO)
