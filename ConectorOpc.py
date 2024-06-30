from opcua import Client,ua

def conect_server(adress):
    client = Client(adress)
    print(adress)
    try:
        client.connect()
        root = client.get_root_node()
        print(f'Conexão com servidor OPC UA. Realizada com sucesso')
        print(f'Número do Root: {root}')
    except:
        print('Não Foi possivel conectar ao servidor OPC')
        client.disconnect()
    return client

def read_input_value(node_id,client):
    client_node = client.get_node(node_id)  # get node
    client_node_value = client_node.get_value()  # read node value
    result = round(float(client_node_value),2)
    return result

'''def write_value_bool(node_id,client,value):
    client_node = client.get_node(node_id)  # get node
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Boolean))
    client_node.set_value(client_node_dv)
    print("Value of : " + str(client_node) + ' : ' + str(client_node_value))'''