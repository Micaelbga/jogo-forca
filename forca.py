import os

class ConfigPartida:
    def __init__(self, palavra):
        self.vida = 5
        self.letrasUsadas = []
        self.palavra = palavra
        self.palavraSecreta = []

partida = ConfigPartida('')

def iniciarJogo():
    partida.palavra = input('\nBem vindo ao jogo da forca!\nDigite a palavra a ser jogada:  ').lower()
    validarPalavra(partida)

def interface(partida):
    
    os.system('cls')
    print('-----------------------------')
    print('Letras já utilizadas: ', ' '.join(partida.letrasUsadas))
    print('Vidas: ', partida.vida)
    print('Palavra: ', ''.join(partida.palavraSecreta))
    print('-----------------------------')
    estadoDoJogo(partida)
    digito = input('Letra: ').lower()
    validarLetra(digito, partida)  

def validarLetra(digito, partida):
    digito = list(digito)
    if(digito[0].isalpha() == False):
        partida.vida -= 1
        interface(partida)
    else:
        i = 0
        while i < len(list(partida.palavra)):
            if(digito[0] == list(partida.palavra)[i]):
                partida.palavraSecreta[i] = list(partida.palavra)[i]
                interface(partida)
            i += 1
        partida.letrasUsadas.append(digito[0])
        partida.vida -= 1 
        interface(partida)

def validarPalavra(partida):
    digitos = list(partida.palavra)
    for digito in digitos:
        if(digito.isalpha() == False):
            print('\nPalavra contém caracter impróprio')
            iniciarJogo()
            return
        else:
            partida.palavraSecreta.append("_")
    interface(partida)

def estadoDoJogo(partida):
    if(partida.vida == 0):
        print('\nSuas vidas acabaram, jogo finalizado.')
        exit()
    if(''.join(partida.palavraSecreta) == partida.palavra):
        print('\nParabéns, você ganhou o jogo!')
        exit()

iniciarJogo()