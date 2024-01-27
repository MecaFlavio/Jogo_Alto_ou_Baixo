from dados import data
from arte import logo, vs
import os
import random

def seleciona_conta():
    return random.choice(data)

def formata_conta(conta):
    nome = conta['name']
    descrição = conta['description']
    pais = conta['country']
    return f"{nome}, {descrição}, de {pais}"

def checar_resposta(resposta, seguidores_A, seguidores_B):
    if seguidores_A > seguidores_B:
        return resposta == "a"
    else:
        return resposta == "b"

def jogo():
    print(logo)
    pontos = 0
    continuar_jogo = True
    conta_A = seleciona_conta()
    conta_B = seleciona_conta()
    
    while continuar_jogo:
        conta_A = conta_B
        conta_B = seleciona_conta()

        while conta_A == conta_B:
            conta_B = seleciona_conta()
        
        print(f"Compare A: {formata_conta(conta_A)}.")
        print(vs)
        print(f"Contra B: {formata_conta(conta_B)}")

        resposta = input("Quem tem mais Seguidores? Responda A ou B: ").lower()
        seguidores_A = conta_A["follower_count"]
        seguidores_B = conta_B["follower_count"]
        correto = checar_resposta(resposta, seguidores_A, seguidores_B)

        os.system('cls')
        print(logo)
        if correto:
            pontos += 1
            print(f"Voce está certo! Pontos atuais: {pontos}")
        else:
            continuar_jogo = False
            print(f"Game Over. Seus pontos foram: {pontos}")
    
    rejogar = input("Deseja Jogar novamente? Digite S ou N: ").lower()
    if rejogar == 's':
        os.system('cls')
        jogo()
    else:
        print("Ate logo então!")        

jogo()