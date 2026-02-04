class Api_BD_maqinas:
    def __init__(self):
        self.Api_maquina = [
            [ "codigo","nombre_maquina", "modelo_maquina", "estado_maquina"],
            ["cod 1234", "brazo mecanio", "x200", "apagado"],
            ["cod 2352", "cinta transportadora", "zx400", "reequiere mantenimiento"],
            ["cod 5648", "Monobrazo", "jk100", "encendida"]
        ]
        
    def imprimir_info(self):
        for i in range(len(self.Api_maquina)):
            print(self.Api_maquina[i])
            
    def buscar_info(self):
        return self.Api_maquina[2][2]