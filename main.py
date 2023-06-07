import random
tesoura = '''  
 ________  
      ___)___________  
            _________)___  
          _______________)  
         (_____)  
 ________(___)  
 '''    

papel = '''
 _________  
       ___)______  
          _________)_  
           __________)  
            _______)  
 ________________)  
     
'''

pedra = '''
     ____________
            _____)
                (_____)
                (_____)
                (_____)
        ________(___)
'''

player = input('Escolha Pedra, Papel ou Tesoura:')
print(' \n')
opcoes = [pedra, papel, tesoura]
player_pc = random.randint(0,2)

print(f'Jogada MAQUINA: ', opcoes[player_pc])
print(' \n')
    
if player == "papel" and player_pc == 1 or player == "pedra" and player_pc == 0 or player == "tesoura" and player_pc == 2 :
    print('Temos um Empate')
elif player == "papel" and player_pc == 0:
    print('Vitória Player 1 - Papel embrulha a pedra !')
elif player == "tesoura" and player_pc == 1:
    print('Vitória Player 1 - Tesoura corta papel !')
elif player == "pedra" and player_pc == 2:
    print('Vitória Player 1 - Pedra destrói a tesoura !')
else:
    print("Vitória da Máquina")

print(' \n')
    
