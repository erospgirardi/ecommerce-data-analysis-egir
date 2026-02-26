import sqlite3
import pandas as pd

# Conexión a SQLite (crea el archivo si no existe)
conn = sqlite3.connect("data/ecommerce.db")

# Leer el Excel
df = pd.read_excel("data/Online_Retail.xlsx", engine="openpyxl")

# Guardar en SQLite
df.to_sql("orders", conn, if_exists="replace", index=False)

print("Base SQLite creada y tabla cargada correctamente")

conn.close()