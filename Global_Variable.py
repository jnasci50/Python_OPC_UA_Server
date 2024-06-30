import datetime
from ConectorOpc import read_input_value


def global_data():
    # Declaração variaveis globais

    # lista dos servidores para conectar
    adress_server = ['opc.tcp://xx.xxx.52.xxx:0x0x']

    #SQL  variaveis
    driver ='SQL Server'
    server_name ='xxxx09xxMSxx'
    database='Drives_DB'
    login ='sa'
    password ='Server1nst@'
    table='Drive_Temperature'

    # Obter a data e hora atual
    #date_actual = datetime.datetime.now()

    # Lista de variaveis para consultar
    node_read_value = ['ns=7;s=MFSASTATION.WinLC RTX.DC_Link',
                       'ns=7;s=MFSASTATION.WinLC RTX.Motor Module Temperature',
                       'ns=7;s=MFSASTATION.WinLC RTX.Motor Temperature',
                       'ns=7;s=MFSASTATION.WinLC RTX.Actual_Motor_Speed']

    return adress_server,driver,server_name,database,login,password,table,node_read_value

#Chamadas das Funções de conexão ao servidor OPCUA

def machine_name(adress_server):
    for index, index_server in enumerate(adress_server):
        if index == 0:
            machine_opc_server = index_server
            machine_name ='crtm40stc98'
        elif index == 1:
            machine_opc_server = index_server
            machine_name = 'crtm40stc97'
        print(f'Endereço Server OPC:,{machine_opc_server}')
        print(f'Machine Name:{machine_name}')

    return machine_opc_server,machine_name

#Aquisição dados das Variaveis
def data_aquisition(conected,node_read_value):

        print(f'consultando variaveis:{node_read_value}')
        DC_LinK = read_input_value(node_read_value[0], conected)
        print(f'Valor DC_Link:{DC_LinK}')
        Drive_Module_Temperature = read_input_value(node_read_value[1], conected)
        print(f'Valor Drive Module:{Drive_Module_Temperature}')
        Servo_Temperature = read_input_value(node_read_value[2], conected)
        print(f'Valor Servo Temperature:{Servo_Temperature}')
        Servo_Actual_Speed =read_input_value(node_read_value[3], conected)
        print(f'Valor Actual Speed:{Servo_Actual_Speed}')
        #sleep(0.2)
        return  DC_LinK,Drive_Module_Temperature ,Servo_Temperature, Servo_Actual_Speed