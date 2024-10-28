#import time
#import datetime
#from ConectorOpc import conect_server
#from Global_Variable import global_data, data_aquisition, machine_name
#from Conector_Sql import conect_Sql, insert_sql
from Model_Predict import predictive_data, load_model
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

df_Maintenance = pd.read_csv('Machine_Model/Predictive Maintenance Dataset.csv')

df_Maintenance.drop(['UDI','Product ID','TWF','HDF','PWF','OSF','RNF'], axis=1, inplace=True)

print(df_Maintenance.head(5))

#Renomeando Colunas para português
df_Maintenance.rename(columns={'Type':'Tipo',
                               'Air temperature [K]':'Temperatura do ar [C°]',
                               'Process temperature [K]':'Temperatura do processo [C°]',
                               'Rotational speed [rpm]':'Velocidade de rotação [rpm]',
                               'Torque [Nm]':'Torque [Nm]',
                               'Tool wear [min]':'Desgaste da ferramenta [min]',
                               'Machine failure':'Falha da máquina',
                            }, inplace=True)

#Selecionando colunas categoricas
categorical_Cols = df_Maintenance.select_dtypes(include='object').columns
print(categorical_Cols)
#Selecionando colunas Numericas
numeric_Cols = df_Maintenance.select_dtypes(exclude='object').columns
print(numeric_Cols)
#Instancia do Encoder
encoder_ordinal = OrdinalEncoder()

#Aplicando a trasformação e convertendo para datafreame novamente
df_Maintenance['Tipo'] = pd.DataFrame(encoder_ordinal.fit_transform(df_Maintenance[categorical_Cols]))

df_predict = df_Maintenance.drop(columns='Falha da máquina',)

'''while True:
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
    time.sleep(120)'''

model_loaded = load_model()

# Fazer a predição

resultado = predictive_data(df_predict,model_loaded)

print(f'Resultado Previsão:{resultado}')

for i in range(len(resultado)):
    print(f'Previsão {i + 1}: {resultado[i]}')












