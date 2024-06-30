import time
import datetime
from ConectorOpc import conect_server
from Global_Variable import global_data, data_aquisition, machine_name
from Conector_Sql import conect_Sql, insert_sql

while True:
    # Obtenção das variáveis globais
    adress_server, driver, server_name, database, login, password, table, node_read_value = global_data()

    # Obtenção do nome do servidor OPC
    opc_server_name,name_machine = machine_name(adress_server)

    # Conexão com o servidor OPC UA
    conected = conect_server(opc_server_name)

    # Chamada função para aquisição de dados PLC
    DC_LinK, Drive_Module_Temperature, Servo_Temperature, Servo_Actual_Speed = data_aquisition(conected,
                                                                                               node_read_value)

    # Chamada Conexão com o banco de dados
    conection_sql, cursor_sql = conect_Sql(driver, server_name, database, login, password)

    # Obter a data e hora atual do sistema
    date_actual = datetime.datetime.now()

    # Chamada Função para inserir dados no banco SQL
    insert_sql(conection_sql, cursor_sql, name_machine, date_actual, table, DC_LinK, Drive_Module_Temperature,Servo_Temperature, Servo_Actual_Speed)
    time.sleep(120)

