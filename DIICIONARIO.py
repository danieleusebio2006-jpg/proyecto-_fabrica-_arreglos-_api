class datos_diccionario :
    def __init__(self):
        self.datos_diccionario = {}

    def longitud_diccionario(self):
        longitud = len(self.datos_diccionario)
        return longitud
        
      
    def limpiar_diccionario(self):
        limpiar = self.datos_diccionario.clear()
            
    def copiar_diccionario(self):
         copiar = self.datos_diccionario.copy()
         return copiar
     
    def sacar_valores(self):
         sacar = self.datos_diccionario.items()
         return sacar         
     
    def devolver_valores(self):
         devolver = self.datos_diccionario.keys()
         return devolver
     
    def sacar_valores(self):
         dato_valores = self.datos_diccionario.values()
         return dato_valores
     
    def eliminar_info(self):
         eliminar = self.datos_diccionario.pop()
         return eliminar
     
    def eliminar_elementos(self):
         eliminar_elementos = self.datos_diccionario.pop()
         return eliminar_elementos
     
    def actualizar_info(self):
         actualizar = self.datos_diccionario.update()
         return actualizar
     
    def imprimir_info(self):
         for clave, valor in self.datos_diccionario.items():
             print(f"dato info: {self.datos_diccionario[clave]}")
    
            
        
        
           
     
     
      