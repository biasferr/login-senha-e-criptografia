



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




print (criptografia('Love123'))

