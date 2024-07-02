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
                data_b[f'km{i + 1}b_data'] = get_opc_data(connected_servers[address], NODE_READ_VALUE[:])
            else:
                data_b[f'km{i + 1}b_data'] = {NODE_READ_VALUE[0]: 0}
        except Exception as e:
            print(f'Erro ao obter dados do servidor {address}: {e}')
            data_b[f'km{i + 1}b_data'] = {NODE_READ_VALUE[0]: 0}

    return render_template('index.html',
                           KM1B_Temperatura=data_b.get('km1b_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU1B_Temperatura=data_b.get('km2b_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM2B_temperatura=data_b.get('km2b_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU2B_Temperatura=data_b.get('pu2b_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM3B_Temperatura=data_b.get('km3b_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU3B_Temperatura=data_b.get('pu3b_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM4B_Temperatura=data_b.get('km4b_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU4B_Temperatura=data_b.get('pu4b_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM5B_Temperatura=data_b.get('km5b_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU5B_Temperatura=data_b.get('pu5b_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM6B_Temperatura=data_b.get('km6b_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU6B_Temperatura=data_b.get('pu6b_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM7B_Temperatura=data_b.get('km7b_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU7B_Temperatura=data_b.get('pu7b_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM8B_Temperatura=data_b.get('km8b_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU8B_Temperatura=data_b.get('pu8b_data', {}).get(NODE_READ_VALUE[0], 0),
                           )


@app.route("/Fila_C")
def FilaC():
    
    data_c = {}

    for i, address in enumerate(ADRESS_SERVER):
        try:
            if address in connected_servers:
                data_c[f'km{i + 1}c_data'] = get_opc_data(connected_servers[address], NODE_READ_VALUE[:])
            else:
                data_c[f'km{i + 1}c_data'] = {NODE_READ_VALUE[0]: 0}
        except Exception as e:
            print(f'Erro ao obter dados do servidor {address}: {e}')
            data_c[f'km{i + 1}c_data'] = {NODE_READ_VALUE[0]: 0}

    return render_template('index.html',
                           KM1C_Temperatura=data_c.get('km1c_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU1C_Temperatura=data_c.get('km2c_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM2C_temperatura=data_c.get('km2c_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU2C_Temperatura=data_c.get('pu2c_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM3C_Temperatura=data_c.get('km3c_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU3C_Temperatura=data_c.get('pu3c_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM4C_Temperatura=data_c.get('km4c_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU4C_Temperatura=data_c.get('pu4c_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM5C_Temperatura=data_c.get('km5c_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU5C_Temperatura=data_c.get('pu5c_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM6C_Temperatura=data_c.get('km6c_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU6C_Temperatura=data_c.get('pu6c_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM7C_Temperatura=data_c.get('km7c_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU7C_Temperatura=data_c.get('pu7c_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM8C_Temperatura=data_c.get('km8c_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU8C_Temperatura=data_c.get('pu8c_data', {}).get(NODE_READ_VALUE[0], 0),
                           )


@app.route("/Fila_D")
def FilaD():
    
    data_d = {}

    for i, address in enumerate(ADRESS_SERVER):
        try:
            if address in connected_servers:
                data_d[f'km{i + 1}d_data'] = get_opc_data(connected_servers[address], NODE_READ_VALUE[:])
            else:
                data_d[f'km{i + 1}d_data'] = {NODE_READ_VALUE[0]: 0}
        except Exception as e:
            print(f'Erro ao obter dados do servidor {address}: {e}')
            data_d[f'km{i + 1}d_data'] = {NODE_READ_VALUE[0]: 0}

    return render_template('index.html',
                           #KM1D_Temperatura=data_c.get('km1d_data', {}).get(NODE_READ_VALUE[0], 0),
                           #PU1D_Temperatura=data_c.get('km2d_data', {}).get(NODE_READ_VALUE[0], 0),
                           #KM2D_temperatura=data_c.get('km2d_data', {}).get(NODE_READ_VALUE[0], 0),
                           #PU2D_Temperatura=data_c.get('pu2d_data', {}).get(NODE_READ_VALUE[0], 0),
                           #KM3D_Temperatura=data_c.get('km3d_data', {}).get(NODE_READ_VALUE[0], 0),
                           #PU3D_Temperatura=data_c.get('pu3d_data', {}).get(NODE_READ_VALUE[0], 0),
                           #KM4D_Temperatura=data_c.get('km4d_data', {}).get(NODE_READ_VALUE[0], 0),
                           #PU4D_Temperatura=data_c.get('pu4d_data', {}).get(NODE_READ_VALUE[0], 0),
                           #KM5D_Temperatura=data_c.get('km5d_data', {}).get(NODE_READ_VALUE[0], 0),
                           #PU5D_Temperatura=data_c.get('pu5d_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM6D_Temperatura=data_c.get('km6d_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU6D_Temperatura=data_c.get('pu6d_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM7D_Temperatura=data_c.get('km7d_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU7D_Temperatura=data_c.get('pu7d_data', {}).get(NODE_READ_VALUE[0], 0),
                           KM8D_Temperatura=data_c.get('km8d_data', {}).get(NODE_READ_VALUE[0], 0),
                           PU8D_Temperatura=data_c.get('pu8d_data', {}).get(NODE_READ_VALUE[0], 0),
                           )


if __name__ == '__main__':
    app.run()