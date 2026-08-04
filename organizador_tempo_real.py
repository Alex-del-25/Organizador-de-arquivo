import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 1. Defina a pasta que será monitorada
PASTA_MONITORADA = os.path.expanduser("~/Downloads")

# 2. Regras de organização por extensão
REGRAS_ORGANIZACAO = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Instaladores": [".exe", ".msi", ".dmg", ".deb"],
    "Audios": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"]
}

def mover_arquivo(caminho_arquivo):
    # Se for um diretório ou arquivo temporário de download (ex: .crdownload), ignora
    if os.path.isdir(caminho_arquivo):
        return
        
    nome_arquivo = os.path.basename(caminho_arquivo)
    _, extensao = os.path.splitext(nome_arquivo)
    extensao = extensao.lower()

    # Ignora arquivos temporários de downloads do Chrome/Firefox/Edge
    if extensao in [".crdownload", ".tmp", ".part"]:
        return

    # Pequena pausa para garantir que o download foi concluído e o arquivo não está bloqueado
    time.sleep(1)

    for categoria, extensoes in REGRAS_ORGANIZACAO.items():
        if extensao in extensoes:
            pasta_destino = os.path.join(PASTA_MONITORADA, categoria)
            os.makedirs(pasta_destino, exist_ok=True)
            
            try:
                shutil.move(caminho_arquivo, os.path.join(pasta_destino, nome_arquivo))
                print(f"⚡ Movido instantaneamente: '{nome_arquivo}' ➔ '{categoria}/'")
            except Exception as e:
                print(f"Erro ao mover {nome_arquivo}: {e}")
            return

    # Se não encontrar nenhuma extensão correspondente, envia para 'Outros'
    if extensao != "":
        pasta_outros = os.path.join(PASTA_MONITORADA, "Outros")
        os.makedirs(pasta_outros, exist_ok=True)
        try:
            shutil.move(caminho_arquivo, os.path.join(pasta_outros, nome_arquivo))
            print(f"⚡ Movido instantaneamente: '{nome_arquivo}' ➔ 'Outros/'")
        except Exception as e:
            print(f"Erro ao mover {nome_arquivo}: {e}")

# Class handler que escuta os eventos da pasta
class ManipuladorDeArquivos(FileSystemEventHandler):
    def on_created(self, event):
        # Disparado assim que um arquivo surge na pasta
        mover_arquivo(event.src_path)

    def on_modified(self, event):
        # Disparado quando um download em andamento é finalizado
        mover_arquivo(event.src_path)

if __name__ == "__main__":
    event_handler = ManipuladorDeArquivos()
    observer = Observer()
    
    # Agenda o monitoramento da pasta alvo (recursive=False para não escutar subpastas)
    observer.schedule(event_handler, PASTA_MONITORADA, recursive=False)
    observer.start()

    print(f"👀 Monitorando a pasta '{PASTA_MONITORADA}' em tempo real...")
    print("Pressione Ctrl+C no terminal para parar.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nMonitoramento encerrado.")
    
    observer.join()