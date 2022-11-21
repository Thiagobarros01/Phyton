LIFE = 3
LETRAS_DIGITADAS = []
def life():
    
    return print(f"Você tem apenas {LIFE} chances")

def status():
    if LIFE == 0:
        return print(f"Você perdeu! A palavra secreta é: {PALAVRA_CHAVE}")
            
    else:
        return print("Você ganhou!")


print("*******PALAVRA MISTERIOSA*********")

x = str(input("Digite uma palavra: "))
print("\n"*100)
dica = str(input("DIGITE A DICA: "))
print(dica)
    # RECEBE A PALAVRA SECRETA + DICA
PALAVRA_CHAVE = x
letras_descobertas = []
palavra_secreta = list(x)
s = len(palavra_secreta)
print(f"A PALAVRA POSSUI {s} letras")
    #TRANSFORMA A PLAVRA DIGITADA EM UMA LISTA E DIZ QUANTAS LETRAS POSSUI

for i in range(0,len(palavra_secreta)):
    letras_descobertas.append('-')
    
    # PERCORRE PARA VER QUANTAS LETRAS POSSUI NA PALAVRA SECRETA E ADICIONA UM ' - '
    

acertou = False
while acertou == False and LIFE != 0:
    print(f"Você tem {LIFE} chances")
    letra = str(input("Digite uma letra: "))  # IMPEDIR DO USUARIO DIGITAR MAIS DE UMA LETRA POR VEZ
    
    if letra in LETRAS_DIGITADAS:
     print("Você já digitou esta letra, digite outra")
         
    elif len(letra) > 1:
           print("DIGITE APENAS UMA LETRA POR VEZ!")
          
    else:
        LETRAS_DIGITADAS.append(letra)
        if not letra in palavra_secreta:
            LIFE -=1
            life()
                 
        for i in range(0, len(palavra_secreta)):
            
            if letra == palavra_secreta[i]:
               letras_descobertas[i] = letra
               
            print(letras_descobertas[i])
            
            
         #VERIFICA SE A LETRA DIGITADA ESTÁ NA LISTA
                 
    for i in range(0, len(letras_descobertas)):
       if letras_descobertas[i] == "-":
            acertou = False    
       else:
           acertou = True
      
      # SE AINDA HOUVER ESPAÇO COM "-", ELE MANTEM A CONDICAO DE REPETICAO
           
status()