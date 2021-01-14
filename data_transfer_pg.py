import psycopg2, json, datetime
from psycopg2 import Error

def insert_data(connection, type, data_json):
    thistime=datetime.datetime.now().timestamp()
    sql="INSERT INTO METRICS VALUES (%s, %s, %s, %s, %s, %s, current_timestamp)"
    cursor=connection.cursor()
    for i in data_json.keys():
        insert_data=(type, i, data_json[i][0], 
                        data_json[i][1], 
                        data_json[i][2], 
                        data_json[i][3])
    cursor.execute(sql,insert_data)
    # print(type, data_json)
    # pass

def import_data(data_json):
    try:
        connection = psycopg2.connect(user='grafana',
                                      password='grafana',
                                      host='148.100.76.61',
                                      port='5432',
                                      database='grafana')
        # cursor=connection.cursor()
        # print("PostgreSQL server information")
        # print(connection.get_dsn_parameters(), "\n")
        # # Executing a SQL query
        # cursor.execute("SELECT version();")
        # # Fetch result
        # record = cursor.fetchone()
        # print("You are connected to - ", record, "\n")
        # print(data_json)
        insert_data(connection, 'STC', data_json['STC'])
        insert_data(connection, 'TSU', data_json['TSU'])
        connection.commit()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:        
        if (connection):
            # cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

if __name__ == "__main__":
    import_data('')