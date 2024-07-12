from conexionBD import*

try:
    micursor=conexion.cursor()
    sql="UPDATE clientes SET direccion='Col. del UTD' WHERE id=1 " 

    micursor.execute(sql)
    #Es necesario ejecutar el commit para que finalice el SQL con exito
    conexion.commit()

except:
    print(f"Ocurrio un error por favor vuelva a intentar...mas tarde...")
else:
    print("Registro Actualizado")