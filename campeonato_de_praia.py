RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
BOLD = "\033[1m"
WHITE = "\033[37m"


def limpar_tela():
    print("\n" * 100)


def listar_dados(matriz, nomes_atletas, nomes_rodadas, nome_esporte):
    limpar_tela()
    print(f"{BOLD}{YELLOW}--- PLACAR: {nome_esporte.upper()} ---{RESET}")

    cabecalho = "Atleta\t\t"
    for rodada in nomes_rodadas:
        cabecalho += f"{rodada}\t"
    print(cabecalho)
    print("-" * (len(cabecalho) + 20))

    for indice, nome_atleta in enumerate(nomes_atletas):
        linha_atleta = f"{nome_atleta}\t"
        pontuacoes = matriz[indice]
        for pontuacao in pontuacoes:
            if pontuacao is None:
                linha_atleta += "-\t\t"
            else:
                linha_atleta += f"{pontuacao:.2f}\t\t"
        print(linha_atleta)

    input("\nPressione Enter para continuar...")


def cadastrar_dados(matriz, nomes_atletas, nomes_rodadas):
    limpar_tela()
    print(f"{BOLD}{YELLOW}--- CADASTRO DE PONTUAÇÃO ---{RESET}")
    try:
        print("\nSelecione o Atleta:")
        for i, nome in enumerate(nomes_atletas):
            print(f"{i + 1} - {nome}")

        atleta_escolha = int(input("Digite o número do atleta ou digite 0 para sair: "))
        if atleta_escolha == 0:
            return
        if not 1 <= atleta_escolha <= len(nomes_atletas):
            print(f"{BOLD}{RED}Erro: Opção de atleta inválida.{RESET}")
            input("\nPressione Enter para continuar...")
            return

        indice_atleta = atleta_escolha - 1

        print("\nSelecione a Rodada:")
        for i, nome in enumerate(nomes_rodadas):
            print(f"{i + 1} - {nome}")

        rodada_escolha = int(input("Digite o número da rodada ou digite 0 para sair: "))
        if rodada_escolha == 0:
            return
        if not 1 <= rodada_escolha <= len(nomes_rodadas):
            print(f"{BOLD}{RED}Erro: Opção de rodada inválida.{RESET}")
            input("\nPressione Enter para continuar...")
            return
            
        indice_rodada = rodada_escolha - 1

        if matriz[indice_atleta][indice_rodada] is not None:
            print(f"\n{BOLD}{RED}Erro: Essa pontuação já foi adicionada.{RESET}")
        else:
            nova_pontuacao = float(input("Digite a nova pontuação: "))
            matriz[indice_atleta][indice_rodada] = nova_pontuacao
            print(f"\n{BOLD}{GREEN}Pontuação cadastrada com sucesso!{RESET}")
        
        input("\nPressione Enter para continuar...")

    except ValueError:
        print(f"\n{BOLD}{RED}Erro: Valor inválido. Por favor, digite apenas números.{RESET}")
        input("\nPressione Enter para continuar...")


def buscar_dado(matriz, nomes_atletas, nomes_rodadas):
    limpar_tela()
    print(f"{BOLD}{CYAN}--- BUSCAR PONTUAÇÃO ---{RESET}")
    try:
        print("\nSelecione o Atleta:")
        for i, nome in enumerate(nomes_atletas):
            print(f"{i + 1} - {nome}")
        atleta_escolha = int(input("Digite o número do atleta ou digite 0 para sair: "))
        if atleta_escolha == 0:
            return
        if not 1 <= atleta_escolha <= len(nomes_atletas):
            print(f"{BOLD}{RED}Erro: Opção de atleta inválida.{RESET}")
            input("\nPressione Enter para continuar...")
            return
        indice_atleta = atleta_escolha - 1

        print("\nSelecione a Rodada:")
        for i, nome in enumerate(nomes_rodadas):
            print(f"{i + 1} - {nome}")
        rodada_escolha = int(input("Digite o número da rodada ou digite 0 para sair: "))
        if rodada_escolha == 0:
            return
        if not 1 <= rodada_escolha <= len(nomes_rodadas):
            print(f"{BOLD}{RED}Erro: Opção de rodada inválida.{RESET}")
            input("\nPressione Enter para continuar...")
            return
        indice_rodada = rodada_escolha - 1

        pontuacao = matriz[indice_atleta][indice_rodada]
        
        if pontuacao is not None:
            print(f"\n{BOLD}{CYAN}--- RESULTADO DA BUSCA ---{RESET}")
            print(f"A pontuação do {nomes_atletas[indice_atleta]} na {nomes_rodadas[indice_rodada]} é: {pontuacao:.2f}")
        else:
            print(f"\n{BOLD}{YELLOW}A pontuação ainda não foi cadastrada.{RESET}")
        
        input("\nPressione Enter para continuar...")
        
    except (ValueError, IndexError):
        print(f"\n{BOLD}{RED}Erro: Opção inválida ou fora do intervalo.{RESET}")
        input("\nPressione Enter para continuar...")


def atualizar_dado(matriz, nomes_atletas, nomes_rodadas):
    limpar_tela()
    print(f"{BOLD}{CYAN}--- ATUALIZAR PONTUAÇÃO ---{RESET}")
    try:
        print("\nSelecione o Atleta que deseja atualizar:")
        for i, nome in enumerate(nomes_atletas):
            print(f"{i + 1} - {nome}")
        atleta_escolha = int(input("Digite o número do atleta ou digite 0 para sair: "))
        if atleta_escolha == 0:
            return
        if not 1 <= atleta_escolha <= len(nomes_atletas):
            print(f"{BOLD}{RED}Erro: Opção de atleta inválida.{RESET}")
            input("\nPressione Enter para continuar...")
            return
        indice_atleta = atleta_escolha - 1

        print("\nSelecione a Rodada que deseja atualizar:")
        for i, nome in enumerate(nomes_rodadas):
            print(f"{i + 1} - {nome}")
        rodada_escolha = int(input("Digite o número da rodada ou digite 0 para sair: "))
        if rodada_escolha == 0:
            return
        if not 1 <= rodada_escolha <= len(nomes_rodadas):
            print(f"{BOLD}{RED}Erro: Opção de rodada inválida.{RESET}")
            input("\nPressione Enter para continuar...")
            return
        indice_rodada = rodada_escolha - 1

        pontuacao_atual = matriz[indice_atleta][indice_rodada]

        if pontuacao_atual is None:
            print(f"\n{BOLD}{YELLOW}Não há pontuação para atualizar. Cadastre uma primeiro.{RESET}")
            input("\nPressione Enter para continuar...")
            return
        
        print(f"\nA pontuação atual é: {pontuacao_atual:.2f}")
        nova_pontuacao = float(input("Digite a nova pontuação: "))

        if nova_pontuacao == pontuacao_atual:
            print(f"\n{BOLD}{CYAN}A pontuação permanece a mesma.{RESET}")
        else:
            matriz[indice_atleta][indice_rodada] = nova_pontuacao
            print(f"\n{BOLD}{GREEN}Pontuação atualizada com sucesso!{RESET}")
        input("\nPressione Enter para continuar...")

    except (ValueError, IndexError):
        print(f"\n{BOLD}{RED}Erro: Valor inválido ou opção fora do intervalo.{RESET}")
        input("\nPressione Enter para continuar...")


def gerar_relatorio(matriz, nomes_atletas, nomes_rodadas, nome_esporte):
    limpar_tela()
    print(f"{BOLD}{BLUE}--- GERAR RELATÓRIO FILTRADO ---{RESET}")
    try:
        print("Filtro: Listar atletas com pontuação acima de um valor em uma rodada.")

        print("\nSelecione a Rodada para o filtro:")
        for i, nome in enumerate(nomes_rodadas):
            print(f"{i + 1} - {nome}")
        rodada_escolha = int(input("Digite o número da rodada ou digite 0 para sair: "))
        if rodada_escolha == 0:
            return
        if not 1 <= rodada_escolha <= len(nomes_rodadas):
            print(f"{BOLD}{RED}Erro: Opção de rodada inválida.{RESET}")
            input("\nPressione Enter para continuar...")
            return
        indice_rodada = rodada_escolha - 1

        valor_filtro = float(input("Listar pontuações maiores que: "))

        limpar_tela()
        print(f"--- RELATÓRIO: Atletas em {nome_esporte} com mais de {valor_filtro:.2f} pontos na {nomes_rodadas[indice_rodada]} ---")

        encontrou_alguem = False
        for i, nome in enumerate(nomes_atletas):
            pontuacao = matriz[i][indice_rodada]
            if pontuacao is not None and pontuacao > valor_filtro:
                print(f"- {nome}: {pontuacao:.2f} pontos")
                encontrou_alguem = True

        if not encontrou_alguem:
            print(f"\n{BOLD}{RED}Nenhum atleta atendeu ao critério do filtro.{RESET}")
        
        input("\nPressione Enter para continuar...")

    except ValueError:
        print(f"\n{BOLD}{RED}Erro: Valor inválido.{RESET}")
        input("\nPressione Enter para continuar...")


def gerar_ranking(matriz, nomes_atletas, nome_esporte):
    limpar_tela()
    print(f"{BOLD}{BLUE}--- RANKING GERAL: {nome_esporte.upper()} ---{RESET}")
    
    ranking = []
    for i, atleta in enumerate(nomes_atletas):
        pontuacoes_validas = [p for p in matriz[i] if p is not None]
        total = sum(pontuacoes_validas)
        ranking.append((atleta, total))
    
    ranking.sort(key=lambda item: item[1], reverse=True)
    
    for pos, (atleta, total) in enumerate(ranking, start=1):
        print(f"{pos}º - {atleta}: {total:.2f} pontos")
        
    input("\nPressione Enter para continuar...")


def menu_esporte(nome_esporte, matriz_esporte, nomes_atletas, nomes_rodadas, cor_menu=CYAN):
    opcao_menu = 0
    while opcao_menu != 7:
        limpar_tela()
        try:
            menu_texto = f"""
    {BOLD}{cor_menu}___ MENU {nome_esporte.upper()} ___
    
    {GREEN}1 - Inserir Pontuação
    2 - Listar Pontuações
    3 - Buscar Pontuação
    4 - Alterar Pontuação
    5 - Gerar Relatório Filtrado
    6 - Ver Ranking Geral{RED}
    7 - Voltar ao Menu Principal
    {BOLD}{cor_menu}____________{RESET}
    
    {BOLD}{WHITE}Selecione uma das opções:{RESET} """
            
            opcao_menu = int(input(menu_texto))

            if opcao_menu == 7:
                continue

            match opcao_menu:
                case 1:
                    cadastrar_dados(matriz_esporte, nomes_atletas, nomes_rodadas)
                case 2:
                    listar_dados(matriz_esporte, nomes_atletas, nomes_rodadas, nome_esporte)
                case 3:
                    buscar_dado(matriz_esporte, nomes_atletas, nomes_rodadas)
                case 4:
                    atualizar_dado(matriz_esporte, nomes_atletas, nomes_rodadas)
                case 5:
                    gerar_relatorio(matriz_esporte, nomes_atletas, nomes_rodadas, nome_esporte)
                case 6:
                    gerar_ranking(matriz_esporte, nomes_atletas, nome_esporte)
                case _:
                    print(f"{BOLD}{RED}Opção inválida!{RESET}")
                    input("\nPressione Enter para continuar...")
                    
        except ValueError:
            print(f"\n{BOLD}{RED}Erro: Digite apenas o número da opção.{RESET}")
            input("\nPressione Enter para continuar...")


rodadas = ["Rodada 1", "Rodada 2", "Rodada 3", "Rodada 4"]
atletas = ["Atleta 1", "Atleta 2", "Atleta 3"]

matriz_surf = [[None] * 4 for _ in range(3)]
matriz_volei = [[None] * 4 for _ in range(3)]

opcao_menu_principal = 0
while opcao_menu_principal != 3:
    limpar_tela()
    try:
        print(f"{BOLD}{CYAN}=" * 100)
        print(f"{BOLD}{YELLOW}    TRABALHO FINAL DE LPI - C3.A2 (CAMPEONATO DE ESPORTES DE PRAIA)")
        print(f"{CYAN}=" * 100 + RESET)
        print(f"{GREEN}Integrantes: Eduardo Bianchini, George Pinheiro e Vitor Soares{RESET}")

        menu_principal_texto = f"""
    {BOLD}{CYAN}___ MENU PRINCIPAL ___
    
    {GREEN}1 - Gerenciar Tabela {CYAN}Surf
    {GREEN}2 - Gerenciar Tabela {YELLOW}Vôlei
    {RED}3 - Sair
    {BOLD}{CYAN}____________{RESET}
    
    {BOLD}{WHITE}Selecione uma das opções:{RESET} """
        
        opcao_menu_principal = int(input(menu_principal_texto))

        if opcao_menu_principal == 3:
            continue

        match opcao_menu_principal:
            case 1:
                menu_esporte("Surf", matriz_surf, atletas, rodadas, cor_menu=CYAN)
            case 2:
                menu_esporte("Vôlei", matriz_volei, atletas, rodadas, cor_menu=YELLOW)
            case _:
                print(f"{BOLD}{RED}Opção inválida!{RESET}")
                input("\nPressione Enter para continuar...")
                
    except ValueError:
        print(f"\n{BOLD}{RED}Erro: Opção principal inválida.{RESET}")
        input("\nPressione Enter para continuar...")

print(f"\n{BOLD}{GREEN}Programa encerrado.{RESET}")