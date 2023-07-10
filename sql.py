import sqlite3

def crear_tabla():
    with sqlite3.connect("puntajes.db") as conexion:
        try:
            sentencia = ''' create  table usuarios
                            (       
                                    id integer primary key autoincrement,
                                    nombre text,
                                    nivel integer,
                                    puntaje integer
                            )
                        '''
            conexion.execute(sentencia)
            print("Se creo la tabla usuarios")                       
        except:
            print("La tabla ya existe")

def insertar_linea(nombre,nivel,puntaje):
    with sqlite3.connect("puntajes.db") as conexion:
        try:
            conexion.execute("insert into usuarios (nombre,nivel,puntaje) values (?,?,?)", (nombre,nivel,puntaje))
            conexion.commit()
        except sqlite3.OperationalError:
            print("error")

def leer_tabla():
    with sqlite3.connect("puntajes.db") as conexion:
        cursor=conexion.execute("SELECT * FROM usuarios")
        for fila in cursor:
            print(fila)