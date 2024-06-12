from app.models.Client import Client
from app.repositories.ClientRepository import ClientRepository

class ClientService:
    def __init__(self, environment):
        self.repository = ClientRepository(environment)

    def agregar_usuario(self, nombres, cedula, correo, direccion, provincia_id, genero_id, eliminado):
        self.repository.insertar_cliente(Client(nombres, cedula, correo, direccion, provincia_id, genero_id, eliminado))

    def obtener_cliente_por_cedula(self, cedula):
        return self.repository.obtener_cliente_por_cedula(cedula)
    
    def actualizar_cliente(self, cedula, nuevo_nombres=None, nuevo_correo=None, nueva_direccion=None, nueva_provincia_id=None, nuevo_genero_id=None, nuevo_eliminado=None):
        return self.repository.actualizar_cliente(Client('', cedula, '', '', '', '', ''), nuevo_nombres, nuevo_correo, nueva_direccion, nueva_provincia_id, nuevo_genero_id, nuevo_eliminado)
    
    def eliminar_cliente(self, cedula):
        return self.repository.eliminar_cliente(Client('', cedula, '', '', '', '', ''))
    
    def obtener_todos_los_clientes(self):
        return self.repository.obtener_todos_los_clientes()
    