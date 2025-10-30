import sqlite3
import pandas as pd
from sqlalchemy import create_engine


def conexion_bd():
   user='user_bases'
   password='123456'
   host='localhost'
   port=3306
   database='sys'

   engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
   return engine.raw_connection()

def ejecutar_sql( conexion):
  df = pd.read_sql_query(query, conexion)
  # Usamos display() porque en Colab presenta las tablas de forma más elegante.
  print(df)

query = """
Select nombre_empleado, apellido_empleado, fecha_contratacion, salario
 from empleados;
"""

conexion_mysql = conexion_bd()

ejecutar_sql(conexion_mysql)
