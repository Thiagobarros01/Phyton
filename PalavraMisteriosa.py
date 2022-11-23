TENTATIVAS_P1 = 0
TENTATIVAS_P2 = 0
LETRAS_DIGITADAS = []
ACERTOS = 0
    # CONSTANTES DE CONTROLE E INFORMAÇÃO DO JOGO.               
def ganhador():
    print(50*"\n")
    print("Parabéns, você ganhou!!")
    print(f"Acertou a palavra: {PALAVRA_CHAVE}")     
           
    #FUNCAO PARA USAR, QUANDO HOUVER UM GANHADOR
print("*******ACHE A PALAVRA MISTERIOSA*********")

x = str(input("Digite uma palavra: "))
print("\n"*100)
dica = str(input("DIGITE A DICA: "))
print(f"A dica é: {dica}")
  # RECEBE A PALAVRA SECRETA + DICA
PALAVRA_CHAVE = x
letras_descobertas = []
palavra_secreta = list(x)
    #TRANSFORMA A PLAVRA DIGITADA EM UMA LISTA E DIZ QUANTAS LETRAS POSSUI
quant_letras = len(PALAVRA_CHAVE)
print(f"A PALAVRA POSSUI {quant_letras} LETRAS")
    #INFORMA QUANTAS LETRAS POSSUI NA PALAVRA

for i in range(0,len(palavra_secreta)):
    letras_descobertas.append('-')
    
    # PERCORRE PARA VER QUANTAS LETRAS POSSUI NA PALAVRA SECRETA E ADICIONA UM : - 



while ACERTOS != len(PALAVRA_CHAVE):
        
    print(f"====PLAYER 1====")
    letra = str(input("Digite uma letra: "))  
    
    if letra in LETRAS_DIGITADAS:
     print("Você já digitou esta letra, digite outra")  # INFORMA O USUARIO QUE A LETRA JA FOI DIGITADA
         
    elif len(letra) > 1:
           print("DIGITE APENAS UMA LETRA POR VEZ!")    # IMPEDIR DO USUARIO DIGITAR MAIS DE UMA LETRA POR VEZ
          
    else:
        TENTATIVAS_P1 +=1
       
            
        LETRAS_DIGITADAS.append(letra)
        
        if not letra in palavra_secreta:
            print(f"A palavra secreta não possui a letra: {letra}") #VERIFICA SE NÃO TEM A LETRA E PASSA A VEZ PRO P2
                                    
            
            while ACERTOS != len(PALAVRA_CHAVE):
                print()
                print(f"====PLAYER 2====")
                letra = str(input("Digite uma letra: "))  # IMPEDIR DO USUARIO DIGITAR MAIS DE UMA LETRA POR VEZ

                if letra in LETRAS_DIGITADAS:
                 print("Esta letra já foi digitada, digite outra")
            
                elif len(letra) > 1:
                 print("DIGITE APENAS UMA LETRA POR VEZ!")
                
                else:
                 TENTATIVAS_P2 +=1
                 LETRAS_DIGITADAS.append(letra) 
                 if not letra in palavra_secreta:
                  print(f"A palavra secreta não possui a letra: {letra}")  
                     
                  break          #SE NAO TIVER A LETRA, ELE QUEBRA E VOLTA PRO P1
                 for i in range(0, len(palavra_secreta)):
                
                  if letra == palavra_secreta[i]:       
                    letras_descobertas[i] = letra       #QUANTIFICA OS ACERTOS E ADICIONA A LETRA NO LUGAR DO : -
                    ACERTOS +=1      
                  print(letras_descobertas[i])
                  
                if ACERTOS == len(PALAVRA_CHAVE):   
                       ganhador()
                       print("******JOGADOR 2 VENCEU*********") 
                       print(f"*****TENTATIVAS: {TENTATIVAS_P2}")
                       exit()                     
                            
                  
                            
                        
            
        for i in range(0, len(palavra_secreta)):
            
            if letra == palavra_secreta[i]:
               letras_descobertas[i] = letra     #QUANTIFICA OS ACERTOS E ADICIONA A LETRA NO LUGAR DO : -
               ACERTOS +=1
            print(letras_descobertas[i])
            
            
         
                 
    
    
    if ACERTOS == len(PALAVRA_CHAVE): 
        ganhador()
        print("******JOGADOR 1 VENCEU*********")
        print(f"*****TENTATIVAS: {TENTATIVAS_P1}")
        exit()

      # SE AINDA HOUVER ESPAÇO COM "-", ELE MANTEM A CONDICAO DE REPETICAO
           
