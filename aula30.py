"""
CONSTANTE = "Váriaveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- contagem de complexidade(ruim)
"""
velocidade = 61 # velocidade atual do carro
local_carro = 98 # local em que o carro está na estrada

RADAR_1 = 60 # A velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância que o radar pega

car_vel_pass_radar_1 = velocidade > RADAR_1
range_radar_1_mais = LOCAL_1 + RADAR_RANGE
range_radar_1_menos = LOCAL_1 - RADAR_RANGE
carro_passou_no_radar_1 = local_carro >= range_radar_1_menos and local_carro <= range_radar_1_mais
carro_multado_radar_1 = car_vel_pass_radar_1 and carro_passou_no_radar_1

if car_vel_pass_radar_1:
    print(f'o carro passou da velocidade do radar.')

if carro_multado_radar_1:
    print('carro foi multado no radar 1')