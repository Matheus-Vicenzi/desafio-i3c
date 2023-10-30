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


def save_item(item: ItemModel):
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
    

def change_item(id: int, new_price_value: float, new_quantity_value: int):
    try:
        conn = create_conn()
        cursor = conn.cursor()

        sql = "UPDATE tb_item SET valor = %s, quantidade = %s WHERE id = %s"
        val = (new_price_value, new_quantity_value, id)
        cursor.execute(sql, val)
        
        conn.commit()
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(e)
        raise Exception("Erro ao alterar item")
    

    
