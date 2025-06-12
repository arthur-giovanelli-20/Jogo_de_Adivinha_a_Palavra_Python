import sys
import random
#
#
#
dificuldade_1 = ['Computador', 'Amizade', 'Laranja', 'Cadeira', 'Telefone', 'Trabalho', 'Alegria', 'Caderno'\
                 ,'Escrever', 'Montanha', 'Caminhone', 'Tradição', 'Vingança', 'Importante', 'Aviadores'     \
                 ,'Formatura', 'Tempestade', 'Educadora', 'Biblioteca', 'Juventude', 'Invernada', 'Militante' \
                 ,'Desenhar', 'Encantador', 'Convidado'] # 8 a 10 letras



dificuldade_2 = ['Insubstituível', 'Internacional', 'Irrecuperável', 'Funcionamento', 'Impressionante'         \
                 ,'Contratualmente', 'Revolucionário', 'Sobrenatural', 'Autoexplicativo', 'Conscientemente'     \
                 ,'Antissocialmente', 'Estacionamento', 'Conceitualmente', 'Extraordinário', 'Aposentadoria'     \
                 ,'Superalimentado', 'Antidemocrático', 'Antiprofissional', 'Sustentabilidade', 'Ultraespecial'   \
                 ,'Conformidade', 'Multiplicativo', 'Neocolonialismo', 'Antirregulatório', 'Desmotivador'] #12 a 15 letras 



dificuldade_3 = ['Inconstitucional', 'Anticoncepcional', 'Intercontinental', 'Descongestionante', 'Inverossimilhança'\
                 , 'Irresponsabilidade', 'Pluriculturalismo', 'Desproporcionalidade', 'Desorganização'                \
                 , 'Reencaminhamento', 'Vice-presidente', 'Anti-inflamatório', 'Ex-primeiro-ministro'                  \
                 ,'Sócio-econômico', 'Auto-organização', 'Primeiro-ministro', 'Infraestruturado'                        \
                 ,'Extraoficialmente', 'Interdepartamental', 'Antirreligiosamente', 'Polirritmicamente'                  \
                 , 'Constitucionalista', 'Internacionalizar', 'Desvalorizadamente', 'Microempreendedor'] # apartir de 16 letras
#
#
#




randomiza_facil = dificuldade_1[:]
randomiza_medio = dificuldade_2[:]
randomiza_dificil = dificuldade_3[:]

random.shuffle(randomiza_facil)
random.shuffle(randomiza_medio)
random.shuffle(randomiza_dificil)

print('dificuldade (1/2/3)')
dificuldade = int(input('escolha a dificuldade: '))

def jogo (dificuldade, lista_randomizada):
    if dificuldade == 1:
        chances = 7
        palavra_randomizada = randomiza_facil[5]
    elif dificuldade == 2:
        chances = 9
        palavra_randomizada = randomiza_medio[5]
    elif dificuldade == 3:
        chances = 11
        palavra_randomizada = randomiza_dificil[5]
    
    # variaveis 
    tentativa = 0
    i = 0
    tentativas_chute = 0
    palavra_aleatoria_formatada = len(palavra_randomizada) * '*'
    lista_randomizada_caracteres = list(map(str, palavra_aleatoria_formatada))
    
    for caracteres in palavra_randomizada:
            if tentativa <= chances :
                letra = input('digite uma letra: ').lower()
                if len(letra) > 1:
                    print('digite apenas uma letra')
                else:
                    tentativa += 1
                    buscas = 1
                    for letras in palavra_randomizada:
                        if letra == letras:
                            if buscas == 1: 
                                while i < len(palavra_randomizada):
                                    if letra == palavra_randomizada[i]:
                                        lista_randomizada_caracteres[i] = letra
                                        i += 1
                                    else:
                                        i += 1
                            else:
                                break            
                    else: 
                        print(f'{lista_randomizada_caracteres}')
                        i = 0
                        buscas += 1
                        if lista_randomizada_caracteres.count('*') < (len(lista_randomizada_caracteres) * 0.5) :
                            while tentativas_chute < 4:
                                if tentativas_chute == 0:
                                    tentar_chutar = input('Tentar chutar? (s/n) (voce so tem 3 tentativas) ')
                                    if tentar_chutar == 's':
                                        tentativas_chute += 1
                                        chute = input(f'Seu {tentativas_chute}º chute: ')
                                        if chute == palavra_randomizada:
                                            print('Venceu!!!!!')
                                            print(f'Você colocou {tentativa} letras e fez {tentativas_chute} chute(s)')
                                            sys.exit() 
                                        else:
                                            print(f'Agora voce so tem {abs(3 - tentativas_chute)} chances')
                                    else:
                                        print('Medroso')
                                        break                       
                                elif tentativas_chute == 1:
                                    tentar_chutar = input(f'chutar novamente? (s/n) (voce so tem mais {abs(3 - tentativas_chute)} tentativas) ')  
                                    if tentar_chutar == 's':
                                        tentativas_chute += 1
                                        chute = input(f'Seu {tentativas_chute}º chute: ')
                                        if chute == palavra_randomizada:
                                            print('Venceu!!!!!')
                                            print(f'Você colocou {tentativa} letras e fez {(tentativas_chute + 1)} de chute(s)')
                                            sys.exit()    
                                        else:
                                            print(f'Agora você só tem {abs(3 - tentativas_chute)} chances')
                                    else:
                                        print('Cagão')
                                        break                  
                                elif tentativas_chute == 2:
                                    tentar_chutar = input(f'Chutar novamente? (s/n) (é a sua ultima chance) ')  
                                    if tentar_chutar == 's':
                                        chute = input(f'Seu ultimo chute: ')
                                        if chute == palavra_randomizada:
                                            print('Venceu!!!!!')
                                            print(f'Você colocou {tentativa} letras e fez {(tentativas_chute + 1)} chute(s)')
                                            sys.exit() 
                                        else:
                                            print('Fim de jogo...')
                                            print(f'Você colocou {tentativa} letras e fez {(tentativas_chute + 1)} chute(s)')
                                            sys.exit()        
                                    else:
                                        print('Sabedoria ou tolice?')
                                        break   
    if tentativa > chances and tentativas_chute < 3:
                                print('Acabou suas chances de jogar letra, advinhe ou perca')
                                print('Boa sorte!')
                                continuar = input('Continuar(s/n)')
                                if continuar == 's':
                                    while tentativas_chute < 4:
                                        if tentativas_chute == 0:
                                            tentativas_chute += 1
                                            chute = input(f'Seu {tentativas_chute}º chute: ')
                                            if chute == palavra_randomizada:
                                                    print('Venceu!!!!!')
                                                    print(f'Você colocou {tentativa} letras e fez {tentativas_chute} chute(s)')
                                                    sys.exit() 
                                            else:
                                                    print(f'Agora voce so tem {abs(3 - tentativas_chute)} chances')                       
                                        if tentativas_chute == 1:
                                                tentativas_chute += 1
                                                chute = input(f'Seu {tentativas_chute}º chute: ')
                                                if chute == palavra_randomizada:
                                                    print('Venceu!!!!!')
                                                    print(f'Você colocou {tentativa} letras e fez {(tentativas_chute + 1)} de chute(s)')
                                                    sys.exit()    
                                                else:
                                                    print(f'Agora você só tem {abs(3 - tentativas_chute)} chances')              
                                        elif tentativas_chute == 2:  
                                                chute = input(f'Seu ultimo chute: ')
                                                if chute == palavra_randomizada:
                                                    print('Venceu!!!!!')
                                                    print(f'Você colocou {tentativa} letras e fez {(tentativas_chute + 1)} chute(s)')
                                                    sys.exit() 
                                                else:
                                                    print('Fim de jogo...')
                                                    print(f'Você colocou {tentativa} letras e fez {(tentativas_chute + 1)} chute(s)')
                                                    print(f'A palavra que você falhou miseravelmente em achar era: {palavra_randomizada}')
                                                    sys.exit()                    
                                else:
                                    print('Patetico...')
                                    print('Faz um favor para si mesmo e desista!')
                                    sys.exit()


if dificuldade == 1:
    print('Você escolheu o modo facil (noob)')
    jogo(1, randomiza_facil)
elif dificuldade == 2:
    print('Você escolheu o modo medio (nhe)')
    jogo(2, randomiza_medio)
elif dificuldade == 3:
    print('Você escolheu o modo dificil, inteligencia ou tolice?')
    jogo(3, randomiza_dificil)
else:
     print('escolha uma dificuldade valida: ')
     




        