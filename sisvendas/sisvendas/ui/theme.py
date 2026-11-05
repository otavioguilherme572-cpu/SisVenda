import tkinter as tk
from tkinter import ttk

# =============================================================================
# PALETA DE CORES MODERNA (Estilo Tailwind / Indigo & Slate Profissional)
# =============================================================================

# Superfícies e Fundos
BG_APP = "#f8fafc"             # Slate 50 (Fundo geral limpo, suave e moderno)
BG_CARD = "#ffffff"            # Branco puro para cartões, tabelas e formulários
BG_CARD_ALT = "#f1f5f9"        # Slate 100 para zebra striping e cabeçalhos de tabela

# Cabeçalho Superior e Barra Lateral (Deep Slate & Navy)
BG_HEADER = "#0f172a"          # Slate 900 (Topo elegante)
BG_SIDEBAR = "#1e293b"         # Slate 800 (Fundo da barra lateral)
BG_SIDEBAR_HOVER = "#334155"   # Slate 700 (Hover sutil dos botões)
BG_SIDEBAR_ACTIVE = "#4f46e5"  # Indigo 600 (Item ativo vibrante e moderno)

# Cores Principais de Ação (Acentos)
PRIMARY = "#4f46e5"            # Indigo 600 (Ação principal premium)
PRIMARY_HOVER = "#4338ca"      # Indigo 700 (Hover do primário)
PRIMARY_LIGHT = "#eef2ff"      # Indigo 50 (Fundo suave de destaque)

SUCCESS = "#059669"            # Emerald 600 (Sucesso / Cadastros)
SUCCESS_HOVER = "#047857"      # Emerald 700 (Hover do sucesso)
SUCCESS_LIGHT = "#ecfdf5"      # Emerald 50 (Fundo suave de sucesso)

DANGER = "#e11d48"             # Rose 600 (Perigo / Exclusões)
DANGER_HOVER = "#be123c"       # Rose 700 (Hover do perigo)
DANGER_LIGHT = "#fff1f2"       # Rose 50 (Destaque sutil para alertas)

WARNING = "#d97706"            # Amber 600 (Alertas)
WARNING_LIGHT = "#fef3c7"      # Amber 50 (Fundo suave de alerta)

INFO = "#0284c7"               # Sky 600 (Informativo / Estatísticas)
INFO_LIGHT = "#f0f9ff"         # Sky 50 (Fundo suave informativo)

# Tipografia e Cores de Texto
TEXT_DARK = "#0f172a"          # Slate 900 (Títulos de alta ênfase)
TEXT_BODY = "#334155"          # Slate 700 (Texto principal de leitura)
TEXT_MUTED = "#64748b"         # Slate 500 (Subtítulos, dicas e legendas)
TEXT_LIGHT = "#f8fafc"         # Slate 50 (Texto em superfícies escuras)

# Bordas e Divisores
BORDER_COLOR = "#cbd5e1"       # Slate 300 (Bordas de campos e foco)
BORDER_LIGHT = "#e2e8f0"       # Slate 200 (Divisores e contornos de cartões)

# Tipografia
FONT_FAMILY = "Segoe UI"
FONT_TITLE = (FONT_FAMILY, 15, "bold")
FONT_SUBTITLE = (FONT_FAMILY, 12, "bold")
FONT_SECTION = (FONT_FAMILY, 10, "bold")
FONT_BODY = (FONT_FAMILY, 10)
FONT_BOLD = (FONT_FAMILY, 10, "bold")
FONT_SMALL = (FONT_FAMILY, 9)
FONT_STAT_NUM = (FONT_FAMILY, 24, "bold")


def apply_theme(root: tk.Tk):
    """Configura os estilos visuais globais do ttk com a paleta refinada."""
    style = ttk.Style(root)

    try:
        style.theme_use("clam")
    except tk.TclError:
        pass

    # Configuração Geral
    style.configure("TFrame", background=BG_APP)
    style.configure("Card.TFrame", background=BG_CARD)
    style.configure("TLabel", background=BG_APP, foreground=TEXT_BODY, font=FONT_BODY)
    style.configure("Card.TLabel", background=BG_CARD, foreground=TEXT_BODY, font=FONT_BODY)
    style.configure("Muted.TLabel", background=BG_CARD, foreground=TEXT_MUTED, font=FONT_SMALL)
    style.configure("Title.TLabel", background=BG_CARD, foreground=TEXT_DARK, font=FONT_TITLE)
    style.configure("Subtitle.TLabel", background=BG_CARD, foreground=TEXT_DARK, font=FONT_SUBTITLE)

    # Botão Primário (Indigo Moderno)
    style.configure(
        "Primary.TButton",
        background=PRIMARY,
        foreground=TEXT_LIGHT,
        font=FONT_BOLD,
        borderwidth=0,
        focuscolor=PRIMARY_HOVER,
        padding=(14, 8)
    )
    style.map(
        "Primary.TButton",
        background=[("active", PRIMARY_HOVER), ("disabled", "#cbd5e1")],
        foreground=[("disabled", "#94a3b8")]
    )

    # Botão Sucesso (Emerald)
    style.configure(
        "Success.TButton",
        background=SUCCESS,
        foreground=TEXT_LIGHT,
        font=FONT_BOLD,
        borderwidth=0,
        focuscolor=SUCCESS_HOVER,
        padding=(14, 8)
    )
    style.map(
        "Success.TButton",
        background=[("active", SUCCESS_HOVER), ("disabled", "#cbd5e1")],
        foreground=[("disabled", "#94a3b8")]
    )

    # Botão Perigo (Rose)
    style.configure(
        "Danger.TButton",
        background=DANGER,
        foreground=TEXT_LIGHT,
        font=FONT_BOLD,
        borderwidth=0,
        focuscolor=DANGER_HOVER,
        padding=(12, 8)
    )
    style.map(
        "Danger.TButton",
        background=[("active", DANGER_HOVER), ("disabled", "#cbd5e1")],
        foreground=[("disabled", "#94a3b8")]
    )

    # Botão Secundário / Outline
    style.configure(
        "Secondary.TButton",
        background="#e2e8f0",
        foreground=TEXT_BODY,
        font=FONT_BOLD,
        borderwidth=0,
        padding=(12, 8)
    )
    style.map(
        "Secondary.TButton",
        background=[("active", "#cbd5e1")]
    )

    # Campos de Texto (Entry)
    style.configure(
        "TEntry",
        fieldbackground=BG_CARD,
        foreground=TEXT_DARK,
        bordercolor=BORDER_COLOR,
        lightcolor=PRIMARY,
        darkcolor=BORDER_COLOR,
        padding=6
    )

    # Caixas de Seleção (Combobox)
    style.configure(
        "TCombobox",
        fieldbackground=BG_CARD,
        background=BG_CARD,
        foreground=TEXT_DARK,
        padding=6
    )

    # Tabela de Dados (Treeview)
    style.configure(
        "Treeview",
        background=BG_CARD,
        fieldbackground=BG_CARD,
        foreground=TEXT_BODY,
        rowheight=30,
        font=FONT_BODY,
        borderwidth=0
    )
    style.configure(
        "Treeview.Heading",
        background=BG_CARD_ALT,
        foreground=TEXT_DARK,
        font=(FONT_FAMILY, 9, "bold"),
        padding=(8, 8),
        borderwidth=0
    )
    style.map(
        "Treeview.Heading",
        background=[("active", "#e2e8f0")]
    )
    style.map(
        "Treeview",
        background=[("selected", PRIMARY)],
        foreground=[("selected", TEXT_LIGHT)]
    )

    # Scrollbars
    style.configure("Vertical.TScrollbar", troughcolor=BG_APP, borderwidth=0)
    style.configure("Horizontal.TScrollbar", troughcolor=BG_APP, borderwidth=0)
