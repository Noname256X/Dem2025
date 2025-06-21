import mysql.connector
from mysql.connector import Error

connector = None

def MySQLconnect():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="toor",
            database="roslyakov"
        )
        print("Подключено к MySQL")
    except Error as e:
        print(f"При попытке подключиться к БД MySQL прозошла ошибка {e}")


def MySQLdisconnect():
    connector.disconnect()
    print("Выполнено отсоединение от MySQL")



if __name__ == "__main__":
    MySQLconnect()
    #MySQLdisconnect()


