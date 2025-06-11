import sys
#
#
#
palavra_secreta = 'pindamonhangaba'
#
#
#

# variaveis 
tentativa = 0
i = 0
tentativas_chute = 0
palavra_formatada = len(palavra_secreta) * '*'
lista_formatada = list(map(str, palavra_formatada))

if tentativa < 7:
    for caracteres in palavra_secreta:
        letra = input('digite uma letra: ').lower()
        if len(letra) > 1:
            print('digite apenas uma letra')
        else:
            tentativa += 1
            buscas = 1
            for letras in palavra_secreta:
                if letra == letras:
                    if buscas == 1: 
                        while i < len(palavra_formatada):
                            if letra == palavra_secreta[i]:
                                lista_formatada[i] = letra
                                i += 1
                            else:
                                i += 1
                    else:
                        break            
            else: 
                print(f'{lista_formatada}')
                i = 0
                buscas += 1
                if lista_formatada.count('*') < (len(palavra_formatada) * 0.5) :
                    while tentativas_chute < 4:
                        if tentativas_chute == 0:
                            tentar_chutar = input('Tentar chutar? (s/n) (voce so tem 3 tentativas) ')
                            if tentar_chutar == 's':
                                tentativas_chute += 1
                                chute = input(f'Seu {tentativas_chute}º chute: ')
                                if chute == palavra_secreta:
                                    print('Venceu!!!!!')
                                    print(f'Você colocou {tentativa} letras e fez {tentativas_chute} chute(s)')
                                    sys.exit() 
                                else:
                                    print(f'Agora voce so tem {abs(3 - tentativas_chute)} chances')
                            else:
                                print('Cagão')
                                break                       
                        elif tentativas_chute == 1:
                            tentar_chutar = input(f'chutar novamente? (s/n) (voce so tem mais {abs(3 - tentativas_chute)} tentativas) ')  
                            if tentar_chutar == 's':
                                tentativas_chute += 1
                                chute = input(f'Seu {tentativas_chute}º chute: ')
                                if chute == palavra_secreta:
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
                                if chute == palavra_secreta:
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
else:
    if tentativa == 15 and tentativas_chute < 3:
        while tentativas_chute < 4:
                        if tentativas_chute == 0:
                            tentar_chutar = input('Tentar chutar? (s/n) (voce so tem 3 tentativas) ')
                            if tentar_chutar == 's':
                                tentativas_chute += 1
                                chute = input(f'Seu {tentativas_chute}º chute: ')
                                if chute == palavra_secreta:
                                    print('Venceu!!!!!')
                                    print(f'Você colocou {tentativa} letras e fez {tentativas_chute} chute(s)')
                                    sys.exit() 
                                else:
                                    print(f'Agora voce so tem {abs(3 - tentativas_chute)} chances')
                            else:
                                print('Cagão')
                                break                       
                        elif tentativas_chute == 1:
                            tentar_chutar = input(f'chutar novamente? (s/n) (voce so tem mais {abs(3 - tentativas_chute)} tentativas) ')  
                            if tentar_chutar == 's':
                                tentativas_chute += 1
                                chute = input(f'Seu {tentativas_chute}º chute: ')
                                if chute == palavra_secreta:
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
                                if chute == palavra_secreta:
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
    else:
        print('Fim de jogo...')
        print(f'Você colocou {tentativa} letras e fez {(tentativas_chute + 1)} chute(s)')         
        

    