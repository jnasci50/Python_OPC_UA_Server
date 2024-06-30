import pyodbc

def conect_Sql(driver, server, database,login,password):
    try:
        string_conection = f"driver={driver};server={server};database={database};uid={login};pwd={password}"
        comm = pyodbc.connect(string_conection)
        cursor = comm.cursor()
        print('Conexão com banco dados. Realizada com sucesso!')
    except:
        print('Erro de conexão SQL !')
    return comm,cursor

def insert_sql(conn,cursor,machine_name,data_event,tabela,value1,value2,value3,value4):
    # Insere dados no banco
    insert_query = f"INSERT INTO {tabela} (machine_name,Event_Date,DC_Link,Drive_Module_Temperature ,Servo_Temperature, Servo_Actual_Speed) VALUES (?,?,?,?,?,?)"
    data_to_insert = (machine_name,data_event,value1,value2,value3,value4)
    cursor.execute(insert_query, data_to_insert)
    conn.commit()
    print('Dados Salvos com sucesso na tabela: SQL ')
    conn.close()
    #return conn