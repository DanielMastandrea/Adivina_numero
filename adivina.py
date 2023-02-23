import random as rd

print ('Bienvenido a "Adivina el numero"\n')

num_pc = rd.randrange (0,100)
num_user = int (input("Adivina que numero del 1 al 100 eligio la Pc: \n"))


while num_pc != num_user:
    if num_pc < num_user:
        num_user = int (input("\nMuy Alto!, elige un numero mas bajo: \n"))
    elif num_pc > num_user:
        num_user = int (input("\nMuy Bajo!, elige un numero mas alto: \n"))
    else:
        num_user = int (input("Debes elegir un numero valido: \n"))
    
print (f'\nAcertaste, el numero que eligio la pc es el {num_pc}')    