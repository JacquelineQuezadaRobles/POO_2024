from conexionBD import*

try:
    micursor=conexion.cursor()
    sql="DELETE FROM clientes WHERE id=1" #tambien puede ser id like

    micursor.execute(sql)
    #Es necesario ejecutar el commit para que finalice el SQL con exito
    conexion.commit()

except:
    print(f"Ocurrio un error por favor vuelva a intentar...mas tarde...")
else:
    print("Registro Eliminado")

