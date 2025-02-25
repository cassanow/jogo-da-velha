tabuleiro = [' 'for _ in range(9)]

def Tabuleiro ():
    print(tabuleiro[0] + "  |  "  + tabuleiro[1] + "  |  "  + tabuleiro[2])
    print("--------------")
    print(tabuleiro[3] + "  |  "  + tabuleiro[4] + "  |  "  + tabuleiro[5])
    print("--------------")
    print(tabuleiro[6] + "  |  "  + tabuleiro[7] + "  |  "  + tabuleiro[8])

def verificacao():
    for x in range (3):
        # verificar as linhas 
        if tabuleiro[x*3] == tabuleiro[x*3+1] == tabuleiro[x*3+2] != ' ':
            return True
        
        # verificar as colunas
        if tabuleiro[x] == tabuleiro[x+3] == tabuleiro[x+6] != ' ':
            return True
        
        # verificar diagonais
        if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] != ' ':
            return True
        
        if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != ' ':
            return True

        return False    
     
def jogatina ():
    jogador = input("Jogador, por favor escolha entre X ou O: ")
    jogador.upper()
    if  jogador not in ['X', 'O']:
        print("Opcao invalida. Por favor escolha X ou O")
        return
    
    jogador_atual = jogador
    while True:
        Tabuleiro()
        posicao = int(input("Por favor " + jogador_atual + " informe em qual espaço (0-8) deseja fazer a sua jogada: "))
        if tabuleiro[posicao] != ' ':
            print("Lamento, mas essa posiçao ja está preenchida")
        else:
            tabuleiro[posicao] = jogador_atual

        if verificacao():
                Tabuleiro()
                print("Parabens, voce venceu!" + jogador_atual)
                print("--------------")
                print("--------------")
                break
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

jogatina()