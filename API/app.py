from flask import Flask, render_template
from opc_data_request import conect_server, get_opc_data, read_input_value

# Declaração de variáveis globais

# Lista dos servidores para conectar
ADRESS_SERVER = ['opc.tcp://192.168.228.128:4840',
                 'opc.tcp://192.168.228.128:4840',
                 'opc.tcp://192.168.228.130:4840',
                 'opc.tcp://192.168.228.131:4840',
                 'opc.tcp://192.168.228.128:4840',
                 'opc.tcp://192.168.228.128:4840',
                 'opc.tcp://192.168.228.128:4840',
                 'opc.tcp://192.168.228.128:4840',
                 'opc.tcp://192.168.228.128:4840',
                 'opc.tcp://192.168.228.128:4840',
                 'opc.tcp://192.168.228.128:4840',
                 'opc.tcp://192.168.228.128:4840',
                 'opc.tcp://192.168.228.128:4840',
                 'opc.tcp://192.168.228.128:4840',
                 'opc.tcp://192.168.228.128:4840',
                 'opc.tcp://192.168.228.128:4840',]

# Lista de variáveis para consultar
NODE_READ_VALUE = ['ns=4;s=|var|CODESYS Control Win V3.Application.PRODUCAO.temp_temp']

# Dicionário para armazenar as conexões dos servidores
connected_servers = {}

# Tenta conectar a cada servidor OPC UA na lista de endereços
for address in ADRESS_SERVER:
    try:
        connected_servers[address] = conect_server(address)
    except Exception as e:
        print(f'Não foi possível conectar ao servidor OPC UA em {address}: Tipo do Erro: {e}')

app = Flask(__name__)

@app.route("/")
def home():
    data_a = {}

    for i, address in enumerate(ADRESS_SERVER):
        try:
            if address in connected_servers:
                data_a[f'km{i+1}a_data'] = get_opc_data(connected_servers[address], NODE_READ_VALUE[:])
            else:
                data_a[f'km{i+1}a_data'] = {NODE_READ_VALUE[0]: 0}
        except Exception as e:
            print(f'Erro ao obter dados do servidor {address}: {e}')
            data_a[f'km{i+1}a_data'] = {NODE_READ_VALUE[0]: 0}

    return render_template('index.html',
                           KM1A_Temperatura=data_a.get('km1a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU1A_Temperatura=data_a.get('km2a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM2A_temperatura=data_a.get('km2a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU2A_Temperatura=data_a.get('pu2a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM3A_Temperatura=data_a.get('km3a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU3A_Temperatura=data_a.get('pu3a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM4A_Temperatura=data_a.get('km4a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU4A_Temperatura=data_a.get('pu4a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM5A_Temperatura=data_a.get('km5a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU5A_Temperatura=data_a.get('pu5a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM6A_Temperatura=data_a.get('km6a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU6A_Temperatura=data_a.get('pu6a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM7A_Temperatura=data_a.get('km7a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU7A_Temperatura=data_a.get('pu7a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM8A_Temperatura=data_a.get('km8a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU8A_Temperatura=data_a.get('pu8a_data', {}).get(NODE_READ_VALUE[0], 0),
                           )

@app.route("/Fila_B")
def FilaB():
    data_b = {}

    for i, address in enumerate(ADRESS_SERVER):
        try:
            if address in connected_servers:
                data_b[f'km{i + 1}a_data'] = get_opc_data(connected_servers[address], NODE_READ_VALUE[:])
            else:
                data_b[f'km{i + 1}a_data'] = {NODE_READ_VALUE[0]: 0}
        except Exception as e:
            print(f'Erro ao obter dados do servidor {address}: {e}')
            data_b[f'km{i + 1}a_data'] = {NODE_READ_VALUE[0]: 0}

    return render_template('index.html',
                           KM1A_Temperatura=data_b.get('km1a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU1A_Temperatura=data_b.get('km2a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM2A_temperatura=data_b.get('km2a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU2A_Temperatura=data_b.get('pu2a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM3A_Temperatura=data_b.get('km3a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU3A_Temperatura=data_b.get('pu3a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM4A_Temperatura=data_b.get('km4a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU4A_Temperatura=data_b.get('pu4a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM5A_Temperatura=data_b.get('km5a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU5A_Temperatura=data_b.get('pu5a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM6A_Temperatura=data_b.get('km6a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU6A_Temperatura=data_b.get('pu6a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM7A_Temperatura=data_b.get('km7a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU7A_Temperatura=data_b.get('pu7a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM8A_Temperatura=data_b.get('km8a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU8A_Temperatura=data_b.get('pu8a_data', {}).get(NODE_READ_VALUE[0], 0),
                           )


@app.route("/Fila_C")
def FilaC():
    data_c = {}

    for i, address in enumerate(ADRESS_SERVER):
        try:
            if address in connected_servers:
                data_c[f'km{i + 1}a_data'] = get_opc_data(connected_servers[address], NODE_READ_VALUE[:])
            else:
                data_c[f'km{i + 1}a_data'] = {NODE_READ_VALUE[0]: 0}
        except Exception as e:
            print(f'Erro ao obter dados do servidor {address}: {e}')
            data_c[f'km{i + 1}a_data'] = {NODE_READ_VALUE[0]: 0}

    return render_template('index.html',
                           KM1A_Temperatura=data_c.get('km1a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU1A_Temperatura=data_c.get('km2a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM2A_temperatura=data_c.get('km2a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU2A_Temperatura=data_c.get('pu2a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM3A_Temperatura=data_c.get('km3a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU3A_Temperatura=data_c.get('pu3a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM4A_Temperatura=data_c.get('km4a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU4A_Temperatura=data_c.get('pu4a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM5A_Temperatura=data_c.get('km5a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU5A_Temperatura=data_c.get('pu5a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM6A_Temperatura=data_c.get('km6a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU6A_Temperatura=data_c.get('pu6a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM7A_Temperatura=data_c.get('km7a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU7A_Temperatura=data_c.get('pu7a_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM8A_Temperatura=data_c.get('km8a_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU8A_Temperatura=data_c.get('pu8a_data', {}).get(NODE_READ_VALUE[0], 0),
                           )


@app.route("/Fila_D")
def FilaD():
    # Machine KM6D
    if ADRESS_SERVER[0] in connected_servers:
        km6d_data = get_opc_data(connected_servers[ADRESS_SERVER[0]], NODE_READ_VALUE[:])
    else:
        km6d_data = {node: 'Servidor indisponível' for node in NODE_READ_VALUE[:]}

    # Machine PU 6D
    if ADRESS_SERVER[1] in connected_servers:
        pu6d_data = get_opc_data(connected_servers[ADRESS_SERVER[1]], NODE_READ_VALUE[:])
    else:
        pu6d_data = {node: 'Servidor indisponível' for node in NODE_READ_VALUE[:]}

    # Machine KM7D
    if ADRESS_SERVER[2] in connected_servers:
        km7d_data = get_opc_data(connected_servers[ADRESS_SERVER[2]], NODE_READ_VALUE[:])
    else:
        km7d_data = {node: 'Servidor indisponível' for node in NODE_READ_VALUE[:]}

    # Machine PU 7D
    if ADRESS_SERVER[3] in connected_servers:
        pu7d_data = get_opc_data(connected_servers[ADRESS_SERVER[3]], NODE_READ_VALUE[:])
    else:
        pu7d_data = {node: 'Servidor indisponível' for node in NODE_READ_VALUE[:]}

    # Machine KM 8D
    if ADRESS_SERVER[4] in connected_servers:
        km8d_data = get_opc_data(connected_servers[ADRESS_SERVER[4]], NODE_READ_VALUE[:])
    else:
        km8d_data = {node: 'Servidor indisponível' for node in NODE_READ_VALUE[:]}

    # Machine PU 8D
    if ADRESS_SERVER[5] in connected_servers:
        pu8d_data = get_opc_data(connected_servers[ADRESS_SERVER[5]], NODE_READ_VALUE[:])
    else:
        pu8d_data = {node: 'Servidor indisponível' for node in NODE_READ_VALUE[:]}



    return render_template('index.html',
                           # Grupo 6D
                           KM6D_Temperatura=km6d_data[NODE_READ_VALUE[0]],
                           PU6D_Temperatura=pu6d_data[NODE_READ_VALUE[0]],
                           # Grupo 7D
                           KM7D_temperatura=km7d_data[NODE_READ_VALUE[0]],
                           PU7D_Temperatura=pu7d_data[NODE_READ_VALUE[0]],
                           # Grupo 8D
                           KM8D_Temperatura=km8d_data[NODE_READ_VALUE[0]],
                           PU8D_Temperatura=pu8d_data[NODE_READ_VALUE[0]],
                           )

if __name__ == '__main__':
    app.run()