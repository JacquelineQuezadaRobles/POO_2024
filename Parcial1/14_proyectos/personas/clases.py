#Clase persona
class Persona:
    def _init_(self, nombre, edad, telefono, info_personal):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.info_personal = info_personal

#Clase estudiantes
class Estudiantes:
    def __init__(self, carrera, matricula, informar_carrera, info_personal):
        self.carrera = carrera
        self.matricula = matricula
        self.informar_carrera = informar_carrera
        self.info_personal = info_personal
#Clase docentes
class Docentes:
    def __init__(self, modalidad, num_empleado, informar_modalidad, info_personal):
        self.modalidad = modalidad
        self.num_empleado = num_empleado
        self.informar_modalidad = informar_modalidad
        self.info_personal = info_personal
    
  