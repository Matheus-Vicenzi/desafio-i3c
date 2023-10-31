import mysql.connector

from model.ItemModel import ItemModel
from infra.Enviroment import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER


def create_conn():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    return conn


def save_item(item: ItemModel):
    try:
        conn = create_conn()
        cursor = conn.cursor()

        sql = "INSERT INTO tb_item (descricao, quantidade, valor, valor_36_meses, valor_60_meses) VALUES (%s, %s, %s, %s, %s)"
        val = (item.descricao, item.quantidade, item.valor,
               item.valor_36_meses, item.valor_60_meses)
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


def get_item(id: int):
    try:
        conn = create_conn()
        cursor = conn.cursor()

        sql = "SELECT * FROM tb_item WHERE id = %s"
        val = (id,)
        cursor.execute(sql, val)

        result = cursor.fetchone()

        item = ItemModel(id=result[0], descricao=result[1], quantidade=result[2],
                         valor=result[3], valor_36_meses=result[4], valor_60_meses=result[5])

        cursor.close()
        conn.close()

        if result is None:
            raise Exception("Item não encontrado")

        return item

    except Exception as e:
        print(e)
        raise Exception("Erro ao buscar item")
