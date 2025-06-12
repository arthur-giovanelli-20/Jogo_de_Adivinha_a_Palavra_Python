import sys
import random
from rich import print

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


ofensas_para_fujoes = ['boboca', 'fraco', 'medroso', 'iniciante', 'lerdo', 'tanso', 'pangaré', 'mané'                                   \
                        ,'banana', 'pateta', 'mole', 'frouxo', 'covarde', 'panaca', 'trouxa', 'zé ruela', 'abobado', 'abestalhado'       \
                        ,'bocó', 'babaca', 'otário', 'pançudo', 'esquisito', 'desajeitado', 'enfezado', 'gaiato', 'xexelento', 'ralé'     \
                        ,'desmiolado', 'tapado', 'burlesco', 'sem noção', 'pangua', 'zé mané', 'zé ninguém', 'maricas', 'fanfarrão'        \
                        ,'dengoso', 'bobalhão','marmota', 'mosca morta', 'encardido', 'vagal', 'matutão', 'bronco', 'canastrão'             \
                        ,'bicho do mato', 'moleirão','molenga', 'xarope', 'malacabado', 'sem sal', 'sem graça', 'carcamano', 'trombiqueiro'  \
                        ,'espalhafatoso','birrento', 'preguiçoso', 'folgado', 'trapalhão', 'chorão', 'cabacinho', 'bichado', 'carente', 'simplório'] # ofensas pro boroca


index_para_randomizar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19]

#
#
#

def jogo (dificuldade):
    randomiza_facil = dificuldade_1[:]
    randomiza_medio = dificuldade_2[:]
    randomiza_dificil = dificuldade_3[:]
    randomiza_numero = index_para_randomizar[:]
    randomiza_ofensa = ofensas_para_fujoes[:]

    random.shuffle(randomiza_facil)
    random.shuffle(randomiza_medio)
    random.shuffle(randomiza_dificil)
    random.shuffle(randomiza_numero)
    random.shuffle(randomiza_ofensa)
    numero_da_vez = randomiza_numero[17]
    if dificuldade == 1:
        chances = 7
        palavra_randomizada = randomiza_facil[numero_da_vez].lower()
    elif dificuldade == 2:
        chances = 9
        palavra_randomizada = randomiza_medio[numero_da_vez].lower()
    elif dificuldade == 3:
        chances = 11
        palavra_randomizada = randomiza_dificil[numero_da_vez].lower()
    
    # variaveis 
    tentativa = 0
    i = 0
    tentativas_chute = 0
    palavra_aleatoria_formatada = len(palavra_randomizada) * '*'
    lista_randomizada_caracteres = list(map(str , palavra_aleatoria_formatada))
    letras_chutadas = []
    
    for caracteres in palavra_randomizada:
            if tentativa <= chances :
                    letra = input('digite uma letra: ').lower()
                    for letras_possiveis in letras_chutadas:
                        if letra == letras_possiveis:
                            while letra == letras_possiveis:
                                letra = input('digite outra letra: ').lower()
                                for lista_letras in letras_chutadas:
                                    if letras_chutadas[i] == letra:
                                        print('Essa letra já foi usada, tente outra')
                                        continue
                                    else:
                                        i += 1
                                continue
                    if len(letra) > 1:
                        print('digite apenas uma letra')
                        continue
                    else:
                        letras_chutadas.append(letra)
                        tentativa += 1
                        buscas = 1
                        i = 0
                        for letras in palavra_randomizada:
                            if letra == letras:
                                if buscas == 1: 
                                    while i < len(palavra_randomizada):
                                        if letra == palavra_randomizada[i]:
                                            lista_randomizada_caracteres[i] = str(f"[green]{letra}[/green]")
                                            i += 1
                                        else:
                                            i += 1
                                else:
                                    break            
                        else:
                            print(f'{lista_randomizada_caracteres}')
                            print(f'[bold]---------------------------[/bold]')
                            print(f'[blue]{letras_chutadas}[/blue]')
                            print(f'Palpite(s): [#ff0095]{tentativa}[/#ff0095];', end='')
                            print(f' Restam: [#b8860b]{abs((chances-tentativa) + 1)}[/#b8860b]')
                            buscas += 1
                            if lista_randomizada_caracteres.count('*') < (len(lista_randomizada_caracteres) * 0.5) :
                                while tentativas_chute < 4:
                                    if tentativas_chute == 0:
                                        tentar_chutar = input('Tentar chutar? (s/n) (voce so tem 3 tentativas) ')
                                        if tentar_chutar == 's':
                                            tentativas_chute += 1
                                            print(f'Seu [red]{tentativas_chute}º[/red] chute: ', end='')
                                            chute = list(input().replace(" ", "").lower())
                                            for caracteres in chute:
                                                        letra = caracteres
                                                        for letras in palavra_randomizada:
                                                                buscas = 1
                                                                i = 0
                                                                for letras in palavra_randomizada:
                                                                    if letra == letras:
                                                                        if buscas == 1: 
                                                                            while i < len(palavra_randomizada):
                                                                                if letra == palavra_randomizada[i]:
                                                                                    lista_randomizada_caracteres[i] = str(f"[green]{letra}[/green]")
                                                                                    i += 1
                                                                                else:
                                                                                    i += 1
                                                                        else:
                                                                            break            
                                            else:
                                                print(f'{lista_randomizada_caracteres}')
                                            if chute == palavra_randomizada:
                                                print('Venceu!!!!!')
                                                print(f'Você colocou [red]{tentativa}[/red] letras e fez [red]{tentativas_chute}[/red] chute(s)')
                                                sys.exit() 
                                            else:
                                                print(f'Agora voce so tem [red]{abs(3 - tentativas_chute)}[/red] chances')
                                        else:
                                            print(f'[#414141]{randomiza_ofensa[numero_da_vez]}[/#414141]')
                                            break                       
                                    elif tentativas_chute == 1:
                                        print(f'chutar novamente? (s/n) (voce so tem mais [red]{abs(3 - tentativas_chute)}[/red] tentativas) ', end='')
                                        tentar_chutar = input()  
                                        if tentar_chutar == 's':
                                            tentativas_chute += 1
                                            print(f'Seu [red]{tentativas_chute}º[/red] chute: ', end='')
                                            chute = list(input().replace(" ", "").lower())
                                            if chute == palavra_randomizada:
                                                print('Venceu!!!!!')
                                                print(f'Você colocou [red]{tentativa}[/red] letras e fez [red]{(tentativas_chute + 1)}[/red] de chute(s)')
                                                sys.exit()
                                            for caracteres in chute:
                                                        letra = caracteres
                                                        for letras in palavra_randomizada:
                                                                buscas = 1
                                                                i = 0
                                                                for letras in palavra_randomizada:
                                                                    if letra == letras:
                                                                        if buscas == 1: 
                                                                            while i < len(palavra_randomizada):
                                                                                if letra == palavra_randomizada[i]:
                                                                                    lista_randomizada_caracteres[i] = str(f"[green]{letra}[/green]")
                                                                                    i += 1
                                                                                else:
                                                                                    i += 1
                                                                        else:
                                                                            break            
                                            else:
                                                print(f'{lista_randomizada_caracteres}')
                                            if chute != palavra_randomizada:
                                                print(f'Agora você só tem [red]{abs(3 - tentativas_chute)}[/red] chances')
                                        else:
                                            print(f'[#414141]{randomiza_ofensa[numero_da_vez]}[/#414141]')
                                            break                  
                                    elif tentativas_chute == 2:
                                        tentar_chutar = input(f'Chutar novamente? (s/n) (é a sua ultima chance) ')  
                                        if tentar_chutar == 's':
                                            chute = list(input().replace(" ", "").lower())
                                            if chute == palavra_randomizada:
                                                print('Venceu!!!!!')
                                                print(f'Você colocou [red]{tentativa}[/red] letras e fez [red]{(tentativas_chute + 1)}[/red] de chute(s)')
                                                sys.exit()
                                            for caracteres in chute:
                                                        letra = caracteres
                                                        for letras in palavra_randomizada:
                                                                buscas = 1
                                                                i = 0
                                                                for letras in palavra_randomizada:
                                                                    if letra == letras:
                                                                        if buscas == 1: 
                                                                            while i < len(palavra_randomizada):
                                                                                if letra == palavra_randomizada[i]:
                                                                                    lista_randomizada_caracteres[i] = str(f"[green]{letra}[/green]")
                                                                                    i += 1
                                                                                else:
                                                                                    i += 1
                                                                        else:
                                                                            break            
                                            else:
                                                print(f'{lista_randomizada_caracteres}') 
                                            if chute != palavra_randomizada:
                                                print('Fim de jogo...')
                                                print(f'Você colocou [red]{tentativa}[/red] letras e fez [red]{(tentativas_chute + 1)}[/red] chute(s)')
                                                sys.exit()        
                                        else:
                                            print(f'Sabedoria ou [red]tolice?[/red]')
                                            break   
    if tentativa > chances and tentativas_chute < 3:
                                    print(f'Acabou seus palpites, advinhe ou [#000090]perca[/#000090]')
                                    print('Boa sorte!')
                                    continuar = input('Continuar(s/n)')
                                    if continuar == 's':
                                        while tentativas_chute < 4:
                                            if tentativas_chute == 0:
                                                tentativas_chute += 1
                                                print(f'Seu [red]{tentativas_chute}º[/red] chute: ', end='')
                                                chute = list(input().replace(" ", "").lower())
                                                if chute == palavra_randomizada:
                                                    print('Venceu!!!!!')
                                                    print(f'Você colocou [red]{tentativa}[/red] letras e fez [red]{(tentativas_chute + 1)}[/red] de chute(s)')
                                                    sys.exit()
                                                for caracteres in chute:
                                                            letra = caracteres
                                                            for letras in palavra_randomizada:
                                                                    buscas = 1
                                                                    i = 0
                                                                    for letras in palavra_randomizada:
                                                                        if letra == letras:
                                                                            if buscas == 1: 
                                                                                while i < len(palavra_randomizada):
                                                                                    if letra == palavra_randomizada[i]:
                                                                                        lista_randomizada_caracteres[i] = str(f"[green]{letra}[/green]")
                                                                                        i += 1
                                                                                    else:
                                                                                        i += 1
                                                                            else:
                                                                                break            
                                                else:
                                                    print(f'{lista_randomizada_caracteres}')
                                                if chute != palavra_randomizada:
                                                    print(f'Agora você só tem [red]{abs(3 - tentativas_chute)}[/red] chances')                      
                                            if tentativas_chute == 1:
                                                    tentativas_chute += 1
                                                    print(f'Seu [red]{tentativas_chute}º[/red] chute: ', end='')
                                                    chute = list(input().replace(" ", "").lower())
                                                    if chute == palavra_randomizada:
                                                        print('Venceu!!!!!')
                                                        print(f'Você colocou [red]{tentativa}[/red] letras e fez [red]{(tentativas_chute + 1)}[/red] de chute(s)')
                                                        sys.exit()
                                                    for caracteres in chute:
                                                            letra = caracteres
                                                            for letras in palavra_randomizada:
                                                                    buscas = 1
                                                                    i = 0
                                                                    for letras in palavra_randomizada:
                                                                        if letra == letras:
                                                                            if buscas == 1: 
                                                                                while i < len(palavra_randomizada):
                                                                                    if letra == palavra_randomizada[i]:
                                                                                        lista_randomizada_caracteres[i] = str(f"[green]{letra}[/green]")
                                                                                        i += 1
                                                                                    else:
                                                                                        i += 1
                                                                            else:
                                                                                break            
                                                    else:
                                                        print(f'{lista_randomizada_caracteres}')
                                                    if chute != palavra_randomizada:
                                                        print(f'Agora você só tem [red]{abs(3 - tentativas_chute)}[/red] chances')              
                                            elif tentativas_chute == 2:  
                                                    print(f'Seu [bold]ULTIMO[/bold] chute')
                                                    chute = list(input().replace(" ", "").lower())
                                                    if chute == palavra_randomizada:
                                                        print('Venceu!!!!!')
                                                        print(f'Você colocou [red]{tentativa}[/red] letras e fez [red]{(tentativas_chute + 1)}[/red] de chute(s)')
                                                        sys.exit()
                                                    for caracteres in chute:
                                                                letra = caracteres
                                                                for letras in palavra_randomizada:
                                                                        buscas = 1
                                                                        i = 0
                                                                        for letras in palavra_randomizada:
                                                                            if letra == letras:
                                                                                if buscas == 1: 
                                                                                    while i < len(palavra_randomizada):
                                                                                        if letra == palavra_randomizada[i]:
                                                                                            lista_randomizada_caracteres[i] = str(f"[green]{letra}[/green]")
                                                                                            i += 1
                                                                                        else:
                                                                                            i += 1
                                                                                else:
                                                                                    break            
                                                    else:
                                                        print(f'{lista_randomizada_caracteres}')
                                                    if chute != palavra_randomizada:
                                                        print('Fim de jogo...')
                                                        print(f'Você colocou [red]{tentativa}[/red] letras e fez [red]{(tentativas_chute + 1)}[/red] chute(s)')
                                                        print(f'A palavra que você falhou miseravelmente em achar era: [red]{palavra_randomizada}[/red]')
                                                        sys.exit()                    
                                    else:
                                        print(f'[#414141]{randomiza_ofensa[numero_da_vez]}[/#414141]')
                                        print('Faz um favor para si mesmo e desista!')
                                        print(f'A palavra que você falhou miseravelmente em achar era: [red]{palavra_randomizada}[/red]')
                                        sys.exit()