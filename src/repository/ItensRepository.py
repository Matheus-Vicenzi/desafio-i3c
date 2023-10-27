import mysql.connector
from model.ItemModel import ItemModel

def create_conn():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="desafio_db"
    )
    return conn


def persist_item(item: ItemModel):
    try:
        conn = create_conn()
        cursor = conn.cursor()

        sql = "INSERT INTO tb_item (descricao, quantidade, valor, valor_36_meses, valor_60_meses) VALUES (%s, %s, %s, %s, %s)"
        val = (item.descricao, item.quantidade, item.valor, item.valor_36_meses, item.valor_60_meses)
        cursor.execute(sql, val)
        
        conn.commit()
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(e)
        raise Exception("Erro ao persistir item")
    

    
