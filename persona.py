class Persona:
    
    def __init__(self,nombre: str = "john",apellido: str = "Doe",du: int = 1234567):       
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__du__ = du
    
    def mostrar_datos(self):
        print(f'Mis datos son nombre = {self.__nombre__}\
               apellido =   {self.__apellido__}\
               documento = {self.__du__}
               ')                        #no tengo que ej: poner __nombre__ y demas porque ya estan dentro del objeto