import sys
from database.connection import init_db
from modules.auth import criar_usuario_admin_padrao, autenticar_usuario, session

def main():
    print("iniciando o sistema de vendas...")

    #1. inicializa o banco de dados (cria as tabelas se não existirem)
    init_db()

    #2. criaq o usuario administrador padrão caso o banco esteja vazio
    criar_usuario_admin_padrao()

    print("\n" + "="*30)
    print("    SISTEMA DE VENDAS v1.0")
    print("="*30)

    # Loop de login
    while True:
        print("\n--- LOGIN---")
        login = input("usuario: ")
        senha = input("senha: ")

        sucesso, msg = autenticar_usuario(login, senha)

        if sucesso:
            print(f"\n[SUCESSO] {msg}")
            menu_principal()
            break
        else:
            print(f"\n[ERRO] {msg}")
            tentar_novamente = input("Deseja tentar novamente? (s/n): ").strip().lower()
            if tentar_novamente == 'n':
                print("Encerrando o sistema...")
                sys.exit(0)

def menu_principal():
    while True:
        print("\n" + "="*30)
        print("    MENU PRINCIPAL")
        print("="*30)
        print(f"Usuario logado: {session.nome} | cargo: {session.cargo}")
        print("-" * 30)
        print("1. Gerenciar Produtos (em breve)")
        print("2. Nova venda (em breve)")
        print("3. Relatórios (em breve)")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == '0':
            print("saindo do sistema... até logo")
            session.clear()
            sys.exit(0)
        elif opcao in ['1', '2', '3']:
            print(f"\n[AVISO] A funcionalidade '{opcao}' ainda não foi implementada.")
        else:
            print("\n[ERRO] Opção inválida.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSistema encerrado pelo usuário.")
        sys.exit(0)