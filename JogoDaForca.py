LIFE1 = 3
LIFE2 = 3
LETRAS_DIGITADAS_P1 = []
ACERTOS = 0
def life():
    
    return print(f"Você tem apenas {LIFE1} chances")

def Perder():
    return print("INFELIZMENTE SUAS CHANCES ACABARAM!!")
            
    

def ganhador():
    print(50*"\n")
    print("Parabéns, você ganhou!!")
    print(f"Acertou a palavra: {PALAVRA_CHAVE}")     
        
    
   


print("*******ACHE A PALAVRA MISTERIOSA*********")

x = str(input("Digite uma palavra: "))
print("\n"*100)
dica = str(input("DIGITE A DICA: "))
print(dica)
    # RECEBE A PALAVRA SECRETA + DICA
PALAVRA_CHAVE = x
PALAVRA_CHAVE2 = x
letras_descobertas = []
palavra_secreta = list(x)
s = len(palavra_secreta)
print(f"A PALAVRA POSSUI {s} letras")
    #TRANSFORMA A PLAVRA DIGITADA EM UMA LISTA E DIZ QUANTAS LETRAS POSSUI

for i in range(0,len(palavra_secreta)):
    letras_descobertas.append('-')
    
    # PERCORRE PARA VER QUANTAS LETRAS POSSUI NA PALAVRA SECRETA E ADICIONA UM ' - '


P1 = False
while ACERTOS != len(PALAVRA_CHAVE) and LIFE1 != 0:
        
    print(f"P1 Você tem {LIFE1} chances")
    letra = str(input("Digite uma letra: "))  # IMPEDIR DO USUARIO DIGITAR MAIS DE UMA LETRA POR VEZ
    
    if letra in LETRAS_DIGITADAS_P1:
     print("Você já digitou esta letra, digite outra")
         
    elif len(letra) > 1:
           print("DIGITE APENAS UMA LETRA POR VEZ!")
          
    else:
       # if letra in palavra_secreta:
           # ACERTOS +=1
            
        LETRAS_DIGITADAS_P1.append(letra)
        
        if not letra in palavra_secreta:
            LIFE1 -=1
            life()
            P2 = False
            for i in range(0,len(palavra_secreta)):
             letras_descobertas.append('-')
            while ACERTOS != len(PALAVRA_CHAVE) and LIFE2 != 0:
                
                print(f"Vez do P2, você tem {LIFE2} chances")
                letra = str(input("Digite uma letra: "))  # IMPEDIR DO USUARIO DIGITAR MAIS DE UMA LETRA POR VEZ

                if letra in LETRAS_DIGITADAS_P1:
                 print("Esta letra já foi digitada, digite outra")
            
                elif len(letra) > 1:
                 print("DIGITE APENAS UMA LETRA POR VEZ!")
                
                else:
                # if letra in palavra_secreta:
                  #ACERTOS +=1   
                 LETRAS_DIGITADAS_P1.append(letra) 
                 if not letra in palavra_secreta:
                  print("A palavra não possui esta letra")
                  LIFE2 -=1   
                  break
                 for i in range(0, len(palavra_secreta)):
                
                  if letra == palavra_secreta[i]:
                    letras_descobertas[i] = letra
                    ACERTOS +=1      
                  print(letras_descobertas[i])
                  
                for i in range(0, len(letras_descobertas)):
                  if letras_descobertas[i] == "-":
                    P2 = False    
                  else:
                    P2 = True
                
                
                       
                            
                  
                            
                        
            
        for i in range(0, len(palavra_secreta)):
            
            if letra == palavra_secreta[i]:
               letras_descobertas[i] = letra
               ACERTOS +=1
            print(letras_descobertas[i])
            
            
         #VERIFICA SE A LETRA DIGITADA ESTÁ NA LISTA
                 
    for i in range(0, len(letras_descobertas)):
       if letras_descobertas[i] == "-":
            P1 = False    
       else:
            P1 = True

if ACERTOS == len(PALAVRA_CHAVE):
    ganhador()
elif LIFE1 == 0:
    print("JOGADOR 1:")
    Perder()  
elif LIFE2 == 0:
    print("JOGADOR 2:")
    Perder()       
      # SE AINDA HOUVER ESPAÇO COM "-", ELE MANTEM A CONDICAO DE REPETICAO
           
