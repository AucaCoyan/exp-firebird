import fdb
import os

print(
    "el path C:\Program Files (x86)\Firebird\Firebird_3_0\\fbclient.dll existe: ",
    os.path.isfile("C:\Program Files (x86)\Firebird\Firebird_3_0\\fbclient.dll"),
)
# os.add_dll_directory('C:\\Program Files (x86)\\Firebird\\Firebird_3_0\\bin\\fbclient.dll')
# os.add_dll_directory(os.getcwd())

user = "SYSDBA"
password = "masterkey"
file = "C:\\firebirdDatabase\\TEST.FDB"


fdb.load_api('C:\Program Files (x86)\Firebird\Firebird_3_0\\fbclient.dll')
# The server is named 'bison'; the database file is at '/temp/test.db'.
connection = fdb.connect(
    database="C:\\firebirdDatabase\TEST.FDB", user=user, password=password
)

cursor = connection.cursor()

cursor.excecute("select * from languages order by year_released")

print(cursor.fetchall())
