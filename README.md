# 📂 Organizador Automático de Arquivos em Tempo Real

Um script em Python desenvolvido para monitorar a pasta de **Downloads** (ou qualquer outra pasta selecionada) e organizar arquivos automaticamente em subpastas com base em suas extensões (`.pdf`, `.png`, `.exe`, etc.).

---

## 🚀 Funcionalidades

- **Organização por Categorias:** Separa arquivos em pastas como *Imagens*, *Documentos*, *Compactados*, *Instaladores*, *Áudios*, *Vídeos* e *Outros*.
- **Monitoramento em Tempo Real:** Utiliza a biblioteca `watchdog` para mover novos arquivos no exato instante em que o download é concluído.
- **Tratamento de Arquivos Temporários:** Ignora arquivos parciais de navegação (ex: `.crdownload` e `.tmp`) até que o download termine.

---

## 🛠️ Tecnologias Utilizadas

- **[Python 3](https://www.python.org/)**
- **[Watchdog](https://pypi.org/project/watchdog/)** (para escutar eventos do sistema de arquivos)

---

## 📋 Como Executar o Projeto

### Prerequisitos
Certifique-se de ter o **Python** instalado na sua máquina.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Alex-del-25/Organizador-de-arquivo.git
   cd Organizador-de-arquivo