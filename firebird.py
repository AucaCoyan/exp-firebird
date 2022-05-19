code = """
import fdb
import os

user = "SYSDBA"
password = "masterkey"
file = r"C:/firebirdDatabase/TEST.FDB"
ruta = os.path.join('C:', '\Program Files (x86)', 'Firebird', 'Firebird_3_0', 'fbclient.dll')
print(ruta)
print('el archivo ', os.path.isfile(ruta), 'existe')

fdb.load_api(ruta)

connection = fdb.connect(
    database=file, user=user, password=password
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM RDB$RELATIONS")
#cursor.execute('select * from languages')

print(cursor.fetchall())
"""

exec(code)

