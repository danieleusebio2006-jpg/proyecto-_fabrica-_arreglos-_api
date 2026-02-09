from Base_datos_empleados import empelado_modelo
from Empleado_modelo import BD_empelados_lista
from diccionario import datos_diccionario

obj_diccionario = datos_diccionario()
info = obj_diccionario.sacar_valores()
print(info)

nuevo_diccionario = {"7714504": {"nombre": "marcos", "apellido" : "quintero", "maquinas":("maquina pinturas", "maquina hidrailica")}}

obj_diccionario.actualizar_diccionario(nuevo_diccionario)
obj_diccionario.imprimir_info()