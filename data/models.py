import sqlobject as SO
from sqlobject import DecimalCol

database = 'mysql://tania:abc123@localhost/prog2_2025'

__connection__ = SO.connectionForURI(database)

class Usuarios(SO.SQLObject):
    user = SO.StringCol(length = 40, varchar = True)
    password =  SO.StringCol(length = 100, varchar = True)

class Cuentas(SO.SQLObject):
    idUser = SO.ForeignKey('Usuarios', default = None, cascade = True)
    moneda =  SO.StringCol(length = 40, varchar = True)
    saldo = DecimalCol(size = 12, precision = 4)

Usuarios.createTable(ifNotExists=True)
Cuentas.createTable(ifNotExists=True)