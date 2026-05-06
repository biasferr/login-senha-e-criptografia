

from pygame import *
import sys


def validarEmail(email):
    return email[-8:] == '@puc.com'

def temMaiuscula(senha):
    for letra in senha:
        if 'A' <= letra <= 'Z': #letra.isupper()
            return True
    return False    

def temMinuscula(senha):
    for letra in senha:
        if 'a' <= letra <= 'z': #letra.islower()
            return True
    return False        

def temNumero(senha):
    for caractere in senha:
        if '0' <= caractere <= '9': 
            return True
    return False        

def validaSenha(senha):
    check_tamanho = len(senha) >= 8
    check_maiuscula = temMaiuscula(senha)
    check_minuscula = temMinuscula(senha)
    check_numero = temNumero(senha)
    return check_tamanho and check_maiuscula and check_minuscula and check_numero


def criptografia(senha):
    senhaCriptografa = ''
    for char in senha:
        if char.isdigit():
            ref_ini = ord('0') #65
            ascii_char = ord(char) #etapa 1
            posicao_alfabeto = ascii_char - ref_ini #etapa 2
            posicao_alfabeto += 3 #etapa 3
            resto = posicao_alfabeto% 10 #etapa 4
            letra_criptografada = chr(ref_ini + resto) #etapa 5
            senhaCriptografa += letra_criptografada

        elif 'A' <= char <= 'Z':
            ref_ini = ord('A') #65
            ascii_char = ord(char) #etapa 1
            posicao_alfabeto = ascii_char - ref_ini #etapa 2
            posicao_alfabeto += 3 #etapa 3
            resto = posicao_alfabeto% 26 #etapa 4
            letra_criptografada = chr(ref_ini + resto) #etapa 5
            senhaCriptografa += letra_criptografada

        elif 'a' <= char <= 'z':
            ref_ini = ord('a') #65
            ascii_char = ord(char) #etapa 1
            posicao_alfabeto = ascii_char - ref_ini #etapa 2
            posicao_alfabeto += 3 #etapa 3
            resto = posicao_alfabeto% 26 #etapa 4
            letra_criptografada = chr(ref_ini + resto) #etapa 5
            senhaCriptografa += letra_criptografada

        else:
            senhaCriptografa += char
    return senhaCriptografa


    #1 - pegar a letra e converter para decimal ('Z' -> 90)
    #2 - subtrair o valor decimal de 65 ('Z' -> 90 - 65 -> 25)
    #3 - somar 3 ao resultado de (passo 2) (ex: 25 + 3 = 28)
    #4 - obter o resto da divisão do resultado de (passo 3) por 26 (ex: 28%26 = 2)
    #5 - somar o resto a 65 e converter valor de volta para letra

init()

#ITENS DA CASINHA:
cachorro_img= image.load("golden retriver.png")
cachorro_img = transform.scale(cachorro_img, (200,200))

cachorro_font= font.Font("Shelter Coffee.otf", 40)



nuvem_x= 750
nuvem_y= 125
velocidade_nuvem= 100
background_color= (151, 209, 250)
sol_x= 150
sol_y= 125
velocidade_sol = 200
cor_manha = (151,209,250)
cor_tarde = (255, 177, 94)
cor_noite = (39, 17, 145)
background_color = (151,209,250)

audio_manha = mixer.Sound ("manhã.mp3")
audio_tarde = mixer.Sound ("tarde.mp3")
audio_noite = mixer.Sound ("noite.mp3")
estado = 'teclado'



#PYGAME 


window = display.set_mode((1280,720))
running = True
clock= time.Clock()
window.fill((255,197,211))
font = font.Font(None, 32)


#variáveis
login= ''
erro_login = ''
pede_login= 'LOGIN:'
etapa = 'login'
pede_senha = ''
senha = ''
erro_senha = ''
informa_criptografia = ''
senhaCriptografada = ''
mensagem_casinha = ''

while True:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
        
        if etapa == 'login':
            if ev.type == KEYDOWN:
                if ev.key == K_BACKSPACE:
                    login = login[:-1]
                elif ev.key == K_RETURN:
                    if validarEmail(login) == False:
                        erro_login = '*Digite um login valido'
                    else:
                        login = ''
                        erro_login = ''
                        pede_login = ''
                        etapa = 'senha'
                        
                else:
                    if ev.unicode.isprintable() or ev.unicode == '':
                        login += ev.unicode
        elif etapa == 'senha':
            pede_senha = 'SENHA:'
            if ev.type == KEYDOWN:
                if ev.key == K_BACKSPACE:
                    senha = senha[:-1]
                elif ev.key == K_RETURN:
                    if validaSenha(senha) == False:
                        erro_senha = '*Digite uma senha válida'
                    else:
                        senhaCriptografada = criptografia(senha)
                        senha = ''
                        erro_senha = ''
                        pede_senha = ''
                        etapa = 'criptografia'        
                else:
                    if ev.unicode.isprintable() or ev.unicode == '':
                        senha+= ev.unicode
        elif etapa == 'criptografia':
            informa_criptografia = 'Senha Criptografada:'
            mensagem_casinha = 'Aperte enter para visualizar a casinha!'
            if ev.type == KEYDOWN:
                if ev.key == K_RETURN:
                    etapa = 'casinha'

        elif etapa == 'casinha':
            #CASINHA
            if ev.type == MOUSEBUTTONUP:
                if ev.button == 1:
                    #mudança de audio
                    
                    if estagio == 'manhã':
                        audio_manha.play()
                        
                    elif estagio == 'tarde':
                        audio_tarde.play()
                        
                    elif estagio == 'noite':
                        audio_noite.play()
                        
            if ev.type == KEYDOWN:
                if ev.key == K_m:
                    if estado == 'mouse':
                        estado = 'teclado'  
                    elif estado == 'teclado':
                        estado = 'mouse'    
            
    
    window.fill((255,197,211))
    #desenhos
    
    


    #TEXTO
    

    digite_novamente_login = font.render(erro_login,True,(255,0,0))
    window.blit(digite_novamente_login,(400,150))

    texto_pede_login = font.render(pede_login ,True,(0,0,0))
    window.blit(texto_pede_login,(400,100))

    login_digitado = font.render(login, True, (0, 0, 0))
    window.blit(login_digitado,(480,100))

    texto_pede_senha = font.render(pede_senha, True, (0,0,0))
    window.blit(texto_pede_senha,(400,100))

    senha_digitada = font.render(senha, True, (0,0,0))
    window.blit(senha_digitada, (490,100))

    digite_novamente_senha = font.render(erro_senha, True, (255,0,0))
    window.blit(digite_novamente_senha,(400,150))

    mensagem_criptografia = font.render(informa_criptografia, True, (0,0,0))
    window.blit(mensagem_criptografia, (400,100))

    criptografada = font.render(senhaCriptografada, True, (0,0,0))
    window.blit(criptografada, (650,100))

    exibe_mensagem_casina = font.render(mensagem_casinha, True, (255,0,0))
    window.blit(exibe_mensagem_casina,(400,150))


    if etapa == 'casinha':
        ##movimentos
        dt= clock.get_time()/1000
        keys= key.get_pressed()
        # mousee = mouse.get_pressed()
            #movimento sol
        
        if estado == 'teclado': 
            if keys[K_RIGHT]:
                if sol_x >= 1175:
                    sol_x= 1175
                else: 
                    sol_x = sol_x + velocidade_sol * dt
            elif keys[K_LEFT]:
                if sol_x <= 100:
                    sol_x = 100
                else:
                    sol_x= sol_x - velocidade_sol * dt
            elif keys[K_UP]:
                if sol_y <= 105:
                    sol_y= 105
                else:
                    sol_y= sol_y - velocidade_sol * dt
            elif keys[K_DOWN]:
                if sol_y >= 740:
                    sol_y= 740
                else:
                    sol_y= sol_y + velocidade_sol * dt
        elif estado == 'mouse':
            sol_x, sol_y = mouse.get_pos()
            
        
        #mudança de cor do céu
        if sol_y < 350:
            background_color = cor_manha
            estagio = 'manhã'
        elif sol_y < 650:
            background_color = cor_tarde
            estagio = 'tarde'
        else:
            background_color = cor_noite 
            estagio = 'noite'

        #movimento da nuvem
        nuvem_x = nuvem_x + velocidade_nuvem * dt 
        if nuvem_x >= 1050:
            velocidade_nuvem = velocidade_nuvem * (-1)
        elif nuvem_x <= 50:
            velocidade_nuvem = velocidade_nuvem * (-1)

        
        
        ##desenhos    
        window.fill(background_color)

        #desenhar sol
        draw.circle(window, (255,222,33), (sol_x,sol_y),(50))
        draw.line(window,(255,222,33),(sol_x,sol_y + 105), (sol_x,sol_y - 105),(7))
        draw.line(window,(255,222,33), (sol_x - 90,sol_y), (sol_x + 110,sol_y),(7))
        draw.line(window, (255,222,33),(sol_x - 90, sol_y - 75), (sol_x + 70,sol_y + 75),(7))
        draw.line(window, (255,222,33),(sol_x + 70, sol_y - 75), (sol_x - 90,sol_y + 75),(7))


        #desenhar nuvem
        draw.circle(window,(255,255,255),(nuvem_x,nuvem_y),50)
        draw.circle(window,(255,255,255),(nuvem_x + 60,nuvem_y),50)
        draw.circle(window,(255,255,255),(nuvem_x + 120,nuvem_y),50)
        draw.circle(window,(255,255,255),(nuvem_x + 180,nuvem_y),50)


        #desenhando casa
        draw.rect(window,(72, 157, 37), (0,620,1280,100))
        draw.rect(window,(255,192,203), (320,360,270,260))
        draw.polygon(window, (94, 33, 41),((320,360),(455,170),(590,360)))
        draw.rect(window,(121, 77, 27), (455,440,80,180))
        draw.rect(window,(13, 23, 100), (353,480,67,100))
        draw.circle(window,(0,0,0),(470,530),6)

        #desenhando arvore
        draw.rect(window, (120, 77, 26), (960,360,55,260))
        draw.circle(window,(71, 156, 37),(987,400), 100)


        #desenhar imagens
        window.blit(cachorro_img,(700,450))

        #desenhar texto
        cachorro_text= cachorro_font.render("Cuidado, cachorro bravo!", True, (0,0,0))
        window.blit(cachorro_text, (700,400))

            
    display.update()
