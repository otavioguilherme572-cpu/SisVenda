"""
Ponto de Entrada Principal - SisVendas Desktop
Inicia o banco de dados e abre a interface gráfica com tela de login, painel principal e cadastro de produtos.
"""
import sys
from pathlib import Path

# Garante o diretório raiz no PATH
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

from ui.app import SisVendasApp


def main():
    app = SisVendasApp()
    app.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSistema encerrado pelo usuário.")
        sys.exit(0)
