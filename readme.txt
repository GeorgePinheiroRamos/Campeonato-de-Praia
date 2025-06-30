-----

```
################################################################################
#                                                                              #
#             SISTEMA DE GERENCIAMENTO DE ESPORTES DE PRAIA                      #
#                                                                              #
################################################################################

AUTORES: Eduardo Bianchini, George Pinheiro e Vitor Soares
VERSÃO: 1.0
DATA: 25/06/2025

================================================================================
ÍNDICE
================================================================================

1. DESCRIÇÃO GERAL
2. GUIA DE USO DO PROGRAMA
   2.1. Menu Principal
   2.2. Menu de Esportes (Surf / Vôlei)
3. EXPLICAÇÃO TÉCNICA DO CÓDIGO
   3.1. Constantes e Variáveis Globais
   3.2. Funções de Gerenciamento de Dados (CRUD)
   3.3. Funções de Relatórios
   3.4. Funções de Interface (Menus)
   3.5. Loop Principal (Execução)

================================================================================
1. DESCRIÇÃO GERAL
================================================================================

Este programa é um sistema de gerenciamento de pontuações para um campeonato
de esportes de praia. Ele permite ao usuário gerenciar de forma independente as
tabelas de pontuação para duas modalidades: Surf e Vôlei.

O sistema oferece funcionalidades para inserir, listar, buscar, alterar
pontuações, além de gerar relatórios filtrados e um ranking geral para cada
esporte. A interface é baseada em texto e menus interativos no console, com
cores para facilitar a visualização.

================================================================================
2. GUIA DE USO DO PROGRAMA
================================================================================

Esta seção explica como um usuário comum pode interagir com o programa depois
de executado.

--------------------------------------------------------------------------------
2.1. MENU PRINCIPAL
--------------------------------------------------------------------------------

Ao iniciar, o programa exibirá o Menu Principal com três opções:

1 - Gerenciar Tabela Surf: Leva você ao menu específico para inserir e
    consultar as pontuações da modalidade Surf.
2 - Gerenciar Tabela Vôlei: Leva você ao menu específico para a modalidade Vôlei.
3 - Sair: Encerra o programa.

Digite o número da opção desejada e pressione Enter.

--------------------------------------------------------------------------------
2.2. MENU DE ESPORTES (SURF / VÔLEI)
--------------------------------------------------------------------------------

Após escolher um esporte, um novo menu aparecerá com as seguintes opções:

1 - Inserir Pontuação:
    - O programa pedirá que você escolha um atleta e uma rodada a partir de
      listas numeradas.
    - Em seguida, você deverá digitar a pontuação para o atleta naquela rodada.
    - Não é possível inserir uma pontuação onde já existe uma.

2 - Listar Pontuações:
    - Exibe uma tabela (placar) completa com as pontuações de todos os atletas
      em todas as rodadas para o esporte selecionado.

3 - Buscar Pontuação:
    - Permite consultar a pontuação de um atleta específico em uma rodada
      específica.

4 - Alterar Pontuação:
    - Similar à inserção, você seleciona um atleta e uma rodada e, em seguida,
      digita a nova pontuação que substituirá a antiga.

5 - Gerar Relatório Filtrado:
    - Permite filtrar atletas que tiveram uma pontuação ACIMA de um valor
      que você define, em uma rodada específica que você também escolhe.
    - Ex: "Listar atletas que fizeram mais de 8.5 pontos na Rodada 2".

6 - Ver Ranking Geral:
    - Calcula a soma total de pontos de cada atleta em todas as rodadas e
      exibe uma lista ordenada do atleta com maior pontuação para o menor.

7 - Voltar ao Menu Principal:
    - Encerra o menu do esporte atual e retorna ao Menu Principal.

================================================================================
3. EXPLICAÇÃO TÉCNICA DO CÓDIGO
================================================================================

Esta seção detalha a estrutura e a função de cada parte do código-fonte.

--------------------------------------------------------------------------------
3.1. CONSTANTES E VARIÁVEIS GLOBAIS
--------------------------------------------------------------------------------

- CORES (RESET, RED, GREEN, etc.): São variáveis que armazenam códigos de escape
  ANSI. Quando impressas no terminal, elas alteram a cor e o estilo do texto
  (como negrito), melhorando a legibilidade da interface.

- `rodadas` e `atletas`: Listas que definem os nomes das rodadas e dos atletas
  participantes. Elas são usadas para exibir os cabeçalhos das tabelas e as
  opções nos menus de seleção.

- `matriz_surf` e `matriz_volei`: São as estruturas de dados centrais. Cada uma
  é uma matriz (lista de listas) onde as linhas representam os atletas e as
  colunas representam as rodadas. Elas são inicializadas com o valor 0 e
  armazenam as pontuações numéricas.

--------------------------------------------------------------------------------
3.2. FUNÇÕES DE GERENCIAMENTO DE DADOS (CRUD)
--------------------------------------------------------------------------------
Estas funções são o coração do programa e manipulam os dados nas matrizes.

- `limpar_tela()`: Uma função simples que imprime 100 linhas em branco para
  limpar a tela do console, organizando a visualização entre os menus.

- `listar_dados()`: Recebe uma matriz e os nomes para formatar e exibir a tabela
  de pontuações completa de um esporte.

- `cadastrar_dados()`: Guia o usuário para selecionar uma "célula" da matriz
  (cruzamento de atleta e rodada) e insere uma nova pontuação nela. Utiliza a
  presença do caractere "." na string da pontuação para verificar se ela já foi
  preenchida (um valor inteiro como 0 não tem ponto, um float como 10.5 tem).

- `buscar_dado()`: Permite a consulta de um único valor na matriz.

- `atualizar_dado()`: Permite a substituição de um valor existente na matriz.

--------------------------------------------------------------------------------
3.3. FUNÇÕES DE RELATÓRIOS
--------------------------------------------------------------------------------

- `gerar_relatorio()`: Filtra a matriz de um esporte para encontrar atletas
  cuja pontuação em uma rodada específica seja maior que um valor definido
  pelo usuário.

- `gerar_ranking()`: Itera sobre a matriz, soma as pontuações de cada atleta
  (cada linha) e armazena o resultado em uma lista de tuplas `(atleta, total)`.
  Em seguida, ordena essa lista usando o método `sort()` com uma função `lambda`
  como chave (`key=lambda x: x[1]`), que especifica que a ordenação deve ser
  baseada no segundo item da tupla (a pontuação total).

--------------------------------------------------------------------------------
3.4. FUNÇÕES DE INTERFACE (MENUS)
--------------------------------------------------------------------------------

- `menu_surf()` e `menu_volei()`: Cada função é responsável por criar o loop de
  interação para seu respectivo esporte. Elas exibem o menu de opções e, com base
  na escolha do usuário, chamam as funções de gerenciamento de dados
  correspondentes, passando a matriz correta (`matriz_surf` ou `matriz_volei`).
  A estrutura `match case` é usada para selecionar a ação a ser executada.

--------------------------------------------------------------------------------
3.5. LOOP PRINCIPAL (EXECUÇÃO)
--------------------------------------------------------------------------------

- O bloco de código no final do arquivo é o ponto de entrada do programa.
- Ele inicializa um loop `while` que exibe o menu principal.
- Com base na escolha do usuário (1, 2 ou 3), ele chama a função de menu
  apropriada (menu_esporte) ou encerra o loop (e o programa).
- Este bloco controla o fluxo geral da aplicação.

```