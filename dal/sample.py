"""

pip install pymysql
pip install cryptography


# if you want to create new user and want to grant to root permissions to him

CREATE USER adam@localhost IDENTIFIED BY 'qwerty@123';
GRANT ALL PRIVILEGES ON *.* TO adam WITH GRANT OPTION;
SHOW GRANTS FOR adam;

'simple way of connecting python to DB'

"""
import pymysql
from typing import List

#connection to database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='rootpassword',
    database='starwarsDB'
)

cursor = connection.cursor()
sql = "select * from starwarsDB.species_sample;"
result = cursor.execute(sql)

def get_db_conn():
    # connection to database
    connection_ = pymysql.connect(
        host='localhost',
        user='root',
        port=3306,
        password='rootpassword',
        database='starwarsDB'
    )
    return connection_


cursor = connection.cursor()
sql_query = "select * from starwarsDB.species_sample;"
result = cursor.execute(sql_query)


def insert_resource(
        table_name: str,
        primary_key_: str,
        primary_value: int,
        columns_: List,
        values: List
):
    """

    Args:
        table_name (str):
        primary_key_ (str):
        primary_value (int):
        columns_ (list):
        values (list):

    Returns:
        number of records inserted in DB table
    """


column_names = ", ".join(columns_)
value_fields = ", ".join(values)

coloumn_names.rstrip(", ")
values_fields.rstrip(", ")

value_fields = ""
for value in values:
    if isinstance(value, str):
        value_fields = value_fields + '''"''' + value + '''"''' + ''','''
    elif isinstance(value, int):
        value_fields = value_fields + str(value) + ''','''

value_fields = value_fields.rstrip(""", """)

result = None
with get_db_conn() as conn:
    cursor = conn.cursor()
    sql_magic = f""" insert into starwarDB.{table_name} ({primary_key_}, {column_names}) values ({primary_value}, {value_fields});"""
    result = cursor.execute(sql_magic)
    conn.commit()
return result