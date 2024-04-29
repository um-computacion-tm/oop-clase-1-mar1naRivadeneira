from persona import Persona                


if __name__ == '__main__':
    persona = Persona()                    #va a devolver 3 referencias
    print(persona.__str__())                #permite ver la persona como si fuera un diccionario (__dict__)
    persona = Persona()      
    print(persona)
    persona = Persona()      
    print(persona)