📌 Descrição

Este projeto é um bot em Python que organiza automaticamente os arquivos de uma pasta, movendo-os para subpastas de acordo com seu tipo (imagens, documentos, vídeos, etc).
É útil para manter pastas como "Downloads" mais organizadas, sem precisar mover arquivos manualmente.

🚀 Tecnologias utilizadas

Python 3

Bibliotecas:

os → para navegar entre arquivos e pastas

shutil → para mover arquivos

⚙️ Como funciona

O bot verifica todos os arquivos dentro de uma pasta escolhida.

Identifica o tipo de arquivo pela extensão.

Cria pastas automaticamente para cada tipo, caso não existam.

Move os arquivos para as respectivas pastas.

▶️ Como executar

Instale o Python 3 no computador.

Baixe/clonar o repositório.

No arquivo main.py, altere a variável pasta_origem para o caminho da pasta que deseja organizar.

Execute no terminal:

python main.py
