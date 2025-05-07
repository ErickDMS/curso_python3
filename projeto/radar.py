velocidade = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100  #essas sao variaveis constantes
RADAR_RANGE = 1




if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
     local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
        print('Sua velocidade esta acima do do permitido')
        print('Voce foi multado')
