TENTATIVAS_P1 = 0
TENTATIVAS_P2 = 0
LETRAS_DIGITADAS_P1 = []
ACERTOS = 0

def Perder():
    
    return print(f"INFELIZMENTE SUAS CHANCES ACABARAM!! \n PALAVRA: {PALAVRA_CHAVE}")
               
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
letras_descobertas = []
palavra_secreta = list(x)
s = len(palavra_secreta)
print(f"A PALAVRA POSSUI {s} letras")
    #TRANSFORMA A PLAVRA DIGITADA EM UMA LISTA E DIZ QUANTAS LETRAS POSSUI

for i in range(0,len(palavra_secreta)):
    letras_descobertas.append('-')
    
    # PERCORRE PARA VER QUANTAS LETRAS POSSUI NA PALAVRA SECRETA E ADICIONA UM ' - '



while ACERTOS != len(PALAVRA_CHAVE):
        
    print(f"===PLAYER 1===")
    letra = str(input("Digite uma letra: "))  # IMPEDIR DO USUARIO DIGITAR MAIS DE UMA LETRA POR VEZ
    
    if letra in LETRAS_DIGITADAS_P1:
     print("Você já digitou esta letra, digite outra")
         
    elif len(letra) > 1:
           print("DIGITE APENAS UMA LETRA POR VEZ!")
          
    else:
        TENTATIVAS_P1 +=1
       
            
        LETRAS_DIGITADAS_P1.append(letra)
        
        if not letra in palavra_secreta:
            print(f"A palavra secreta não possui a letra: {letra}")
                                    
            for i in range(0,len(palavra_secreta)):
             letras_descobertas.append('-')
            while ACERTOS != len(PALAVRA_CHAVE):
                print()
                print(f"====PLAYER 2====")
                letra = str(input("Digite uma letra: "))  # IMPEDIR DO USUARIO DIGITAR MAIS DE UMA LETRA POR VEZ

                if letra in LETRAS_DIGITADAS_P1:
                 print("Esta letra já foi digitada, digite outra")
            
                elif len(letra) > 1:
                 print("DIGITE APENAS UMA LETRA POR VEZ!")
                
                else:
                 TENTATIVAS_P2 +=1
                 LETRAS_DIGITADAS_P1.append(letra) 
                 if not letra in palavra_secreta:
                  print(f"A palavra secreta não possui a letra: {letra}")
                     
                  break
                 for i in range(0, len(palavra_secreta)):
                
                  if letra == palavra_secreta[i]:
                    letras_descobertas[i] = letra
                    ACERTOS +=1      
                  print(letras_descobertas[i])
                  
                if ACERTOS == len(PALAVRA_CHAVE):
                          
                       ganhador()
                       print("******JOGADOR 2 VENCEU*********")
                       print(f"**TENTATIVAS: {TENTATIVAS_P2}**")
                       exit()                     
                            
                  
                            
                        
            
        for i in range(0, len(palavra_secreta)):
            
            if letra == palavra_secreta[i]:
               letras_descobertas[i] = letra
               ACERTOS +=1
            print(letras_descobertas[i])
            
            
         
                 
    
    
    if ACERTOS == len(PALAVRA_CHAVE):
        
        ganhador()
        print("******JOGADOR 1 VENCEU*********")
        print(f"**TENTATIVAS: {TENTATIVAS_P1}**")
        exit()

      # SE AINDA HOUVER ESPAÇO COM "-", ELE MANTEM A CONDICAO DE REPETICAO
           
